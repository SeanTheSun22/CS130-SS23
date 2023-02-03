def binary_search_descending(numbers, item):
    if len(numbers) == 0:
        return False

    mid = len(numbers) // 2
    left = numbers[:mid]
    right = numbers[mid + 1:]
    print(left, numbers[mid], right)

    if numbers[mid] == item:
        return True
    if numbers[mid] > item:
        return binary_search_descending(right, item)
    return binary_search_descending(left, item)

test_list = [42, 32, 19, 17, 13, 8, 2, 1, 0]
print(binary_search_descending(test_list, 13))

test_list = [42, 32, 19, 17, 13, 8, 2, 1, 0]
print(binary_search_descending(test_list, 3))