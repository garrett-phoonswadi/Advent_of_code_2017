#!/usr/bin/env python
import sys

def check_sum(matrix):
    total = 0
    for y in range(0, len(matrix)):
        min = matrix[y][0]
        max = 0
        for x in range(0, len(matrix[y])):
            value = int(matrix[y][x])
            if int(min) > value:
                min = value
            if value > max:
                max = value
        total += int(max)-int(min)

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
    print("total: " + str(total))
