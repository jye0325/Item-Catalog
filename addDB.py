from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import User, Category, Item, Base

engine = create_engine('sqlite:///main.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

"""
# Test User
user1 = User(name="Test User", email="None")
session.add(user1)
session.commit()
"""

# Category/Item Setup
category1 = Category(name="Category 1")
session.add(category1)
session.commit()

categoryItem1 = Item(name="catItem1", description="Place holder for category 1, item 1.", category=category1)
session.add(categoryItem1)
session.commit()

categoryItem2 = Item(name="catItem2", description="Place holder for category 1, item 2.", category=category1)
session.add(categoryItem2)
session.commit()

category2 = Category(name="Category 2")
session.add(category2)
session.commit()

categoryItem1 = Item(name="catItem1", description="Place holder for category 2, item 1.", category=category2)
session.add(categoryItem1)
session.commit()

categoryItem2 = Item(name="catItem2", description="Place holder for category 2, item 2.", category=category2)
session.add(categoryItem2)
session.commit()

category3 = Category(name="Category 3")
session.add(category3)
session.commit()

categoryItem1 = Item(name="catItem1", description="Place holder for category 3, item 1.", category=category3)
session.add(categoryItem1)
session.commit()

categoryItem2 = Item(name="catItem2", description="Place holder for category 3, item 2.", category=category3)
session.add(categoryItem2)
session.commit()

category4 = Category(name="Category 4")
session.add(category4)
session.commit()

categoryItem1 = Item(name="catItem1", description="Place holder for category 4, item 1.", category=category4)
session.add(categoryItem1)
session.commit()

categoryItem2 = Item(name="catItem2", description="Place holder for category 4, item 2.", category=category4)
session.add(categoryItem2)
session.commit()

print "DB Updated!"
