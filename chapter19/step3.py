
from flask import Flask, jsonify, make_response, abort, request
from flask_httpauth import HTTPBasicAuth
import sqlite3
import subprocess


auth = HTTPBasicAuth()
app = Flask(__name__)


@auth.get_password
def get_password(username):
    if username == 'william':
        return 'secret_password'
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


def check_database(com):
    """
    :param com: command str()
    :return: str()
    """
    ar = []
    print(com)
    ar.append(com)
    print(ar)
    con = sqlite3.connect('todo.db')
    c = con.cursor()
    c.execute(com)
    message = c.fetchall()
    con.commit()
    con.close()
    return message


@app.route('/task/db', methods=['POST'])
@auth.login_required
def check_db():
    """
    :return: sql query tool send requires json() in request
    """
    if not request.json or 'sql' not in request.json:
        abort(400)
    result = check_database(request.json['sql'])
    return jsonify({"sql command": result})


def external(success):
    """
    :return: str()
    """
    print(success)
    result = subprocess.check_output(
        [success], shell=True
    )
    return result.decode().strip().replace("    ", "")  # convert byte 2 str


@app.route('/')
def index():
    return "<p>Hello, World!\n" \
           "<br>curl -i http://localhost:5000/todo/tasks"


task_list = [
    {
        'id': 1,
        'title': u'Mop Kitchen',
        'description': u'get bucket, mob, and soap',
        'done': False
    },
    {
        'id': 2,
        'title': u'Clean Garage',
        'description': u'Put away tools, sweep',
        'done': False
    }
]


@app.route('/todo/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': task_list})


@app.route('/todo/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in task_list if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@app.route('/todo/tasks', methods=['POST'])
def create_new_task():
    if not request.json:
        abort(400)
    task = {
        'id': task_list[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json['description'],
        'done': False
    }
    task_list.append(task)
    return jsonify({'task': task}), 201


@app.route('/todo/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in task_list if task['id'] == task_id]
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})


@app.route('/task/stat/<task_name>', methods=['GET'])
def stats(task_name):
    """
    :param task_name: str()
    :return: json()
    """
    if task_name == "stats":
        task = fix_list(external("top -b -n 1"))
        return jsonify({'top': task})
    if task_name == "access":
        task = fix_list(external("tail -n 100 /srv/access.log"))
        return jsonify({'access log': task})
    if task_name == "error":
        task = fix_list(external("tail -n 100 /srv/gunicorn.log"))
        return jsonify({'error log gunicorn': task})
    else:
        abort(404)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
