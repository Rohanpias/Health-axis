# Health Axis

## Introduction

Health Axis is a comprehensive medical records filing system aimed at providing efficient management of patient health data. It offers a user-friendly interface for healthcare professionals to access, update, and securely store medical records.

## Features

- **User Authentication**: Secure login system for authorized healthcare personnel.
- **Medical Record Management**: Efficient filing and retrieval of patient health records.
- **Interactive Dashboard**: Intuitive dashboard for quick access to essential information.
- **Real-time Monitoring**: Monitoring system to track application performance and usage.
- **Azure Integration**: Utilizes Azure services for scalability, security, and reliability.

## Contribution

1. **Frontend Team (Kishore Shyam Raj J)**: Responsible for designing and implementing the user interface using HTML, CSS, and JavaScript. They focus on creating an intuitive and user-friendly experience for accessing and managing medical records.

2. **Backend Team (Rohanpias A)**: Tasked with developing the server-side logic and database management. This includes handling data storage, retrieval, and processing. Security and compliance with healthcare regulations may also fall under their responsibility.

3. **Cloud Engineer (Abishek K)**: Manages the deployment and scaling of the application on Azure cloud infrastructure. They ensure the application runs smoothly, efficiently utilizes resources, and stays highly available. They may also be involved in setting up monitoring and automation processes using Azure Monitor and other relevant tools.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: SQLite3
- **Cloud**: Azure Static Web Apps, Azure Monitor, Azure Bot Service
- **Version Control**: Git, GitHub

## Project Description

Health Axis is a comprehensive web platform designed to streamline the healthcare experience for patients and healthcare organizations alike. With a user-friendly login/signup interface, patients can easily enroll and access their medical records, including diagnosis processes, medical history, and prescriptions. Through secure channels, healthcare organizations can seamlessly upload patient details, ensuring efficient communication and accurate record-keeping. Health Axis is the bridge between patients and healthcare providers, prioritizing accessibility, security, and convenience in healthcare management.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Initialize the databases:
    ```bash
    python app.py
    ```

5. Run the Flask application:
    ```bash
    flask run
    ```

## Usage

1. Navigate to `http://127.0.0.1:5000/` in your web browser.

2. Register as a new user or log in with an existing account. Admins can log in using the predefined credentials:
    - Email: `admin@gmail.com`
    - Password: `Admin@99419`

3. After logging in, users will be redirected to their respective dashboards.

### Admin Dashboard

- Admins can add new patient records, including uploading test reports and prescriptions.
- Admins can also update existing patient records.

### User Dashboard

- Users can view their personal patient details.
- Users can download their test reports and prescriptions if available.

## File Structure

- `app.py`: The main application file containing the Flask routes and logic.
- `templates/`: Directory containing HTML templates.
    - `index.html`: Home page template.
    - `admin_dashboard.html`: Admin dashboard template.
    - `user_dashboard.html`: User dashboard template.
- `static/`: Directory containing static files like CSS and JavaScript.
    - `admin.css`: CSS file for the admin dashboard.
    - `user.css`: CSS file for the user dashboard.
    - `nav.js`: JavaScript file for handling form submissions.

## Database Schema

### Users Table
- `id`: Integer, primary key.
- `email`: Text, unique.
- `password`: Text.

### Admins Table
- `id`: Integer, primary key.
- `email`: Text, unique.
- `password`: Text.

### Patients Table
- `id`: Integer, primary key.
- `name`: Text.
- `age`: Integer.
- `email`: Text.
- `phone`: Text.
- `consultation_date`: Text.
- `test_result`: BLOB.
- `prescription`: BLOB.
- `doctor_description`: Text.