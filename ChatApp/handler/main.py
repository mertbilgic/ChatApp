from .base import BaseHandler
from .chatsocket import ChatSocketHandler

class MainHandler(BaseHandler):
    def get(self):
        self.render("index.html",messages=ChatSocketHandler.cache)