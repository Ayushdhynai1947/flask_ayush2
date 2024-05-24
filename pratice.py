from flask import Flask,jsonify
from flask_restful import Resource,abort,reqparse,Api,fields,marshal_with
from flask_sqlalchemy import SQLAlchemy




app= Flask(__name__)
api=Api(app)

app.config['SQLALCHEMY_DATABASE_URI']= ''
db =SQLAlchemy(app)


class User(db.Model):
    id =db.Column(db.Integer,Primary_key=True)
    task =db.Column(db.String(80))
    summary =db.Column(db.String(120))
    
    
db.create_all()




todos ={
    1: {"task":"write hellow world","summary":"write summery of the task"},
    2: {"task":"this is task 2","summary":"write summery of the task2"},
    3: {"task":"task 3","summary":"write summery of task 3"}
}


task_post_args =reqparse.RequestParser()
task_post_args.add_argument("task",type=str,help="task is required ",required=True)
task_post_args.add_argument("summary",type=str,help="summary is required")


task_put_args =reqparse.RequestParser()
task_put_args.add_argument("task",type=str)
task_put_args.add_argument("summary",type=str)

resource_fields ={
    'id':fields.Integer,
    'task':fields.String,
    'summary':fields.String
}

class TodoList(Resource):
    @marshal_with(resource_fields)
    def get(self):
        task =User.query.all()
        return task ,200
    
class Todo(Resource):
    @marshal_with(resource_fields)
    def get(self,todo_id):
        task=User.query.filter_by(id=todo_id).first()
        if not task:
            abort(404,message="task not found")
        return task,200
    
    @marshal_with(resource_fields)
    def post(self,todo_id):
        args=task_post_args.parse_args()
        task=User.query.filter_by(id =todo_id).first()
        if task:
            abort(404,'task id already exist')
        new_task =User()
        todos[todo_id]={"task":args['task'],"summary":args["summary"]}
        return todos[todo_id]
    
    
    def delete(self,todo_id):
        if todo_id not in todos:
            abort(404,"not found")
        del todos[todo_id]
        return todos
    
    def put(Self,todo_id):
        args =task_put_args.parse_args()
        if todo_id not in todos:
            abort(404,"entery nto found")
        if args["task"]:
            todos[todo_id]["task"]=args["task"]
        if args["summary"]:
            todos[todo_id]["summary"]=args["summary"]
        return todos[todo_id],200
        
    



api.add_resource(Todo,'/todos/<int:todo_id>')
api.add_resource(TodoList,'/todos')


if __name__=='__main__':
    app.run(debug= True)