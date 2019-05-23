import os
from app import db
from app.models import ImageProfile

# Data to initialize database with
IMAGES = [
    {
    	"fname": "John", 
    	"lname": "Doe", 
    	"image_name": "filename.jpeg", 
    	"results": '[{"0": 0, "1": 1, "2": 2, "3": 3, "4": 4}]',
    	"description": "description"
    	},
    {
    	"fname": "Jane", 
    	"lname": "Doe", 
    	"image_name": "filename1.jpeg", 
    	"results": '[{"0": 0, "1": 1, "2": 2, "3": 3, "4": 4}]',
    	"description": "description"
    	},
]

# Delete database file if it exists currently
if os.path.exists("imageprofiles.db"):
    os.remove("imageprofiles.db")

# Create the database
db.create_all()

# iterate over the PEOPLE structure and populate the database
for profile in IMAGES:
    p = ImageProfile(lname=profile.get("lname"), 
    		fname=profile.get("fname"), 
    		image_name=profile.get("image_name"), 
    		results=profile.get("results"),
    		description=profile.get("description"))
    db.session.add(p)

db.session.commit()


# Alembic is a database migration tool created specifically for use with SQLAlchemy. 
# It lets us keep a versioned history of our database schema so that we can later upgrade 
# to a new schema and even downgrade back to an older one.