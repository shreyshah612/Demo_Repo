import requests
import json
import pandas as pd

base_url = "http://127.0.0.1:5000/"

response = requests.get(base_url + "racing")
resp = response.json()

# print(df)
print(type(resp))
print(resp)
# print(type(df))
df = pd.DataFrame(resp.items())
print(type(df))
print(df)

