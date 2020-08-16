from market_endpoints import *
from marketplace import *


def login_method(username,password):
    user = session.query(Customer).filter_by(username=username,password=password).first()
    if user:
        return "Logged in Successfully"
    else:
        return "Invalid Credentials"

def available_categories():
    category_list = []
    categories = session.query(Category).all()
    for category in categories:
        obj = {
            'id': category.category_id,
            'name': category.category_name,
            'description': category.description
        }
        category_list.append(obj)
    return category_list


def items_in_category(category_id):
    items = session.query(Item).filter_by(category_id=category_id).all()
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

def item_add_to_cart(customer_id,item_id,quantity):
    exists = session.query(CustomerCart).filter_by(customer_id=customer_id,item_id=item_id).first()
    if exists:
        return "This item has been already in your cart"
    else:
        avail_quantity = session.query(Item).filter_by(item_id=item_id).first()
        if int(avail_quantity.available_quantity) >= int(quantity):
            total = int(avail_quantity.price) * int(quantity)
            result = CustomerCart(customer_id=customer_id, item_id=item_id, quantity=quantity, total_price=total)
            session.add(result)
            session.commit()
            return "Successfully Added to cart"
        else:
            return "Out of stock"

def items_in_cart(customer_id):
    item_in_cart = session.query(CustomerCart).filter_by(customer_id=customer_id).all()
    cart_list = []
    for item in item_in_cart:
        obj = {
            'item id': item.item_id,
            'quantity': item.quantity,
            'Total_price': int(item.total_price)
        }
        cart_list.append(obj)
    return cart_list

def update_method(cart_id,quantity):
    cart = session.query(CustomerCart).filter_by(id=cart_id).first()
    item = cart.item_id
    needed_quantity = session.query(Item).filter_by(item_id=item).first()
    cart.quantity = quantity
    if int(needed_quantity.available_quantity) >= int(quantity):
        cart.total_price = int(quantity) * int(needed_quantity.price)
        session.add(cart)
        session.commit()
        return "Updated Successfully"
    else:
        return "Out of Stock"

def delete_method(cart_id):
    item = session.query(CustomerCart).filter_by(id=cart_id).one()
    session.delete(item)
    session.commit()
    return "deleted Successfully"
