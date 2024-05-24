from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource , abort , reqparse , marshal_with



app = Flask(__name__)
api= ap
db =SQLAlchemy(app)



@app.route('/',method=['get'])






if __name__=="__main__":
    app.run(debug=True)