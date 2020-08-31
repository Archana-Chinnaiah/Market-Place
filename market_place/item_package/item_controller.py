from flask import jsonify, Blueprint
from item_package.item_dao  import *


item_link = Blueprint('item_link',__name__)


@item_link.route("/categories/<category_id>/items", methods=["GET"])
def items_list(category_id):
    return jsonify(items_in_category(category_id))
