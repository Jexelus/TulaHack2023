from flask import redirect, render_template, request, session, url_for, flash
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import auth
from .. import db, Staff
import os


@auth.route('/registration')
def registration():
    data = request.json
    if data is None:
        data = request.form.to_dict()
    registration_data = data['registration_data']
    new_user = Staff(login=registration_data['login'], password=generate_password_hash(registration_data['password'], method='sha256'), role='employee')
    db.session.add(new_user)
    db.session.commit()
    redirect(url_for('')) #TODO: make login

@auth.route('/login')
def login_post():
    # авторизация
    login = request.form.get('login')
    password = request.form.get('password')

    user = Staff.query.filter_by(login=login).first()

    if not user or not check_password_hash(user.password, password):
        flash('wrong pass')
        return redirect(url_for('auth.login'))

    session['login'] = request.form.get('login')

    login_user(user)

    return redirect(url_for('')) #TODO: make main

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))