from flask_restful import Resource, reqparse, abort, fields, marshal_with
from .models import USER
from . import db

task_post_args = reqparse.RequestParser()
task_post_args.add_argument('task', type=str, help="Task is required", required=True)
task_post_args.add_argument('summary', type=str, help="Summary is required", required=True)

task_put_args = reqparse.RequestParser()
task_put_args.add_argument('task', type=str)
task_put_args.add_argument('summary', type=str)

resource_fields = {
    'id': fields.Integer,
    'task': fields.String,
    'summary': fields.String
}

class Todos(Resource):
    @marshal_with(resource_fields)
    def get(self):
        tasks = USER.query.all()
        return tasks, 200

class TodoList(Resource):
    @marshal_with(resource_fields)
    def get(self, todo_id):
        task = USER.query.filter_by(id=todo_id).first()
        if not task:
            abort(404, message="Task not found, please check the ID")
        return task, 200

    @marshal_with(resource_fields)
    def post(self, todo_id):
        task = USER.query.filter_by(id=todo_id).first()
        args = task_post_args.parse_args()
        if task:
            abort(400, message="Task with this ID already exists")
        new_task = USER(id=todo_id, task=args['task'], summary=args['summary'])
        db.session.add(new_task)
        db.session.commit()
        return new_task, 201

    @marshal_with(resource_fields)
    def delete(self, todo_id):
        task = USER.query.filter_by(id=todo_id).first()
        if not task:
            abort(404, message="Task not found, cannot delete")
        db.session.delete(task)
        db.session.commit()
        return '', 204

    @marshal_with(resource_fields)
    def put(self, todo_id):
        task = USER.query.filter_by(id=todo_id).first()
        args = task_put_args.parse_args()
        if not task:
            abort(404, message="Task not found, cannot update")
        if args['task']:
            task.task = args['task']
        if args['summary']:
            task.summary = args['summary']
        db.session.commit()
        return task, 200
