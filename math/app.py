import random
from flask import Flask, jsonify

app = Flask(__name__)

# Simulated data for different groups
def generate_group_data(operation):
    # Generate 3 random values between 1 and 100 for each group member
    values = [random.randint(1, 100) for _ in range(3)]
    return {
        "operation": operation,
        "members": {
            "member1": values[0],
            "member2": values[1],
            "member3": values[2]
        }
    }

@app.route('/group1', methods=['GET'])
def group1_addition():
    # Group 1 performs addition
    return jsonify(generate_group_data("addition"))

@app.route('/group2', methods=['GET'])
def group2_subtraction():
    # Group 2 performs subtraction
    return jsonify(generate_group_data("subtraction"))

@app.route('/group3', methods=['GET'])
def group3_multiplication():
    # Group 3 performs multiplication
    return jsonify(generate_group_data("multiplication"))

@app.route('/group4', methods=['GET'])
def group4_division():
    # Group 4 performs division
    return jsonify(generate_group_data("division"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
