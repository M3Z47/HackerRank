#!/bin/python3

import sys

def sockMerchant(n, ar):
    count = 0
    index = 0
    while index < len(ar)-1:
        i = index + 1
        while i < len(ar):
            if ar[index] == ar[i]:
                ar.remove(ar[index])
                ar.remove(ar[i-1])
                count += 1
                index = -1
                break
            i += 1
        index += 1
    return count

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
