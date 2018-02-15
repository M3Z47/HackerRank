#!/bin/python3

import sys

def funnyString(s, q):
    ans = [''] * q
    for item in range(0, len(s)):
        count = 0
        for i in range(0, len(s[item])-1):
            if abs(ord(s[item][i+1])-ord(s[item][i])) == abs(ord(s[item][len(s)-i-1])-ord(s[item][len(s)-i-2])):
                count += 1
        if count == len(s[item])-1:
            ans[item] = 'Funny'
        else:
            ans[item] = 'Not Funny'
    return ans

q = int(input().strip())
s = ['NO'] * q
for a0 in range(q):
    aa = input().strip()
    s[a0] = aa
result = funnyString(s, q)
for i in range(0, len(s)):
    print(result[i])