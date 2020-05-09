import os
from flask import Flask
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app

app = Flask(__name__)
app.debug = True
CORS(app)

# connect to Firebase DB
cred = credentials.Certificate(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
default_app = initialize_app(cred)
db = firestore.client()

@app.route("/")
def home_page():
  doc_ref = db.collection(u'users').document(u'alovelace')
  setData = doc_ref.set({
    'first': 'Ada',
    'last': 'Lovelace',
    'born': 1815
  })
  print(setData)
  return str(setData)

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

