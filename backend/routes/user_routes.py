from flask import jsonify
from app import app, db
from app.models.user import User

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.username for user in users])
