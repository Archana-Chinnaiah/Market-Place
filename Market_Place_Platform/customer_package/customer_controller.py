from flask import request, Blueprint
from customer_package.customer_dao import *

customer_link = Blueprint('customer_link',__name__)


@customer_link.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        return login_method(username,password)


@customer_link.route("/logout",methods=["GET"])
def logout():
    return "you have logged out successfully"

