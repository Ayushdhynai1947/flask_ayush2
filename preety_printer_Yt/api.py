from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app= Flask(__name__)

app.config['SECREAT_KEY']='thisisecret'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:////mnt/c/User/antho/Documnets/api_example/todo.do'


db = SQLAlchemy(app)

class User(db.Model):
    id = db.column(db.Integer,primary_key=True)
    


if __name__=='__main__':
    app.run(debug=True)