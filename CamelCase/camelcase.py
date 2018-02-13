import sys

def camelcase(s):
    # Complete this function
    count = 1
    for char in s:
        if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            count += 1
    return count

if __name__ == "__main__":
    s = input().strip()
    result = camelcase(s)
    print(result)
