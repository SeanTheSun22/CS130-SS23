def print_dictionary_descending(a_dict):
    sorted_dict = sorted(a_dict.items(), key = lambda x:x[1], reverse = True)
    for values in sorted_dict:
        print(values[0], values[1])


a_dict = {'e':2, 'b':6, 'a':3, 'c':4, 'd':1}
print_dictionary_descending(a_dict)

print()

a_dict = {'x' : 99}
print_dictionary_descending(a_dict)

print()

data = {'Northland': 471, 'Waitemata': 2366, 'Auckland': 1667, 'Counties Manukau': 2087, 'Waikato': 1285, 'Bay of Plenty': 594, 'Lakes': 314, 'Taranaki': 375, "Hawke's Bay": 452, 'Whanganui': 222}
print_dictionary_descending(data)