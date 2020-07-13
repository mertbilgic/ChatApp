let socket = new WebSocket("ws://localhost:8888/socket");

let userName = prompt("What's your name?");

socket.onopen = function(e) {
    console.log("Connection To Server");
};

function sendMessage() {
    console.log("Send");
    let messageInput = document.getElementById("message");
    let message = messageInput.value;
    let payload = {
        "user": userName,
        "message": message
    }
    socket.send(JSON.stringify(payload));
    console.log("Send Message");
    messageInput.value = "";
}
socket.onmessage = function(event) {
    let message = JSON.parse(event.data);
    let messageBox = document.createElement("div");
    messageBox.innerHTML = "<b>" +message.user +"</b>"+ ": " + message.message;
    const messages = document.getElementById('messages');
    messages.appendChild(messageBox);
    messages.scrollTop = messages.scrollHeight;
    console.log("Received Message From Server");
  };

function enterPress(e){ 
    if (e.keyCode == 13) {
        sendMessage();
    }
}
