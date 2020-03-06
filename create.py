from application import db
from application.models import *

db.drop_all()
db.create_all()

usRoles = ["Guest","Couple","2nd line","Wedding party"]

for i in usRoles:
    roleAdd = User_roles(role = i)
    db.session.add(roleAdd)
    db.session.commit()

