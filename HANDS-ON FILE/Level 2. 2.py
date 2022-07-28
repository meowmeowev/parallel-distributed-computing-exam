def triangle():
    if ((x ** 2) + (y ** 2) == (z ** 2)):
        print('It is a right triangle!')
    else:
        print('Not a right triangle!')


if __name__ == "__main__":
    x = int(input('Enter the length of 1st side: '))
    y = int(input('Enter the length of 2nd side: '))
    z = int(input('Enter the length of 3rd side: '))

triangle()