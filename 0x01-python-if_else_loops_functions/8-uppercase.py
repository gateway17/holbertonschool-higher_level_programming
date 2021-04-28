#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if i >= "a" and i <= "z":
            new = ord(i) - 32
        else:
            new = ord(i)
        print("{:c}".format(new), end='')
    print("")
