from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api


db =SQLAlchemy()


def create_app():
    app =Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ayush@localhost/product'
    db.init_app(app)
    
    api =Api(app)
    
    

    from .resource import Todos,Todoslist
    api.add_resource(Todos,'/summary')
    api.add_resource(Todoslist,'/summary/<int:emp_no>')
    
    
    
    
    with app.app_context():
        db.create_all()
    
    return app
    
    
    
    
    
    