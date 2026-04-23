from flask import render_template, request, redirect, url_for
from app import app, db
from app.models.recipe import Recipe

@app.route('/')
@app.route('/recipes')
def index():
    recipes = Recipe.query.all()
    return render_template('index.html', recipes=recipes)
