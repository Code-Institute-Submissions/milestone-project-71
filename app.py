import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env
    
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    _recipes = mongo.db.recipes.find()
    recipe_list = [recipe for recipe in _recipes]
    return render_template('recipes.html', recipes = recipe_list)

@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html')   

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)