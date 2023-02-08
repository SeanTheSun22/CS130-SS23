from NodeLinkedList import *

class LinkedListHashTable:
    def __init__(self, size=7):
        self.__size = size
        self.__slots = [LinkedList() for i in range(self.__size)]
    
    def get_hash_code(self, key):
        return key % self.__size
    
    def __str__(self):
        return "\n".join(str(linked_list) for linked_list in self.__slots)

hash_table = LinkedListHashTable()
key1, key2 = 2, 1
print(f'Hash value for {key1}: {hash_table.get_hash_code(key1)}')
print(f'Hash value for {key2}: {hash_table.get_hash_code(key2)}')
print()
print('Hash table:')
print(hash_table)

hash_table = LinkedListHashTable(4)
key = 23
print(f'Hash value for {key}: {hash_table.get_hash_code(key)}')
print()
print('Hash table:')
print(hash_table)