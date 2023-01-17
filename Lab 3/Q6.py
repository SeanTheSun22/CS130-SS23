def no_positives(numbers):
    for number in numbers:
        if number > 0:
            return False
    return True


numbers = [-5, -1, 3, 4]
print(no_positives(numbers))

print()

numbers = []
print(no_positives(numbers))

print()

numbers = [3]
print(no_positives(numbers))