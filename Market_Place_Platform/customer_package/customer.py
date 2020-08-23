from base_class import *
class Customer(Base):
    __tablename__ = 'customer'
    customer_id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, unique=True, nullable=False)
    address = Column(String, unique=True, nullable=False)
    mobile_no = Column(Integer, nullable=False)