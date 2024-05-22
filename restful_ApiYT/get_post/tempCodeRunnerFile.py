from flask import Flask
from flask_restful import Resource,Api






app = Flask(__name__)
api = Api(app)

todos ={
    1: {"task":"write hellow world","summary":"write summery of the task"}
}

class ToDo(Resource):
    def get(self,todo_id):
        return todos[todo_id]





api.add_resource(ToDo,'/todos/<int:todo_id>')



if __name__=='__main__':
    app.run(debug=True)