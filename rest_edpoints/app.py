import random
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/metric1', methods=['GET'])
def metrics1():
    # Simulate some metrics for endpoint 1
    metrics = {
        "metric_name": "endpoint1_metric",
        "value": random.uniform(10, 100)
    }
    return jsonify(metrics)

@app.route('/metric2', methods=['GET'])
def metrics2():
    # Simulate some metrics for endpoint 2
    metrics = {
        "metric_name": "endpoint2_metric",
        "value": random.uniform(20, 200)
    }
    return jsonify(metrics)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
