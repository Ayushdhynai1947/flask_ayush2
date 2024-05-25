from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

# Import configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///view/data.db'

# Initialize the database
db = SQLAlchemy(app)

# Ensure the parent directory exists for the database file


# Import models within the app context to avoid circular import
with app.app_context():
    db.create_all()

# Import and register resources
from resources import Todos
# Add resources
api.add_resource(Todos, '/todos')

from resource import TodoList
api.add_resource(TodoList, '/todos/<int:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
