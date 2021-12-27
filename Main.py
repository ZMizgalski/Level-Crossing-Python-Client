import threading

import clientReconnectHandler
# from flask import Flask, render_template, Response
# import VideoCamera
# import threading


# pi_camera = VideoCamera.VideoCamera(flip=False)

# app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('index.html')


# def generate(camera):
#     while True:
#         frame = camera.get_frame()
#         yield b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'
#
#
# @app.route('/stream')
# def video_feed():
#     return Response(generate(pi_camera), mimetype='multipart/x-mixed-replace; boundary=frame')
#

if __name__ == "__main__":
    HOST = "192.168.1.212"
    HOST_PORT = 10001
    CLIENT_PORT = 8080
    CLIENT_IP = "192.168.1.40"
    client = clientReconnectHandler.ClientReconnectHandler(HOST, HOST_PORT, CLIENT_IP, CLIENT_PORT)
    client.start()


    # socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # socket.connect((HOST, HOST_PORT))
    # client = client.SocketClient(socket, HOST, HOST_PORT, True)
    # client.start()
    # threading.Thread(target=ClientSocketHandler.ClientSocketHandler,
    #                  args=[HOST, HOST_PORT, CLIENT_IP, CLIENT_PORT]).start()
    # threading.Thread(target=lambda: app.run(host='192.168.1.40', debug=False, port=CLIENT_PORT)).start()
