def generate_histogram(a_dict):
    sorted_dict = sorted(a_dict.items())
    for values in sorted_dict:
        print("{0:10}|".format(values[0]), 'X' * values[1], sep = "")


data = {'egg':8, 'banana':4, 'apple':9, 'cat':3, 'dog':1}
generate_histogram(data)

print()

data = {'a':21, 'b':11, 'c':24, 'd':20, 'e':3, 'f':22, 'g':9, 'h':17, 'i':14}
generate_histogram(data)