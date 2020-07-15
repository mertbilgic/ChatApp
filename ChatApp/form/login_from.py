from wtforms import validators
from wtforms.fields import StringField,PasswordField
from wtforms_tornado import Form

class LoginForm(Form):

    username = StringField('Username')
    password = PasswordField("Password")