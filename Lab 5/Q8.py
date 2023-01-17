def rate(n):
    count = 4
    total = 0
    i = 1
    while i < 8:
        total += i
        i *= 2
        count += 3
    print(f"Number of operations: {count}")
    return total


rate(2)
