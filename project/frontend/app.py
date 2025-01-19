import requests
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Hospital Management System</h1>
    <ul>
        <li><a href="/patients">View Patients</a></li>
        <li><a href="/doctors">View Doctors</a></li>
        <li><a href="/appointments">View Appointments</a></li>
    </ul>
    '''

@app.route('/patients')
def patients():
    patients = requests.get('http://patient-service:5003/patients').json()
    return jsonify(patients)

@app.route('/doctors')
def doctors():
    doctors = requests.get('http://doctor-service:5001/doctors').json()
    return jsonify(doctors)

@app.route('/appointments')
def appointments():
    appointments = requests.get('http://appointment-service:5002/appointments').json()
    return jsonify(appointments)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
