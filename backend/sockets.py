from app import socketio
from flask_socketio import join_room, leave_room, send

@socketio.on('join')
def on_join(data):
    room = data['code']
    join_room(room)
    send(f'{data["username"]} has entered the quiz', to=room)

@socketio.on('leave')
def on_leave(data):
    room = data['code']
    leave_room(room)
    send(f'{data["username"]} has left the quiz', to=room)
