from flask import Flask
from flask_restful import Resource,Api,abort,reqparse


app = Flask(__name__)
api = Api(app)


todo = {
    1: {"task":"write hellow world","summary":"write summery of the task"},
    2: {"task":"this is task 2","summary":"write summery of the task2"},
    3: {"task":"task 3","summary":"write summery of task 3"}
}


task_port_args = reqparse.RequestParser()
task_port_args.add_argument("task",type=str,help="task is required",required = True)
task_port_args.add_argument("summary",type=str,help="summary is required",require = True)

# @app.route('/')
# def hello():
#     return "hello world"

# @app.route('/product ')
# def show():
#     return "welcome to the product "

# @app.route('/')
# def no():
#     return ren


#get_request
class heelo(Resource):
    def get(self):
        return todo
    
class NO(Resource):
    def get(self,to_do_id):
        return todo[to_do_id]
    
    
    def port(self,to_do_list):
        args =task_port_args.parse_args()
        if to_do_list in todo:
            abort(404,'already exist in ')
        todo[to_do_list]={"task":args["task"],"summary":args["summary"]}
        return todo[to_do_list]
    
    
# class check(Resource):
#     def get(self,num):
#         return {"task":'is this,{}'.format(num)}


api.add_resource(heelo,'/home/5')
# api.add_resource(NO,'/home')
api.add_resource(NO,'/home/<int:num>')


if __name__ =='__main__':
    app.run(debug=True)