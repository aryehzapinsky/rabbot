from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, ControllerForm, PlaybackForm
from app.recorder import Recorder
from app.playback import Player

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Aryeh'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/controller', methods=['GET', 'POST'])
def controller():
    form = ControllerForm()
    if form.validate_on_submit():
        if form.stop_motors.data:
            Recorder.stop_motors()
            flash('Stop motors was clicked')
        elif form.start_motors.data:
            Recorder.start_motors()
            flash('Start motors was clicked')
        elif form.save_sequence.data:
            Recorder.save_sequence(form.name.data)
            flash('Save sequence was clicked')
        elif form.reset_sequence.data:
            Recorder.reset_sequence()
            flash('Reset sequence was clicked')
        elif form.record_positions.data:
            Recorder.record_positions()
            flash('Record positions was clicked')
        return redirect(url_for('controller'))
    return render_template('controller.html', form=form)

@app.route('/playback', methods=['GET', 'POST'])
def playback():
    form = PlaybackForm()

    sequence_dict = Player().get_sequences()
    choices = [(k, k) for k in sequence_dict.keys()]
    form.selection.choices = choices

    if form.validate_on_submit():
        sequence = form.selection.data
        if form.play_forward.data:
            Player.play_sequence(sequence)
        elif form.play_backward.data:
            Player.play_sequence(sequence, backwards=True)
        flash(sequence)
    return render_template('playback.html', form=form)
