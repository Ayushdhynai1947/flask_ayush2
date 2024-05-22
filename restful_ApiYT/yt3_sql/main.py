from flask import Flask
from flask_restful import Resource,Api,reqparse,abort
from flask_sqlalchemy import SQLAlchemy






app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

todos ={
    1: {"task":"write hellow world","summary":"write summery of the task"},
    2: {"task":"this is task 2","summary":"write summery of the task2"},
    3: {"task":"task 3","summary":"write summery of task 3"}
    
}

task_post_args = reqparse.RequestParser()
task_post_args.add_argument("task", type=str, help="task is reqired ",required=True)
task_post_args.add_argument("summary", type=str, help="summary is required .",required=True)

task_put_args = reqparse.RequestParser()
task_put_args.add_argument("task",type=str)
task_put_args.add_argument("summary",type=str)


    
class ToDolist(Resource):
    def get(self):
        return todos
    
class ToDo(Resource):
    
    def get(self,todo_id):
        return todos[todo_id]  
    
     
    def post(self,todo_id):
        args = task_post_args.parse_args()
        if todo_id in todos:
            abort(404,'task Id is already ')
        todos[todo_id ] ={"task":args["task"],"summary":args["summary"]}
        return todos[todo_id]
    
    def delete(self,todo_id):
        del todos[todo_id]
        return todos
    
    
    def put(self,todo_id):
        args=task_put_args.parse_args()
        if todo_id  not in todos:
            abort(404,message="task doesnt exist,cannot update.")
        if args["task"]:
            todos[todo_id]["task"]= args["task"]
        if args["summary"]:
            todos[todo_id]["summary"] =args["summary"]
        return todos[todo_id] ,200
            
        
api.add_resource(ToDo,'/todos/<int:todo_id>')
api.add_resource(ToDolist,'/todos')

if __name__=='__main__':
    app.run(debug=True)