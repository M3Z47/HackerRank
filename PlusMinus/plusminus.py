import sys

def plusMinus(n,arr):
    neg_count = 0
    pos_count = 0
    zero_count = 0
    # Complete this function
    for i in range(0,n):
        if arr[i] < 0:
            neg_count = neg_count + 1
        elif arr[i] > 0:
            pos_count = pos_count + 1
        else:
            zero_count = zero_count + 1
    print(pos_count/n)
    print(neg_count/n)
    print(zero_count/n)

n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))
plusMinus(n,arr)
