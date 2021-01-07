import requests
import json
import pandas as pd

base_url = "http://127.0.0.1:5000/"

response = requests.get(base_url + "racing")

resp = response.json()
print(type(resp))
print(resp)
df = pd.DataFrame(resp.items())
print(type(df))
print(df)


# def get_all_values(nested_dictionary):
#     for key, value in nested_dictionary.items():
#         if (type(value) is dict):
#             get_all_values(value)
#         else:
#             print(key, ":", value)
