from flask import Flask 
from flask_restful import Resource, Api, reqparse
#import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('userId', required=True)  # add args
        args = parser.parse_args()
        
        dict = {'a1b': 'Joe', 'a2c': 'Jenny', 'b1b': 'Jack'}
        
        if args['userId'] in dict.keys():
            return {'data': dict[args['userId']]}, 200  # return data and 200 OK
        else:
            return {'message': f"'{args['userId']}' does not exists."}, 409
        
        
        

                    
class Locations(Resource):
    def get(self,locationId):     
        
        dict = {'1': 'Cafe Florance', '2': 'Cafe Tabac', '3': 'Rosslyn Coffee,'}
        
        if locationId in dict.keys():
            return {'data': dict[locationId]}, 200  # return data and 200 OK
        else:
            return {'message': f"'{locationId}' does not exists."}, 409

        
        
        
class Admin(Resource):
    def get(self):
        data={"data":"Welcome to admin panel."}
        return data
    

api.add_resource(Users, '/users')  # add endpoints
api.add_resource(Locations, '/locations/<locationId>')
api.add_resource(Admin, '/admin')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5002')  # run our Flask app
