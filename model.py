# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

# db = SQLAlchemy()

# class User(db.Model) :

#     __tablename__="users"

#     name = db.Column(db.String, nullable=False)
#     email = db.Column(db.String, primary_key=True)
#     password = db.Column(db.String, nullable=True)
#     dob = db.Column(db.String, nullable=False)
#     gender = db.Column(db.String, nullable=False)
#     timestamp = db.Column(db.DateTime, nullable=False)

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Test(db.Model):
      __tablename__="book"
      name = db.Column(db.String(100),primary_key=True)
      password = db.Column(db.String(120), nullable=False)
      mobile = db.Column(db.String(15),primary_key=True,nullable=False)
      dob = db.Column(db.String,nullable=False)
      email = db.Column(db.String(80), nullable=False)
      gender = db.Column(db.String(80), nullable=False)
      timestamp= db.Column(db.String(80), nullable=False)




      def __init__(self, name,password,mobile,dob,email,gender,timestamp):
          self.name = name
          self.password = password
          self.mobile = mobile
          self.dob = dob
          self. email= email
          self.gender = gender
          self.timestamp=timestamp

class title(db.Model):
    __tablename__="bookss"
    isbn = db.Column(db.String(100), primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    year = db.Column(db.String(100))
    
    def __init__(self, isbn,title,author,year):
        self.isbn = isbn
        self.title= title
        self.author = author
        self.year = year


# users=Test.query.all()
#     for user in users:
#         if user.username==name and user.password==password:
#             return render_template("hello.html",names=name)
