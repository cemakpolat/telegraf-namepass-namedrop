from flask import Flask, jsonify
import random

app = Flask(__name__)

# Function to convert liters to gallons
def liters_to_gallons(liters):
    return liters * 0.264172  # Convert liters to gallons

# Generate drinking water data
def generate_drinking_water_data():
    flow_rate_liters = random.uniform(5.0, 15.0)
    return {
        "type": "drinking",
        "flow_rate_gallons": liters_to_gallons(flow_rate_liters),
        "temperature_fahrenheit": random.uniform(5.0, 25.0),
        "quality_index": random.uniform(90.0, 100.0)
    }

# Generate irrigation water data
def generate_irrigation_water_data():
    flow_rate_liters = random.uniform(10.0, 30.0)
    return {
        "type": "irrigation",
        "flow_rate_gallons": liters_to_gallons(flow_rate_liters),
        "temperature_fahrenheit": random.uniform(10.0, 35.0),
        "particulate_matter": random.uniform(0.0, 50.0)  # in mg/L
    }

# Generate industrial water data
def generate_industrial_water_data():
    flow_rate_liters = random.uniform(20.0, 50.0)
    return {
        "type": "industrial",
        "flow_rate_gallons": liters_to_gallons(flow_rate_liters),
        "temperature_fahrenheit": random.uniform(15.0, 40.0),
        "chemical_content": random.uniform(0.0, 200.0)  # in mg/L
    }

@app.route('/drinking_water', methods=['GET'])
def get_drinking_water_data():
    return jsonify(generate_drinking_water_data()), 200

@app.route('/irrigation_water', methods=['GET'])
def get_irrigation_water_data():
    return jsonify(generate_irrigation_water_data()), 200

@app.route('/industrial_water', methods=['GET'])
def get_industrial_water_data():
    return jsonify(generate_industrial_water_data()), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
