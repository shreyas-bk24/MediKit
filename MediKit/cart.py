from itertools import count
import json
from statistics import quantiles

from flask import render_template, request, url_for, jsonify, session, flash
from flask_login import current_user, login_required
from sqlalchemy import update, delete

from werkzeug.utils import redirect

from MediKit import models, app
from MediKit.models import Products, db, Cart, CategoryTable
from MediKit.routes import csrf


@app.route('/addCart', methods=['POST'])
@csrf.exempt
@login_required
def addCart():
    res = request.form.to_dict()
    id = res.get('pro_id')
    qty = res.get('quantity')
    new_cart = Cart(
        user_id=current_user.id,
        product_id=id,
        quantity=qty
    )
    try:
        db.session.add(new_cart)
        db.session.commit()
    except Exception:
        return "server_error"
    return '', 204


@app.route("/cart", methods=['GET', 'POST'])
@login_required
def cart():
    cart_pro = Products.query.join(Cart).add_columns(Cart.quantity, Products.price, Products.product_name, Products.id,
                                                     Products.image).filter_by(user_id=current_user.id).all()
    count = Cart.query.filter_by(user_id=current_user.id).count()
    total = 0
    for pro in cart_pro:
        total += int(pro.price * pro.quantity)
    print(total)
    return render_template('cart_1.html', responce=cart_pro, total=total, count=count)


@app.route("/removeFromCart", methods=['GET', 'POST'])
@login_required
@csrf.exempt
def removeFromCart():
    if request.method == 'POST':
        res = request.form.to_dict()
        pro_id = res.get('pro_id')
        print(pro_id)
        stmt = delete(Cart).where(Cart.product_id == pro_id and Cart.user_id == current_user.id)
        db.session.execute(stmt)
        db.session.commit()
        return "", 204


@app.route("/updateCart", methods=['GET', 'POST'])
@login_required
@csrf.exempt
def updateCart():
    if request.method == 'POST':
        res = request.form.to_dict()
        id = res.get('pro_id')
        qty = res.get('quantity')
        print(f"qty:{qty},pro:{id}")
        stmt = (
            update(Cart).
            where(Cart.product_id == id and Cart.user_id == current_user.id).
            values(quantity=qty)
        )
        db.session.execute(stmt)
        db.session.commit()
        return "", 204
