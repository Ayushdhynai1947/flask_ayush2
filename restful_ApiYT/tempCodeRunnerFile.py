#import flask first
from flask import Flask
from flask_restful import Resource,Api

#basic syntax of flask 
#initalising the app
app = Flask(__name__)
api =Api(app)



class helloworld(Resource):
    def get(self):
        return  {'data':'heelow , jonny!'}
    

class HelloName(Resource):
    def get(self,name):
        return {'data':'hello, {}'.format(name)}
        



    


#app having two end points

# /toddos
# /todas/2


# GEt  local host:5000/helloworld
#heelo world
api.add_resource(helloworld,'/helloworld')


# get local host:5000/helloworld/ayush
# HEllo ,ayush 
api.add_resource(HelloName,'/helloworld/<string:name')






# @app.route('/homeworld',helloworld) tp be continued






# @app.route('/')
# def hello():
#     return "hi my name is ayush"


if __name__=='__main__':
    app.run(debug=True)