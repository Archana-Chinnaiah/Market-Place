from database_connection import db_connection
from customer_cart_package import customer_cart as c
from item_package import item as i

session = db_connection()

def item_add_to_cart(customer_id,item_id,quantity):
    exists = session.query(c.CustomerCart).filter_by(customer_id=customer_id,item_id=item_id).first()
    if exists:
        return "This item has been already in your cart"
    else:
        avail_quantity = session.query(i.Item).filter_by(item_id=item_id).first()
        if int(avail_quantity.available_quantity) >= int(quantity):
            total = int(avail_quantity.price) * int(quantity)
            result = c.CustomerCart(customer_id=customer_id, item_id=item_id, quantity=quantity, total_price=total)
            session.add(result)
            session.commit()
            return "Successfully Added to cart"
        else:
            return "Out of stock"

def items_in_cart(customer_id):
    item_in_cart = session.query(c.CustomerCart).filter_by(customer_id=customer_id).all()
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
    cart = session.query(c.CustomerCart).filter_by(id=cart_id).first()
    item = cart.item_id
    needed_quantity = session.query(i.Item).filter_by(item_id=item).first()
    cart.quantity = quantity
    if int(needed_quantity.available_quantity) >= int(quantity):
        cart.total_price = int(quantity) * int(needed_quantity.price)
        session.add(cart)
        session.commit()
        return "Updated Successfully"
    else:
        return "Out of Stock"

def delete_method(cart_id):
    item = session.query(c.CustomerCart).filter_by(id=cart_id).one()
    session.delete(item)
    session.commit()
    return "deleted Successfully"
