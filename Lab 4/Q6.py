def get_sum_scores_continue(scores_list):
    sum = 0
    for value in scores_list:
        try:
            if (float(value) >= 0) and (float(value) <= 100):
                sum += float(value)
        except:
            pass
    return round(sum)

print(get_sum_scores_continue([-1, 0, 10, 20, 'ten', 35, 45, 105, 20]))

print()

print(get_sum_scores_continue([-1, '-2', -3, '4']))

print()

print(get_sum_scores_continue([['NA'], 1]))
