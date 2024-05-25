from flask_restful import Resource, reqparse, abort, fields, marshal_with
from .models import USER
from .import db










resource_fields={
    'emp_no':fields.Integer,
    'product_name':fields.String,
    'first_name':fields.String,
    'last_name':fields.String,
    
}



class Todos(Resource):
    @marshal_with(resource_fields)
    def get(self):
        tasks = USER.query.all()
        return tasks, 200
    
    
class Todoslist(Resource):
    @marshal_with(resource_fields)
    def get(self,emp_no):
        task=USER.query.filter_by(emp_no=emp_no).first()
        if not task:
            abort(403,'not found')
        return task
    