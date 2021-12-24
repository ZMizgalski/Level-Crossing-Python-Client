import ConnectToSocket

if __name__ == "__main__":
    HOST = "192.168.1.212"
    TCP_PORT = 10001
    CLIENT_PORT = 8080
    ConnectToSocket.ConnectToSocket(HOST, TCP_PORT, CLIENT_PORT)
