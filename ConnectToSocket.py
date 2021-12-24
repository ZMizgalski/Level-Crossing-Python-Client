import socket
from time import sleep


class ConnectToSocket(object):
    def __init__(self, IP="", TCP_PORT=0000, CLIENT_PORT=00000):
        self.HOST_IP = IP
        self.TCP_PORT = TCP_PORT
        self.CLIENT_PORT = CLIENT_PORT
        self.CONNECTED = False
        self.DATA_TRANSMITTED = False
        self.DATA = "http://" + IP + ":" + str(CLIENT_PORT)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.createConnection()

    def __del__(self):
        self.sock.close()

    def createConnection(self):
        try:
            self.sock.connect((self.HOST_IP, self.TCP_PORT))
            print("Connected")
            sleep(1)
            if not self.DATA_TRANSMITTED:
                self.sock.send(bytes(self.DATA + "\n", "UTF-8"))
                print(self.DATA)
                self.DATA_TRANSMITTED = True
                self.CONNECTED = True
                while self.CONNECTED:
                    sleep(2)
                    try:
                        self.sock.send(bytes('', "UTF-8"))
                    except socket.error:
                        self.CONNECTED = False
                        self.DATA_TRANSMITTED = False
                self.sock.close()
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.createConnection()
        except socket.error:
            if not self.CONNECTED:
                print("Reconnecting......")
                self.DATA_TRANSMITTED = False
                self.createConnection()