# Sort the first two-thirds of the list in ascending order if the arithmetic mean of all elements is greater than 0;
# otherwise, sort only the first third.
# The rest of the list is not sorted but arranged in reverse order.
def puzzle_sort(lst):
    length = len(lst)
    art_mean = sum(lst) / length
    if art_mean > 0:
        two_thirds = (length * 2) // 3
        lst[:int(two_thirds)] = sorted(lst[:int(two_thirds)])
        lst[two_thirds:] = lst[two_thirds:][::-1]
    else:
        first_third = length // 3
        lst[:int(first_third)] = sorted(lst[:int(first_third)])
        lst[first_third:] = lst[first_third:][::-1]

    return lst

# sorted_list = puzzle_sort([3, 1, 5, 6, 2, 9])
# print(sorted_list)

# Progress ap
def progress():
    grades = []
    for i in range(10):
        grade = int(input(f"Enter grade -{i + 1} (1-12): "))
        grades.append(grade)
    while True:
        print("\nMenu:")
        print("1. Output grades")
        print("2. Retake exam")
        print("3. Check scholarship eligibility")
        print("4. Output sorted grades")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == '1':
            print(grades)
        elif choice == '2':
            index = int(input("Enter an index (0-11) of the grade to retake the exam\n: "))
            new_grade = int(input("Enter your new grade (1-12): "))
            grades[index] = new_grade
        elif choice == '3':
            avg = sum(grades) / len(grades)
            if avg > 10.7:
                print("\nYou got the scholarship!")
            else:
                print("\nNo scholarship")
        elif choice == '4':
            order = input("Ascending or descending: (a-d)")
            if order == 'a':
                print(sorted(grades))
            elif order == 'd':
                print(sorted(grades, reverse=True))
            else:
                print("Wrong Input!")
        elif choice == '5':
            print("Exiting...\n")
            break
        else:
            print("Invalid choice. Try again..")

# progress()

# Create an app that sorts a list using the advanced bubble sort.
# The improvement is to analyze the number of swaps at each step;
# if this number is equal to 0, there is no point in continuing sorting — the list has been sorted.
def advanced_bubble(lst):
    n = len(lst)
    for i in range(n-1):
        swaps = 0
        for j in range(n-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swaps += 1
        if swaps == 0:
            break
    return lst

# my_lst = [1,10,23,5]
# print(advanced_bubble(my_lst))
