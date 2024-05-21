from flask import Flask



def create_app():
    app = Flask(__name__)
    
    from.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auht_blueprint
    app.register_blueprint(auht_blueprint)
    
    return app


