from flask import Blueprint,render_template,request,flash,redirect,url_for

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    data=request.form
    print(data)
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

        if(len(email)< 5):
            flash('Email must be at least 5 characters',category='error')
        elif(len(first_name)==0):
                flash('First Name should not be empty',category='error')
        elif(password1!=password2 or len(password1)<5 ):
            flash('Passwords must match and length should be more than 5 characters',category='error')
        else:
            flash('You have successfully registered',category='success')
    return render_template("sign_up.html")