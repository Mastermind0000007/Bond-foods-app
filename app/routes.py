```
from app import app
from app.models import User, FoodItem, Order
from flask import jsonify, request

User Routes
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.email for user in users])

@app.route('/users', methods=['POST'])
def create_user():
    email = request.json.get('email')
    password = request.json.get('password')
    user = User(email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

FoodItem Routes
@app.route('/food-items', methods=['GET'])
def get_food_items():
    food_items = FoodItem.query.all()
    return jsonify([food_item.name for food_item in food_items])

@app.route('/food-items', methods=['POST'])
def create_food_item():
    name = request.json.get('name')
    price = request.json.get('price')
    food_item = FoodItem(name=name, price=price)
    db.session.add(food_item)
    db.session.commit()
    return jsonify({'message': 'Food item created successfully'}), 201

Order Routes
@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([order.id for order in orders])

@app.route('/orders', methods=['POST'])
def create_order():
    user_id = request.json.get('user_id')
    food_item_id = request.json.get('food_item_id')
    quantity = request.json.get('quantity')
    order = Order(user_id=user_id, food_item_id=food_item_id, quantity=quantity)
    db.session.add(order)
    db.session.commit()
    return jsonify({'message': 'Order created successfully'}), 201
```


These routes will handle the API requests and return responses accordingly.
