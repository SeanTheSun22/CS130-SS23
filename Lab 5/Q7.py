def rate(n):
    count = 4
    total = 0
    i = 0
    while i < n:
        total += i
        i += 2
        count += 3
    print(f"Number of operations: {count}")
    return total


rate(2)
rate(4)
rate(7)
rate(8)