import sys

def timeConversion(s):
    # Complete this function
    hour = 0
    if s[0] == '12':
        if 'AM' in s[2]:
            s[2] = s[2].strip('AM')
            result = "00:{}:{}".format(s[1],s[2])
            return result
        if 'PM' in s[2]:
            s[2] = s[2].strip('PM')
            result = "12:{}:{}".format(s[1],s[2])
            return result
    elif 'A' in s[2]:
        s[2] = s[2].strip('AM')
        result = '{}:{}:{}'.format(s[0], s[1], s[2])
        return result
    else:
        hour = 12 + int(s[0])
        s[2] = s[2].strip('PM')
        result = '{}:{}:{}'.format(hour,s[1], s[2])
        return result

s = input().strip().split(':')
result = timeConversion(s)
print(result)
