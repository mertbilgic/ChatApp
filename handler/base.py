from tornado import web

class BaseHandler(web.RequestHandler):
        
    def render_page(self,template_name):
        self.render(template_name)
    