from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug='True')

class Task:
    def __init__(self, id, title, description, due_date, assignee):

        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.assignee = assignee
        self.created_at = datetime.now()

tasks = []

# Defining routes for CRUD tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify([task.__dict__ for task in tasks])

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task.id == task_id), None)
    if task:
        return jsonify(task.__dict__)
    else:
        return jsonify({"error": "Task not found"}), 404

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    task = Task(id=len(tasks) + 1, title=data['title'], description=data['description'], due_date=data['due_date'], assignee=data['assignee'])
    tasks.append(task)
    return jsonify(task.__dict__), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    task = next((task for task in tasks if task.id == task_id), None)
    if task:
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.due_date = data.get('due_date', task.due_date)
        task.assignee = data.get('assignee', task.assignee)
        return jsonify(task.__dict__)
    else:
        return jsonify({"error": "Task not found"}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    return '', 204