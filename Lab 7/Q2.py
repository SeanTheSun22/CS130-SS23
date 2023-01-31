def selection_sort_fast(data):
    complexity = []
    for pass_num in range(len(data) - 1, 0, -1):
        comparisons = 0
        swaps = 0
        position_largest = 0
        for i in range(1, pass_num + 1):
            comparisons += 1
            if data[i] > data[position_largest]:
                position_largest = i
        if position_largest != pass_num:
            data[position_largest], data[i] = data[i], data[position_largest]
            swaps += 1
        complexity.append([comparisons, swaps])
    
    return complexity


numbers2 = [76, 53, 48, 24, 12]
result2 = selection_sort_fast(numbers2)
print(result2)

numbers2 = [95, 55, 92, 9]
result2 = selection_sort_fast(numbers2)
print(result2)