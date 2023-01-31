def print_even_between(start, end):
    print("Count", start)
    if end < start:
        return
    if start % 2 == 0:
        print(start, end=' ')
    print_even_between(start+1, end)

print_even_between(-3, 3)