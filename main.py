#from register import *
from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
#registerForEvent("06:00 PM", "Tennis")


class status(Resource):    
     def get(self):
         try:
            return {'data': 'Api running'}
         except(error): 
            return {'data': error}


if __name__ == '__main__':
    app.run(debug=True)


