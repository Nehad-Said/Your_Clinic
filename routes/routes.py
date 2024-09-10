from flask import Blueprint, render_template, request, redirect, url_for, flash
from forms.forms import PatientForm, TreatmentForm, AppointmentForm, LoginForm
from flask_login import login_required, current_user, login_user, logout_user
# Define the blueprint
main = Blueprint('main', __name__)

# Route for the home page
@main.route('/')
def index():
    from models.models import Equipment
    from models import db
    equipment = Equipment.query.all()
    return render_template('index.html', equipment=equipment)

# Route to register a new patient
@main.route('/register_patient', methods=['GET', 'POST'])
@login_required
def register_patient():
    from models.models import Patient
    form = PatientForm()
    if form.validate_on_submit():
        new_patient = Patient(
            name=form.name.data,
            email=form.email.data,
            phone=form.phone.data,
            medical_history=form.medical_history.data
        )
        db.session.add(new_patient)
        db.session.commit()
        flash('Patient Registered Successfully', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('register_patient.html', form=form)

# Dashboard showing patients and appointments
@main.route('/dashboard')
@login_required
def dashboard():
    from models.models import Patient, Appointment
    patients = Patient.query.all()
    appointments = Appointment.query.all()
    return render_template('dashboard.html', patients=patients, appointments=appointments)

# View and manage a patient's profile, treatments, and appointments
@main.route('/patient/<int:patient_id>', methods=['GET', 'POST'])
@login_required
def patient_profile(patient_id):
    from models.models import Patient, Treatment, Appointment
    patient = Patient.query.get_or_404(patient_id)
    treatments = Treatment.query.filter_by(patient_id=patient_id).all()
    treatment_form = TreatmentForm()
    appointment_form = AppointmentForm()

    # Add a new treatment
    if treatment_form.validate_on_submit():
        new_treatment = Treatment(
            description=treatment_form.description.data,
            patient_id=patient.id
        )
        db.session.add(new_treatment)
        db.session.commit()
        flash('Treatment Added Successfully', 'success')
        return redirect(url_for('main.patient_profile', patient_id=patient.id))

    # Schedule a new appointment
    if appointment_form.validate_on_submit():
        new_appointment = Appointment(
            patient_id=appointment_form.patient_id.data,
            doctor_id=appointment_form.doctor_id.data,
            appointment_time=appointment_form.appointment_time.data
        )
        db.session.add(new_appointment)
        db.session.commit()
        flash('Appointment Scheduled Successfully', 'success')
        return redirect(url_for('main.dashboard'))

    return render_template('patient_profile.html', patient=patient, treatments=treatments,
                           treatment_form=treatment_form, appointment_form=appointment_form)

# Route to manage appointments
@main.route('/manage_appointments')
@login_required
def manage_appointments():
    from models.models import Appointment
    appointments = Appointment.query.all()
    return render_template('manage_appointments.html', appointments=appointments)

# Route to manage equipment
@main.route('/manage_equipment')
@login_required
def manage_equipment():
    from models.models import Equipment
    equipment = Equipment.query.all()
    return render_template('manage_equipment.html', equipment=equipment)

# Route to view notifications
@main.route('/notifications', methods=['GET', 'POST'])
@login_required
def notifications():
    from models.models import Notification
    notifications = Notification.query.filter_by(recipient_id=current_user.id).all()
    return render_template('notifications.html', notifications=notifications)

# Route to generate reports for patients and treatments
@main.route('/reports')
@login_required
def reports():
    from models.models import Treatment, Patient
    patients = Patient.query.all()
    treatments = Treatment.query.all()
    return render_template('reports.html', patients=patients, treatments=treatments)

# Login route
@main.route('/login', methods=['GET', 'POST'])
def login():
    from models.models import User
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user, remember=form.remember.data)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)

# Logout route
@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

