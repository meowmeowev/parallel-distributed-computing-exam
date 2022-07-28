firstNum = int(input('Enter a number: '))
lastNum = int(input('Enter a number: '))

three = []
four = []
five = []

for i in range(firstNum, lastNum):
    if i % 3 == 0:
        three.append(i)
    elif i % 4 == 0:
        four.append(i)
    elif i % 5 == 0:
        five.append(i)

print('numbers that are divisible by 3: ', three)
print('numbers that are divisible by 4: ', four)
print('numbers that are divisible by 5: ', five)