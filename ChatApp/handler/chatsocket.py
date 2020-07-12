import tornado.websocket
import uuid

class ChatSocketHandler(tornado.websocket.WebSocketHandler):
    message = set()
    cache = []
    cache_size = 200

    def open(self):
        self.message.add(self)

    @classmethod
    def update_cache(cls, chat):
        cls.cache.append(chat)
        if len(cls.cache) > cls.cache_size:
            cls.cache = cls.cache[-cls.cache_size :]

    def on_message(self, message):
        [client.write_message(message) for client in self.message]
        payload = tornado.escape.json_decode(message)
        chat =  self.render_string("message.html", payload=payload)

        ChatSocketHandler.update_cache(chat)
        

    def on_close(self):
        self.message.remove(self)