MoviWebApp
Table of Contents

General Info

Technologies

Features

CRUD Operations

OMDb API Integration

Setup

Usage

Project Purpose

General Info

MoviWebApp is a web application that allows users to search, browse, and manage movie data through an interactive interface. It leverages the OMDb API to fetch movie details in real-time and demonstrates Python-based web development with modular code structure and dynamic HTML generation.

Technologies

Python 3.8+

Flask (Python web framework)

HTML / CSS for front-end templates

OMDb API for movie data

requests library for API calls

requirements.txt for dependency management

Features

User-friendly search and browse functionality for movie data

Dynamic HTML pages generated based on user input

Modular Python structure:

app.py → main server and route handling

data_manager.py → movie data retrieval and processing

models.py → data structures

Display of movie details such as title, genre, release date, rating, and synopsis

Error handling for missing or invalid movie entries

CRUD Operations

MoviWebApp supports full CRUD functionality for managing movie entries:

Create – Add new movie entries via a form on the web interface.

Read – Browse and search existing movie records dynamically.

Update – Edit existing movie details (title, genre, rating, etc.) through the UI.

Delete – Remove movie entries from the database or data store securely.

These operations are implemented in data_manager.py and exposed through Flask routes in app.py, ensuring modular and maintainable code.

OMDb API Integration

MoviWebApp uses the OMDb API
 to fetch movie details. Key points:

API provides real-time information for movies, series, and episodes.

Requires a personal API key from OMDb
.

API calls are handled in data_manager.py using the requests library.

Example usage in the app:

import requests

response = requests.get(f"http://www.omdbapi.com/?t={movie_title}&apikey={OMDB_API_KEY}")
movie_data = response.json()
Setup

Clone the repository:

git clone https://github.com/jess-compliance-dev/MoviWebApp.git
cd MoviWebApp

Create a virtual environment:

python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

Install dependencies:

pip install -r requirements.txt

Configure your OMDb API key:

Create a .env file in the project root:

OMDB_API_KEY=your_api_key_here

Make sure data_manager.py reads this key for API requests.

Usage

Run the main application:

python app.py

Open your browser at http://localhost:5000

Search, browse, and manage movie records with full CRUD support powered by OMDb API.

Project Purpose

This project is designed for learning and demonstration of:

Python web development with Flask

Modular code structure

Dynamic HTML generation

Integration with external APIs (OMDb)

Handling user input and CRUD operations

Error handling and fallback messages

Dependency management with requirements.txt
