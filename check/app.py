from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
api = Api(app)

# Import configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///view/data.db'

# Initialize the database
db = SQLAlchemy(app)

# Ensure the parent directory exists for the database file
database_dir = os.path.dirname(app.config['SQLALCHEMY_DATABASE_URI'])
if not os.path.exists(database_dir):
    os.makedirs(database_dir)

# Import models within the app context to avoid circular import
with app.app_context():
    from models import User
    db.create_all()

# Import and register resources
from resources import Todos, TodoList
# Add resources
api.add_resource(Todos, '/todos')
api.add_resource(TodoList, '/todos/<int:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
