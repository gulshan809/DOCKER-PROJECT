from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Welcome to the Appointment Service!"

@app.route('/appointments', methods=['GET'])
def get_appointments():
    return jsonify([
        {"id": 1, "patient_id": 1, "doctor_id": 1, "date": "2025-01-16"},
        {"id": 2, "patient_id": 2, "doctor_id": 2, "date": "2025-01-17"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
