from database_connection import db_connection
from customer_package import customer as c


session = db_connection()

def login_method(username,password):
    print("hi")
    user = session.query(c.Customer).filter_by(username=username,password=password).first()
    if user != None:
        id = user.customer_id
        print(id)
        return True,id
    else:
        return False,username



