#!/bin/bash
# Write a Bash script that takes in a URL as an argument ends a GET request to the URL, and displays the body of the response
curl -sH "X-HolbertonSchool-User-Id: 98" -GET "$1"
