import os
from flask import Flask
from models import db  # Importing db to link it with the app
from data_manager import DataManager

app = Flask(__name__)

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
    """test route - welcoming"""
    return "Welcome to MoviWeb App!"


if __name__ == '__main__':
    app.run(debug=True)