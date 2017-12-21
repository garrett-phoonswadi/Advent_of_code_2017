#!/usr/bin/env python

import sys


def verify_input_iterative(sequence, total=0):
    x = 0
    end = len(sequence) - 1
    while x <= end / 2:
        next_pos = ((len(sequence) / 2) + x) % len(sequence)
        if sequence[x % len(sequence)] == sequence[next_pos]:
            total += (int(sequence[x]) * 2)
        x += 1
    check_ends(sequence, total)
    return total


def check_ends(a, total):
    if a[-1] == a[(len(a) / 2) - 1]:
        total += (int(a[-1]) * 2)


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        sequence = [line.strip() for line in f]
    # print("input: " + str(input))
    inputs = list()
    [inputs.append(x) if x != '\'' and x != '[' and x != ']' else "" for x in str(sequence)]
    # print("new input: " + str(inputs))
    total = verify_input_iterative(inputs)
    print("total = " + str(total))
