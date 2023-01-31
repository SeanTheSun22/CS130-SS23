def is_even_list(numbers):
    if len(numbers) == 0:
        return []
    if numbers[0] % 2 == 0:
        return [True] + is_even_list(numbers[1:])
    return [False] + is_even_list(numbers[1:])

numbers_list = [1, 2, 3, 4, 5]
print(is_even_list(numbers_list))