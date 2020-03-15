
from flask import Flask, jsonify

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)
