from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

users = [
    {"username": "user1", "password": "password1", "email": "user1@example.com", "role": "user"},
    {"username": "user2", "password": "password2", "email": "user2@example.com", "role": "admin"}
]

#defining route
@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({"error": "Authentication failed"}), 401
    
    user = next((user for user in users if user['username'] == auth.username), None)
    if not user or user['password'] != auth.password:
        return jsonify({"error": "Authentication failed"}), 401
    
    return jsonify({"message": "Login successful", "user": user}), 200

#Authorization Middleware
def requires_role(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            auth = request.authorization
            if not auth or not auth.username:
                return jsonify({"error": "Unauthorized"}), 401
            
            user = next((user for user in users if user['username'] == auth.username), None)
            if not user or user['role'] != role:
                return jsonify({"error": "Unauthorized"}), 401
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

@app.route('/admin/dashboard')
@requires_role('admin')
def admin_dashboard():
    return jsonify({"message": "Welcome to admin dashboard"}), 200