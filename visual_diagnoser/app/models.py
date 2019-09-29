# ourapp/models.py

from . import db, ma
from datetime import datetime
# from config import db, ma
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username


class ImageProfile(db.Model):
    """Details needed with the image to be stored in the db"""
    __tablename__ = "profiles"
    image_id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32))
    fname = db.Column(db.String(32))
    image_name = db.Column(db.String(100))
    results = db.Column(db.String(64))
    description = db.Column(db.String(400))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def __init__(self, lname, fname, image_name, results, description):
        self.lname = lname
        self.fname = fname
        self.image_name = image_name
        self.results = results
        self.description = description

    def __repr__(self):
        return f"<image_id: {self.image_id}"


class ImageProfileSchema(ma.ModelSchema):
    class Meta:
        model = ImageProfile
        sqla_session = db.session
        # fields = (
        #     'image_id', 
        #     'lname', 
        #     'fname',
        #     'image_name',
        #     'results',
        #     'description',
        #     'timestamp')



image_schema = ImageProfileSchema(strict=True)
images_schema = ImageProfileSchema(many=True, strict=True)