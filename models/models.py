from . import db
from flask_login import UserMixin
from datetime import datetime


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return f"<Role id={self.id} name={self.name}>"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    def __repr__(self):
        return f"<User id={self.id} username={self.username} email={self.email} role_id={self.role_id}>"

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    medical_history = db.Column(db.Text)
    registered_at = db.Column(db.DateTime, default=datetime.utcnow)
    treatments = db.relationship('Treatment', backref='patient', lazy=True)

    def __repr__(self):
        return f"<Patient id={self.id} name={self.name} email={self.email} phone={self.phone}>"

class Treatment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    description = db.Column(db.Text, nullable=False)
    treatment_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Treatment id={self.id} patient_id={self.patient_id} description={self.description} treatment_date={self.treatment_date}>"

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    appointment_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='scheduled')

    def __repr__(self):
        return f"<Appointment id={self.id} patient_id={self.patient_id} doctor_id={self.doctor_id} appointment_time={self.appointment_time} status={self.status}>"

class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    stock_quantity = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Equipment id={self.id} name={self.name} description={self.description} image_url={self.image_url} stock_quantity={self.stock_quantity}>"

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    is_read = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Notification id={self.id} recipient_id={self.recipient_id} message={self.message} is_read={self.is_read} timestamp={self.timestamp}>"

