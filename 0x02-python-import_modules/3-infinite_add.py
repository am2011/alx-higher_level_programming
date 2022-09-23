#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    for indx in range(len(sys.argv)):
        if (indx == 0):
            continue
        else:
            result += int(sys.argv[indx])
    print(result)
