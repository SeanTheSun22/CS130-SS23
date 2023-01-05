def remove_duplicates(numbers_list):
    numbers_list.sort()
    j = 1
    for i in range(1, len(numbers_list)):
        if numbers_list[j] == numbers_list[j - 1]:
            numbers_list.pop(j)
        else:
            j += 1      
    return 

values = [5, 3, 1, 2, 3, 2, 6, 2, 1]
remove_duplicates(values)
print(values)

values = [1, 2, 3, 2, 1, 2, 3]
remove_duplicates(values)
print(values)

values = [1, 1, 2, 2]
remove_duplicates(values)
print(values)