#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arguments = len(argv) - 1
    if arguments == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(arguments))
        for i in range(arguments):
            print("{}: {}".format(i + 1, argv[i + 1]))
