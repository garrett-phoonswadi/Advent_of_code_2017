#!/usr/bin/env python

import sys

sum = list()

def verify_input_iterative(file):
    x = 0
    end = len(file)-1
    while x <= end/2:
        if x == (len(file)-1)/2:
            return
        current = file[x]
        next_pos = ((len(file)/2) + x) % len(file)
        next = file[next_pos]
        if current == next:
                sum.append(int(file[x])*2)
                x += 1
        else:
            x += 1


def check_ends(a):
    if a[-1] == a[(len(a)/2)-1]:
        end = a[-1]
        mid = a[(len(a)/2)-1]
        sum.append(int(a[-1])*2)


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        input = [line.strip() for line in f]
    # print("input: " + str(input))
    a = list()
    for x in str(input):
        if x != '\'' and x != '[' and x != ']':
            a.append(x)
    #print("new input: " + str(a))
    verify_input_iterative(a)
    check_ends(a)
    #print("sum: " + str(sum))
    total = 0
    for x in sum:
        total += int(x)
    print("total = " + str(total))

