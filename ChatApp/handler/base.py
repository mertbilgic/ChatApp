from tornado import web
import tornado.escape

class BaseHandler(web.RequestHandler):
        
    def render_page(self,template_name):
        self.render(template_name)
    
    def get_current_user(self):
        user_json = self.get_cookie("user")
        if user_json:
            return user_json
        else:
            return None
    