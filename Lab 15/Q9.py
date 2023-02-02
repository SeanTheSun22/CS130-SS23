from LinkedList import LinkedList

def convert_to_python_list(a_linked_list):
    return [node for node in a_linked_list]

def create_squared_linked_list(a_linked_list):
    list = convert_to_python_list(a_linked_list)
    return_linked_list = LinkedList()
    for i in list:
        return_linked_list.add(i ** 2)
    return_linked_list.reverse()
    return return_linked_list 

list_numbers = LinkedList()
list_numbers.add(3)
list_numbers.add(2)
list_numbers.add(1)
print(list_numbers)
list_squared = create_squared_linked_list(list_numbers)
print(list_squared)
print(type(list_squared))

list_numbers = LinkedList()
list_numbers.add(5)
list_numbers.add(10)
list_numbers.add(15)
print(list_numbers)
list_squared = create_squared_linked_list(list_numbers)
print(list_squared)