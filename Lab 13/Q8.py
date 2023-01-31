
def evaluate_f(n):
    if round(n) == 1:
        return (1, 0)
    if n % 2 == 0:
        tuple = evaluate_f(int(n / 2))
        return (2 * tuple[0] + n ** 2, tuple[1] + 1)
    tuple = evaluate_f(int(n - 1))
    return (tuple[0] + n, tuple[1] + 1)


print(evaluate_f(1))
print(evaluate_f(2))
print(evaluate_f(6))
