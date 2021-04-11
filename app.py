import datetime
from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash



app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/submit", methods=["GET","POST"])
def submit():
    if request.method == "GET":
        return "Please submit the form"
    else:
        name = request.form.get("name")
        password = request.form.get("password")
        mobile = request.form.get("mobile")
        dob = request.form.get("dob")
        email = request.form.get("email")
        gender = request.form.get("gender")
        

        return render_template("submit.html", name=name, password=generate_password_hash(password, method='sha256'), mobile=mobile, dob=dob, email=email, gender=gender)
       
