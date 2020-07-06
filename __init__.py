"""from flask import Flask, render_template, request
from dbconnect import database
from wtforms import Form , TextField,PasswordField,validators
from passlib.hash import sha256_crypt
import gc

app = Flask(__name__)




class RegistartionForm(Form):

    email = TextField("Email",[validators.Length[5,10]])

    password = PasswordField("Password", [validators.Required(),validators.Equalto(confirm)])

    confirm = PasswordField("Confirm Password")

@app.route('/register/',methods=['GET','POST'])
def register_page():
    try:

        form = RegistrationForm(request.form)

        if request.method =='POST' and form.validate():
            email = form.email.data
            password = sha256_crypt.encrypt(form.password.data)
            cursor ,connection=database()
            x = cursor.execute("SELECT * FROM tbl_login WHERE email = (%s)",email)
            if int(length(x)) >0:
                flash("User with this Email is already Registered!! Please proceed with Login ..")
                render_template("login.html",form=form)
            else:
                cursor.execute('''INSERT into tbl_login(email,password,confirm_password) VALUES(%s,%s,%s)''',
                               (email, pwd, cf_pwd))
                connection.commit()
                flash("Thanks for registering !!")
                cursor.close()
                connection.close()
                gc.collect()

                session['logged_in']='True'
                session['email'] = email

                return redirect("login.html")

    except Exception as e:
        return(str(e))


if __name__ == "__main__":
    app.run()

"""

