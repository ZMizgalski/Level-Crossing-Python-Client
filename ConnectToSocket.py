import socket
from time import sleep
import threading
import sys
import keyboard


class StoppableThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()


class ConnectToSocket(object):
    def __init__(self, IP="", TCP_PORT=0000, CLIENT_PORT=00000):
        self.HOST_IP = IP
        self.TCP_PORT = TCP_PORT
        self.CLIENT_PORT = CLIENT_PORT
        self.CONNECTED = False
        self.CLOSE_APP = False
        self.DATA_TRANSMITTED = False
        self.DATA = "http://" + IP + ":" + str(CLIENT_PORT) + "\n"
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.thread = StoppableThread(target=self.createConnection, args=())
        self.thread.daemon = True
        self.thread.start()
        self.startKeyboardLister(list('c'), self.listen)
        while not self.CLOSE_APP:
            sleep(1)

    @staticmethod
    def startKeyboardLister(keys, function):
        for thread in [threading.Thread(target=function, kwargs={"key": key}) for key in keys]:
            thread.start()

    def listen(self, key):
        while True:
            keyboard.wait(key)
            self.CLOSE_APP = True
            sys.exit(0)

    def __del__(self):
        print("Closing...")
        self.sock.close()
        self.thread.stop()
        self.CONNECTED = False
        self.DATA_TRANSMITTED = False
        self.CLOSE_APP = True

    def createConnection(self):
        sleep(0.4)
        try:
            self.sock.connect((self.HOST_IP, self.TCP_PORT))
            print("Connected")
            if not self.DATA_TRANSMITTED:
                self.sock.send(self.DATA.encode("UTF-8"))
                print(self.DATA)
                self.DATA_TRANSMITTED = True
                self.CONNECTED = True
                while self.CONNECTED:
                    try:
                        self.sock.send(''.encode("UTF-8"))
                    except socket.error:
                        self.CONNECTED = False
                        self.DATA_TRANSMITTED = False
                self.sock.close()
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.createConnection()
        except socket.error:
            if not self.CONNECTED:
                if not self.CLOSE_APP:
                    print("Reconnecting......")
                    self.DATA_TRANSMITTED = False
                    self.createConnection()
