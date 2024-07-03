import tornado.ioloop
import tornado.web
import sys
sys.path.append('/Users/dineshkumarkolimi/Library/Python/3.9/lib/python/site-packages')
from handlers import MainHandler, GetFormHandler, PostFormHandler, ItemHandler

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/get", GetFormHandler),
        (r"/post", PostFormHandler),
        (r"/item/([^/]+)?", ItemHandler),
        (r"/item", ItemHandler),
    ],
    template_path="static",  # Directory for HTML templates
    static_path="static"  # Directory for static files
    )

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Tornado server is running at http://127.0.0.1:8888")
    tornado.ioloop.IOLoop.current().start()
