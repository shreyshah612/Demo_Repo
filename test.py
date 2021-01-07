import requests
import json
import pandas as pd

base_url = "http://127.0.0.1:5000/"

response = requests.get(base_url + "racing")

resp = response.json()


def get_all_values(nested_dictionary):
    for key, value in nested_dictionary.items():
        if(type(value) is dict):
            print("Race Number = "+key)
            get_all_values(value)
        else:
            print(key, ":", value)

get_all_values(resp)