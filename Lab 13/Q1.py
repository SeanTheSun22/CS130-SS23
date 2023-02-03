def count_up(n):
    if n == 0:
        print("Go!")
        return
    count_up(n - 1)
    print(n)

count_up(3)
count_up(0)
