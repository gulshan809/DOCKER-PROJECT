from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Welcome to the Doctor Service!"

@app.route('/doctors', methods=['GET'])
def get_doctors():
    return jsonify([
        {"id": 1, "name": "Doctor A", "specialty": "Cardiology"},
        {"id": 2, "name": "Doctor B", "specialty": "Neurology"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
