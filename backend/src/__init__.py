from flask import Flask, request, jsonify,redirect,url_for,make_response
from flask_cors import CORS
from pymongo import MongoClient
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from werkzeug.security import check_password_hash,generate_password_hash

app = Flask(__name__)
app.debug = True
CORS(app)

bcrypt = Bcrypt(app)

# Connect to mongodb
client = MongoClient('localhost', 27017)
db = client["online-exam"] #DB name
USERS_TABLE = db["users"] #users table

def get_hash(passwd_str):
  print("String pass is - ", passwd_str)
  print()
  return generate_password_hash(passwd_str, "sha256")

def check_hash(sha_passwd, plain_passwd):
  return check_password_hash(sha_passwd, plain_passwd)


@app.route("/")
def home_page():
  return "Welcome to Home page"


@app.route('/login', methods=['GET', 'POST'])
def login():
  login_form = request.json # getting the form data sent by form on the react front end
  email = login_form.get('email')
  password = login_form.get('password')

  if request.method == "POST":
    # check whether user exists or not in DB
    usrQuery = {"email" : email}
    usr_exists = USERS_TABLE.find_one(usrQuery) # as email id is a primary key, we are using find_one to get one record
    if usr_exists:
      if bcrypt.check_password_hash(usr_exists["password"], password):
        print(usr_exists)
        print('login succesful')
        return usr_exists
      else:
        print("User Credentials are wrong")
    else:
      print("User Credentials not found")
  # find ueser here -
  #test = coll.find_one({"email": email, "password": password})
  # if test:
  #   access_token = create_access_token(identity=email)
  #   return jsonify(message="Login Succeeded!", access_token=access_token), 201
  # else:
  #   return jsonify(message="Bad Email or Password"), 401
  return {}


@app.route("/signup",methods=['POST','GET'])
def signup():
  print('inside signup block')
  client = MongoClient('localhost', 27017)
  db = client["online-exam"] #DB name
  USERS_TABLE = db["users"] #users table
  if request.method == 'POST':
    response = request.json   # getting the form data sent by form on the react front end
    email = response.get('email')
    print(email)
    password=response.get('passsword')
    print(password)
    password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    print('password hashed')
    first_name = response.get('firstName')
    last_name = response.get('lastName')
    new_user={"email":email,"password":password_hash,"firstName":first_name,"lastName":last_name}
    print(new_user)
    new_entry = USERS_TABLE.insert_one(new_user)
    print('user added')
  return str(new_entry.inserted_id)



