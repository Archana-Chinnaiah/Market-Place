from flask import jsonify, Blueprint
from category_package.category_dao import *

category_link = Blueprint('category_link',__name__)

@category_link.route("/categories", methods=["GET"])
def list_categories():
    return jsonify(available_categories())


