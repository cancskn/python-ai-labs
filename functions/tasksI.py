# 1- Write a function that prints formatted text given below

def show_formatted_text():
    quote = """\
"Don't compare yourself...
if you do so, you are insulting yourself."
                             Bill Gates"""
    print(quote)

show_formatted_text()

# 2- Write a function that takes two numbers as a parameter and displays all even numbers in between

def display_even(num1, num2):
    for num in range(num1, num2+1):
        if num % 2 == 0:
            print(num)

display_even(3, 11)

"""
3- Write a function that prints an empty or solid square made out of some symbol. 
The function takes the following as parameters: the length of the side of the square, a symbol, and a boolean variable:
if it is True, the square is solid;
if False, the square is empty.
"""
def show_shape(len_square, symbol, isSolid=False):
    if isSolid:
        for _ in range(len_square):
            print(symbol * len_square)
    else:
        for row in range(len_square):
            if row == 0 or row == len_square - 1:
                print(symbol * len_square)
            else:
                print(symbol + ' ' * (len_square - 2) + symbol)

print(show_shape(5,'.'))


# 4 - Smallest num

def find_smallest(n1, n2, n3, n4, n5):
    return min(n1, n2, n3, n4, n5)

print(find_smallest(1,3,2,6,9))

# 5 - Product of a range

def find_product(n1, n2):
    if n1 > n2:
        n1, n2 = n2, n1
    
    product = 1
    for i in range(n1, n2 + 1):
        product *= i
    
    return product

print(find_product(2, 3))

# 6 - How many digits of a number

def count_digits(num):
    count = len(str(abs(num)))
    print(count)

count_digits(21312)


# 7 - Is Palindrome

def is_palindrome(n):
    return n == n[::-1]