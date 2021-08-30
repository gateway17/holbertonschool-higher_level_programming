#!/usr/bin/env python3

import urllib.request as request

url = 'https://intranet.hbtn.io/status'

data_object = request.Request(url)
with request.urlopen(data_object) as response:
    the_page = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(the_page)))
    print("\t- content: {}".format(the_page))
    print("\t- utf8 content: {}".format(the_page.decode("utf-8")))
