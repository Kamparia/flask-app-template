from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from forms import CreateUserForm
from models import db, User, Project, Form, Map

app = Flask(__name__)

## Connect app to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/geoform_main'
db.init_app(app)

app.secret_key = "development_key"

@app.route('/')
def index():
	return render_template("index.html")

#adding variables
@app.route('/user/<username>')
def show_user(username):
  #returns the username
  return 'Username: %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
  #returns the post, the post_id should be an int
  return str(post_id)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        static_file = request.files['the_file']
        # here you can send this static_file to a storage service
        # or save it permanently to the file system
        static_file.save('/var/www/uploads/profilephoto.png')
        return "Success"
    else:
        return "Failed"