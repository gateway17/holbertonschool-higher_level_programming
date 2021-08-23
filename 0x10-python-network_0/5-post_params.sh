#!/bin/bash
# Score: 0.00% (Checks completed: 0.00%)

# Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response

#    A variable email must be sent with the value hr@holbertonschool.com
#    A variable subject must be sent with the value I will always be here for PLD
#    You have to use curl

curl -s "$1" -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" -X POST
