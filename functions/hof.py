# higher-order function is a function that can accept one or more functions as arguments or return a function as its result

#  III. To solve this task, be sure to use the mechanism of higher order functions.
# Create a function that displays a line (horizontal or vertical) using a symbol specified by a user.
# A user determines the symbol and which line to display.

def function_to_call(symbol, line):
    if line:
        for _ in range(0, 10):
            print(symbol, end='')
        print()
    else:
        for _ in range(0, 10):
            print(symbol)

def show_line(symbol, function_to_call):
    line = int(input('Horizantal (1) or Vertical (0)?: '))
    return function_to_call(symbol, line)

# print(show_line('*', function_to_call))