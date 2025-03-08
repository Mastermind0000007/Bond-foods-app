```
from app.models import User, FoodItem, Order

def create_user(email, password):
    user = User(email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return user

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def create_food_item(name, price, description=None):
    food_item = FoodItem(name=name, price=price, description=description)
    db.session.add(food_item)
    db.session.commit()
    return food_item

def get_food_item_by_id(id):
    return FoodItem.query.get(id)

def create_order(user_id, food_item_id, quantity):
    order = Order(user_id=user_id, food_item_id=food_item_id, quantity=quantity)
    db.session.add(order)
    db.session.commit()
    return order

def get_orders_by_user_id(user_id):
    return Order.query.filter_by(user_id=user_id).all()
```
