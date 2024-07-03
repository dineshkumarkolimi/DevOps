from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient
from config import Config

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email_id = Column(String(255))


engine = create_engine("mysql+pymysql://{Config.MYSQL_USERNAME}:{Config.MYSQL_PASSWORD}@{Config.MYSQL_HOST}/{Config.MYSQL_DBNAME}")
Session = sessionmaker(bind=engine) 

mongo_client = MongoClient(Config.MONGO_URI)
mongo_db = mongo_client.get_database()