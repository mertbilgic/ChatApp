# General modules.
import os
import os.path
from typing import Final
import uuid
import base64

# Tornado modules.
import tornado
from tornado.options import define,options

ROOT_DIR: Final[str] = os.path.dirname(os.path.abspath(__file__))

# Define port from command line parameter.
define("port", default=8888, help="run on the given port", type=int)
# Define Cookie Secret from command line parameter.
define("cookie_secret", default="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__", help="Cookie Secret", type=str)
# Define Debug Mode from command line parameter.
define("debug", default=True, help="Run in debug mode", type=bool)
# This line will setup default options.
tornado.options.parse_command_line()

settings = dict(
    template_path=os.path.join(ROOT_DIR, "templates"),
    static_path = os.path.join(ROOT_DIR, "static"),
    static_url_prefix = '/static/',
    debug = options.debug,
    cookie_secret = options.cookie_secret,
    login_url="/login"
)   