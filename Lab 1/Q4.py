def apply_discount(amounts):
    for i in range(len(amounts)):
        if amounts[i] > 100:
            amounts[i] = 0.9 * amounts[i]
    return

a_list = [1.5, 232.5, 99, 45, 299]
apply_discount(a_list)
print(a_list)

a_list = [28, 147, 455, 25, 94, 123]
apply_discount(a_list)
print(a_list)

a_list = [11, 63, 96]
apply_discount(a_list)
print(a_list)