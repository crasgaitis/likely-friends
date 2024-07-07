from flask import request, jsonify, render_template
from app import app # , db
from mock_db import db
from models import User, Quiz
from utils import generate_quiz_code

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_quiz', methods=['POST'])
def create_quiz():
    print('hello')
    data = request.get_json()
    title = data.get('title')
    user_id = data.get('user_id')
    # generate a unique quiz code
    code = generate_quiz_code()
    print(code)
    new_quiz = Quiz(title=title, code=code, user_id=user_id)
    db.session.add(new_quiz)
    db.session.commit()

    return jsonify({'message': 'Quiz created successfully', 'quiz_code': code}), 201

@app.route('/join_quiz', methods=['POST'])
def join_quiz():
    data = request.get_json()
    quiz = Quiz.query.filter_by(code=data['code']).first()
    if quiz:
        return jsonify({'message': 'Joined quiz successfully', 'quiz_id': quiz.id}), 200
    return jsonify({'message': 'Quiz not found'}), 404

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/join')
def join_quiz_page():
    return render_template('join_quiz.html')

@app.route('/create')
def create_quiz_page():
    return render_template('create_quiz.html')
