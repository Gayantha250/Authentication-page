from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash
from . import db


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():

    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user=User.find_by_email(email)
        if user is not None:
           if check_password_hash(user.password== password):
               flash('You are now logged in!', 'success')
           else:
                flash('Wrong password or Email Adress', 'danger')
                return redirect(url_for('views.home'))
        else:
            flash("user doesnt exist", category='error')
            return redirect(url_for('auth.signup'))
    # data=request.form
    # print(data)
    return render_template("login.html" , boolean=True)

@auth.route('/logout')
def logout():
    return render_template("log_out.html")

@auth.route('/sign-up', methods=['GET','POST'])
def signup():
    if request.method == "POST":
        email=request.form.get('email')
        first_name= request.form.get('first_name')
        password1=request.form.get('password1')
        password2=request.form.get('password2')
    user= User.query.filter_by(email=email).first()
    if user is None:
        if(len(email)< 5):
            flash('Email must be at least 5 characters',category='error')
        elif(len(first_name)==0):
                flash('First Name should not be empty',category='error')
        elif(password1!=password2 or len(password1)<5 ):
            flash('Passwords must match and length should be more than 5 characters',category='error')
        else:
            new_user= User(email=email,first_name=first_name,password1=generate_password_hash(password1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('You have successfully registered',category='success')
            return redirect(url_for('views.home'))
    else:
        flash('User already exists',category='error')

    return render_template("sign_up.html")