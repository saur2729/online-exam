from flask import Blueprint, request, jsonify
import json
import os
import sys
from bson import ObjectId
from pymongo import MongoClient


# JSON encoder to manage the MongoDB Object
class JSONEncoder(json.JSONEncoder):
  def default(self, o):
    if isinstance(o, ObjectId):
      return str(o)
    return json.JSONEncoder.default(self, o)


