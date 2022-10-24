import random
from flask import request, render_template, url_for, session, flash
from flask_login import current_user, login_required
from flask_mail import Message
from sqlalchemy import update
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from MediKit import app
from MediKit.models import Users, db
from MediKit.routes import mail


@app.route('/forgot', methods=['GET', 'POST'])
def forgot():
    if request.method == 'POST':
        enterd_email = request.form['email']
        if db.session.query(Users).filter(Users.email == enterd_email).first():
            session['email'] = enterd_email
            return redirect(url_for('get_otp'))
        else:
            flash(message='This email dose not exists', category='warnings')
    return render_template('forgot_password.html')


@app.route('/get_otp', methods=['GET', 'POST'])
def get_otp():
    otp = random.randrange(100000, 999999)
    session['otp'] = otp
    try:
        sender = "bharadwatest@gmail.com"
        # receiver = current_user.email
        message = f"Hello we have received password reset request from your account\n" \
                  f"This is your OTP please dont share this code with anyone\n" \
                  f"OTP: {otp}\n" \
                  f"Enter this code in the reset password textbox to reset your password"
        subject = "Team MediKit"
        msg = Message(subject, sender=sender, recipients=['shreyas.bharadwaj41@gmail.com'])
        msg.body = message
        mail.send(msg)
    except Exception as e:
        print(e)
    return render_template('otp.html')


@app.route('/validate', methods=['GET', 'POST'])
def validate():
    if request.method == 'POST':
        if 'otp' in session:
            s = session['otp']
            session.pop('otp', None)
            print(s)
            otp_enterd = request.form['otp']
            if int(otp_enterd) == s:
                return redirect(url_for('reset_password'))
            else:
                return redirect(url_for('forgot'))


@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        password = generate_password_hash(request.form['password'], method="pbkdf2:sha256", salt_length=8)
        if check_password_hash(password, request.form['c_password']):
            if 'email' in session:
                email = session['email']
                session.pop('email', None)
                change_password = update(Users).values({"password": password}).where(Users.email == email)
                try:
                    db.session.execute(change_password)
                    db.session.commit()
                except Exception as e:
                    print(e)
                flash(message="please login with your new credentials")
                return redirect(url_for('login'))

    return render_template('password_reset.html')
