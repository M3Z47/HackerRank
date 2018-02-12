
import sys


# NOT DONE CORRECTLY

def super_reduced_string(s):
    char = 0
    while char < len(s)-1:
        if s != []:
            if s[char] == s[char+1]:
                s = s.replace(s[char], "", 1)
                s = s.replace(s[char], "", 1)
                char = 0
                break
            if s[char] != s[char+1]:
                char += 1

    if s == []:
        return 'Empty String'
    if s != []:
        return s


s = input().strip()
result = super_reduced_string(s)
print(result)
