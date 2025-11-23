from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Apna JWT yaha daalo
JWT = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiI1ODM4NTgzMzg4IiwianRpIjoiNTI1ZjM2MGEtNzc1MC00ZDBmLWJhNWYtNGM1ZjJlNWRhNWIyIiwiZXhwIjoxNzk0MjM1NTM1fQ.nQ3VAZihD4reG1g4UjyO02RkRmi5YbzLZmsFknSH3z3Nsa5oDKmqCDlJNdw4dOzsdvYB9fZ2MD1pJz2ireJhXmqsiqMbz6tpukD3TKwkei2-S-z_rmO0Ku1LOGDO_cQk-dOypyNejuwPM0glSTZ4G1UK0CK-lGnZ9XCIu-y7WZY"

@app.route("/user-details")
def user_details():
    user_id = request.args.get("user")

    if not user_id:
        return jsonify({"success": False, "error": "Missing user ID"}), 400

    url = f"https://funstat.info/api/v1/users/{user_id}/stats_min"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {JWT}"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return jsonify({"success": False, "error": "Failed to fetch user info", "code": response.status_code}), 500
        
        data = response.json()
        return jsonify({"success": True, "data": data})
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
