#!/usr/bin/env python

import sys

sum = list()


def verify_helper(file, match):
    index = 0
    for x in range(0, len(file)):
        if file[x] == match:
            index += 1
        else:
            break
    # print("helper found: " + str(index))
    return index


def verify_input_iterative(file):
    x = 0
    end = len(file) - 1
    while x <= end:
        current = file[x]
        if x == len(file) - 1:
            return
        next = file[x + 1]
        if current == next:
            check_for_more = verify_helper(file[x+1:], next)
            if check_for_more > 1:
                sum.append(int(file[x])*check_for_more)
                x += check_for_more
            else:
                sum.append(file[x])
                x += 2
        else:
            x += 1


def verify_input_recursion(file, start):
    # print("file: " + str(file))
    # print("index: %d" % start)
    if len(file) == 1 or len(file) == 0:
        return
    current = file[start]
    if start == len(file):
        next = file[-1]
    else:
        next = file[start + 1]
    if current == next:
        diff = verify_helper(file[start:], next)
        if diff > 2:
            sum.append(int(file[start]) * diff)
            verify_input_recursion(file[start + diff:], 0)
        else:
            sum.append(file[start])
            verify_input_recursion(file[start + 2:], 0)
    else:
        if start == len(file):
            return
        verify_input_recursion(file[start + 1:], 0)


def check_ends(a):
    if a[0] == a[-1]:
        sum.append(a[0])


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        input = [line.strip() for line in f]
    # print("input: " + str(input))
    a = list()
    for x in str(input):
        if x == '\'' or x == '[' or x == ']':
            continue
        a.append(x)
    #print("new input: " + str(a))
    verify_input_iterative(a)
    check_ends(a)
    print("sum: " + str(sum))
    total = 0
    for x in sum:
        total += int(x)
    print("total = " + str(total))
