from base_class import *
class Item(Base):
    __tablename__ = 'item'
    item_id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    seller_name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    available_quantity = Column(Integer)
    category_id = Column(Integer, ForeignKey('Category.category_id'))
