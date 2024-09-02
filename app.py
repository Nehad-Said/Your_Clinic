from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from models import User, Patient, Appointment, Equipment, NotificationForm, TreatmentForm
from forms import RegistrationForm, LoginForm, PatientForm, AppointmentForm, NotificationForm, TreatmentForm
import os

app = Flask(__name__)
app.config.form_object('config.config')
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'Login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    equipment = Equipment.query.all()
    return render_template('index.html', equipment=equipment)

@app.route('/register_patient', methods=['GET', 'POST'])
@login_required
def register_patient():
    form = PatientForm()
    if form.validate_on_submit():
        new_patient = patient(name=form.name.data, email=form.email.data, phone=form.phone.data, medical_history= form.medical_history.data)
        db.session.add(new_patient)
        db.session.commit()
        flash('Patient Registered Successfully', 'success')
        return redirect(url_for('dashboard'))
    return render_template('register_patient.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    patients = patient.query.all()
    appointments = Appointment.query.all()
    return render_template('dashboard.html', patients=patients, appointments=appointments)

@app.route('/patient/<int:patient_id>', methods=['GET', 'POST'])
@login_required
def patient_profile(patient_id):
    patient = patient.query.get_or_404(patient_id)
    treatments = Treatment.query.filter_by(patient_id=patient_id).all()
    treatment_form = TreatmentForm()
    appointment_form = AppointmentForm()

    if treatment_form.validate_on_submit():
        new_treatment = Treatment(description=treatment_form.description.data, patient_id=patient.id)
        db.session.add(new_treatment)
        db.session.commit()
        flash('Treatment Added Successfully', 'success')
        return redirect(url_for('patient_profile', patient_id=patient.id))

    if appointment_form.validate_on_submit():
        new_appointment = Appointment(patient_id=appointment_form.patient_id.data, doctor_id=appointment_form.doctor_id.data, appointment_time=appointment_form.appointment_time.data)
        db.session.add(new_appointment)
        db.session.commit()
        flash('Appointment Scheduled Successfully', 'success')
        return redirect(url_for('dashboard'))

    return render_template('patient_profile.html', patient=patient, treatments=treatments, treatment_form=treatment_form, appointment_form=appointment_form)


@app.route('/manage_appointments')
@login_required
def manage_appointments():
    appointments = Appointment.query.all()
    return render_template('manage_appointments.html', appointments=appointments)


@app.route('/manage_equipment')
@login_required
def manage_equipment():
    equipment = Equipment.query.all()
    return render_template('manage_equipment.html', equipment=equipment)


@app.route('/notifications', methods=['GET', 'POST'])
@login_required
def notifications():
    notifications = Notification.query.filter_by(recipient_id=current_user.id).all()
    return render_template('notifications.html', notifications=notifications)

@app.route('/reports')
@login_required
def reports():
    patients = Patient.query.all()
    treatments = Treatment.query.all()
    return render_template('reports.html', patients=patients, treatments=treatments)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user, remember=form.remember.data)
            return redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
        
