from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column('id', db.Integer, primary_key=True)
	user_id = db.Column('user_id', db.String(160), unique=True, nullable=False))
	firstname = db.Column('firstname', db.String(160))
	lastname = db.Column('lastname', db.String(160))
	email = db.Column('email', db.String(160), unique=True, nullable=False))
	about = db.Column('about', db.String(355))
	pwdhash = db.Column('pwdhash', db.String(355), nullable=False)
	created_on = db.Column('created_on', db.DateTime())
	last_login = db.Column('last_login', db.DateTime())

	def __init__(self, user_id, firstname, lastname, email, about, password, created_on, last_login):
		self.user_id = user_id
		self.firstname = firstname.title()
		self.lastname = lastname.title()
		self.email = email.lower()
		self.about = about.title()
		self.set_password(password)
		self.created_on = created_on.title()
		self.last_login = last_login.title()

	def set_password(self, password):
		self.pwdhash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.pwdhash, password)
