#!/usr/bin/python3

import sys

def convert(name):
    try:
        f = open(name, "rU")
        line = f.read()
        line = str(line)
        # print(line)
    except:
        print("bad stuff happened")
        return
    line.replace(", \"event\":", "}\n{\"event\":")
    print(line)

def main():
    convert(sys.argv[1])

main()