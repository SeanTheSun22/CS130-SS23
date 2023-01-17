def rate(n):
    count = 4
    total = 0
    i = 0
    while i < n:
        j = 0
        while j < 2 * n:
            total += j 
            j += 1
            count += 3
        i += 1
        count += 4
    print(f"Number of operations: {count}")
    return total
rate(2)
