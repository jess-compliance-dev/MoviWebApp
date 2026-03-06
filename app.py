import os
from flask import Flask, render_template
from models import db, User, Movie

app = Flask(__name__)

# Configuration for the SQLite database file
# This creates a 'data' folder path and a 'moviweb.db' file inside it
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'data', 'moviweb.db')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Connect the database object to the Flask app
db.init_app(app)

# Create the database and tables if they don't exist yet
with app.app_context():
    # Ensure the 'data' directory exists
    if not os.path.exists(os.path.join(basedir, 'data')):
        os.makedirs(os.path.join(basedir, 'data'))
    db.create_all()

@app.route('/')
def index():
    # Fetch all users to display them on the home page
    users = User.query.all()
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)