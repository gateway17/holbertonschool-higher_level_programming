#!/usr/bin/python3

from sys import argv
import requests

email = argv[2]
host = argv[1]
parr = {
    'email': email
}

data = requests.post(host, data=parr)
print(data.text)
