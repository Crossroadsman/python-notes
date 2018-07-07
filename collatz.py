def isEven(num):
    return num % 2 == 0

def isOdd(num):
    return not isEven(num)

def get_number():
    is_valid = False
    while not is_valid:
        user_input = input('Enter an integer > ')
        try:
            user_int = int(user_input)
        except ValueError:
            print("Invalid value, please try an actual integer")
        else:
            is_valid = True
    return user_int

def collatz(num):
    if isEven(num):
        return num // 2
    else:
        return (3 * num) + 1

collatz_number = get_number()
while collatz_number != 1:
    collatz_number = collatz(collatz_number)
    print(collatz_number)
