from tornado.web import authenticated
from tornado import escape

from .base import BaseHandler
from .chatsocket import ChatSocketHandler as chat
from helpers.isthere import is_there_room



class MainHandler(BaseHandler):
    @authenticated
    def get(self,room=None):
        if not room:
            self.redirect("/room/1")
            return
        chat.cache = is_there_room(chat.cache,"room"+room)

        self.render("index.html",messages=chat.cache.get("room"+room))