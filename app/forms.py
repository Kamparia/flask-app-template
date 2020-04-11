from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, FileField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired, Email, Length
from werkzeug import secure_filename

class CreateUserForm(Form):
	first_name = StringField('First Name', validators=[DataRequired("Please enter your first name.")])
	last_name = StringField('Last Name', validators=[DataRequired("Please enter your last name.")])
	email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter a valid email address.")])
	password = PasswordField('Password', validators=[DataRequired("Please enter your password."), Length(min=8, message="Password must be 8 characters or more.")])
	about = TextAreaField('About Me', validators=[Length(max=160, message="Text can not be more than 160 characters.")])
    photo = FileField('Profile Photo', validators=[DataRequired("")])
	submit = SubmitField('Create User')