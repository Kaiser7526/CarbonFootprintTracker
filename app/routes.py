from flask import Flask, render_template, request, redirect, url_for
import requests
from app import app

# Google Maps API Key
GOOGLE_MAPS_API_KEY = 'YOUR_GOOGLE_MAPS_API_KEY'

# Define the home page route
@app.route('/')
def home():
    return render_template('index.html')

# Define the calculate route
@app.route('/calculate', methods=['POST'])
def calculate():
    # Get user input from the form
    origin = request.form['origin']
    destination = request.form['destination']
    energy = float(request.form['energy'])
    shopping = float(request.form['shopping'])

    # Calculate distance using Google Maps API
    distance = get_distance(origin, destination)

    # Calculate carbon footprint (simple formula for now)
    # Assumptions:
    # - 0.2 kg CO2 per km for driving
    # - 0.5 kg CO2 per kWh for energy
    # - 0.1 kg CO2 per dollar spent on shopping
    carbon_footprint = (distance * 0.2) + (energy * 0.5) + (shopping * 0.1)

    # Round the result to 2 decimal places
    carbon_footprint = round(carbon_footprint, 2)

    # Pass the result to the result template
    return render_template('result.html', carbon_footprint=carbon_footprint)

# Function to get distance using Google Maps API
def get_distance(origin, destination):
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={origin}&destinations={destination}&key={GOOGLE_MAPS_API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Extract distance in kilometers
    distance = data['rows'][0]['elements'][0]['distance']['value'] / 1000
    return distance