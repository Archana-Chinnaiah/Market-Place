from base_class import *
class Category(Base):
    __tablename__ = 'category'
    category_id = Column(Integer, primary_key=True)
    category_name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=False)