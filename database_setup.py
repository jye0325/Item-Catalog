import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'
	name = Column(String(250), nullable = False)
	id = Column(Integer, primary_key = True)
	email = Column(String(250), nullable = False)
	admin = Column(Boolean, default=False)
	
class Category(Base):
	__tablename__ = 'category'
	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	user = relationship(User)
	user_id = Column(Integer, ForeignKey('user.id'))

class Item(Base):
	__tablename__ = 'item'
	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	description = Column(String(500))
	user = relationship(User)
	user_id = Column(Integer, ForeignKey('user.id'))
	category = relationship(Category)
	category_id = Column(Integer, ForeignKey('category.id'))
	

engine = create_engine('sqlite:///main.db')
Base.metadata.create_all(engine)