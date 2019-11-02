import os
from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response, jsonify
from flask_sqlalchemy import get_debug_queries
from werkzeug.utils import secure_filename
from .. import db
from ..models import ImageProfile, image_schema
from . import diagnoser
from . forms import ImageForm
from .classify import predict


@diagnoser.route("/diagnoser", methods=["GET", "POST"])
def diagnose():
	form=ImageForm()
	if form.validate_on_submit():
		f = form.image.data
		filename = secure_filename(f.filename)
		# save file
		thisdir = os.path.abspath(os.path.dirname(__file__))
		IMAGES_FOLDER = os.path.join(thisdir, 'saved_images')
		f.save(os.path.join( IMAGES_FOLDER, filename ))
		# classify
		file_path = os.path.join( IMAGES_FOLDER, filename )
		print(file_path)
		prediction = predict(file_path)
		results = str(prediction[0])
		print(results)
		# save data
		firstname = form.firstname.data
		lastname = form.lastname.data
		description = form.description.data
		image_data = ImageProfile(firstname=firstname,
								  lastname=lastname,
								  imagename=filename,
								  result=results,
								  description=description)
		db.session.add(image_data)
		db.session.commit()
		return image_schema.jsonify(image_data)
	return render_template("diagnoser/upload.html", form=form)


# @auth.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = User(email=form.email.data.lower(),
#                     username=form.username.data,
#                     password=form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         token = user.generate_confirmation_token()
#         send_email(user.email, 'Confirm Your Account',
#                    'auth/email/confirm', user=user, token=token)
#         flash('A confirmation email has been sent to you by email.')
#         return redirect(url_for('auth.login'))
#     return render_template('auth/register.html', form=form)