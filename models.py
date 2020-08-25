from app import db

class Project(db.Model):

    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False,unique=True)
    description = db.Column(db.String(600),unique=True,index=True)
    image = db.Column(db.String(128),unique=True,index=True)
    url = db.Column(db.String(500))