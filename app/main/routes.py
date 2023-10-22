from .. import db
from .. import models
from flask_login import login_required, current_user, logout_user
from flask import request, render_template, url_for, redirect, jsonify, Response
from . import main


@main.route('/')
@main.route('/table', methods=['GET'])
@login_required
def table():
    try:
        tasks = models.Tasks.query.all()
    except:
        tasks = None
        print('no tasks!')

    print(current_user)
    if request.method == 'GET':
        return render_template('table.html', tasks=tasks)
