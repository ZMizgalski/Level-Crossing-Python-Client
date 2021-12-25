import ClientSocketHandler
from flask import Flask, render_template, Response
import VideoCamera
import threading

pi_camera = VideoCamera.VideoCamera(flip=False)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/stream')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    HOST = "192.168.1.212"
    HOST_PORT = 10001
    CLIENT_PORT = 8080
    CLIENT_IP = "192.168.1.40"
    ClientSocketHandler.ClientSocketHandler(host_ip=HOST, host_port=HOST_PORT, client_ip=CLIENT_IP,
                                            client_port=CLIENT_PORT)
    app.run(host='192.168.1.40', debug=False, port=CLIENT_PORT)
