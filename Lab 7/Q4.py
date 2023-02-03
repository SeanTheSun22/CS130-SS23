def bubble_sort_fast(data):
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
        if swaps == 0:
            break
    return complexity



numbers2 = [12, 15, 19, 37, 39]
result2 = bubble_sort_fast(numbers2)
print(result2)

numbers2 = [55, 34, 98, 63]
result2 = bubble_sort_fast(numbers2)
print(result2)