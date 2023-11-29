#!/usr/bin/python3
for number in range(10):
    for s in range(number, 10):
        if number < s:
            print("{:d}{:d}".format(number, s), 
                    end="\n" if number == 8 and s == 9 else ", ")
