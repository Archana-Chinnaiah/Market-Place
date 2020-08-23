from database_connection import db_connection
from item_package import item as i

session = db_connection()

def items_in_category(category_id):
    items = session.query(i.Item).filter_by(category_id=category_id).all()
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
    return items_list