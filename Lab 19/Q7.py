class QuadraticStringHashTable:
    def __init__(self, size = 7):
        self.size = size
        self.slots = [None] * size

    def __str__(self):
        return str(self.slots)

    def get_sum_of_ascii(self, key):
        return sum(ord(letter) for letter in key)
    
    def get_hash_index(self, key, step = 0):
        return (self.get_sum_of_ascii(key) + (step ** 2)) % self.size

    def put(self, key):
        step = 0
        index = self.get_hash_index(key, step)
        while self.slots[index] is not None:
            step += 1
            index = self.get_hash_index(key, step)
        self.slots[index] = key

my_hash_table = QuadraticStringHashTable(5)
my_hash_table.put('at')
my_hash_table.put('for')
my_hash_table.put('be')
my_hash_table.put('not')
print(my_hash_table)

my_hash_table = QuadraticStringHashTable(13)
my_hash_table.put('at')
my_hash_table.put('for')
my_hash_table.put('be')
my_hash_table.put('not')
my_hash_table.put('hello')
my_hash_table.put('hashtable')
print(my_hash_table)