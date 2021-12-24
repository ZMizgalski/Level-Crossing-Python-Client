import ConnectToSocket
import threading
import keyboard
from flask import Flask, render_template, Response, request


# import VideoCamera
#
# pi_camera = VideoCamera.VideoCamera(flip=False)
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
#
#
# @app.route('/video_feed')
# def video_feed():
#     return Response(gen(pi_camera),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    HOST = "192.168.1.212"
    TCP_PORT = 10001
    CLIENT_PORT = 8080
    sock = ConnectToSocket.ConnectToSocket(HOST, TCP_PORT, CLIENT_PORT)
    # app.run(host='192.168.1.40', debug=False, port=8080)
