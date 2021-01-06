# installing dependencies
from flask import Flask
from flask_restful import Resource, Api

import os
import pandas as pd
import csv
import json

#using flask's restful api
app = Flask(__name__)
api = Api(app)

class Race(Resource):
    def get(self):
        data = pd.read_csv('Race.csv')  # read CSV
        data.set_index("RaceId", drop=True, inplace=True) # convert dataframe to dictionary
        dictionary = data.to_dict(orient="index")
        # sorting
        return dictionary
     

api.add_resource(Race, "/racing")


# this is gonna start our flask application 
# on our server in debug mode.

if(__name__ == "__main__"):
    app.run(debug = True)