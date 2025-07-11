"""
# FUNCTIONAL 1ST ------------------------

# Exmaple usage:
# http://127.0.0.1:5000/

from flask import Flask, request, jsonify

# Create flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

# Check if this script is being run directly (not imported as a module)
if __name__ == "__main__":
    app.run(debug=True)
"""

"""
# FUNCTIONAL 2ND ------------------------

# Example usage:
# http://127.0.0.1:5000/get-user/123?extra=%22BTC-New-ATH%22

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-user/<user_id>")
def get_user(user_id):
    
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    
    return jsonify(user_data), 200


if __name__ == "__main__":
    app.run(debug=True)
"""

# FUNCTIONAL 3RD ------------------------

# Example usage:
# GET
# http://127.0.0.1:5000/get-user/123?extra=%22BTC-New-ATH%22
# POST
# http://127.0.0.1:5000/create-user

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-user/<user_id>")
def get_user(user_id):
    
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    
    return jsonify(user_data), 200

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()
    return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True)
