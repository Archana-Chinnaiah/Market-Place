from flask import Flask, jsonify, request
from marketplace import Category, Item,Customer, CustomerCart
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:archu@localhost:1521/market_place")
Session = sessionmaker(bind=engine)
session = Session()
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        user = session.query(Customer).filter_by(username=username,password=password).first()
        if user:
            return "Logged in Successfully"
        else:
            return "Invalid Credentials"

@app.route("/categories", methods=["GET"])
def list_categories():
    categories = []
    category = session.query(Category).all()

    for category in category:
        obj = {
            'id': category.category_id,
            'name': category.category_name,
            'description': category.description
        }
        categories.append(obj)
    return jsonify(categories)

@app.route("/categories/<category_id>/items", methods=["GET"])
def item_list(category_id):
    items = session.query(Item).filter_by(category_id=category_id).all()
    items_list = []
    for item in items:
        obj = {
            'id': item.item_id,
            'name': item.item_name,
            'seller name': item.seller_name,
            'available quantity': item.available_quantity,
            'description': item.description
        }
        items_list.append(obj)
    return jsonify(items_list)

@app.route("/cart/<customer_id>", methods=["GET"])
def item_list(customer_id):
    items_in_cart = session.query(CustomerCart).filter_by(customer_id=customer_id).all()
    cart_list = []
    for item in items_in_cart:
        obj = {
            'item id': item.item_id,
            'quantity': item.quantity,
            'Total_price': int(item.total_price)
        }
        cart_list.append(obj)
    return jsonify(cart_list)

@app.route("/cart", methods=["POST"])
def add_to_cart():
    customer_id = request.form['customer_id']
    item_id = request.form['item_id']
    quantity = request.form['quantity']
    exists = session.query(CustomerCart).filter_by(customer_id=customer_id,item_id=item_id).first()
    if exists:
        return "This item has been already in your cart"
    else:
        avail_quantity = session.query(Item).filter_by(item_id=item_id).first()
        if int(avail_quantity.available_quantity) >= int(quantity):
            total = int(avail_quantity.price) * int(quantity)
            result = CustomerCart(customer_id=customer_id, item_id=item_id, quantity=quantity, total_price=total)
            session.add(result)
            session.commit()
            return "Successfully Added to cart"
        else:
            return "Out of stock"

@app.route("/cart/<cart_id>", methods=["PUT"])
def update_quantity(cart_id):
    quantity = request.form['quantity']
    cart = session.query(CustomerCart).filter_by(id=cart_id).first()
    item = cart.item_id
    need = session.query(Item).filter_by(item_id=item).first()
    cart.quantity = quantity
    cart.total_price = int(quantity) * int(need.price)
    session.add(cart)
    session.commit()
    return "Updated Successfully"

@app.route("/cart/<cart_id>", methods=["DELETE"])
def delete_items(cart_id):
    item = session.query(CustomerCart).filter_by(id=cart_id).one()
    session.delete(item)
    session.commit()
    return "deleted Successfully"

@app.route("/logout",methods=["GET"])
def logout():
    return "you have logged out successfully"


if __name__ == "__main__":
    app.run()
