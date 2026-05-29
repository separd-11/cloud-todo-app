from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# CORS is required so our separate frontend can communicate with this backend
# CORS is required so our separate frontend can communicate with this backend
CORS(app) 

tasks = []

@app.route('/api/tasks', methods=['GET', 'POST'])
def handle_tasks():
    if request.method == 'POST':
        data = request.get_json()
        if data and 'task' in data:
            tasks.append(data['task'])
            return jsonify({"status": "success"}), 201
    return jsonify(tasks), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)