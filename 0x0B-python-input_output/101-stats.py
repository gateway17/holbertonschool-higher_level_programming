#!/usr/bin/python3

"""
Write a script that reads stdin line by line and computes metrics:

    Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
    Each 10 lines and after a keyboard interruption (CTRL + C), prints those statistics since the beginning:
        Total file size: File size: <total size>
        where is the sum of all previous (see input format above)
        Number of lines by status code:
            possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
            if a status code doesn’t appear, don’t print anything for this status code
            format: <status code>: <number>
            status codes should be printed in ascending order

"""

