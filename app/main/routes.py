from .. import db
from .. import models
from flask_login import login_required, current_user, logout_user
from flask import request, render_template, url_for, redirect, jsonify, Response, stream_with_context
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

    if request.method == 'GET':
        return render_template('table.html', tasks=tasks)

@main.route('/gen_analytic/<int:user_id>', methods=['GET'])
def generate_analytic(user_id):
    import json
    import time
    def analytic_update():
        import random
        while True:
            mouths = [x for x in range(1, 12)]
            mouth = random.choice(mouths)
            json_data = json.dumps({
                'mouth': str(mouth),
                'tasks_comleted': len(models.Tasks.query.filter_by(completed_mounth=str(mouth), completed_by=current_user.get_id()).all())})
            #print(len(models.Tasks.query.filter_by(completed_mounth=str(mouth), completed_by=current_user.get_id()).all()))
            yield f'data:{json_data}\n\n'
            time.sleep(3)
    response = Response(stream_with_context(analytic_update()), mimetype="text/event-stream")
    response.headers["Cache-Control"] = "no-cache"
    response.headers["X-Accel-Buffering"] = "no"
    return response


@main.route('/profile')
@main.route('/profile/<int:user_id>', methods=['GET'])
@login_required
def profile_view(user_id=None):
    # print(len(models.Tasks.query.filter_by(comleted_mounth=10, complited_by=user_id)))
    user = models.User.query.filter_by(id=user_id).first()
    if user == None:
        user = models.User.query.filter_by(id=current_user.get_id()).first()
    users = models.User.query.all()

    return render_template('profile.html', 
                           user=user, 
                           users=users)

@main.route('/new_task', methods=['POST'])
@login_required
def new_task():
    pocket = request.json
    data = pocket['task']
    print(f"new task {data['task_header']}, {data['task_group']}, {data['task_group']}, {data['task_state']}")
    task = models.Tasks(task_header=data['task_header'], task_body=data['task_body'], task_group=data['task_group'], task_state=data['task_state'])
    db.session.add(task)
    db.session.commit()
    return jsonify({'msg': 'ok'}), 200

@main.route('/delete_task', methods=['POST'])
def delete_task():
    pocket = request.json
    id = pocket['id']
    db.session.delete(models.Tasks.query.filter_by(task_id=id).first())
    db.session.commit()
    return jsonify({'msg':'ok'}), 200

@main.route('/complete_task', methods=['POST'])
def complete_task():
    from datetime import datetime
    pocket = request.json
    print(dict(pocket))
    id = pocket['id']
    task = models.Tasks.query.filter_by(task_id=id).first()
    task.completed_day = str(datetime.now().day)
    task.completed_mounth = str(datetime.now().month)
    task.task_state = 'completed'
    task.completed_by = str(current_user.get_id())
    db.session.commit()
    return jsonify({'msg':'ok'}), 200