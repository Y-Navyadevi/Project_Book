from flask import Flask, session, request, render_template
from flask.helpers import flash
from model import *
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, time

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:Navya@0@localhost:5432/project'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "baukfb13256$%^sfqu3oeghroq"

db.init_app(app)

def main() :
    db.create_all()
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
  return render_template("register.html")



@app.route("/login")
def login():
  return render_template("login.html")

@app.route("/submit1", methods = ["POST"])
def submit1(): 
    name = request.form.get("name")
    password = request.form.get("password")
    users=Test.query.all()
    for user in users:
        if user.name==name and check_password_hash(user.password, password):
            return render_template("hello.html",names=name)
        # elif user.name!=name or user.password!=password:
        # else:
        #     return render_template("error.html",names=name)
        # else:
    return render_template('register.html')


@app.route("/search", methods=["POST"])
def search():
    name = request.form.get("search")
    user = title.query.all()
    # for i in user:
    #     if i.isbn==name or i.author==name or i.title==name or i.year==name :
    #         return render_template("hello.html",isbn = i.isbn,title=i.title,author=i.author,year=i.year)
        # else:
    return render_template("hello.html", users=user, name=name)


@app.route("/submit", methods = ["GET","POST"])
def submit(): 
    name = request.form.get("name")
    password = request.form.get("password")
    mobile = request.form.get("mobile")
    dob = request.form.get("dob")
    email = request.form.get("email")
    gender = request.form.get("gender")
    timestamp=datetime.now()
    s= Test(name=name,password=generate_password_hash(password, method='sha256'),mobile=mobile,dob=dob,email=email,gender=gender, timestamp=timestamp)

    usern = Test.query.filter_by(email=email).first()
    if usern:  # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return render_template("login.html")


    db.session.add(s)
    db.session.commit()


    return render_template("login.html",users = Test.query.all())
    




if __name__ == "__main__" :

    with app.app_context() :
        main()