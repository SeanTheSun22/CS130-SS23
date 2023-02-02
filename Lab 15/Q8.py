from LinkedList import LinkedList

def convert_to_python_list(a_linked_list):
    return [node for node in a_linked_list]

listA = LinkedList()
listA.add('3')
listA.add('2')
listA.add('1')
list1 = convert_to_python_list(listA)
print(list1)
print(type(list1))

listA = LinkedList()
listA.add(2)
listA.add(1)
list1 = convert_to_python_list(listA)
print(list1)