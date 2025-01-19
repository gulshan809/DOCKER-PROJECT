**Hospital Management System**
This project is a microservice-based application for managing hospital-related functionalities, including patient management, doctor management, and appointments.
A frontend service connects all the backend services to provide a user-friendly interface.
**Project Structure**
The system is divided into the following services:
**Patient Service**
Manages patient information.
Runs on port 5003.
**Doctor Service**
Handles doctor-related data.
Runs on port 5001.
**Appointment Service**
Manages appointments between patients and doctors.
Runs on port 5002.
**Frontend**
The user interface for the application.
Runs on port 5000.
**Technologies Used**
Backend Services: Each service is independently built and containerized using Docker.
Frontend: Connected to the backend via REST APIs.
Docker: Used for containerization and networking.
**Prerequisites**
Docker installed on your machine.
**Getting Started**
Step 1: Clone the Repository
git clone <repository_url>
cd <repository_folder>
Step 2: Build and Start the Services
Use Docker Compose to build and start all services:
docker-compose up --build
Step 3: Access the Application
Frontend: http://localhost:5000
Backend Services (APIs):
Patient Service: http://localhost:5003
Doctor Service: http://localhost:5001
Appointment Service: http://localhost:5002
Step 4: Stop the Services
To stop all running services:
docker-compose down
Network Configuration
All services are connected through a Docker network (hospital-network) using the bridge driver.
**Future Enhancement**
Add authentication for secure access.
Extend the frontend with more features like dashboards and notifications.
Implement a database for persistent storage.
