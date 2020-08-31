from flask import request, Blueprint,jsonify
from customer_package.customer_dao import *
from flask_cors import CORS,cross_origin

customer_link = Blueprint('customer_link',__name__)
CORS(customer_link,resource={r"/api/*":{"origins":"*"}})


@customer_link.route("/login", methods=["GET","POST"])
@cross_origin()
def login():
    data = request.get_json()
    if request.method == "POST":
        username = data['username']
        password = data['password']
        print(username)
        print((password))
        (status,customer_id) =  login_method(username,password)
        print(status)
        if status == True:
            print("hi")
            data = {
                "status":200,
                "customer_id":customer_id
            }
            print(data)
            return jsonify(data)
        elif status == False:
            print("hello")
            data = {
                "status":404,
                "message":"invalid credentials"
            }
            return jsonify(data)


@customer_link.route("/logout",methods=["GET"])
def logout():
    return "you have logged out successfully"

