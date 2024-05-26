from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


# Initialize the database
db = SQLAlchemy()




def check_you():
    app = Flask(__name__)
    # Import configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///view/data.db'
    db.init_app(app)
    
    
    
    api = Api(app)
    # Import models within the app context to avoid circular import
    from .resources import TodoList,Todos
    api.add_resource(Todos,'/todos')
    api.add_resource(TodoList,'/todos/<int:todo_id>')
    
    with app.app_context():
        db.create_all()
        
        
    
    return app