def selection_sort(data):
    complexity = []
    for pass_num in range(len(data) - 1, 0, -1):
        comparisons = 0
        swaps = 0
        position_largest = 0
        for i in range(1, pass_num + 1):
            comparisons += 1
            if data[i] > data[position_largest]:
                position_largest = i
        data[position_largest], data[i] = data[i], data[position_largest]
        swaps += 1
        complexity.append([comparisons, swaps])
    
    return complexity


numbers = [6]
result = selection_sort(numbers)
print(result)

numbers = [70, 48, 54, 79, 33]
result = selection_sort(numbers)
print(result)