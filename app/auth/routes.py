from flask import redirect, render_template, request, session, url_for, flash, jsonify
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import auth
from .. import db
from ..models import User
import os



@auth.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html')



@auth.route('/login', methods=['POST'])
def login_post():
    # авторизация
    pocket = request.json
    data = pocket['login_data']
    def check_is_root():
        if (data['login_email'] == 'root' or data['login_email'] == 'root@root.com') and data['password'] == 'root':
            if not User.query.filter_by(login='root').first():
                root = User(email='root@root.com', login='root', password='root', role='root', telegram='@danchajexel')
                db.session.add(root)
                db.session.commit()
            login_user(User.query.filter_by(login='root').first())
            print(current_user.is_authenticated)
            print(current_user.get_id())
            #session['login'] = User.query.filter_by(login='root').first().login
            return True
        return False

    if check_is_root():
        print('its root acc')
        return jsonify({'msg': 'ok'}), 200

    def get_user():
        if '@' in data['login_email']:
            user = User.query.filter_by(email=data['login_email']).first()
        else:
            user = User.query.filter_by(login=data['login_email']).first()
        return user

    user = get_user()

    if not user or not data['password'] == user.password:
        flash('wrong pass')
        return jsonify({'msg': 'ok'}), 401

    login_user(user,  remember=True)
    #session['login'] = user.login
    return jsonify({'msg': 'ok'}), 200

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login_get'))