from .base import BaseHandler

class MainHandler(BaseHandler):
    def get(self):
        self.render_page("index.html")