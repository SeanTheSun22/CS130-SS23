def get_sum_scores(scores_list):
    sum = 0
    i = 0
    while True:
        try:
            if (float(scores_list[i]) >= 0) and (float(scores_list[i]) <= 100):
                sum += float(scores_list[i])
        except:
            return sum
        i += 1


print(get_sum_scores([0, 5, -5, 10, 50, 105, 20]))

print()

print(get_sum_scores([['NA'], 1]))

print()

print(get_sum_scores([-1, 0, 10, 20, 100, 1, 'ten', 35, 45, 105, 20]))