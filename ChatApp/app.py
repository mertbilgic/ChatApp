# General modules.
import os
from typing import Final

# Tornado modules.
import tornado.web
from tornado.options import options
from tornado.options import define

# Import application modules.
from route import routes
from settings import settings

class Application(tornado.web.Application):
    
    def __init__(self):
 
        tornado.web.Application.__init__(self, routes, **settings)

def main():
    """
    Main function to run the chat application.
    """
    # Create an instance of the main application.
    application = Application()
    # Start application by listening to desired port and starting IOLoop.
    application.listen(options.port)

    print (f"Starting server on http://localhost:{options.port}")

    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        print ("\nStopping server.")

if __name__ == "__main__":
    main()