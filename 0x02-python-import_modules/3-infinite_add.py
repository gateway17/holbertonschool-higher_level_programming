#!/usr/bin/python3
import sys
a = 0
for i in range(len(sys.argv) - 1):
    a = int(a) + int(sys.argv[i + 1])
print(a)
