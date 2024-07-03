import os
import tornado.ioloop
import tornado.web

from handlers.main_handler import MainHandler
from handlers.user_handler import UserHandler
from handlers.mongo_handler import MongoHandler

def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
        (r'/users/', UserHandler),
        (r'/mongo', MongoHandler)],
        template_path="/usr/share/nginx/html/templates", 
        static_path="/usr/share/nginx/html/static")

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

    