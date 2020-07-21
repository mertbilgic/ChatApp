import tornado.websocket
import uuid

from helpers.isthere import is_there_room,is_there_client
class ChatSocketHandler(tornado.websocket.WebSocketHandler):
    ws_clients = {}
    cache = {}
    cache_size = 200
    room_no = str()
    room_name = str()

    def open(self,room="1"):
        ChatSocketHandler.room_name = "room"+room
        self.room = str(room)

        self.ws_cilents = is_there_client(self.ws_clients,self.room_name)
        self.ws_clients[self.room_name].add(self)


    @classmethod
    def update_cache(cls, chat):
        cls.cache[cls.room_name].append(chat)
        if len(cls.cache[cls.room_name]) > cls.cache_size:
            cls.cache[cls.room_name] = cls.cache[-cls.cache_size :]

    def on_message(self, message):
        [client.write_message(message) for client in self.ws_clients[self.room_name]]
        payload = tornado.escape.json_decode(message)
        chat =  self.render_string("message.html", payload=payload)

        ChatSocketHandler.update_cache(chat)
        

    def on_close(self):
        self.ws_clients[self.room_name].remove(self)