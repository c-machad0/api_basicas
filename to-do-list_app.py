from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
    'id': 1,
    'description': 'Ir para academia'
    }
]

@app.route('/')
def home():
    return 'To-do-list API'

@app.route('/tasks')
def get_tasks():
    return jsonify(tasks), 200

@app.route('/tasks', methods=['POST'])
def create_tasks():
    request_task = request.get_json()
    task = {
        'id': request_task['id'],
        'description': request_task['description']
    }

    tasks.append(task)

    return jsonify(task)

app.run(port=5000) # inicializa a api