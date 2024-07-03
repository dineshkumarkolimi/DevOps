import os

class Config():
    MYSQL_USERNAME = os.environ.get('MYSQL_USERNAME', 'admin')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'pass')
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
    MYSQL_DBNAME = os.environ.get('MYSQL_DBNAME', 'my_sql_db')
    MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://mongo:27017/my_mongo_db')
