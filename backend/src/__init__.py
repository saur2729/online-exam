from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
app.debug = True
CORS(app)

client = MongoClient('localhost', 27017)  # Connect to mongodb


@app.route("/")
def home_page():
  return "Welcome to Home page"

@app.route("/login")
def login():
  coll_list = []
  db = client["online-exam"]
  collections = db.list_collection_names()
  for coll in collections:
    coll_list.append(coll)
  print(coll_list)
  return {"DBS" : coll_list}

@app.route("/signup")
def signup():
  """
  email 
  password
  first name
  last name
  """

  return {"strr" : instance_id}

# @app.route("/add-job")
# def add_job(obj):

#   return {"strr" : "instance_id"}


# @app.route("/getAllInstance")
# def get_all_instance():

#   return {"strr" : "instance_id"}

