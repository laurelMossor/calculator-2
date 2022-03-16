"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
# loop through the list, index 0 = operand, 1 = num1, and 2 = num2

def calculate():
    input_string = input("What do you want to calculate?: \n> ")

    if 'q' in input_string:
        print('later!')
        return

    tokens = input_string.split(' ')
    print(tokens)
    operand = tokens[0]
    print(operand)
    num1 = tokens[1]
    print(num1)
    num2 = tokens[2]
    print(num2)





calculate()