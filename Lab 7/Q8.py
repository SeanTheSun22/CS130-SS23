def binary_search(numbers, target_value):
    left = 0
    right = len(numbers) - 1
    mid = (left + right) // 2
    while numbers[mid] != target_value and left <= right:
        print(f"left: {left}, right: {right}, mid: {mid}")
        if numbers[mid] < target_value:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2
    if numbers[mid] == target_value:
        print(f"left: {left}, right: {right}, mid: {mid}")
        return mid
    return -1

numbers = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
print(binary_search(numbers, 18))
print()
numbers = [13, 18, 54, 61, 78, 93]
print(binary_search(numbers, 10))