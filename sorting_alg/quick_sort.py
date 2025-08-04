# i. choose pivot
#

data = [2, 4, 5, 1, 8, 9, 0]

def quick(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst.pop()
    small_element = []
    large_element = []

    for i in lst:
        if i < pivot:
            small_element.append(i)
        else:
            large_element.append(i)

    return quick(small_element) + [pivot] + quick(large_element)

data = [5, 2, 9, 1, 7]
print(quick(data))
