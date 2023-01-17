def remove_all_positives(numbers):
    popped = 0
    for index in range(len(numbers)):
        num = numbers[index - popped]
        if num > 0:
            numbers.pop(index - popped)
            popped += 1


numbers = [1, -2, -5, 7, 4, 6, -8, 9, -3]
remove_all_positives(numbers)
print(numbers)

print()

numbers = []
remove_all_positives(numbers)
print(numbers)