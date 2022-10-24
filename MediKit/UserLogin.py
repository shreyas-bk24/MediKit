from flask import request, url_for, flash, render_template, session
from flask_login import login_user, current_user, logout_user, LoginManager, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from MediKit import app
from MediKit.models import Users, db, AddressTable, Cart

login = LoginManager()
login.init_app(app)
login.login_view = 'login'


@login.user_loader
def load_user(id):
    return Users.query.get(int(id))


@app.route("/signup", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        # hashing password and store it in a variable

        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8)
        confirm_password = generate_password_hash(
            request.form.get('password2'),
            method='pbkdf2:sha256',
            salt_length=8)

        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        user_exists = Users.query.filter_by(email=email).first()
        if not user_exists:
            try:
                # noinspection PyArgumentList
                new_user = Users(
                    last_name=lastname,
                    first_name=firstname,
                    email=email,
                    password=hash_and_salted_password
                )
                db.session.add(new_user)
                db.session.commit()

                # login with the new user account
                login_user(new_user)
                if AddressTable.query.filter_by(user_id=current_user.id).first() is None:
                    return redirect(url_for('address'))
                else:
                    return redirect(url_for('index'))

            except Exception:
                return "server is unreachable"

        elif user_exists:
            flash("Email already exists you can login to your")
            return redirect(url_for('login'))

    return render_template("signup.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # saving the session
        session["email"] = request.form["email"]
        session["password"] = request.form["password"]
        email = request.form.get('email')
        password_entered = request.form.get('password')
        user = Users.query.filter_by(email=email).first()
        try:
            if user:
                if check_password_hash(user.password, password_entered):
                    login_user(user)
                    if AddressTable.query.filter_by(user_id=current_user.id).first() is None:
                        return redirect('address')
                    else:
                        return redirect('index')
                else:
                    flash("Invalid username or password",category='danger')
            else:
                flash('no user found on this email',category='danger')
        except Exception:
            flash("Invalid username or password")
    return render_template('Login.html')


@app.route('/address', methods=['GET', 'POST'])
@login_required
def address():
    if request.method == 'POST':
        fname = request.form['first_name']
        lname = request.form.get('last_name')
        email_id = request.form.get('email')
        phone = request.form.get('phno')
        house_no = request.form.get('house_no')
        street = request.form.get('street')
        town = request.form.get('Town')
        city = request.form.get('city')
        pincode = request.form.get('pincode')
        subdist = request.form.get('subdist')
        district = request.form.get('dist')
        state = request.form.get('state')
    

        new_address = AddressTable(
            user_id=current_user.id,
            first_name=fname,
            last_name=lname,
            email=email_id,
            ph_no=phone,
            house_no=house_no,
            street=street,
            town=town,
            city=city,
            sub_district=subdist,
            district=district,
            pincode=pincode,
            state=state
        )
        try:
            db.session.add(new_address)
            db.session.commit()
            flash("address updated successfully!")
            return redirect(url_for('index'))
        except Exception:
            flash("sorry cant process a request")
            return redirect(url_for('index'))
    return render_template('address.html')


@app.route('/profile')
@login_required
def profile():
    users = Users.query.join(AddressTable).add_columns(Users.first_name,
                                                       AddressTable.last_name,
                                                       AddressTable.email,
                                                       AddressTable.ph_no, AddressTable.house_no, AddressTable.city,
                                                       AddressTable.state, AddressTable.street,
                                                       AddressTable.sub_district, AddressTable.town).filter_by(
        id=current_user.id, user_id=current_user.id).first()

    return render_template('profile.html', user=users, count=0)
  


@app.route('/logout')
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('home'))

