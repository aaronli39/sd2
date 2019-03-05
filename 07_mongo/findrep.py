#!/usr/bin/python3

import sys


def convert(name):
    try:
        f = open(name, "rU")
        line = f.read()
        line = str(line)
        # print(line)
        f.close()
    except:
        print("bad stuff happened")
        return
    ret = line.replace("{\"event\":", "\n{\"event\":")
    # print(line.replace("{\"event\":", "\n{\"event\":"))
    try:
        f = open(name, "w")
        f.write(ret)
        f.close()
    except:
        print("error writing")

def main():
    convert(sys.argv[1])

main()
