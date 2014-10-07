ray
===

q1 - 4th occurance of a string in a file

q1.sh - fast and dirty bash one-liner - assumes string exists at least 4 times in file
./q1.sh inputfile string

----

q1-simple.py - fast and dirty python that reads line by line, doesn't read the rest of the file after finding 4th string
             - assumes file exists and is readable, prints nothing if 4th occurance not found

./q1-simple.py input APPLE

----

That was 3 minutes in - I wrote a more polished pep8-compliant q1 in python that does some error checking, but 
assumes the whole file fits in memory easily

./q1.py input string

It will print nice errors if it can't open the input file, there is (limited) command line argument checking, and if not 
found it will let you know it couldn't find it.

-----

q2.c - count bits in an unsigned byte - use 'Make' to build - compiles with gcc on my macbook, linux or freebsd (with gcc) 
       I added a little main function to demonstrate it.


