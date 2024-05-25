from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource , abort , reqparse , marshal_with,Api,fields


#screen setup
app = Flask(__name__)
api= Api(app)


#database setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ayush@localhost/employees'
db =SQLAlchemy(app)


class employees(db.Model):
    __tablename__ ='employees'
    emp_no =db.Column(db.Integer,primary_key=True)
    birth_date =db.Column(db.Date,nullable=False)
    first_name =db.Column(db.String(60),nullable=False)
    last_name =db.Column(db.String(50),nullable=False)
    gender =db.Column(db.String(50),nullable=False)
    hire_date =db.Column(db.Date,nullable=False)



#create database tables
with app.app_context():
    db.create_all()

Resource_filds ={
    'emp_no':fields.Integer,
    'birth_date':fields.DateTime(dt_format='iso8601'),
    'first_name':fields.String,
    'last_name':fields.String,
    'gender':fields.String,
    'hire_date':fields.DateTime(dt_format='iso8601')
    
}

class todos(Resource):
    @marshal_with(Resource_filds)
    def get(self):
        task=employees.query.all()
        if not task:
            abort(201,message ="task not found")
        return task


class todlist(Resource):
    pass







api.add_resource(todos,'/employee')
api.add_resource(todlist,'/employee/<int:emp_no>')







if __name__=="__main__":
    app.run(debug=True)