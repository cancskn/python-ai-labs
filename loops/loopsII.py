# The user types in two numbers.
# Find the sum of all even, odd numbers and multiples of 9 in the specified range, as well as arithmetic mean of each group.
def analyze_range(s, e):
    nums = range(s, e + 1)
    evens = [num for num in nums if num % 2 == 0]
    odds = [num for num in nums if num % 2 != 0]
    multiple9 = [num for num in nums if num % 9 == 0]
    mean_nums = sum(nums) / len(nums)
    mean_evens = sum(evens) / len(evens)
    mean_odds = sum(odds) / len(odds)
    mean_multiple9 = sum(multiple9) / len(multiple9)
    return nums, evens, odds, multiple9, mean_nums, mean_evens, mean_odds, mean_multiple9
# print(analyze_range(1, 20))


# The user types in the length of a line and a symbol to fill the line.
# Print a vertical line made out of the typed in symbol of the specified length.
def show_shape(len_line, symbol):
    for _ in range(len_line):
        print(symbol + '\n')
# show_shape(5, '-')


# The user types in numbers.
# If the number is greater than 0, print "Your number is positive";
# if it is less than zero, print "Your number is negative";
# if it is equal to 0, print "Your number is equal to zero."
# When the user types in 7, the program stops and prints "Goodbye!"
def game_num():
    while True:
        num = int(input('num: '))
        if num > 0:
            print("Your number is positive")
        elif num < 0:
            print("Your number is negative")
        else:
            print("Your number is equal to zero.")
        if num == 7:
            print('Goodbye')
            break
# game_num()


# The user types in numbers.
# The program must calculate their sum and find the maximum and minimum.
# When the user types in 7, the program stops and prints "Goodbye!".
def calculate():
    total = 0
    max_num = None
    min_num = None

    while True:
        num = int(input('num: '))
        total += num

        if max_num is None or num > max_num:
            max_num = num
        if min_num is None or num < min_num:
            min_num = num

        if num == 7:
            print('Sum: ' + str(total))
            print('Maximum number: ' + str(max_num))
            print('Minimum number' + str(min_num))
            print('Goodbye!')
            break
# calculate()






