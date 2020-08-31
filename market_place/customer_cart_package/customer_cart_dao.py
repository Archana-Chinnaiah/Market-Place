from database_connection import db_connection
from customer_cart_package import customer_cart as c
from item_package import item as i

session = db_connection()


def item_add_to_cart(customer_id,item_id):
    print("add to cart")
    quantity = 1
    exists = session.query(c.CustomerCart).filter_by(customer_id=customer_id,item_id=item_id).first()
    if exists:
        return True,False
    else:
        avail_quantity = session.query(i.Item).filter_by(item_id=item_id).first()
        if int(avail_quantity.available_quantity) >= int(quantity):
            total = int(avail_quantity.price)
            result = c.CustomerCart(customer_id=customer_id, item_id=item_id, quantity=quantity, total_price=total)
            session.add(result)
            session.commit()
            return True,True
        else:
            return False,False

def items_in_cart(customer_id):
    item_in_cart = session.query(c.CustomerCart).filter_by(customer_id=customer_id).all()
    items = session.query(i.Item.item_name).filter_by().all()
    cart_list = []

    for item in item_in_cart:
        obj={}
        obj['cart_id'] = item.id
        obj['customer_id'] = item.customer_id
        obj['item_id'] = item.item_id
        obj['quantity'] = item.quantity
        obj['total_price'] = float(item.total_price)
        item_name = str(items[(item.item_id)-1]).replace("('","")
        obj['item_name'] = item_name.replace("',)","")
        cart_list.append(obj)
    return cart_list

def update_method(cart_id,quantity):
    cart = session.query(c.CustomerCart).filter_by(id=cart_id).first()
    item = cart.item_id
    needed_quantity = session.query(i.Item).filter_by(item_id=item).first()
    print(quantity)
    cart.quantity = quantity
    if int(needed_quantity.available_quantity) >= int(quantity):
        cart.total_price = int(quantity) * int(needed_quantity.price)
        session.add(cart)
        session.commit()

        return True,cart_id
    else:
        return False,0

def delete_method(cart_id):
    item = session.query(c.CustomerCart).filter_by(id=cart_id).one()
    session.delete(item)
    session.commit()
    return True
