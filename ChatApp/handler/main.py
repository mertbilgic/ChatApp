from tornado.web import authenticated
from tornado import escape

from .base import BaseHandler
from .chatsocket import ChatSocketHandler as chat
from helpers.isthere import is_there_room

class MainHandler(BaseHandler):
    @authenticated
    def get(self,room_no=None):
        if not room_no:
            self.redirect("/room/1")
            return
            
        room= f"room{room_no}"
        chat.cache = is_there_room(chat.cache,room)

        self.render("index.html",messages=chat.cache.get(room))