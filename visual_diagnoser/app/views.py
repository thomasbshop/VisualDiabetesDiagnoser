import os
from flask import Flask, flash, jsonify, request, redirect, url_for, send_from_directory, render_template
from werkzeug.utils import secure_filename


# custom
from . import app
from . import db
from . import models
from .ai_model.make_prediction import predict

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

# Use os.getenv("key") to get environment variables
app_name = os.getenv("APP_NAME")

# session
app.config['SESSION_TYPE'] = 'filesystem'


@app.route("/")
def home():
    return render_template("home.html")

# @app.route("/contact-us/")
# def contact_us():
#     return "<h1>Contact Us</h1>"

# @app.route("/about-us/")
# def about_us():
#     return "<h1>About Us</h1>"


# @app.route("/user/<username>/")
# def profile(username):

#     return "<h1>Hello {username}</h1>".format(username=username)

# @app.route("/jobs/<job_id>/")
# def jobs(job_id):
#     # run job 12
#     return "<h1>Hello {username}</h1>".format(username=username)


# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500