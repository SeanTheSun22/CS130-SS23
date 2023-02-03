def is_ascending(numbers):
    if len(numbers) == 1:
        return True
    if numbers[0] <= numbers[1] and is_ascending(numbers[1:]):
        return True
    return False
        


number_list = [1,4,2,3,5]
print(is_ascending(number_list))

number_list = [10, 10, 10, 10]
print(is_ascending(number_list))

number_list = [2, 4, 4, 6, 8, 8, 10]
print(is_ascending(number_list))