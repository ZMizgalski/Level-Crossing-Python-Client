import clientReconnectHandler

if __name__ == "__main__":
    HOST = "192.168.1.212"
    HOST_PORT = 10001
    CLIENT_PORT = 8080
    CLIENT_IP = "192.168.1.40"
    client = clientReconnectHandler.ClientReconnectHandler(HOST, HOST_PORT, CLIENT_IP, CLIENT_PORT)
    client.start()