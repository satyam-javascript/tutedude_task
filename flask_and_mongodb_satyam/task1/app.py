import json
import os
from flask import Flask, jsonify

app = Flask(__name__)

# Define the path to the backend data file
DATA_FILE = "data.json"

@app.route('/api', methods=['GET'])
def get_api_data():
    # 1. Check if the file exists to prevent errors
    if not os.path.exists(DATA_FILE):
        return jsonify({"error": "Data file not found"}), 404
        
    try:
        # 2. Open and read the JSON file
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            data_list = json.load(file)
            
        # 3. Return the parsed Python list as a JSON response
        return jsonify(data_list), 200

    except json.JSONDecodeError:
        # Gracefully handle the error if the file format gets corrupted
        return jsonify({"error": "Failed to decode backend data file"}), 500

if __name__ == '__main__':
    # Run the server locally on http://127.0.0.1:5000
    app.run(debug=True)
