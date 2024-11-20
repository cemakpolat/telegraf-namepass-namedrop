from flask import Flask, jsonify
import random

app = Flask(__name__)

standard_robots = ["robot1","robot2"]
delivery_robots = ["robot3","robot4"]
inspection_robots = ["robot5","robot6"]

# Function to generate data based on robot type
def generate_robot_data(robot_id, robot_type):
    data = {
        "robot_id": robot_id,
        "robot_type": robot_type,
        "location": [random.randint(0, 10), random.randint(0, 10)],  # X, Y grid
        "battery_level": random.randint(10, 100),  # Battery percentage
    }

    # Customize fields based on robot type
    if robot_type == "standard":
        data["status"] = random.choice(["idle", "assisting", "carrying"])
        data["current_load"] = 0
        if data["status"] == "carrying":
            data["current_load"] = random.randint(80, 150)  # Higher likelihood of carrying load
    elif robot_type == "delivery":
        data["current_load"] = 0
        data["status"] = random.choice(["idle", "carrying"])  # Delivery robots are usually active
        if data["status"] == "carrying":
            data["current_load"] = random.randint(80, 150)  # Higher likelihood of carrying load
    elif robot_type == "inspection":
        data["quality_check"] = "pass"
        data["status"] = random.choice(["idle", "inspecting"])  # Delivery robots are usually active
        if data["status"] == "inspecting":
            data["quality_check"] = random.choice(["pass", "fail"])  # Quality check result
    else:
        print("wrong path")

    return data


# Routes for each robot
@app.route('/robot/<robot_id>', methods=['GET'])
def get_robot_data(robot_id):
    # Assign robot type based on ID for simplicity
    if robot_id in standard_robots:
        robot_type = "standard"
    elif robot_id in delivery_robots:
        robot_type = "delivery"
    elif robot_id in inspection_robots:
        robot_type = "inspection"
    else:
        print("unknown robot type")
        return
    return jsonify(generate_robot_data(robot_id, robot_type))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
