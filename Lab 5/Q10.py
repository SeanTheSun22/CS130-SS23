def rate(n):
    count = 4
    total = 0
    i = 1
    while i < n:
        j = 0
        while j < n:
            total += j 
            j += 1
            count += 3
        i *= 2
        count += 4
    print(f"Number of operations: {count}")

    return total

rate(2)
