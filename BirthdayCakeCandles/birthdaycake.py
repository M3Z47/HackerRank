# import sys
import operator
def birthdayCakeCandles(n, ar):
    # Complete this function
    index, max_height = max(enumerate(ar), key=operator.itemgetter(1))
    count = 0
    for i in range(0,n):
        if ar[i] == max_height:
            count = count + 1
    return count

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
