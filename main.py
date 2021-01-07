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
        data = pd.read_csv('Race.csv')                                      # read CSV
        data.columns=data.columns.str.strip()                               #removes white spaces
        sorted_data = data.sort_values(by='RaceStartTime', ascending=True)  # sorting 
        sorted_data.set_index("RaceId", drop=True, inplace=True)            # convert dataframe to dictionary
        data_dict = sorted_data.to_dict(orient="index")
        return data_dict
     

api.add_resource(Race, "/racing")


# this is gonna start our flask application 
# on our server in debug mode.

if(__name__ == "__main__"):
    app.run(debug = True)