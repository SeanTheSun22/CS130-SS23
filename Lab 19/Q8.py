class DoubleStringHashTable:
    def __init__(self, size=11, secondary_hash_value=7):
        self.size = size
        self.slots = [None] * size
        self.secondary_hash_value = secondary_hash_value

    def __str__(self):
        return str(self.slots)
        
    def get_sum_of_ascii(self, key):
        return sum(ord(letter) for letter in key)

    def get_step_size(self, key):
        return self.secondary_hash_value - (self.get_sum_of_ascii(key) % self.secondary_hash_value)

    def get_hash_index(self, key, step = 0, step_size = 1):
        return (self.get_sum_of_ascii(key) + (step * step_size)) % self.size

    def put(self, key):
        step = 0
        step_size = self.get_step_size(key)
        index = self.get_hash_index(key, step, step_size)
        while self.slots[index] is not None:
            step += 1
            index = self.get_hash_index(key, step, step_size)
        self.slots[index] = key

my_hash_table = DoubleStringHashTable(5, 3)
my_hash_table.put('at')
my_hash_table.put('for')
my_hash_table.put('be')
my_hash_table.put('not')
print(my_hash_table)

my_hash_table = DoubleStringHashTable(13, 11)
my_hash_table.put('at')
my_hash_table.put('for')
my_hash_table.put('be')
my_hash_table.put('not')
my_hash_table.put('hello')
my_hash_table.put('hashtable')
print(my_hash_table)