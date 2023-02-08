from NodeLinkedList import *

class LinkedListHashTable:
    def __init__(self, size=7):
        self.__size = size
        self.__slots = [LinkedList() for i in range(self.__size)]
    
    def get_hash_code(self, key):
        return key % self.__size
    
    def __str__(self):
        return "\n".join(str(linked_list) for linked_list in self.__slots)

    def put(self, key):
        self.__slots[self.get_hash_code(key)].add(key)

    def __len__(self):
        return sum(len(linked_list) for linked_list in self.__slots)

hash_table = LinkedListHashTable(5)
hash_table.put(3)
hash_table.put(6)
hash_table.put(9)
hash_table.put(11)
hash_table.put(21)
hash_table.put(13)
print(hash_table)
print(f"The linked list hash table "+
      f"contains {len(hash_table)} items.")