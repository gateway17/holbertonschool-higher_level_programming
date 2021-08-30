#!/usr/bin/python3
""" Write a Python script that takes in a URL, sends a request to the URL
    and displays the body of the response (decoded in utf-8).

    You have to manage urllib.error.HTTPError exceptions and print:
        Error code: followed by the HTTP status code
    You must use the packages urllib and sys
    You are not allowed to import other packages than urllib and sys
    You don’t need to check arguments passed to the script (number or type)
    You must use the with statement
"""
from urllib import request, error
from sys import argv

target = argv[1]

try:
    respond = request.Request(target)
    with request.urlopen(respond) as buffer:
        """ Make a GET request and decode in utf-8 """
        file = buffer.read()
        print(file.decode('utf-8'))

except error.HTTPError as e:
    print("Error code: {}".format(e.code))
