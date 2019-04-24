from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, ControllerForm
from app.recorder import Recorder

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
