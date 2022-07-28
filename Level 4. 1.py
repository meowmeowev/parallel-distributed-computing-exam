import random

array = []
arrayE = []
arrayO = []
div = []
prime = []
nines = []

for number in range(100):
    number = random.randrange(100,999)
    array.append(number)

    if number % 9 == 0:
        div.append(number)
    elif '9' in str(number):
        nines.append(number)
    elif number % 2 == 0:
       arrayE.append(number)
    else:
        arrayO.append(number)

    divisor_count = 0
    for j in range(1, number+1):
        if number % j == 0:
            divisor_count +=1
    if divisor_count == 2:
        prime.append(number)


print('List of 3 digit numbers: ', array)
print('Even Numbers: ', arrayE)
print('Odd Numbers: ', arrayO)
print('Divisible by 9: ', div)
print('Prime Numbers: ', prime)
print('Numbers with 9: ', nines)

