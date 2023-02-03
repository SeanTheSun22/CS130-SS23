class EvenNumbersList:
    def __init__(self, evens = None):
        if evens == None:
            self.numbers = []
        else:
            self.numbers = evens
    
    def add_number(self, value):
        if value % 2 == 0:
            self.numbers.append(value)
        
    def __str__(self):
        return str(self.numbers)

d1 = EvenNumbersList()
d1.add_number(4)
print("d1:", d1)
d2 = EvenNumbersList()
d2.add_number(6)
print("d2:", d2)
d3 = EvenNumbersList()
d3.add_number(8)
print("d3:", d3)