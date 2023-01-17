def get_min_between(numbers, start_index, end_index):
    new_numbers = []
    if len(numbers) <= start_index:
        print("Empty range!")
        return

    for i in range(start_index, end_index + 1):
        try:
            new_numbers.append(numbers[i])
        except:
            print(i, "is an invalid index")

    print("The minimum is =", min(new_numbers))


get_min_between([1, 2, 3, 4, 5], 3, 3)

print()

get_min_between([1, 2, 3, 4, 5], 1, 8)

print()

get_min_between([1, 2, 3, 4, 5], 7, 8)