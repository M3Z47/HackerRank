#!/bin/python3

import sys

def utopianTree(n):
    for item in range(0, len(n)):
        i = 1
        height = 1
        while i in range(1, n[item]+1):
            if i%2 == 0:
                switchSpring = 0
                switchSummer = 1
            if i%2 != 0:
                switchSpring = 1
                switchSummer = 0
            if switchSpring == 1:
                height *= 2
            if switchSummer == 1:
                height += 1
            i += 1
        print(height)

if __name__ == "__main__":
    t = int(input().strip())
    n = [1] * t
    for a0 in range(t):
        n1 = int(input().strip())
        n[a0] = n1
    utopianTree(n)
