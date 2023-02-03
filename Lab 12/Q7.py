def my_selection_sort(data):
    comparisons = 0
    swaps = 0	
    for pass_num in range(len(data) - 1, 0, -1):           
        position_highest = 0
        for i in range(1, pass_num+1):
            comparisons += 1
            if data[i] > data[position_highest]:
                position_highest = i
        swaps += 1
        data[position_highest], data[i] = data[i], data[position_highest]
    return (comparisons, swaps)


def merge(list1, list2):
    comparisons = 0
    len_list1 = len(list1)
    len_list2 = len(list2)
    index1 = 0
    index2 = 0
    index3 = 0
    list3 = [0] * (len_list1 + len_list2)
    while index1 < len_list1 and index2 < len_list2:
        comparisons += 1
        if list1[index1] <= list2[index2]:
            list3[index3] = list1[index1]
            index1 += 1
        else:
            list3[index3] = list2[index2]
            index2 += 1
        index3 += 1
 
    # Copy the remaining elements of list 1 if any
    while index1 < len_list1:
        list3[index3] = list1[index1]
        index1 += 1
        index3 += 1
 
    # Copy the remaining elements of list 2 if any
    while index2 < len_list2:
        list3[index3] = list2[index2]
        index2 += 1
        index3 += 1
    return (list3, comparisons)

def zip_sort(numbers):
    list1 = []
    list2 = []

    for i in range(len(numbers)):
        if i % 2 == 0:
            list1.append(numbers[i])
        else:
            list2.append(numbers[i])

    complexity1 = my_selection_sort(list1)
    complexity2 = my_selection_sort(list2)

    complexity3 = merge(list1, list2)

    return (complexity1[0] + complexity2[0] + complexity3[1], complexity1[1] + complexity2[1], complexity3[0])

data = []
(num_comparisons, num_swaps, result)=zip_sort(data)
print("Number of comparisons =", num_comparisons)
print("Number of swaps =", num_swaps)
print("Sorted list =",result)

data = [3,2,1]
(num_comparisons, num_swaps, result)=zip_sort(data)
print("Number of comparisons =", num_comparisons)
print("Number of swaps =", num_swaps)
print("Sorted list =",result)

data = [1,2,3]
(num_comparisons, num_swaps, result)=zip_sort(data)
print("Number of comparisons =", num_comparisons)
print("Number of swaps =", num_swaps)
print("Sorted list =",result)

data = [1,5,3,7,4,2]
(num_comparisons, num_swaps, result)=zip_sort(data)
print("Number of comparisons =", num_comparisons)
print("Number of swaps =", num_swaps)
print("Sorted list =",result)