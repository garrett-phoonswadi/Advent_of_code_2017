#!/usr/bin/env python
import sys

def check_sum(matrix):
    total = 0
    for y in range(0, len(matrix)):
        d_index = 0
        found = False
        while not found:
            denominator = int(matrix[y][d_index])
            for x in range(0, len(matrix[y])):
                if (x == d_index):
                    continue
                numerator = int(matrix[y][x])
                if int(numerator) % int(denominator) == 0:
                    print("Found %d -------------------- denominator %d Numerator %d" % (y, denominator, numerator))
                    total += int(numerator)/int(denominator)
                    found = True
                    break
            if d_index == len(matrix[y]):
                break
            else:
                d_index += 1
    return total

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        sequence = [line.strip() for line in f]
    matrix = list()
    for x in sequence:
        temp = list()
        for thing in x.strip(" ").split():
            if thing != ' ' and thing != '\t':
                temp.append(thing)
        matrix.append(temp)
    total = check_sum(matrix)
    print("total: %d" % total)
