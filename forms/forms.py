from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, DateTimeField, IntegerField, SelectField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    role = SelectField('Role', choices=[('Admin', 'Admin'), ('Doctor', 'Doctor'), ('Receptionist', 'Receptionist')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class PatientForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])
    medical_history = TextAreaField('Medical History')
    submit = SubmitField('Register Patient')

class TreatmentForm(FlaskForm):
    description = TextAreaField('Treatment Description', validators=[DataRequired()])
    submit = SubmitField('Add Treatment')

class AppointmentForm(FlaskForm):
    patient_id = SelectField('Patient', coerce=int, validators=[DataRequired()])
    doctor_id = SelectField('Doctor', coerce=int, validators=[DataRequired()])
    appointment_time = DateTimeField('Appointment Time', validators=[DataRequired()])
    submit = SubmitField('Schedule Appointment')

class NotificationForm(FlaskForm):
    recipient_id = SelectField('Recipient', coerce=int, validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Notification')

