from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, Item

app = Flask(__name__)

engine = create_engine('sqlite:///main.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

"""@TODO: 
		Functions:
		login(),
		logout(),
		newCategory(),
		newItem(),
		itemMenu(), 
		editItem(), 
		deleteItem()
"""

# Routing for login
@app.route('/login/')
def login():
    """This returns a webpage for users to login"""
    return "This is a test page for login()"
# Routing for logout
@app.route('/logout/')
def logout():
    """This returns a webpage for users to logout"""
    return "This is a test page for logout()"

# Routing for main menu
@app.route('/')
@app.route('/main/')
def mainMenu():
	"""Returns a list of categories in the menu pane and the latest 5 added
	items in the item pane."""
	#categories = session.query(Category).all()
	#latestItems = session.query(Item).limit(5)
	#return render_template('main.html', categories=categories)
	return "This is a test page for mainMenu()"

@app.route('/main/<int:category_id>/')
def categoryItems(category_id):
	"""Updates the item pane with a list of items specific to that category"""
	#items = session.query(Item).filter_by(category_id=category_id)
	#return render_template('main.hmtl', items=items, category_id=category_id)
	return "This is a test page for categoryItems"

@app.route('/main/new/')
def newCategory():
	"""Creates a new category -- Requires Admin Privileges"""
	return "This is a test page for newCategory()"

@app.route('/main/newItem/')
def newUItem():
	"""Creates a new item for an unspecified category.
	This WILL have a drop down menu to specify the category."""
	return "This is a test page for newUItem()"

@app.route('/main/<int:category_id>/newItem/')
def newSItem(category_id):
	"""Creates a new item for a specified category.
	This WILL NOT have a drop down menu to specify a different category."""
	return "This is a test page for newSItem()"

# Routing for item menu
@app.route('/main/<int:category_id>/item/<int:item_id>/')
def itemMenu(category_id, item_id):
	"""Returns details about the particular item in the item page"""
	return "This is a test page for itemMenu()"

@app.route('/main/<int:category_id>/item/<int:item_id>/edit/')
def editItem(category_id, item_id):
	"""Edit the details about the particular item"""
	return "This is a test page for editItem()"
	
@app.route('/main/<int:category_id>/item/<int:item_id>/delete')
def deleteItem(category_id, item_id):
	"""Deletes the particular item"""
	return "This is a test page for deleteItem()"

if __name__ == '__main__':
	app.secret_key = 'root'
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)
