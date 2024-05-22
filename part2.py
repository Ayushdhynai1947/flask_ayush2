from flask import Flask
from flask_restful import Resource,Api,abort,reqparse




app= Flask(__name__)
api = Api(app)

todos ={
    1: {"task":"write hellow world","summary":"write summery of the task"},
    2: {"task":"this is task 2","summary":"write summery of the task2"},
    3: {"task":"task 3","summary":"write summery of task 3"}
    
}

task_post_args =reqparse.RequestParser()
task_post_args.add_argument("task", type=str,help="task is required ",required=True)
task_post_args.add_argument("summary ", type=str,help="summary is to be given  ",required=True)

task_put_args=reqparse.RequestParser()
task_put_args.add_argument("task",type=str)
task_post_args.add_argument("summary",type=str)


class Todo(Resource):
    def get(self):
        return todos
    
class ToDolist(Resource):
    def get(self,todo_d):
        return todos[todo_d]
    
    def post(self,todo_d):
        args=task_post_args.parse_args()
        if todo_d in todos:
            abort(404,"task ID is not avilable")
        todos[todo_d]= {"task":args["task"],"summary":args["summary"]}
        return todos[todo_d]
    
    
    def delete(self,todo_d):
        if todo_d in todos:
            abort(404,"task is not define ")
        del todos[todo_d]
        return todos
    
    def push(self,todo_d):
        args=task_put_args.parse_args()
        if todo_d not in todos:
            abort(405,"Id is not avilable")
        if args["task"]:
            todos[todo_d]["task"]= args["task"]
        if args["summary"]:
            todos[todo_d]["summary"]=args["summary"]
        return todos[todo_d]
            
            
        
        



api.add_resource(Todo,'/todos')
api.add_resource(ToDolist,'/todos/<int:todo_d>')



if __name__ =="__main__":
    app.run(debug=True)