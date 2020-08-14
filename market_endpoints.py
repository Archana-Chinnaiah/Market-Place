from flask import Flask, request,jsonify,url_for
from marketplace import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from market_methods import *

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
        return login_method(username,password)

@app.route("/categories", methods=["GET"])
def list_categories():
    return available_categories()

@app.route("/categories/<category_id>/items", methods=["GET"])
def items_list(category_id):
    return items_in_category(category_id)

@app.route("/cart", methods=["POST"])
def add_to_cart():
    customer_id = request.form['customer_id']
    item_id = request.form['item_id']
    quantity = request.form['quantity']
    return item_add_to_cart(customer_id,item_id,quantity)

@app.route("/cart/<customer_id>", methods=["GET"])
def item_list(customer_id):
    return items_in_cart(customer_id)

@app.route("/cart/<cart_id>", methods=["PUT"])
def update_quantity(cart_id):
    quantity = request.form['quantity']
    return update_method(cart_id,quantity)

@app.route("/cart/<cart_id>", methods=["DELETE"])
def delete_items(cart_id):
    return delete_method(cart_id)

@app.route("/logout",methods=["GET"])
def logout():
    return "you have logged out successfully"


if __name__ == "__main__":
    app.run()