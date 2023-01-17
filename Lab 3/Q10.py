def append_name_to(name, names_list=None):
    if names_list is None:
        names_list = []
    names_list.append(name)
    return names_list


my_list = append_name_to('Michael')
print(my_list)
my_list = append_name_to('Dick')
print(my_list)

print()

my_list = append_name_to('Paul')
print(my_list)
my_list = append_name_to('Mary', my_list)
print(my_list)
my_list = append_name_to('May')
print(my_list)

print()

my_list = []
my_list = append_name_to('Smith', my_list )
print(my_list)