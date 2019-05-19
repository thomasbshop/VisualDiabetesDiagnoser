import os
from flask import Flask, flash, jsonify, request, redirect, url_for, send_from_directory, render_template
from werkzeug.utils import secure_filename


# custom
from . import app
# import config
from . import models


# port
# port = int(os.getenv("PORT", 9099))
# port = int(os.getenv("VCAP_APP_PORT"))

# Use os.getenv("key") to get environment variables
# app_name = os.getenv("APP_NAME")

# session
app.secret_key = 'thesecretkey'
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


# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename)

# post the image.
@app.route('/api/upload', methods=['GET', 'POST'])
def add_profile():
	if request.method == 'POST':
		# check if the post request has the file part
	    if 'image' not in request.files:
	        flash('No file part')
	        # return redirect(request.url)
	        return jsonify({"description":"no file part"})
	        
	    file = request.files['image']
	    # if user does not select file, browser also
	    # submit an empty part without filename
	    if file.filename == '':
	        flash('No selected file')
	        # return redirect(request.url)
	        return jsonify({"description":"no selected file"})

	    if file and allowed_file(file.filename):
	        filename = secure_filename(file.filename)
	        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	        # data
	        lname = request.form['lastname']
	        fname = request.form['firstname']
	        results = request.form['results']
	        description = request.form['description']
	        image_name = filename

	        new_profile = models.ImageProfile(lname, fname, image_name, results, description)

	        config.db.session.add(new_profile)
	        config.db.session.commit()

	        response = new_profile

	        return models.image_schema.jsonify(response)
	        # return redirect(url_for('uploaded_file', filename=filename))
	    else:
	    	print("That file extension is not allowed")
	    	return redirect(request.url)

	return render_template("upload.html")

