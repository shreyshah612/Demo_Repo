import requests
import json
import pandas as pd

base_url = "http://127.0.0.1:5000/"

response = requests.get(base_url + "racing")
resp = response.json()

def get_all_values(nested_dictionary):
    for key, value in nested_dictionary.items():
        if (type(value) is dict):
            get_all_values(value)
        else:
            print(key, ":", value)

get_all_values(resp)


# print(type(df))
# race_list = []
# for rowid, r_info in df.items():
#     for key in r_info:
#         print(key + ':', r_info[key])



# print(type(resp))
# print(resp)
