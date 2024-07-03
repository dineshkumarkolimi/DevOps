import tornado.web
from sqlalchemy.orm import sessionmaker
from models import Item, engine
import json

Session = sessionmaker(bind=engine)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class GetFormHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("get.html")

class PostFormHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("post.html")

class ItemHandler(tornado.web.RequestHandler):
    def get(self, item_id=None):
        session = Session()
        if not item_id:
            item_id = self.get_argument('id', None)
        item = session.query(Item).filter(Item.id == item_id).first()
        if item:
            self.write({'id': item.id, 'name': item.name, 'email': item.email, 'phone number': item.phone_number})
        else:
            self.set_status(404)
            self.write({"error": "Item not found"})
        session.close()

    def post(self):
        session = Session()
        # if self.get_argument('_method', None) == 'put':
        #     return self.put()
        try:
            item_id = self.get_argument('id')
            item_name = self.get_argument('name')
            item_phone_number = self.get_argument('phone_number')
            item_email = self.get_argument('email')
            item = Item(id=item_id, name=item_name, email=item_email, phone_number=item_phone_number)
            session.add(item)
            session.commit()
            self.set_status(201)
            # self.write({"message": "Item created"})
            self.render("success.html")
        except Exception as e:
            session.rollback()
            self.set_status(400)
            self.write({"error": str(e)})
        finally:
            session.close()
