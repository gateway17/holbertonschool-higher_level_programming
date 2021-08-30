#!/usr/bin/python3
""" Write a Python script that fetches https://intranet.hbtn.io/status

    You must use the package requests
    You are not allow to import packages other than requests
    The body of the response must be display like the following
        example (tabulation before -)
"""
# Imports module to use
import requests
# Page we want to request
target = 'https://intranet.hbtn.io/status'
# Make request, gets http request object
respond = requests.get(target)
# Print response out
print("Body response:")
print("\t- type: {}\n\t- content: {}".format(type(respond.text), respond.text))
