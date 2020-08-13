from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class Category(Base):
    __tablename__ = 'category'
    category_id = Column(Integer, primary_key=True)
    category_name = Column(String,unique=True,nullable=False)
    description = Column(String,nullable=False)


class Item(Base):
    __tablename__ = 'item'
    item_id = Column(Integer, primary_key=True)
    item_name = Column(String,nullable=False)
    price = Column(Integer,nullable=False)
    seller_name = Column(String,nullable=False)
    availabale_quantity = Column(Integer)
    category_id = Column(Integer, ForeignKey('Category.category_id'))

class Customer(Base):
    __tablename__ = 'customer'
    customer_id = Column(Integer, primary_key=True)
    username  = Column(String,unique=True,nullable=False)
    password = Column(String,unique=True,nullable=False)
    address = Column(String,unique=True,nullable=False)
    mobile_no = Column(Integer,nullable=False)



class CustomerCart(Base):
    __tablename__ = 'customer_cart'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.customer_id'))
    item_id = Column(Integer, ForeignKey('item.item_id'))
    quantity = Column(Integer)
    total_price = Column(Integer)