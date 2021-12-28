import pickle
import socket
import struct
import threading
import time
from time import sleep
import cv2
import imutils


class ClientReconnectHandler(threading.Thread):
    def __init__(self, host_ip, host_port, client_ip, client_port):
        threading.Thread.__init__(self)
        self.client_ip = client_ip
        self.client_port = client_port
        self.host_ip = host_ip
        self.host_port = host_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False
        self.first_connected = False

    def run(self):
        global client
        while True:
            try:
                self.socket.send(''.encode("UTF-8"))
                self.socket.connect((self.host_ip, self.host_port))
                self.first_connected = True
                client = SocketClient(self.socket, self.host_ip, self.host_port, True, self.client_ip,
                                      self.client_port)
                client.start()
            except socket.error:
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    if client.is_alive():
                        ClientReconnectHandler(self.host_ip, self.host_port, self.client_ip, self.client_port).start()
                        break
                except NameError:
                    pass

                while not self.connected:
                    try:
                        self.socket.connect((self.host_ip, self.host_port))
                        self.connected = True
                        self.first_connected = True
                        print("Connected")
                        client = SocketClient(self.socket, self.host_ip, self.host_port, True, self.client_ip,
                                              self.client_port)
                        client.start()
                        break
                    except socket.error:
                        time.sleep(2)
                        print("Reconnecting....")


class SocketClient(threading.Thread):
    def __init__(self,
                 sock,
                 host_ip="localhost",
                 host_port=00000,
                 connection_established=True,
                 client_ip="localhost",
                 client_port=0000):
        threading.Thread.__init__(self)
        self.host_ip = host_ip
        self.host_port = host_port
        self.client_ip = client_ip
        self.client_port = client_port
        self.connection_established = connection_established
        self.socket = sock
        self.camera = cv2.VideoCapture(0)
        self.encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
        self.img_frame_counter = 0
        self.ip_transferred = False

    def run(self):
        crossingStatus(self.socket).start()
        while self.connection_established:
            try:
                if not self.ip_transferred:
                    ip = "http://" + self.client_ip + ":" + str(self.client_port)
                    self.socket.send(ip.encode("UTF-8"))
                    self.ip_transferred = True
                ret, frame = self.camera.read()
                frame = imutils.resize(frame, width=320)
                frame = cv2.flip(frame, 180)
                result, image = cv2.imencode('.jpg', frame, self.encode_param)
                data = pickle.dumps(image, 0)
                size = len(data)
                if self.img_frame_counter % 5 == 0:
                    self.socket.send(struct.pack(">L", size) + data)
                    cv2.imshow(self.client_ip + ":" + str(self.client_port), frame)
                self.img_frame_counter += 1
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            except socket.error:
                self.camera.release()
                cv2.destroyWindow(self.client_ip + ":" + str(self.client_port))
                self.connection_established = False
                break


class crossingStatus(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.socket = sock
        self.connection_established = True

    def run(self):
        while self.connection_established:
            try:
                data = self.socket.recv(4096)
                strData = str(data).replace("b", "").replace("'", "")
                if strData == "open":
                    print("open")
                elif strData == "close":
                    print("close")

            except socket.error:
                self.connection_established = False
                break
