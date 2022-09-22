#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    if (argc == 0):
        print("{:d} arguments.".format(argc))
    elif (argc == 1):
        print("{:d} argument:".format(argc))
    else:
        print("{:d} arguments:".format(argc))
        for indx in range(len(sys.argv)):
            if (indx == 0):
                continue
            print("{:d}: {:s}".format(indx, sys.argv[indx]))
