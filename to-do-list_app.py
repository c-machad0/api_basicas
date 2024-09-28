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

    for i in tasks:
        if i['id'] == request_task['id']:
            return jsonify('message: Tarefa não pode ser criada. {id} ja existe'), 400
        elif i['description'] == request_task['description']:
            return jsonify('message: Tarefa não pode ser criada. {description} ja existe'), 400
        
    tasks.append(task)

    return jsonify(task), 200

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    request_task = request.get_json()
    for task in tasks:
        if task['id'] == id:
            task['description'] = request_task.get('description', task['description'])
            return jsonify(task), 200
        
    return jsonify(f'message: Tarefa {id} não encontrada'), 404

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    for task in tasks:
        if task['id'] == id:
            tasks.remove(task)
            return jsonify(f'Tarefa {id} foi removida'), 200
    return jsonify(f'message: Tarefa {id} não encontrada'), 404

app.run(port=5000)