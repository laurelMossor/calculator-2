"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
# loop through the list, index 0 = operand, 1 = num1, and 2 = num2

def calculate():
    while True:
        input_string = input("What do you want to calculate?: \n> ")

        if input_string == "q":
            print('later!')
            break
        
        tokens = input_string.split(' ')
        operand = tokens[0]
        num1 = float(tokens[1])

        if len(tokens) == 3:
            num2 = float(tokens[2])
            print(num2)

        if operand == "+":
            print(add(num1, num2))
        
        if operand == "-":
            print(subtract(num1, num2))

        if operand == "*":
            print(multiply(num1, num2))

        if operand == "/":
            print(divide(num1, num2))

        if operand == "square":
            print(square(num1))

        if operand == "pow":
            print(power(num1,num2))

        if operand == "mod":
            print(mod(num1, num2))
    
    
calculate()