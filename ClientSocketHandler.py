import socket
import jpysocket
import keyboard
from time import sleep
import threading


class ClientSocketHandler(object):

    def __init__(self, host_ip="localhost", host_port=00000, client_ip="0.0.0.0", client_port=0000):
        self.HOST_IP = host_ip
        self.HOST_PORT = host_port
        self.CLIENT_PORT = client_port
        self.CLIENT_IP = client_ip
        self.DATA_TO_TRANSFER = "http://" + self.CLIENT_IP + ":" + str(self.CLIENT_PORT) + "\n"
        self.CONNECTED = True
        self.CLIENT_SOCKET = socket.socket()
        threading.Thread(target=self.initializeConnection(), args=())

    def initializeConnection(self):
        print("Press 'e' to close ->")
        while not keyboard.is_pressed("e"):
            try:
                self.CLIENT_SOCKET.send(jpysocket.jpyencode(self.DATA_TO_TRANSFER))
            except socket.error:
                connected = False
                self.CLIENT_SOCKET = socket.socket()
                while not connected:
                    try:
                        self.CLIENT_SOCKET.connect((self.HOST_IP, self.HOST_PORT))
                        connected = True
                        print("Connected to: " + self.HOST_IP + ":" + str(self.HOST_PORT))
                    except socket.error:
                        sleep(2)
                        print("reconnecting.....")
