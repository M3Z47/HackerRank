#!/bin/python3

import sys

def hackerrankInString(s):

    # Complete this function
    ans = []

    for element in range(0, len(s)):
        testString = 'hackerrank'
        for char in range(0, len(s[element])):
            if s[element][char] == testString[0]:
                if len(testString) > 1:
                    testString = testString[1:]
                else:
                    testString = ''
                    break
        if testString == '':
            ans.append('YES')
        else:
            ans.append(('NO'))
    return ans


if __name__ == "__main__":
    q = int(input().strip())
    s = ['NO'] * q
    for a0 in range(q):
        aa = input().strip()
        s[a0] = aa
    result = hackerrankInString(s)
    for i in range(0, len(result)):
        print(result[i])

