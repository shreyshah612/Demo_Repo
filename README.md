# This is a Demo for CodeChallenge(3)

Thank you for your time. I appreciate your valuable time for considering my work. 
Since we are flexible to build our API in language of our choice I am using pythons Flask library to build an API. 

Server side - main.py
This documentation is a brief about how to build an API to fetch data from given endpoints. As there is flexibility, we will be hosting a dummy flask server in dev mode (on localhost = 127.0.0.1:5000) to serve the api calls called from client application. 

Here we are creating an api to cater data-request from small application. For sake of this prototype project we shall be saving our data locally in a csv file but practically it would be in the form of application resources stored on a flexible database (eg - mongoDB, AWS Dynamo, Firebase etc). To use our data as an endpoint we fetch and initialize it in the form of application resource via Race class (which extends Resource class) 

Here we create a race api (basically we override the get() - challenege requirements) which fetches the data from csv, data formatting and sorting is done according to challeneg requirements. we convert it to dictionary because Restful api service call are communicated in 2 formats viz XML and JSON. this means Whenever the api call is made the get method will get executed.

Client side i.e. test.py
Here we request the data using get method. The data is collected in the form of response and parsed using json format (api communicates in JSON) then the JSON is recursively accessed to fetch required information from data set.