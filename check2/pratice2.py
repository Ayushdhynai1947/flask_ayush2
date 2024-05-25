from flask             import Flask
from flask_restful     import Resource  , reqparse , abort , fields , marshal_with , Api
from flask_sqlalchemy  import SQLAlchemy




app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///view/data.db'
db = SQLAlchemy(app)


class USER(db.Model):
    id   = db.Column(db.Integer,primary_key =True)
    task = db.Column(db.String(60))
    summary  = db.Column(db.String(600))
    
    
with app.app_context():
    db.create_all()
    

task_post_args = reqparse.RequestParser()
task_post_args.add_argument('task'   , type=str , help="task is required ")
task_post_args.add_argument('summary', type=str , help="summary is required ")
    
task_put_args=reqparse.RequestParser()
task_put_args.add_argument('task'   , type=str)
task_put_args.add_argument('summary', type=str)

    
resourse_fields={
    'id'      :  fields.Integer,
    'task'    :  fields.Integer,
    'summary' :  fields.String
    
}
    



class Todos(Resource):
    @marshal_with(resourse_fields)
    def get(self):
        task =USER.query.all()
        return task,200
    

class TodoList(Resource):
    @marshal_with( resourse_fields )
    def get( self , todo_id ):
        task =USER.query.filter_by( id=todo_id ).first()
        if  not task:
            abort(404,'not found pls check ')
        return task,200
    
    @marshal_with(resourse_fields)
    def post(self,todo_id):
        task=USER.query.filter_by(id =todo_id).first()
        args=task_post_args.parse_args()
        if task:
            abort(400,'already exists ')
        new_task=USER(id=todo_id,task=args['task'],summary=args['summary'])
        db.session.add(new_task)
        db.session.commit()
        return new_task,201
    
    @marshal_with(resourse_fields)
    def delete(self,todo_id):
        task=USER.query.filter_by(id=todo_id).first()
        if not task:
            abort(404,message="task is not found")
        db.session.delete(task)
        db.session.commit()
        return  ' ',202
        
    @marshal_with(resourse_fields)
    def put(self,todos_id):
        task=USER.query.filter_by(id = todos_id).first()
        args=task_put_args.parse_args()
        if not task:
            abort(404,'task not found ')
        if args['task']:
            task.task=args['task']
        if args['summary']:
            task.summary=args['summary']
        db.session.commit()
        return task
    
            
        
        
        
            



api.add_resource(Todos,'/todos')
api.add_resource(TodoList,'/todos/<int:Todo_id>')


if __name__=='__main__':
    app.run(debug=True)
