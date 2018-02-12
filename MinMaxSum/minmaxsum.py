import sys

def miniMaxSum(arr):
    # Complete this function
    arr_a = sorted(arr, key=int)
    arr_d = sorted(arr, key=int, reverse = True)
    sum_max = 0
    sum_min = 0
    for i in range(0,len(arr)-1):
        sum_max = sum_max + arr_d[i]
        sum_min = sum_min + arr_a[i]
    return (print(sum_min, sum_max))

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)