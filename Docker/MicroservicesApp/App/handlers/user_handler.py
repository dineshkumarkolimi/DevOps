import tornado.web
import json
from models.models import Session, User

class UserHandler(tornado.web.RequestHandler):
    def post(self):
        data = json.loads(self.request.body)
        session = Session()
        user = User(name=data['name'], email_id=data['email_id'])
        session.add(user)
        session.commit()
        session.close()
        self.write({'status': 'success','user': {'name': user.name, 'email': user.email_id}})

    def frame_response(self, results):
        response = []
        for user in results:
            response.append({'id': user.id, 'name': user.name, 'email_id': user.email_id})
        return response
    
    def get(self):
        session = Session()
        print(self.request.arguments)
        query = session.query(User).filter(User.name == self.request.arguments['name'], User.email_id == self.request.arguments['email'])
        results = query.all()
        session.close()
        response = self.frame_response(results)
        self.write(response)