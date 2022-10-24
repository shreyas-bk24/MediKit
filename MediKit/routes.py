import csv
import os
import random
from datetime import datetime
from unicodedata import category
from urllib import response

from flask import render_template, request, session, url_for
from flask_admin import Admin as AdminObj
from flask_admin.contrib.sqla import ModelView
from flask_login import login_required, current_user
from flask_mail import Mail, Message
from flask_security import Security
from flask_session import Session
from flask_wtf.csrf import CSRFProtect
from sqlalchemy import delete
from sqlalchemy.sql.expression import update
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect

from MediKit.models import *

admin = AdminObj(app)

security = Security(app)


class MyModelView(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated and current_user.super_user:
            return True


admin.add_view(MyModelView(Users, db.session))
admin.add_view(MyModelView(Products, db.session))
admin.add_view(MyModelView(Complaints, db.session))
admin.add_view(MyModelView(Vendor, db.session))
admin.add_view(MyModelView(CategoryTable, db.session))

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

csrf = CSRFProtect(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'bharadwatest@gmail.com'

# use the app password created
app.config['MAIL_PASSWORD'] = 'lznclcmjcebzetnp'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.before_first_request
def create_table():
    db.create_all()

@app.route('/')
@app.route('/home', methods=['GET'])
def home():
    babycare = Products.query.filter_by(category_id=1).all()
    personalcare = Products.query.filter_by(category_id=2).all()
    bp = Products.query.filter_by(category_id=3).all()
    cc=Products.query.filter_by(category_id=4).all()
    ayur = Products.query.filter_by(category_id=5).all()
    first_aid = Products.query.filter_by(category_id=6).all()
    sugar = Products.query.filter_by(category_id=7).all()
    HH = Products.query.filter_by(category_id=8).all()
    others = Products.query.filter_by(category_id=9).all()

    cart_items = db.session.query(Cart.product_id).all()
    query = request.args.get('query')
    if query:
        return redirect(url_for('search', q=query))
    print(generate_password_hash("Admin@MediKit123", method="pbkdf2:sha256", salt_length=8))
    return render_template("home.html", baby_needs=babycare, personal_care=personalcare,bp=bp,cc=cc,ayur=ayur,first_aid=first_aid,sugar=sugar,hh=HH,others=others, cart=cart_items)


@app.route("/index", methods=['GET'])
@login_required
def index():
    query = request.args.get('query')
    if query:
        return redirect(url_for('search', q=query))
    babycare = Products.query.filter_by(category_id=1).all()
    personalcare = Products.query.filter_by(category_id=2).all()
    bp = Products.query.filter_by(category_id=3).all()
    cc=Products.query.filter_by(category_id=4).all()
    ayur = Products.query.filter_by(category_id=5).all()
    first_aid = Products.query.filter_by(category_id=6).all()
    sugar = Products.query.filter_by(category_id=7).all()
    HH = Products.query.filter_by(category_id=8).all()
    others = Products.query.filter_by(category_id=9).all()
    count = db.session.query(Cart.product_id).filter_by(user_id=current_user.id).count()
    return render_template("home.html", count=count, baby_needs=babycare, personal_care=personalcare,bp=bp,cc=cc,ayur=ayur,first_aid=first_aid,sugar=sugar,hh=HH,others=others)


@app.route('/search/<q>', methods=['GET', 'POST'])
def search(q):
    product = Products.query.filter(Products.product_name.like('%' + q + '%')).all()
    count = Products.query.filter(Products.product_name.like('%' + q + '%')).count()
    return render_template('search.html', query=q, products=product, count=count)


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == "POST":
        name = request.form['usr_name']
        email = request.form.get('email')
        rating = request.form.get('rating')
        feedback_responce = request.form.get('feedback')
        new_case = Complaints(
            user_name=name,
            user_id=current_user.id,
            email=email,
            rating=rating,
            response=feedback_responce,
            posted_on=datetime.now()
        )
        try:
            db.session.add(new_case)
            db.session.commit()
            return render_template('thanks.html')
        except Exception as e:
            return e
    return render_template('feedback.html')


@app.route('/payment')
def payment():
    return render_template('pay.html')


@app.route('/thankyou')
def ThankYou():
    # update the order details to the order table
    cart = Products.query.join(Cart).add_columns(Cart.quantity, Cart.product_id, Products.price, Products.Discount,
                                                 Products.Discount, Products.product_name, Products.vendor_id,
                                                 Products.no_of_pieces
                                                 ).filter_by(user_id=current_user.id).all()
    # get the address of the user
    add = db.session.query(AddressTable).filter_by(id=current_user.id).first()
    total = 0
    orderID = random.randrange(100000, 999999)
    for pro in cart:
        total += pro.price
        # to get the total number of available products
        total_no = pro.no_of_pieces
        current_total = int(total_no - int(pro.quantity))

        new_order = Order(
            pro_id=pro.product_id,
            total_amt=total,
            discount=pro.Discount,
            qty=pro.quantity,
            order_id=orderID,
            user_id=current_user.id,
            pay_mode="Pay on delivery",
            orderd_on=datetime.now()
        )
        try:
            db.session.add(new_order)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            print("error")
        try:
            # to update the product quantity
            update_stmt = update(Products).values({"no_of_pieces": current_total}).where(Products.id == pro.product_id)
            db.session.execute(update_stmt)
            db.session.commit()
        except Exception as e:
            return f"{e}"
        try:
            # to send email to the vendor
            sender = "bharadwatest@gmail.com"
            receiver = db.session.query(Vendor.email).filter_by(id=pro.vendor_id).first()
            message = f"Hello vendor you have an order,\nPlease send these items to the below mentioned address,\n" \
                      f"product_id :{pro.product_id} ,product_name:{pro.product_name},quantity:{pro.quantity},price:{pro.price}\n" \
                      f"To this address\n" \
                      f"{add.first_name} {add.last_name},{add.ph_no},{add.house_no},{add.street}\n" \
                      f"{add.city},{add.town},{add.sub_district},{add.district},{add.state},{add.pincode}"
            subject = "New Order"
            msg = Message(subject, sender=sender, recipients=[receiver.email])
            msg.body = message
            mail.send(msg)
        except Exception as e:
            print(f"{e}")

    stmt = delete(Cart).where(Cart.user_id == current_user.id)
    db.session.execute(stmt)
    db.session.commit()
    return render_template('thanks.html')


@app.route('/comp_display')
@login_required
def comp_display():
    if current_user.super_user:
        comp = db.session.query(Complaints).order_by(Complaints.posted_on and Complaints.is_resolved).all()
        return render_template('feedback_display.html', responce=comp)
    return render_template("404.html")


@app.route('/resolve', methods=['POST'])
@csrf.exempt
def resolve():
    if request.method == 'POST':
        if current_user.super_user:
            res = request.form.to_dict()
            id = res.get('comp_id')
            stmt = (
                update(Complaints).
                where(Complaints.id == id).
                values(is_resolved=True)
            )
            db.session.execute(stmt)
            db.session.commit()
    return "", 204

@app.route('/details/<pro_id>',methods=['GET','POST'])
def details(pro_id):
    pro=db.session.query(Products).where(Products.id==pro_id).first()
    see_also=db.session.query(Products).where(Products.category_id==pro.category_id).all()
    return render_template('search_Res.html',responce=pro,see_also=see_also)