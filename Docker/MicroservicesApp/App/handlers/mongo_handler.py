import tornado.web

import json
from bson import ObjectId
from models.models import mongo_db

class MongoHandler(tornado.web.RequestHandler):
    def post(self):
        data = json.load(self.request.body)
        collection = mongo_db['mycollection']
        result = collection.insert_one(data)
        self.write({"status": "success", "id": str(result.inserted_id)})
        
    def get(self):
        collection = mongo_db['mycollection']
        query_params = {k:v for k,v in self.request.arguments.items()}
        if '_id' in query_params:
            query_params['_id'] = ObjectId(query_params['_id'])
        documents = list(collection.find(query_params))
        for doc in documents:
            doc['_id'] = str(doc['_id'])
        self.write({"documents": documents})