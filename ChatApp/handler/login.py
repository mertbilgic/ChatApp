from .base import BaseHandler
from http import cookies
class LoginHandler(BaseHandler):
    def get(self):
        if not self.get_cookie("mycookie"):
            self.write('<html><body><form method="post">'
                    'Name: <input type="text" name="name">'
                    '<input type="submit" value="Sign in">'
                    '</form></body></html>')
        else:
            self.write("Your cookie was set!")

    def post(self):
        self.set_cookie("user", self.get_argument("name"))
        self.redirect("/")