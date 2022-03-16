"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
# loop through the list, index 0 = operand, 1 = num1, and 2 = num2

def calculate(input_string):
    if "q" in input_string:
        break
    
    tokens = input_string.split(' ')
