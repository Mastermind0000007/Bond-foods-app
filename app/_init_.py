*app/*init*.py*
```
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
```
This file initializes the Flask app, loads the configuration, and sets up the database connection.

*app/models.py*
```
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"User('{self.email}')"

class FoodItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"FoodItem('{self.name}')"
```
This file defines the database models using Flask-SQLAlchemy.

*app/routes.py*
```
from app import app
from app.models import User, FoodItem

@app.route('/')
def index():
    return 'Welcome to the Food App!'

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.email for user in users])

@app.route('/food-items', methods=['GET'])
def get_food_items():
    food_items = FoodItem.query.all()
    return jsonify([food_item.name for food_item in food_items])
```
This file defines the API endpoints using Flask.

*app/schemas.py*
```
from marshmallow import Schema, fields

class UserSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)

class FoodItemSchema(Schema):
    name = fields.Str(required=True)
    price = fields.Float(required=True)
```
This file defines the data validation schemas using Marshmallow.

*app/services.py*
```
from app.models import User, FoodItem

def create_user(email, password):
    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return user

def create_food_item(name, price):
    food_item = FoodItem(name=name, price=price)
    db.session.add(food_item)
    db.session.commit()
    return food_item
```
This file defines the business logic and services.
