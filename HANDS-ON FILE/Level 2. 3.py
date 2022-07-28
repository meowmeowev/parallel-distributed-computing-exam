import string

pick = int(input('Pick a number: '))
alphabet = list(string.ascii_uppercase)

if pick <= 9:
    print('Output: ', pick)

elif pick >= 10 and pick <= 35:
    print(alphabet[pick - 10])

else:
    print('Invalid number!')