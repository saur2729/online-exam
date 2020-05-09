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

# @app.route("/db")
# def db_page():
#   coll_list = []
#   db = client["job-scheduler"]
#   collections = db.list_collection_names()
#   for coll in collections:
#     coll_list.append(coll)
#   print(coll_list)
#   return {"DBS" : coll_list}

# @app.route("/jobs")
# def get_jobs(instance_id="local", job_name="demo"):

#   return {"strr" : instance_id}

# @app.route("/add-job")
# def add_job(obj):

#   return {"strr" : "instance_id"}


# @app.route("/getAllInstance")
# def get_all_instance():

#   return {"strr" : "instance_id"}

