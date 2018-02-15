list1 = input().strip().split(' ')
list2 = input().strip().split(' ')
charge = input().strip()

correctCharge = 0
for item in range(0, len(list2)):
    if item != int(list1[1]):
        correctCharge += int(list2[item])

if int(charge) == correctCharge//2:
    print("Bon Appetit")
else:
    correctCharge = int(charge) - correctCharge//2
    print(correctCharge)