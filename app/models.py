# ourapp/models.py

from . import db, ma
from datetime import datetime
# from config import db, ma


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