from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application import db
from application.models import *
from flask_login import current_user

def Valid_role():
    message = 'role is not in the permited roles'
    def _Valid_role(form, feild):
        if str(User_roles.query.filter_by(role = feild.data).all()) == '[]':
            raise ValidationError("Role enter is not in the allowed roles"+User_roles.query.all())
    return _Valid_role

def Valid_id():
    message = 'Id is not yet assigned to a gift'
    def _Valid_id(form, feild):
        if str(Gift_list.query.filter_by(id = feild.data).all()) == '[]':
            raise ValidationError("The ID ented has no gift assigned")
    return _Valid_id

def Valid_float():
    message = 'Value not empty or float'
    def _Valid_float(form, feild):
        if feild.data != '':
            try:
                float(element)
            except ValueError:
                raise ValidationError("")        
    return _Valid_float

class UpdateAccountForm(FlaskForm):
    first_name = StringField('First Name',
        validators=[
            DataRequired(),
            Length(min=1, max=30)
        ])
    last_name = StringField('Last Name',
        validators=[
            DataRequired(),
            Length(min=1, max=30)
        ])
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ])
    submit = SubmitField('Update')

    def validate_email(self,email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already in use')


class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField('Password',
        validators=[
            DataRequired()
        ]
    )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',
    validators=[
        DataRequired(),
        Length(min=1, max=30)
        ]
    )
    last_name = StringField('Last Name',
    validators=[
        DataRequired(),
        Length(min=1, max=30)
        ]
    )
    email = StringField('Email',
        validators = [
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField('Password',
        validators = [
            DataRequired(),
        ]
    )
    confirm_password = PasswordField('Confirm Password',
        validators = [
            DataRequired(),
            EqualTo('password')
        ]
    )
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already in use')


class Add_Gift_Form(FlaskForm):
    name = StringField('Gift name',
            validators = [
                DataRequired(),
                Length(min=1,max=50)
            ]
        )
    description = StringField('Description',
            validators = [
                DataRequired(),
                Length(min=5,max=500)
            ]
        )
    url = StringField('Url for gift',
            validators = [
                DataRequired(),
                Length(min=5,max=500)
            ]
        )
    price = FloatField('Price',
            validators = [
                DataRequired()
            ]
        )
    submit = SubmitField('Add gift')

class Modify_Account_Form(FlaskForm):

    def valid_role(self, role):
        roles = User_roles.query.all()

        if role not in roles:
            raise ValidationError('Not a valid role')

    id = IntegerField('ID of account being altered',
            validators = [
                DataRequired()
            ]
        )
    first_name = StringField('First name',
            validators = [
            ]
        )
    last_name = StringField('Last name',
            validators = [
            ]
        )
    role = StringField("User role", 
            validators = [
                Valid_role()
            ]
        )
    email = StringField('Email',
        validators = [
        ]
    )
    password = PasswordField('Password',
        validators = [
        ]
    )
    confirm_password = PasswordField('Confirm Password',
        validators = [
            EqualTo('password')
        ]
    )
    submit = SubmitField('Change user')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already in use')


class Modify_Gift_Form(FlaskForm):



    id = IntegerField('ID of gift being altered',
            validators = [
                DataRequired(),
                Valid_id()
            ]
        )
    name = StringField('Gift name',
            validators = [
            ]
        )
    description = StringField('Description',
            validators = [
            ]
        )
    url = StringField('Url for gift',
            validators = [
            ]
        )
    price = FloatField('Price'
        )
    submit = SubmitField('update gift')
