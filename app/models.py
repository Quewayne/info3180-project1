from . import db

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(64))
    lname = db.Column(db.String(64))
    age = db.Column(db.String(4))
    sex= db.Column(db.String(2))
    img = db.Column(db.String(150))
    uname= db.Column(db.String(64))
    bio= db.Column(db.String(1500))
    added=db.Column(db.DateTime)
    uid=db.Column(db.String(20))

    def __init__(self, fname, lname, age, sex,img,uname, bio,added, uid):
       self.fname = fname
       self.lname = lname
       self.age = age
       self.sex = sex
       self.img=img
       self.uname = uname
       self.bio=bio 
       self.added = added
       self.uid = uid
       
