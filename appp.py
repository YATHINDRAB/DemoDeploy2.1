from flask import Flask, render_template
from flask_socketio import SocketIO

appp = Flask(__name__)
socketio = SocketIO(appp)

@appp.route('/')
def index():
    return render_template('index.html')

@socketio.on('vote')
def handle_vote(data):
    socketio.emit('vote_result', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(appp)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Real-Time Voting App</title>
</head>
<body>
    <h1>Vote for BRS Party</h1>
    <button onclick="vote()">Vote</button>
    <div id="result"></div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/3.1.3/socket.io.js"></script>
    <script>
        var socket = io.connect('http://' + document.domain + ':' + location.port);

        function vote() {
            var data = {
                party: 'BRS Party',
                details: 'Party members and their details go here.',
            };
            socket.emit('vote', data);
        }

        socket.on('vote_result', function (data) {
            document.getElementById('result').innerHTML = 'Vote for ' + data.party + ' received!<br>' + data.details;
        });
    </script>
</body>
</html>

