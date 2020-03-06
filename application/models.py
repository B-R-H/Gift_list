from application import db, login_manager
from flask_login import UserMixin

class User_roles(db.Model):
    role = db.Column(db.String(30), primary_key=True)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable = False)
    last_name = db.Column(db.String(30), nullable = False)
    permission = db.Column(db.String(30), db.ForeignKey('user_roles.role'), default='Guest')
    email = db.Column(db.String(150), nullable = False, unique=True)
    password = db.Column(db.String(500), nullable = False)

    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.id), '\r\n',
            'Email: ', self.email, '\r\n',
            'Name: ', self.first_name, ' ', self.last_name
        ])

class Gift_list(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(1000))
    url = db.Column(db.String(100))
    price = db.Column(db.Float)

class Claimed_compilation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gift_id = db.Column(db.Integer, db.ForeignKey('gift_list.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


