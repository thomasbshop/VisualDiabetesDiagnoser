import os
from flask import Flask, flash, jsonify, request, redirect, url_for, send_from_directory, render_template
from werkzeug.utils import secure_filename


# custom
from app import app
from app import db
from app import models
from ..ai_model.make_prediction import predict

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
           

@app.route('/api/upload', methods=['GET', 'POST'])
def add_profile():
	if request.method == 'POST':
		# check if the post request has the file part
	    if 'image' not in request.files:
	        flash('No file part')
	        # return redirect(request.url)
	        return jsonify({"description":"no file part"})
	        # return json.dumps("no file part."), 201
	        
	    file = request.files['image']
	    # if user does not select file, browser also
	    # submit an empty part without filename
	    if file.filename == '':
	        flash('No selected file')
	        # return redirect(request.url)
	        return jsonify({"description":"no selected file"})
	        # return json.dumps("no selected file."), 202

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

	        db.session.add(new_profile)
	        db.session.commit()

	        response = new_profile

	        return models.image_schema.jsonify(response)
	        # return redirect(url_for('uploaded_file', filename=filename))
	    else:
	    	print("That file extension is not allowed")
	    	return redirect(request.url)

	return render_template("upload.html")


# predict.
@app.route('/api/predict', methods=['GET', 'POST'])
def new_prediction():
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
	        description = request.form['description']
	        image_name = filename
	        # get the file path
	        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
	        # make the prediction
	        prediction = predict(file_path)
	        results = str(prediction)

	        new_profile = models.ImageProfile(lname, fname, image_name, results, description)

	        db.session.add(new_profile)
	        db.session.commit()

	        response = new_profile

	        return models.image_schema.jsonify(response)
	        # return redirect(url_for('uploaded_file', filename=filename))
	    else:
	    	print("That file extension is not allowed")
	    	return redirect(request.url)

	return render_template("upload.html")