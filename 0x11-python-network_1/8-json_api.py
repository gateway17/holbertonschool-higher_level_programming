#!/usr/bin/python3  


from sys import argv
import requests

target = 'http://0.0.0.0:5000/search_user'
q = argv[1]

data = requests.post(target, data=q)

if type(data.text) is not dict:
    print("Not a valid JSON")

elif not bool(data):
    print("No result")
else:
    print("[{}] {}".format(data.))
    