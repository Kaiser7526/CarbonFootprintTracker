from flask import Flask, render_template, request, redirect, url_for
import requests
from app import app, db
from app.models import User

# Google Maps API Key
GOOGLE_MAPS_API_KEY = 'YOUR_GOOGLE_MAPS_API_KEY'

# Simulated Energy Usage API
def get_energy_usage():
    # Simulate energy usage data (replace with a real API call)
    return 50  # Example: 50 kWh

# Define the home page route
@app.route('/')
def home():
    return render_template('index.html')

# Define the calculate route
@app.route('/calculate', methods=['POST'])
def calculate():
    # Get user input from the form
    name = request.form['name']
    origin = request.form['origin']
    destination = request.form['destination']
    shopping = float(request.form['shopping'])

    # Fetch energy usage data
    energy = get_energy_usage()

    # Calculate distance using Google Maps API
    distance = get_distance(origin, destination)

    # Calculate carbon footprint
    carbon_footprint = (distance * 0.2) + (energy * 0.5) + (shopping * 0.1)
    carbon_footprint = round(carbon_footprint, 2)

    # Calculate points (1 point for every kg of CO2 reduced)
    # Assume a baseline carbon footprint of 100 kg CO2
    baseline = 100
    points = max(0, baseline - carbon_footprint)

    # Save user data to the database
    user = User(name=name, points=points)
    db.session.add(user)
    db.session.commit()

    # Pass the result to the result template
    return render_template('result.html', carbon_footprint=carbon_footprint, points=points)

@app.route('/rewards')
def rewards():
    # Get all rewards
    rewards = rewards.query.all()
    return render_template('rewards.html', rewards=rewards)

# Function to get distance using Google Maps API
def get_distance(origin, destination):
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={origin}&destinations={destination}&key={GOOGLE_MAPS_API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Extract distance in kilometers
    distance = data['rows'][0]['elements'][0]['distance']['value'] / 1000
    return distance