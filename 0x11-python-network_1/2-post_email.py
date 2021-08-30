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

from sys import argv
from urllib import request, parse

url = argv[1]
email = argv[2]
value = {
    'email': email
}

data = parse.urlencode(value)
data = data.encode('utf-8')
req = request.Request(url, data)
with request.urlopen(req) as response:
    """ Make a POST request, sending a Email """
    resp = response.read()
    print(resp)
