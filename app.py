# General modules.
import os

# Tornado modules.
import tornado.web
import tornado.options

# Import application modules.
from handler.main import MainHandler
from handler.chatsocket import ChatSocketHandler

# Define port from command line parameter.
tornado.options.define("port", default=8888, help="run on the given port", type=int)

class Application(tornado.web.Application):
    
    def __init__(self):

        handlers = {
            (r"/",MainHandler),
            (r"/socket",ChatSocketHandler)
        }
    
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
        )

        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    """
    Main function to run the chat application.
    """
     # This line will setup default options.
    tornado.options.parse_command_line()
    # Create an instance of the main application.
    application = Application()
    # Start application by listening to desired port and starting IOLoop.
    application.listen(tornado.options.options.port)

    print (f"Starting server on http://localhost:{tornado.options.options.port}")

    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        print ("\nStopping server.")

if __name__ == "__main__":
    main()