import tornado.websocket

class ChatSocketHandler(tornado.websocket.WebSocketHandler):
    message = set()

    def open(self):
        self.message.add(self)

    def on_message(self, message):
        [client.write_message(message) for client in self.message]

    def on_close(self):
        self.message.remove(self)