import string
import secrets
from mock_db import db
from models import Quiz

def generate_quiz_code(length=6):
    """Generate a unique quiz code."""
    characters = string.ascii_uppercase + string.digits
    while True:
        code = ''.join(secrets.choice(characters) for _ in range(length))
        # check if code is unique
        if not Quiz.query.filter_by(code=code).first():
            return code
