# The user types in two numbers (start and end points of the range).
# Analyze all the numbers in this range as follows: if the number is a multiple of 7, print it.
def show_nums(start, end):
    for num in range(start, end+1):
        if num % 7 == 0:
            print(num)
# show_nums(1, 77)


# The user types in two numbers (start and end points of the range). Analyze all the numbers in this range.
# Print the following:
# All numbers in the range;
# All numbers in the range in descending order;
# All numbers that are multiples of 7;
# How many numbers are multiples of 5.
def analyze_range(start, end):
    nums = [num for num in range(start, end+1)]
    print('all numbers: ' + str(nums))
    print('in descending order: ' + str(sorted(nums, reverse=True)))
    print('multiples of 7: ' + str([num for num in nums if num % 7 == 0]))
    print('multiples of 5: ' + str([num for num in nums if num % 5 == 0]))
# analyze_range(5, 10)

# The user types in two numbers (start and end points of the range).
# If the number is a multiple of 3 (divisible by 3 without remainder), print the word Fizz.
# If it is a multiple of 5, print Buzz. If it is a multiple of 3 and 5, print Fizz Buzz.
# If the number is not a multiple of 3 or 5, print the number itself.
def fizzbuzz(start, end):
    for num in range(start, end + 1):
        if num % 3 == 0 and num % 5 == 0:
            print('fizzbuzz')
        elif num % 3 == 0:
            print('fizz')
        elif num % 5 == 0:
            print('buzz')
        else:
            print(num)
# fizzbuzz(4, 30)
