from flask import render_template
from app import app

# Define the home page route
@app.route('/')
def home():
    return render_template('index.html')