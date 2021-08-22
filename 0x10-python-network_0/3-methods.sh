#!/usr/bin/env bash
# Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

#    You have to use curl


curl -sI "$1" | grep -i Allow | cut --complement -d " " -f1