from database_connection import db_connection
from item_package import item as i

session = db_connection()

def items_in_category(category_id):
    items = session.query(i.Item).filter_by(category_id=category_id).all()
    items_list = []
    for item in items:
        obj = {
            'item_id': item.item_id,
            'name': item.item_name,
            'seller_name': item.seller_name,
            'available_quantity': item.available_quantity,
            'description': item.description,
            'price': float(item.price),
            'category id':int(item.category_id)
        }
        items_list.append(obj)
    return items_list