data = [11, 2, 5, 3, 14, 1, 1, 5]

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    # 🔧 Parçaları sıralıyoruz
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # 🔧 Sonra birleştiriyoruz
    return merge(left_sorted, right_sorted)

def merge(lst1, lst2):
    sorted_lst = []
    i, j = 0, 0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            sorted_lst.append(lst1[i])
            i += 1
        else:
            sorted_lst.append(lst2[j])
            j += 1

    sorted_lst.extend(lst1[i:])
    sorted_lst.extend(lst2[j:])

    return sorted_lst

print(merge_sort(data))