from database_connection import db_connection
from category_package import category as c

session = db_connection()

def available_categories():
    category_list = []
    categories = session.query(c.Category).all()
    for category in categories:
        obj = {
            'category_id': category.category_id,
            'name': category.category_name,
            'description': category.description
        }
        category_list.append(obj)
    return category_list