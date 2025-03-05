from flask import Flask

# Create the Flask app
app = Flask(__name__, template_folder="../templates")


# Import routes
from app import routes