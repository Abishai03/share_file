from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# This will hold shared text
shared_text = ""

@app.route('/')
def index():
    return render_template('index.html', text=shared_text)

@socketio.on('update text')
def handle_text(data):
    global shared_text
    shared_text = data['text']
    emit('text updated', {'text': shared_text}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5010)
