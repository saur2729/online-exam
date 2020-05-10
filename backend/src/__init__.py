from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

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


@app.route("/signup")
def signup():
  """
  email
  password
  first name
  last name
  """

  return {"strr" : "instance_id"}

# @app.route("/add-job")
# def add_job(obj):

#   return {"strr" : "instance_id"}


# @app.route("/getAllInstance")
# def get_all_instance():

#   return {"strr" : "instance_id"}

