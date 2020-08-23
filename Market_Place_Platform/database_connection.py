from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def db_connection():
    engine = create_engine("postgresql://postgres:archu@localhost:1521/market_place")
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
print("Successfully connected to the Database")
