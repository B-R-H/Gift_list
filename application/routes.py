from application import app, db, bcrypt
from flask import render_template, redirect, url_for, request
from application.models import *
from application.forms import *
from flask_login import login_user, current_user, logout_user, login_required


# define routes for / & /home, this function will be called when these are accessed
@app.route('/')
@app.route('/home')
def home():
    list_of_gifts = Gift_list.query.all()
    return render_template('home.html', title='Home' , gifts=list_of_gifts)


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name        
        form.email.data = current_user.email        
    return render_template('account.html', title='Account', form=form)

@app.route("/account/delete", methods=["GET", "POST"])
@login_required
def account_delete():
    user = current_user.id
    account = User.query.filter_by(id=user).first()
    user_posts = Posts.query.filter_by(user_id = user).all()
    logout_user()
    for i in user_posts:
        db.session.delete(i)
    db.session.delete(account)
    db.session.commit()
    return redirect(url_for('register'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()

    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)
        
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=hash_pw
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/admin",methods=['GET', 'POST'])
@login_required
def admin():
    if current_user.permission == "Guest":
        return redirect(url_for('home'))
    gifts = Gift_list.query.all()

    form = Modify_Gift_Form()

    if form.validate_on_submit():
        gift = Gift_list.query.filter_by(id=form.id.data).first()
        if gift:
            if form.name.data != '':
                gift.name = form.name.data
                db.session.commit()
            if form.description.data != '':
                gift.description = form.description.data
                db.session.commit()
            if form.url.data != '':
                gift.url = form.url.data
                db.session.commit()
            if form.price.data != '':
                gift.price = float(form.price.data)
                db.session.commit()
            return redirect(url_for('admin'))

    return render_template('admin.html',title='Admin page',gifts=gifts,form =form)

@app.route("/add_gift", methods=['GET', 'POST'])
@login_required
def add_gift():
    if current_user.permission == "Guest":
        return redirect(url_for('home'))

    form = Add_Gift_Form()
    if form.validate_on_submit():

        gift = Gift_list(
                name = form.name.data,
                description = form.description.data,
                url = form.url.data,
                price = form.price.data
            )

        db.session.add(gift)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('giftAdd.html',title='Add gifts',form = form)

@app.route("/edit_users", methods=['GET', 'POST'])
@login_required
def edit_users():
    if current_user.permission not in ["Couple","2nd line","Wedding party"]:
        return redirect(url_for('home'))

    users=User.query.all()

    form = Modify_Account_Form()
    if form.validate_on_submit():
        user = User.query.filter_by(id=form.id.data).first()
        if user:
            if form.first_name.data != '':
                user.first_name = form.first_name.data
                db.session.commit()
            if form.last_name.data != '':
                user.last_name = form.last_name.data
                db.session.commit()
            if form.role.data in ["Guest","Couple","2nd line","Wedding party"]:
                user.permission = form.role.data
                db.session.commit()
            if form.email.data != '':
                user.email = form.email.data
                db.session.commit()
            if form.password.data != '':
                user.password = bcrypt.generate_password_hash(form.password.data)
                db.session.commit()
            return redirect(url_for('edit_users'))
        else:
            if form.role not in ["Guest","Couple","2nd line","Wedding party"]:
                r = "Guest"
            else:
                r= form.role.data
            user = User(
                first_name = form.first_name.data,
                last_name = form.last_name.data,
                permission = r,
                email = form.email.data,
                password = bcrypt.generate_password_hash(form.password.data)
            )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('edit_users'))


    return render_template('editAccounts.html',title='Edit users',form = form , users= users)

@app.route('/admin/delete/<id>')
@login_required
def delete_gift_by_id(id):
    if current_user.permission == "Couple":
        gift = Gift_list.query.filter_by(id=id).first()
        db.session.delete(gift)
        db.session.commit()
        return redirect(url_for('home'))

