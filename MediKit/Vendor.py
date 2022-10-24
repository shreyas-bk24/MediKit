from random import random, randint

from flask import render_template, request, url_for, flash, session
from flask_login import login_required, login_user, LoginManager, current_user, logout_user
from sqlalchemy import delete, update
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from MediKit import app
from MediKit.models import db, Products, Vendor, Cart
from MediKit.routes import csrf
from flask_mail import Message
from MediKit.routes import mail

vendor_login = LoginManager()
vendor_login.init_app(app)
vendor_login.login_view = 'vendor_login'


@vendor_login.user_loader
def load_user(id):
    return Vendor.query.get(int(id))


@app.route('/vendor_home')
@login_required
def vendor_home():
    username = db.session.query(Vendor.first_name).filter_by(id=current_user.id).first()
    products = db.session.query(Products).filter(Products.vendor_id == current_user.id).all()
    print(username)
    return render_template('vendor_dashboard.html', username=username, products=products)


@app.route('/vendor_login', methods=['GET', 'POST'])
def vendor_login():
    if request.method == 'POST':
        email = request.form.get('email')
        password_entered = request.form.get('password')
        vendor = Vendor.query.filter_by(email=email).first()
        if vendor:
            try:
                if check_password_hash(vendor.password, password_entered):
                    login_user(vendor)
                    return redirect('vendor_home')
                else:
                    flash(message="Incorrect username or password", category="danger")
            except Exception:
                return render_template('404.html')
        else:
            flash("No user account found on this email,please create your own account")
            return redirect(url_for('vendor_signup'))
    return render_template('vendor_login.html')

# creating a new vendor account
@app.route('/vendor_signup', methods=['GET', 'POST'])
def vendor_signup():
    if request.method == 'POST':
        # generating a password
        hash_and_salted_password = generate_password_hash(
            request.form.get('pwd'),
            method='pbkdf2:sha256',
            salt_length=8)
        cpwd=request.form.get('cpwd')
        # confirm password

        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        user_exists = Vendor.query.filter_by(email=email).first()
        vid = f"VD{randint(100000, 999999)}"

        if not user_exists:
           if check_password_hash(hash_and_salted_password,cpwd):
                new_vendor = Vendor(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=hash_and_salted_password,
                    vendor_id=vid
                )
                try:
                    db.session.add(new_vendor)
                    db.session.commit()
                    # login with the new user account
                    login_user(new_vendor)

                    sender = "bharadwatest@gmail.com"
                    receiver = new_vendor.email
                    message = f"Hello { new_vendor.first_name },\nThanks for being a part of Supply chain of MediKit\n\nYour vendor ID is {new_vendor.vendor_id}\n\nBest wishes from Team MediKit\n\n <b>MediKit</b>"
                    subject = "Welcome to MediKit family"
                    # sending mail to new vendors
                    msg = Message(subject, sender=sender, recipients=[receiver])
                    msg.body = message
                    mail.send(msg)

                    return redirect('vendor_home')

                except Exception:
                    return render_template('404.html')
           else:
                flash("Passwords should match")
        else:
            flash("Email already exists you can login to your")
            return redirect(url_for('vendor_login'))
    return render_template("vendor_signin.html")


@app.route('/vendor')
@app.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        name = request.form['pname']
        category = int(request.form.get('category'))
        img = request.form['img-url']
        price = request.form['price']
        discount = float(request.form.get('discount'))
        no_of_pro = int(request.form['no_of_product'])
        desc = request.form['description']
        vid = current_user.id

        # adding new product to the database

        new_pro = Products(
            product_name=name,
            image=img,
            price=price,
            category_id=category,
            Discount=discount,
            no_of_pieces=no_of_pro,
            description=desc,
            vendor_id=vid
        )
        try:
            db.session.add(new_pro)
            db.session.commit()
        except Exception():
            return "Server error please info"
    return render_template('admin_page.html')

# to update a product

@app.route('/product_update', methods=['POST'])
@csrf.exempt
def product_update():
    res = request.form.to_dict()
    id = res.get('pro_id')
    qty = res.get('quantity')
    print(f"qty:{qty},pro:{id}")
    pro = Products.query.filter(Products.id == id and Products.vendor_id == current_user.id).first()
    new_total=int(pro.no_of_pieces)+int(qty)
    stmt = (
        update(Products).
        where(Products.id == id and Products.vendor_id == current_user.id).
        values(no_of_pieces=new_total)
    )
    db.session.execute(stmt)
    db.session.commit()
    return "", 204

#to delete a product

@app.route('/delete_pro', methods=['POST'])
@csrf.exempt
def delete_pro():
    if request.method == 'POST':
        res = request.form.to_dict()
        pro_id = res.get('pro_id')
        print(pro_id)
        stmt = delete(Products).where(Products.id == pro_id and Vendor.id == current_user.id)
        db.session.execute(stmt)
        db.session.commit()
    return "", 204

# vendor logout

@app.route('/vlogout')
def vlogout():
    logout_user()
    session.clear()
    return redirect(url_for('home'))
