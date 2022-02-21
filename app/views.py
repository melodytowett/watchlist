from email import message
from flask import render_template
from app import app
# @app.route('/')

@app.route('/movie/<int:movie_id>')
# def movie(movie_id):
def index():


    # message = 'Hello world'
    title = 'Home - welcome to the best movie review website online '
    return render_template('index.html',title = title)