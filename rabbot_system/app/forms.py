from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import SelectField, RadioField
from wtforms.validators import DataRequired
from app.playback import Player

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
    unlock_hips = SubmitField('Unlock Hips')
    unlock_knees = SubmitField('Unlock Knees')
    unlock_ankles = SubmitField('Unlock Ankles')
    unlock_group_1 = SubmitField('Unlock Group 1')
    unlock_group_2 = SubmitField('Unlock Group 2')
    unlock_group_3 = SubmitField('Unlock Group 3')
    name = StringField('Name')

class PlaybackForm(FlaskForm):
    selection = RadioField('Sequences')

    play_forward = SubmitField('Forward')
    play_backward = SubmitField('Backward')
