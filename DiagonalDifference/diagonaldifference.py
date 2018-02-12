import sys

def diagonalDifference(a):
    # Complete this function
    n = len(a)
    sum_d1 = 0
    sum_d2 = 0
    for i in range(0,n):
        sum_d1 = sum_d1 + a[i][i]
        sum_d2 = sum_d2 + a[i][n-1-i]
    return(abs(sum_d1-sum_d2))

if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
        a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
        a.append(a_t)
    result = diagonalDifference(a)
    print(result)