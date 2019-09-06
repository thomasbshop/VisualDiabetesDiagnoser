import os
from flask import Flask, flash, jsonify, request, redirect, url_for, send_from_directory, render_template
from werkzeug.utils import secure_filename


# custom
from . import app
from . import db
from . import models
from .ai_model.make_prediction import predict


# Use os.getenv("key") to get environment variables
app_name = os.getenv("APP_NAME")

# session
app.config['SESSION_TYPE'] = 'filesystem'

# upload folder
basedir = app.config["BASEDIR"]
UPLOAD_FOLDER = os.path.join(basedir, 'uploads')
# UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])


# fun to check the file type
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    return render_template("home.html")

@app.route("/contact-us/")
def contact_us():
    return "<h1>Contact Us</h1>"

@app.route("/about-us/")
def about_us():
    return "<h1>About Us</h1>"


@app.route("/user/<username>/")
def profile(username):

    return "<h1>Hello {username}</h1>".format(username=username)

@app.route("/jobs/<job_id>/")
def jobs(job_id):
    # run job 12
    return "<h1>Hello {username}</h1>".format(username=username)


# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename)

# post the image.
