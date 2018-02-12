#import sys

def simpleArraySum(n):
    # Complete this function
    sum = 0
    number = 0
    n = n.strip()
    new_n = n;
    for i in n:
        if n[i] == " ":
            number = new_n[0:i]
            print("Value of number is {}".format(number))
            new_n = n[i+1:]
            print("Value of n is {}".format(new_n))
            print("Value of i is {}".format(i))
        sum = sum + int(number)
    return sum

n = input("Enter the numbers")
# n = int(input("Enter a number\n").strip())
# print(n)
# ar = list(map(int, input().strip().split(' ')))
# print(ar)
result = simpleArraySum(n)
print(result)
