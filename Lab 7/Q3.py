def bubble_sort(data):
    complexity = []
    for pass_num in range(len(data) - 1, 0, -1):
        checks = 0
        swaps = 0
        for i in range(0, pass_num):
            checks += 1
            if data[i] > data[i+1]:
                swaps += 1
                data[i], data[i+1] = data[i+1], data[i]
        complexity.append([checks, swaps])
    return complexity


numbers = [12, 78, 81, 99, 91]
result = bubble_sort(numbers)
print(result)

numbers = [92, 33, 63, 6, 66, 77, 74, 51, 30, 86]
result = bubble_sort(numbers)
print(result)