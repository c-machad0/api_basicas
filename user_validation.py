from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {
    'id': 1,
    'nome': 'Christian',
    'email': 'realc.machado@hotmail.com'
    }
]

@app.route('/')
def home():
    return 'API User Validation'

@app.route('/users')
def get_user():
    return jsonify(users), 200

@app.route('/users', methods=['POST'])
def create_user():
    request_user = request.get_json()
    user = {
        'id': request_user['id'],
        'nome': request_user['nome'],
        'email': request_user['email']
    }

    users.append(user)

    return jsonify(user), 201


app.run(port=5000)