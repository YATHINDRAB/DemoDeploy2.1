from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('vote')
def handle_vote(data):
    socketio.emit('vote_result', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
