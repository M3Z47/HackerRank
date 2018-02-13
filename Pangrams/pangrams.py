# # Enter your code here. Read input from STDIN. Print output to STDOUT
S = input().strip()
s = S.lower()
test = 'abcdefghijklmnopqrstuvwxyz'
for char in s:
    if char in test:
        test = test.replace(char,"",1)
if test == '':
    print('pangram')
else:
    print('not pangram')
