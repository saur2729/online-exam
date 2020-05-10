from flask import Flask, request, jsonify,redirect,url_for,make_response
from flask_cors import CORS
from pymongo import MongoClient
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from werkzeug.security import check_password_hash,generate_password_hash

app = Flask(__name__)
app.debug = True
CORS(app)

client = MongoClient('localhost', 27017)  # Connect to mongodb


@app.route("/")
def home_page():
  return "Welcome to Home page"

@app.route('/login', methods=['GET', 'POST'])
def login():
  email = request.form.get('email')
  password = request.form.get('password')

  db = client["online-exam"]
  coll = db["users"]
  # find ueser here -
  test = coll.find_one({"email": email, "password": password})
  if test:
    access_token = create_access_token(identity=email)
    return jsonify(message="Login Succeeded!", access_token=access_token), 201
  else:
    return jsonify(message="Bad Email or Password"), 401


@app.route("/signup",methods=['POST','GET'])
def signup():
  coll_list = []
  db = client["online-exam"]
  user_col=db["users"]
  if request.method == 'POST':
    respone = request.json   # getting the form data sent by form on the react front end
    email = respone.get('email')
    password_hash = generate_password_hash(respone.get('password'),method='sha256')
    first_name = respone.get('firstName')
    last_name = respone.get('lastName')
    new_user={"email":email,"password":password_hash,"firstName":first_name,"lastName":last_name}
    new_entry = user_col.insert_one(new_user)  
  return str(new_entry.inserted_id)

  # else:
  #   return redirect(url_for('signup'))

# @app.route("/add-job")
# def add_job(obj):

#   return {"strr" : "instance_id"}


# @app.route("/getAllInstance")
# def get_all_instance():

#   return {"strr" : "instance_id"}

