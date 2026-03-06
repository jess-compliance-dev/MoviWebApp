from models import db, User, Movie

class DataManager:
    # 1. User Operations
    def create_user(self, name):
        """Adds a new user to the database."""
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()

    def get_users(self):
        """Returns a list of all users."""
        return User.query.all()

    # 2. Movie Retrieval
    def get_movies(self, user_id):
        """Returns all movies for a specific user ID."""
        return Movie.query.filter_by(user_id=user_id).all()

    # 3. Movie CRUD Operations
    def add_movie(self, movie_object):
        """Adds a movie to the database."""
        db.session.add(movie_object)
        db.session.commit()

    def update_movie(self, movie_id, new_title):
        """Updates the title of a specific movie."""
        movie = Movie.query.get(movie_id)
        if movie:
            movie.name = new_title
            db.session.commit()
            return True
        return False

    def delete_movie(self, movie_id):
        """Deletes a movie from the database by its ID."""
        movie = Movie.query.get(movie_id)
        if movie:
            db.session.delete(movie)
            db.session.commit()
            return True
        return False