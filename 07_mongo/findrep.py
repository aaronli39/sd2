
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

    idx = line.find("\"event\"")
    line = line[idx: len(line)-1]
    #ret = line.replace("{\"result\": {\"count\": \"37859\"}", "{\"result\": {\"count\": \"37859\"}}")
    ret = line.replace(", \"event\":", "}\n{\"event\":")
    ret = ret[:-1]
    res = "{"
    res += ret
    res += "}"
    #print(ret)
    # print(line.replace("{\"event\":", "\n{\"event\":"))
    try:
        f = open(name, "w")
        f.write(res)
        f.close()
    except:
        print("error writing")

def main():
    convert(sys.argv[1])

main()