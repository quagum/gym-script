#from register import *
from flask import Flask, jsonify
from flask_restful import Resource, Api


#inputs || time in text format. may need to change later. 
registration_time = '03:00 PM'
event = 'WEC'

class status(Resource):    
     def get(self):
         try:
            return {'data': 'Api running'}
         except(error): 
            return {'data': error}


#adds ublock for ad blocking
op = Options()
op.add_extension(r'C:\CSProjects\gym-registration\ublock.crx')


