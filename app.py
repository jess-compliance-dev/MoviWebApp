import os
import requests
from flask import Flask, request, redirect, url_for, render_template
from dotenv import load_dotenv
from models import db, User, Movie
from data_manager import DataManager

# load API key
load_dotenv()
app = Flask(__name__)

OMDB_API_KEY = os.getenv('OMDB_API_KEY')

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data/movies.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Link the database and the app
db.init_app(app)

data_manager = DataManager()

with app.app_context():
    if not os.path.exists(os.path.join(basedir, 'data')):
        os.makedirs(os.path.join(basedir, 'data'))
    db.create_all()

@app.route('/')
def home():
    """Home page"""
    users = data_manager.get_users()
    return render_template('index.html', users=users)


@app.route('/users', methods=['POST'])
def add_user():
    """Handles the POST request to add a new user."""
    user_name = request.form.get('name')
    if user_name:
        data_manager.create_user(user_name)
    return redirect(url_for('home'))


@app.route('/users/<int:user_id>/movies', methods=['GET'])
def user_movies(user_id):
    """Displays the list of favorite movies for a specific user."""
    user = User.query.get_or_404(user_id)
    movies = data_manager.get_movies(user_id)
    return render_template('user_movies.html', movies=movies, user_id=user_id)


@app.route('/users/<int:user_id>/movies', methods=['POST'])
@app.route('/users/<int:user_id>/movies', methods=['POST'])
def add_movie(user_id):
    movie_title = request.form.get('title')

    if movie_title and OMDB_API_KEY:

        response = requests.get(
            "http://www.omdbapi.com/",
            params={"apikey": OMDB_API_KEY, "t": movie_title}
        )

        data = response.json()
        print("OMDB RESPONSE:", data)

        if data.get('Response') == 'True':
            raw_year = data.get('Year', '0')
            clean_year = "".join(filter(str.isdigit, raw_year))[:4]

            new_movie = Movie(
                name=data.get('Title'),
                director=data.get('Director'),
                year=int(clean_year) if clean_year else 0,
                poster_url=data.get('Poster'),
                user_id=user_id
            )

            data_manager.add_movie(new_movie)

    return redirect(url_for('user_movies', user_id=user_id))


@app.route('/users/<int:user_id>/movies/<int:movie_id>/update', methods=['POST'])
def update_movie(user_id, movie_id):
    """Updates the title of a specific movie."""
    new_title = request.form.get('title')
    if new_title:
        data_manager.update_movie(movie_id, new_title)
    return redirect(url_for('user_movies', user_id=user_id))


@app.route('/users/<int:user_id>/movies/<int:movie_id>/delete', methods=['POST'])
def delete_movie(user_id, movie_id):
    """Deletes a movie from the user's list."""
    data_manager.delete_movie(movie_id)
    return redirect(url_for('user_movies', user_id=user_id))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


print(OMDB_API_KEY)

if __name__ == '__main__':
    app.run(debug=True)