from .. import db
from .. import models
from flask_login import login_required, current_user, logout_user
from flask import request, render_template, url_for, redirect, jsonify, Response
from . import main

@main.route('/main', methods=['GET', 'POST'])
@login_required
def main_page():
    if request.method == 'GET':
        return render_template('')
