from flask import Flask, jsonify, request
import json
import os
import random
import string

app = Flask(__name__)
DATA_FILE = 'data.json'

def generate_random_token(length=16):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

@app.route('/login', methods=['GET'])
def get_login():
    auth_token = generate_random_token()
    return jsonify({'auth_token': auth_token}), 200

@app.route('/login', methods=['POST'])
def post_login():
    data = request.get_json()
    print(data)
    if data:
        # Extract username and password from the received JSON data
        username = data.get('username')
        password = data.get('password')

        # Prepare response data
        response_data = {
            'message': 'Data received successfully',
            'username': username,
            'password': password
        }

        # Read existing data from the file
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as file:
                try:
                    existing_data = json.load(file)
                except json.JSONDecodeError:
                    existing_data = []
        else:
            existing_data = []

        # Append the new data
        existing_data.append(data)

        # Write the updated data back to the file
        with open(DATA_FILE, 'w') as file:
            json.dump(existing_data, file, indent=4)

        return jsonify(response_data), 200
    else:
        return jsonify({'error': 'No JSON data received'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8673)
