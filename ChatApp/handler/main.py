from tornado.web import authenticated
from tornado import escape

from .base import BaseHandler
from .chatsocket import ChatSocketHandler


class MainHandler(BaseHandler):
    @authenticated
    def get(self):
        name = self.get_cookie("user")
        print(name)
        self.render("index.html",messages=ChatSocketHandler.cache)