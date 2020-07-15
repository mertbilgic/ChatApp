let socket = new WebSocket("ws://localhost:8888/socket");


socket.onopen = function(e) {
    console.log("Connection To Server");
};

function sendMessage() {
    console.log("Send");
    let username = getCookie("user")
    let messageInput = document.getElementById("message");
    let message = messageInput.value;
    let payload = {
        "user": username,
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

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
      var c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
  }
