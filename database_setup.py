import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'
	name = Column(String(250), nullable = False)
	id = Column(Integer, primary_key = True)
	email = Column(String(250), nullable = False)
	admin = Column(Boolean)
	
class Category(Base):
	__tablename__ = 'category'
	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	user_id = Column(Integer, ForeignKey('user.id')
	user = relationship(User)

class Item(Base):
	__tablename__ = 'item'
	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	description = Column(String(500))
	user_id = Column(Integer, ForeignKey('user.id')
	user = relationship(User)
	category_id = Column(Integer, ForeignKey('category.id')
	category = relationship(Category)\

engine = create_engine('sqlite:///main.db')
Base.metadata.create_all(engine)