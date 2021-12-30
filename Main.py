import clientReconnectHandler

if __name__ == "__main__":
    HOST = "192.168.1.212"
    HOST_PORT = 10001
    CAMERA_NAME = "Camera 1"
    client = clientReconnectHandler.ClientReconnectHandler(HOST, HOST_PORT, CAMERA_NAME)
    client.start()