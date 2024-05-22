from flask import Flask
from flask_restful import Resource,Api,reqparse,abort,fields,marshal_with
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(80))
    summary = db.Column(db.String(120))

with app.app_context():
    db.create_all()

task_post_args = reqparse.RequestParser()
task_post_args.add_argument("task", type=str, help="task is reqired ",required=True)
task_post_args.add_argument("summary", type=str, help="summary is required .",required=True)

task_put_args = reqparse.RequestParser()
task_put_args.add_argument("task",type=str)
task_put_args.add_argument("summary",type=str)

resource_fields={
    'id':fields.Integer,
    'task':fields.String,
    'summary':fields.String
}


    
class ToDolist(Resource):
    
    
    @marshal_with(resource_fields)
    def get(self):
        tasks=User.query.all()
        return tasks ,200
    
class ToDo(Resource):
    @marshal_with(resource_fields)
    def get(self,todo_id):
        task =User.query.filter_by(id=todo_id).first()
        if not task:
            abort(404, message="Task not found")
        return task,200
    
    @marshal_with(resource_fields)
    def post(self,todo_id):
        args = task_post_args.parse_args()
        task =User.query.filter_by(id = todo_id).first()
        if task:
            abort(404,'task Id is already ')
        new_task = User(id=todo_id,task=args['task'],summary=args['summary'])
        db.session.add(new_task)
        db.session.commit()
        return new_task
    
    def delete(self,todo_id):
        task=User.query.filter_by(id=todo_id).first()
        if not task:
            abort(404,message="task is not found")
        db.session.delete(task)
        db.session.commit()
        return ' ',204
    
    @marshal_with(resource_fields)
    def put(self,todo_id):
        args=task_put_args.parse_args()
        task = User.query.filter_by(id=todo_id).first()
        if not task:
            abort(404,message="task doesnt exist,cannot update.")
        if args["task"]:
            task.task=args['task']
        if args["summary"]:
            task.summary=args['summary']
        db.session.commit()
        return task,200
            
        
api.add_resource(ToDo,'/todos/<int:todo_id>')
api.add_resource(ToDolist,'/todos')

if __name__=='__main__':
    app.run(debug=True)