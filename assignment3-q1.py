from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page <br> Put /api in the URL to get the API data"


@app.route('/api')
def api():
    with open('assign3.json') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
