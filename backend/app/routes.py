from flask import Blueprint,jsonify
import json
import os

api = Blueprint('api',__name__)
@api.route('/recipes', methods = ["GET"])
def get_recipes():
    file_path=os.path.join("data","recipes.json")
    with open(file_path,"r",encoding="utf-8")as f:
        recipes=json.load(f)

    return jsonify(recipes)