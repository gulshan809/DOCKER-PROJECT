from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Welcome to the Patient Service!"

@app.route('/patients', methods=['GET'])
def get_patients():
    return jsonify([
        {"id": 1, "name": "Patient A"},
        {"id": 2, "name": "Patient B"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
