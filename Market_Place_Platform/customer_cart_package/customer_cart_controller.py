from flask import request,jsonify, Blueprint
from customer_cart_dao import *

customer_cart_link = Blueprint('custoemr_cart_link',__name__)


@customer_cart_link.route("/cart", methods=["POST"])
def add_to_cart():
    customer_id = request.form['customer_id']
    item_id = request.form['item_id']
    quantity = request.form['quantity']
    return item_add_to_cart(customer_id,item_id,quantity)

@customer_cart_link.route("/cart/<customer_id>", methods=["GET"])
def item_list(customer_id):
    return jsonify(items_in_cart(customer_id))

@customer_cart_link.route("/cart/<cart_id>", methods=["PUT"])
def update_quantity(cart_id):
    quantity = request.form['quantity']
    return update_method(cart_id,quantity)

@customer_cart_link.route("/cart/<cart_id>", methods=["DELETE"])
def delete_items(cart_id):
    return delete_method(cart_id)


