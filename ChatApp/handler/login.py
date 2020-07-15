from .base import BaseHandler
from http import cookies
from form.login_from import LoginForm
class LoginHandler(BaseHandler):
    def get(self):
        form = LoginForm()
        self.render("login.html",form=form)

    def post(self):
        form = LoginForm(self.request.arguments)
            
        username = form.username.data

        self.set_cookie("user", username)
        self.redirect("/")