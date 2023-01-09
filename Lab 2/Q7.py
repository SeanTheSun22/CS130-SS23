def get_largest_value(dictionary):
    sorted_dict = sorted(dictionary.items(), key = lambda x:x[1], reverse = True)
    return sorted_dict[0][1]


data = {'e':2, 'b':6, 'a':3, 'c':4, 'd':1}
print(get_largest_value(data))

print()

data = {'a':5, 'c':3, 'b':0}
print(get_largest_value(data))