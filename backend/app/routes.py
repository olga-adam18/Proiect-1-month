from flask import Blueprint,jsonify,request
import json
import os

api = Blueprint('api',__name__)
@api.route('/recipes', methods = ["GET"])
def get_recipes():
    file_path=os.path.join("data","recipes.json")
    with open(file_path,"r",encoding="utf-8")as f:
        recipes=json.load(f)

    return jsonify(recipes)

@api.route("/recipes", methods=['POST'])
def add_recipes():
    recipe = request.get_json()
    file_path=os.path.join("data","recipes.json")

    with open(file_path,"r",encoding="utf-8") as file:
        recipes=json.load(file)  

        recipe["id"] = recipes[-1]["id"] + 1 # generate a new id      
        recipes.append(recipe)
    
    with open(file_path,"w",encoding="utf-8") as fl:
        json.dump(recipes,fl)
        
    return jsonify(recipes)
