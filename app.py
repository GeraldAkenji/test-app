from flask import Flask, render_template, request
import requests as r
import os
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
LOGIN_URL = os.getenv('LOGIN_MICROSERVICE_URL')

@app.route('/', methods=['GET', 'POST'])
def index():
    output = ''
    if request.method == 'POST':
        username = request.form.get('username')
        passw = request.form.get('paswd')
        print(username, passw)
        
        payload = {
            'username': username,
            'password': passw
        }
        headers = {
            'Content-Type': "application/json"
        }
        try:
            response = r.post(f"{LOGIN_URL}", json=payload, headers=headers)
            output = response.text
            print(output)  # Print response for debugging purposes
        except Exception as e:
            output = str(e)
            print(f"An error occurred: {output}")

    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
