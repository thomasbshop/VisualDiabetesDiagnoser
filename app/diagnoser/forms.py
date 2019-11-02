from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField

from wtforms.validators import DataRequired, InputRequired, Length, Email, Regexp, EqualTo, Required
from flask_wtf.file import FileField, FileAllowed, FileRequired
from werkzeug.utils import secure_filename

class ImageForm(FlaskForm):
	"""Upload Image Form"""

	# firstname = StringField('First name', validators=[InputRequired(message='Add first name.')])
	firstname = StringField('First name', validators=[InputRequired()])
	lastname = StringField('Last name', validators=[InputRequired()])
	image = FileField('image', validators=[FileRequired(),
						FileAllowed(['jpg', 'png'], 'Images only!')])
	description = TextAreaField('Short description', validators=[InputRequired()])
	submit = SubmitField('Submit')
