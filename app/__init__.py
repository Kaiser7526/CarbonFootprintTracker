from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create the Flask app
app = Flask(__name__, template_folder="../templates", static_folder="../static")

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///carbon_footprint.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Import routes
from app import routes