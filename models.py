from sqlalchemy import Boolean,Column,Integer,String
from database import Base

class User(Base):
    __tablename__ = "Users"

    id = Column(Integer,primary_key=True, index=True)
    username = Column(String(50),unique=True)
    age= Column(Integer)
    city = Column(String(50))

class Post(Base):
    __tablename__ = "Post"

    id =  Column(Integer,primary_key=True, index=True)
    title = Column(String(50))
    content = Column(String(100))
    user_id = Column(Integer)
