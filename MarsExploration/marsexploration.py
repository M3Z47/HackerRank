import sys

def marsExploration(s):
    # Complete this function
    count = 0
    for message in range(0, len(s)-2, 3):
        if s[message] != 'S':
            count += 1
        if s[message+1] != 'O':
            count += 1
        if s[message+2] != 'S':
            count += 1
    return count

if __name__ == "__main__":
    s = input().strip()
    result = marsExploration(s)
    print(result)