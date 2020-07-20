# Tornado modules.
import tornado.web

# Import application modules.
from handler.main import MainHandler
from handler.chatsocket import ChatSocketHandler
from handler.login import LoginHandler


from settings import settings

routes = [
    (r"/static/(.*)",tornado.web.StaticFileHandler,{"path":settings.get("static_path")}),
    (r"/",MainHandler),
    (r"/room/([a-zA-Z0-9]*)$",MainHandler),
    (r"/login",LoginHandler),
    (r"/socket/([a-zA-Z0-9]*)$",ChatSocketHandler),
    (r"/socket",ChatSocketHandler)
]