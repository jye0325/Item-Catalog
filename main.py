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
"""

# Routing for login
@app.route('/login/')
def login():
    """This returns a webpage for users to login"""
    state = ''.join(random.choice(string.ascii_uppercase+string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)
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
	categories = session.query(Category).all()
	latestItems = session.query(Item).limit(5)
	return render_template('main.html', categories=categories, latestItems=latestItems)

@app.route('/main/<int:category_id>/')
def categoryItems(category_id):
	"""Updates the item pane with a list of items specific to that category"""
	categories = session.query(Category).all()
	items = session.query(Item).filter_by(category_id=category_id)
	return render_template('main.html', categories=categories, items=items, category_id=category_id)

@app.route('/main/newCategory/', methods=['GET','POST'])
def newCategory():
	"""Creates a new category -- Requires Admin Privileges"""
	if request.method == 'POST':
		category = Category(name=request.form['name'])
		session.add(category)
		session.commit()
		flash('Successfully added new category, ' + category.name)
		return redirect(url_for('mainMenu'))
	else:
		return render_template('newCategory.html')

@app.route('/main/<int:category_id>/edit', methods=['GET','POST'])
def editCategory(category_id):
	"""Edits a specified category."""
	category = session.query(Category).filter_by(id=category_id).one()
	if request.method == 'POST':
		category.name = request.form['name']
		session.add(category)
		session.commit()
		flash('Successfully editted category, ' + category.name)
		return redirect(url_for('mainMenu'))
	else:
		return render_template('editCategory.html', category=category, id=category_id)

@app.route('/main/<int:category_id>/delete', methods=['GET','POST'])
def deleteCategory(category_id):
	"""Deletes a specific category."""
	category = session.query(Category).filter_by(id=category_id).one()
	if request.method == 'POST':
		session.delete(category)
		session.commit()
		flash('Successfully deleted category, ' + category.name)
		return redirect(url_for('mainMenu'))
	else:
		return render_template('deleteCategory.html', category=category, id=category_id)

# Routing for item menu
@app.route('/main/<int:category_id>/item/<int:item_id>/')
def itemMenu(category_id, item_id):
	"""Returns details about the particular item in the item page"""
	category = session.query(Category).filter_by(category_id=category_id).one()
	item = session.query(Item).filter_by(category_id=category_id, id=item_id).one()
	return render_template('item.html', category=category, item=item)

@app.route('/main/<int:category_id>/newItem/', methods=['GET','POST'])
def newItem(category_id):
	"""Creates a new item for an unspecified category."""
	if request.method == 'POST':
		item = Item(name=request.form['name'], category_id=category_id, description=request.form['description'])
		session.add(item)
		session.commit()
		flash('Successfully added new category, ' + item.name)
		return redirect(url_for('mainMenu'))
	else:
		return render_template('newItem.html', id=category_id)

@app.route('/main/<int:category_id>/item/<int:item_id>/edit/', methods=['GET','POST'])
def editItem(category_id, item_id):
	"""Edit the details about the particular item"""
	item = session.query(Item).filter_by(category_id=category_id, id=item_id).one()
	if request.method == 'POST':
		item.name=request.form['name']
		item.description=request.form['description']
		session.add(item)
		session.commit()
		flash('Successfully editted item, ' + item.name)
		return redirect(url_for('mainMenu'))
	else:
		return render_template('editItem.html', item=item, id=category_id, item_id=item_id)
	
@app.route('/main/<int:category_id>/item/<int:item_id>/delete', methods=['GET', 'POST'])
def deleteItem(category_id, item_id):
	"""Deletes the particular item"""
	item = session.query(Item).filter_by(category_id=category_id, id=item_id).one()
	if request.method == 'POST':
		session.delete(item)
		session.commit()
		flash('Successfully deleted item, ' + item.name)
		return redirect(url_for('mainMenu'))
	else:
		return render_template('deleteItem.html', item=item, id=category_id, item_id=item_id)
"""
@app.route('/main/<int:category_id>/newItem/', methods=['GET','POST'])
def newSItem(category_id):
	#Creates a new item for a specified category.
	#This WILL NOT have a drop down menu to specify a different category.
	if request.method == 'POST':
		item = Item(name=request.form['name'], description=request.form['description'], category_id=category_id)
		session.add(item)
		session.commit()
		flash('Successfully added new item, ' + item.name)
		return render_template('main.html')
	else:
		return render_template('new.html')
"""

#JSON 
@app.route('/main/JSON')
def mainMenuJSON():
	category = session.query(Category).all()
	return jsonify(Category=[i.serialize for i in category])

@app.route('/main/<int:category_id>/item/JSON')
def itemMenuJSON(category_id):
	category = session.query(Category).all()
	item = session.query(Item).filter_by(category_id=category_id).all()
	return jsonify(Item=[i.serialize for i in item])

@app.route('/main/<int:category_id>/item/<int:item_id>/JSON')
def specificItemJSON(category_id, item_id):
	category = session.query(Category).all()
	item = session.query(Item).filter_by(id=item_id, category_id=category_id).one()
	return jsonify(Item=item.serialize)

if __name__ == '__main__':
	app.secret_key = 'root'
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)