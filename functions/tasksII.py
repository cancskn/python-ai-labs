# I - product
def product_list(lst):
    product = 1
    for n in lst:
        product *= n
    return product

# II - min in a list
def find_min(lst):
    return min(lst)

# III - Count primes
def count_primes(lst):
    def prime_num(n):
        if n < 1:
            return False
        
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
    count = 0
    for num in lst:
        if prime_num(num):
            count += 1
    
    return count

# IV - Removing a num, amount of removes
def remove_count(lst, target):
    count = lst.count(target)
    lst[:] = [n for n in lst if n != target]
    return count

# V - Merging lists
def merge_list(lst1, lst2):
    merged_lst = lst1 + lst2
    return merged_lst

# VI - power of x in list elements
def calculate_powers(lst, power):
    for i in range(len(lst)):
        lst[i] = lst[i] ** power
    return lst




