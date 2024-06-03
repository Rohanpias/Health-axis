# Health Axis
## Introduction

Health Axis is a comprehensive medical records filing system aimed at providing efficient management of patient health data. It offers a user-friendly interface for healthcare professionals to access, update, and securely store medical records.

## Features

- *User Authentication*: Secure login system for authorized healthcare personnel.
- *Medical Record Management*: Efficient filing and retrieval of patient health records.
- *Interactive Dashboard*: Intuitive dashboard for quick access to essential information.
- *Real-time Monitoring*: Monitoring system to track application performance and usage.
- *Azure Integration*: Utilizes Azure services for scalability, security, and reliability.

## Contribution

1. *Frontend Team (Kishore Shyam Raj J)*: Responsible for designing and implementing the user interface using HTML, CSS, and JavaScript. They focus on creating an intuitive and user-friendly experience for accessing and managing medical records.

2. *Backend Team (Rohanpias A)*: Tasked with developing the server-side logic and database management. This includes handling data storage, retrieval, and processing. Security and compliance with healthcare regulations may also fall under their responsibility.

3. *Cloud Engineer ( Abishek K)*: Manages the deployment and scaling of the application on Azure cloud infrastructure. They ensure the application runs smoothly, efficiently utilizes resources, and stays highly available. They may also be involved in setting up monitoring and automation processes using Azure Monitor and other relevant tools.

## Technologies Used

- *Frontend*: HTML, CSS, JavaScript
- *Backend*: SQLite3
- *Cloud*: Azure Static Web Apps, Azure Monitor, Azure Bot Service
- *Version Control*: Git, GitHub

## Project Description

Health Axis is a comprehensive web platform designed to streamline the healthcare experience for patients and healthcare organizations alike. With a user-friendly login/signup interface, patients can easily enroll and access their medical records, including diagnosis processes, medical history, and prescriptions. Through secure channels, healthcare organizations can seamlessly upload patient details, ensuring efficient communication and accurate record-keeping. Health Axis is the bridge between patients and healthcare providers, prioritizing accessibility, security, and convenience in healthcare management.

## Installation

1. *Clone the repository:*
    bash
    git clone https://github.com/Rohanpias/Health-axis.git
    cd your-repo
    

2. *Create a virtual environment and activate it:*
    bash
    python3 -m venv venv
    source venv/bin/activate
    

3. *Install the required packages:*
    bash
    pip install -r requirements.txt
    

4. *Initialize the databases:*
    bash
    python app.py
    

5. *Run the Flask application:*
    bash
    flask run
    
## Usage

1. Navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your web browser.

2. Register as a new user or log in with an existing account. Admins can log in using the predefined credentials:
    - Email: admin@gmail.com
    - Password: Admin@99419

3. After logging in, users will be redirected to their respective dashboards.

### Admin Dashboard

- Admins can add new patient records, including uploading test reports and prescriptions.
- Admins can also update existing patient records.

### User Dashboard

- Users can view their personal patient details.
- Users can download their test reports and prescriptions if available.

## File Structure

- app.py: The main application file containing the Flask routes and logic.
- templates/: Directory containing HTML templates.
    - index.html: Home page template.
    - admin_dashboard.html: Admin dashboard template.
    - user_dashboard.html: User dashboard template.
- static/: Directory containing static files like CSS and JavaScript.
    - admin.css: CSS file for the admin dashboard.
    - user.css: CSS file for the user dashboard.
    - nav.js: JavaScript file for handling form submissions.

## Database Schema

### Users Table
- id: Integer, primary key.
- email: Text, unique.
- password: Text.

### Admins Table
- id: Integer, primary key.
- email: Text, unique.
- password: Text.

### Patients Table
- id: Integer, primary key.
- name: Text.
- age: Integer.
- email: Text.
- phone: Text.
- consultation_date: Text.
- test_result: BLOB.
- prescription: BLOB.
- doctor_description: Text.

## Links
- [GitHub Repository](https://github.com/Rohanpias/Health-axis.git)
- [Project Demo](https://youtu.be/FhxzgVXZRho)

![1](https://github.com/Rohanpias/Health-axis/assets/100913880/73ea08b6-9d4f-4707-a1cf-33763710d23e)
![2](https://github.com/Rohanpias/Health-axis/assets/100913880/602da21e-8d67-410e-a837-fcbc4e962280)
![3](https://github.com/Rohanpias/Health-axis/assets/100913880/7c810d1d-619f-4c76-ab80-dfa738b2f3c3)
![4](https://github.com/Rohanpias/Health-axis/assets/100913880/e4ea0de6-7327-499a-a392-99fc378e63e7)
![5](https://github.com/Rohanpias/Health-axis/assets/100913880/769df857-0b43-4436-991d-bdb22ce0ed8a)
![6](https://github.com/Rohanpias/Health-axis/assets/100913880/c3fc329e-b799-4710-9d9a-13fa895fdc14)
![7](https://github.com/Rohanpias/Health-axis/assets/100913880/c7affb67-73c7-42d1-85be-7ad916702a12)
![8](https://github.com/Rohanpias/Health-axis/assets/100913880/6c606194-8a95-4cad-a776-030485e41d67)
![9](https://github.com/Rohanpias/Health-axis/assets/100913880/f17577e2-00f0-4cef-8e51-aaaa651d4afe)
![10](https://github.com/Rohanpias/Health-axis/assets/100913880/c4e2e027-3f4e-4167-b99d-724b02fa3c17)
![11](https://github.com/Rohanpias/Health-axis/assets/100913880/4628fb5a-7f25-4f4d-9482-c4bade400856)
![12](https://github.com/Rohanpias/Health-axis/assets/100913880/424aa954-63f1-4e8b-bc15-7eb12ae4418c)
![13](https://github.com/Rohanpias/Health-axis/assets/100913880/9210edff-1a4a-42d2-81f3-0627235638de)
![14](https://github.com/Rohanpias/Health-axis/assets/100913880/13c78195-3343-4b4f-93b2-0ae28b3737d4)
![15](https://github.com/Rohanpias/Health-axis/assets/100913880/addf6220-1a50-4239-8836-e971816bc79f)
![16](https://github.com/Rohanpias/Health-axis/assets/100913880/b8dbddf1-d1fc-4656-98a8-1d7da80ab0ea)
![17](https://github.com/Rohanpias/Health-axis/assets/100913880/6b77bd36-360d-4c33-bfe5-a38cfb06e30a)
![18](https://github.com/Rohanpias/Health-axis/assets/100913880/96dc3983-acfe-441b-be6e-12ec41b5d586)
![19](https://github.com/Rohanpias/Health-axis/assets/100913880/d7475a5b-eb87-4d1b-ae4d-2aa640122f30)
![20](https://github.com/Rohanpias/Health-axis/assets/100913880/778e3f6a-1761-4dc0-8cc8-68df9ef35fb2)
![21](https://github.com/Rohanpias/Health-axis/assets/100913880/52925e83-9c0e-48e2-8a73-35928f3b9c3a)
![22](https://github.com/Rohanpias/Health-axis/assets/100913880/199f0e84-abaf-44aa-8bcd-a5521b3d9c4c)
![23](https://github.com/Rohanpias/Health-axis/assets/100913880/e5f92a60-d35e-4696-a7e1-b0472c0f17ea)
![24](https://github.com/Rohanpias/Health-axis/assets/100913880/8eb299d8-3c42-450b-8742-a5e62f88452b)
![25](https://github.com/Rohanpias/Health-axis/assets/100913880/ace7b206-bfc5-4bc2-a12c-af84b3fc965b)
