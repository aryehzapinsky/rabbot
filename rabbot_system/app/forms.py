from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class ControllerForm(FlaskForm):
    stop_motors = SubmitField('Stop Motors')
    record_positions = SubmitField('Record Positions')
    start_motors = SubmitField('Start Motors')
    save_sequence = SubmitField('Save Sequence')
    reset_sequence = SubmitField('Reset Sequence')
    name = StringField('Name')
