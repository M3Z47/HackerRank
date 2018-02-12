
import sys

def solve(grades,n):
    rearr = []
    rearr_i = 0
    # Complete this function
    for i in range(0,n):
        if grades[i] < 37:
            # print(i)
            rearr_i = grades[i]
            rearr.append(rearr_i)
        else:
            remainder = grades[i] % 5
            bench = grades[i] + 5 - remainder
            # print(bench)
            if (bench - grades[i]) < 3:
                # print(i)
                rearr_i = bench
                rearr.append(rearr_i)
            else:
                # print(i)
                rearr_i = grades[i]
                rearr.append(rearr_i)
    return rearr

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)
# print(grades[0])
result = solve(grades,n)
print ("\n".join(map(str, result)))


