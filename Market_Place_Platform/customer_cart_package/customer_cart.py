from base_class import *
from customer_package import customer
class CustomerCart(Base):
    __tablename__ = 'customer_cart'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.customer_id'))
    item_id = Column(Integer, ForeignKey('item.item_id'))
    quantity = Column(Integer)
    total_price = Column(Integer)