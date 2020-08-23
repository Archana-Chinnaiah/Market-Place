from database_connection import db_connection
from customer_package import customer as c

session = db_connection()

def login_method(username,password):
    user = session.query(c.Customer).filter_by(username=username,password=password).first()
    if user:
        return "Logged in Successfully"
    else:
        return "Invalid Credentials"
