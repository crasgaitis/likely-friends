const socket = io.connect(window.location.origin);

const urlParams = new URLSearchParams(window.location.search);
const username = urlParams.get('username');
const code = urlParams.get('code');

if (username && code) {
    socket.emit('join', { username, code });
}

socket.on('message', (message) => {
    const messagesDiv = document.getElementById('messages');
    const messageElement = document.createElement('div');
    messageElement.innerText = message;
    messagesDiv.appendChild(messageElement);
});
