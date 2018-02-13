#!/bin/python3

import sys

def funnyString(s):
    

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = funnyString(s)
    print(result)
