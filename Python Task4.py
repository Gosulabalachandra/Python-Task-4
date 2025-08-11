# Python-Task-4
#This is my task4 in python  developer internship----07/08/2025
from flask import Flask, request, jsonify
app = Flask(__name__)
users = {}
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({'error': 'User not found'}), 404
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user_id = data.get('id')
    if not user_id:
        return jsonify({'error': 'User id is required'}), 400
    if user_id in users:
        return jsonify({'error': 'User id already exists'}), 409
    users[user_id] = data
    return jsonify({'message': 'User created', 'user': data}), 201
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    data = request.json
    users[user_id].update(data)
    return jsonify({'message': 'User updated', 'user': users[user_id]}), 200
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({'message': 'User deleted'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

