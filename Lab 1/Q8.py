def create_list_of_odd_squares(n):
    return [x ** 2 for x in range(1, n + 1) if x % 2 == 1]

print(create_list_of_odd_squares(10))
print(create_list_of_odd_squares(1))