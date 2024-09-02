Your Clinic App
Overview
The Your Clinic App is a web-based application designed to streamline the operations of a dental clinic. It allows clinic staff to register patients, manage appointments, track dental equipment, and handle various administrative tasks efficiently. The app also provides a user-friendly interface for both clinic staff and patients to interact with the clinic's services.

Features
Patient Management: Register new patients, view and update patient profiles, and track their medical history.
Appointment Management: Schedule, view, and manage patient appointments with ease.
Equipment Management: Track and display the clinic's equipment, ensuring that staff can monitor inventory and showcase new acquisitions.
Notifications: Receive notifications about upcoming appointments, equipment updates, and more.
User Authentication: Secure login system for clinic staff, with session management and protected routes.
Dashboard: Centralized dashboard providing a comprehensive overview of patients, appointments, and equipment.
Tech Stack
Backend: Flask - A lightweight WSGI web application framework in Python.
Database: SQLite - A C-language library that provides a relational database management system.
Frontend: HTML5, CSS3 (Bootstrap), JavaScript.
Authentication: Flask-Login - User session management for Flask.
ORM: SQLAlchemy - Python SQL toolkit and Object-Relational Mapping (ORM) library.
## Project Structure

```plaintext
dentistry_app/
├── app.py                    # Main application file
├── models.py                 # Database models
├── forms.py                  # Form classes using Flask-WTF
├── templates/                # HTML templates
│   ├── base.html             # Base template
│   ├── index.html            # Homepage displaying equipment
│   ├── login.html            # Login page
│   ├── dashboard.html        # Dashboard for managing the clinic
│   ├── register_patient.html # Page for registering new patients
│   ├── patient_profile.html  # Patient profile page
│   ├── manage_appointments.html # Manage appointments page
│   ├── manage_equipment.html # Manage equipment page
│   ├── reports.html          # Reports page
│   └── notifications.html    # Notifications page
├── static/                   # Static files (CSS, JS, images)
│   ├── css/
│   │   ├── bootstrap.min.css # Bootstrap CSS
│   │   ├── style.css         # Custom styles
│   ├── js/
│   │   ├── bootstrap.bundle.min.js # Bootstrap JS bundle
│   │   ├── main.js           # Custom JavaScript
├── config.py                 # Configuration file
└── data.db                   # SQLite database file

Installation
Clone the repository:

git clone https://github.com/yourusername/Your_Clinic.git

cd Your_Clinic

Create a virtual environment and activate it:

python3 -m venv venv
source venv/bin/activate


Set up the database:


flask db upgrade

Run the application:

flask run

Access the application:

Open your web browser and navigate to http://127.0.0.1:5000/.

Usage
Login: Use the credentials provided to access the dashboard.
Dashboard: Manage patients, appointments, and equipment from the centralized dashboard.
Register New Patients: Use the patient registration form to add new patients to the system.
Manage Appointments: Schedule and track appointments.
Equipment Management: View and update the clinic's equipment inventory.
