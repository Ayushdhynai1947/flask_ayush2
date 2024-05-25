from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    db.init_app(app)
    
    api = Api(app)

    from .resources import Todos, TodoList

    api.add_resource(Todos, '/todos')
    api.add_resource(TodoList, '/todos/<int:todo_id>')

    with app.app_context():
        db.create_all()

    return app
