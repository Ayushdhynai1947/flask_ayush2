from flask_restful import Resource, reqparse, abort, fields, marshal_with
from app import db

task_post_args = reqparse.RequestParser()
task_post_args.add_argument('task', type=str, required=True, help="task is required")
task_post_args.add_argument('summary', type=str, required=True, help="summary is required")

task_put_args = reqparse.RequestParser()
task_put_args.add_argument('task', type=str)
task_put_args.add_argument('summary', type=str)

resource_fields = {
    'id': fields.Integer,
    'task': fields.String,
    'summary': fields.String
}
from models import User
class Todos(Resource):
    @marshal_with(resource_fields)
    def get(self):
        tasks = User.query.all()
        return tasks, 200

class TodoList(Resource):
    @marshal_with(resource_fields)
    def get(self, todo_id):
        task = User.query.filter_by(id=todo_id).first()
        if not task:
            abort(404, message="Task not found, please check")
        return task, 200

    @marshal_with(resource_fields)
    def post(self, todo_id):
        args = task_post_args.parse_args()
        task = User.query.filter_by(id=todo_id).first()
        if task:
            abort(400, message="Task ID already exists")
        new_task = User(id=todo_id, task=args['task'], summary=args['summary'])
        db.session.add(new_task)
        db.session.commit()
        return new_task, 201

    @marshal_with(resource_fields)
    def delete(self, todo_id):
        task = User.query.filter_by(id=todo_id).first()
        if not task:
            abort(404, message="Task not found")
        db.session.delete(task)
        db.session.commit()
        return '', 204

    @marshal_with(resource_fields)
    def put(self, todo_id):
        args = task_put_args.parse_args()
        task = User.query.filter_by(id=todo_id).first()
        if not task:
            abort(404, message="Task not found")
        if args['task']:
            task.task = args['task']
        if args['summary']:
            task.summary = args['summary']
        db.session.commit()
        return task, 200
