from flask import Flask, jsonify, request
from marketplace import Category, Item, Customer, CustomerCart
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:archu@localhost:1521/market_place")
Session = sessionmaker(bind=engine)
session = Session()

app=Flask(__name__)
app.config["DEBUG"]=True


@app.route("/categories", methods = ["GET"])
def list_categories():
    categories=[]
    category =session.query(Category).all()
    for category in category:
        obj = {
            'id': category.category_id,
            'name': category.category_name,
            'description':category.description
        }
        categories.append(obj)
    return jsonify(categories)


@app.route("/cart", methods = ["POST"])
def add_to_cart():
    customer_id = request.form['customer_id']
    item_id = request.form['item_id']
    quantity = request.form['quantity']
    result=CustomerCart(customer_id =customer_id,item_id=item_id,quantity=quantity)
    session.add(result)
    session.commit()
    return "Successfully Added to cart"


if __name__ == "__main__":
    app.run()
