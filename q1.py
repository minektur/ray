#!/usr/bin/env python
""" Sample code for Raytheon Interview"""
import sys


def main(argv):
    """ find and print 4th occurance of supplied string in file """
    if len(argv) != 3:
        usage(argv)
    try:
        with  open(argv[1], "r") as infile:
            lines = infile.readlines()
            infile.close()
            lines = [line for line in lines if argv[2] in line]
            if len(lines) < 4:
                print("4th occurance not found")
            else:
                print(lines[3].strip())
    except IOError as ioe:
        print("Error opening file %s: %s\n" % (argv[1], ioe.strerror))
        usage(argv)

def usage(argv):
    """ print program usage and exit"""
    print("%s: <filename> <string>" % (argv[0]))
    print ("Print 4th occurance of string in filename")
    sys.exit(1)

if __name__ == "__main__":
    main(sys.argv)
