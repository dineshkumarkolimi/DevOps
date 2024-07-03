from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone_number = Column(String)
    email = Column(String)
    

engine = create_engine('sqlite:///items.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
