from flask import request,jsonify, Blueprint
from customer_cart_package.customer_cart_dao import  *
from flask_cors import CORS,cross_origin
from item_package import item as i

customer_cart_link = Blueprint('custoemr_cart_link',__name__)
CORS(customer_cart_link,resource={r"/api/*":{"origins":"*"}})

@customer_cart_link.route("/cart", methods=["POST"])
@cross_origin()
def add_to_cart():
    data = request.get_json()
    customer_id = data['customer_id']
    item_id = data['item_id']
    (status,message) = item_add_to_cart(customer_id,item_id)
    if status == True and message == True:
        print("add to cart")
        datae={
            'message':'success',
            'customer_id':customer_id,
            'item_id':item_id,
            }
        print(datae)
        return jsonify(datae)
    elif status == True and message == False:
        print("add in exsists")
        datas={
            'message':'exsists',
            'customer_id':customer_id,
            'item_id':item_id
        }
        return jsonify(datas)
    else:
        return jsonify({'status':'out of stock'})


@customer_cart_link.route("/cart/<customer_id>", methods=["GET"])
@cross_origin()
def item_list(customer_id):
    return jsonify(items_in_cart(customer_id))

@customer_cart_link.route("/cart/<cart_id>", methods=["PUT"])
@cross_origin()
def update_quantity(cart_id):
    data = request.get_json()
    quantity = data['quantity']
    (msg,cart_id) = update_method(cart_id,quantity)
    if msg == True:
        result ={
            'msg':'updated',
            'id':cart_id
        }
        return jsonify(result)
    if msg == False:
        return {'msg':'out of stock'}


@customer_cart_link.route("/cart/<cart_id>", methods=["DELETE"])
@cross_origin()
def delete_items(cart_id):
    msg = delete_method(cart_id)
    if msg == True:
        return jsonify(({'msg':'deleted'}))


