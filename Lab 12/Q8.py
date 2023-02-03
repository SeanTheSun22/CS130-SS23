def binary_search(numbers, value):
    comparisons = 0
    right = len(numbers) - 1
    left = 0
    while (left <= right):
        mid = (left + right) // 2
        if (numbers[mid] == value):
            comparisons += 1
            return (comparisons, mid)
        elif (numbers[mid] < value):
            comparisons += 2
            left = mid + 1
        else:
            comparisons += 2
            right = mid - 1
        
    if mid == 0:
        return (comparisons, mid)
    if numbers[mid] > value:
        if abs(numbers[mid] - value) >= abs(numbers[mid - 1] - value):
            return (comparisons, mid - 1)
        else:
            return (comparisons, mid)
    if mid >= len(numbers) - 1:
        return (comparisons, mid)
    if abs(numbers[mid] - value) < abs(numbers[mid + 1] - value):
        return (comparisons, mid)
    else:
        return (comparisons, mid + 1)


def closest_number_binary_search(numbers, target_value):
    return binary_search(numbers, target_value)

print(closest_number_binary_search([1,3],1))
print(closest_number_binary_search([1,3],4))
print(closest_number_binary_search([1,3],2))


