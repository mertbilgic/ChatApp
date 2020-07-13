# General modules.
import os
import os.path
from typing import Final

# Tornado modules.
import tornado
import tornado.options
from tornado.options import define

ROOT_DIR: Final[str] = os.path.dirname(os.path.abspath(__file__))

# Define port from command line parameter.
define("port", default=8888, help="run on the given port", type=int)
# This line will setup default options.
tornado.options.parse_command_line()

settings = dict(
    template_path=os.path.join(ROOT_DIR, "templates"),
    static_path = os.path.join(ROOT_DIR, "static"),
    static_url_prefix = '/static/',
    debug = True,
)   