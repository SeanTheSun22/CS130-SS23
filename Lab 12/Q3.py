class Budget:
    def __init__(self, title, amount):
        self.title = title
        self.amount = amount
        self.parent_title = None
    
    def __str__(self):
        return f"{self.title}(${round(self.amount)})"

    def get_title(self):
        return self.title

    def get_amount(self):
        return self.amount

    def get_parent_title(self):
        return self.parent_title


budget1 = Budget("Electricity", 201.9)
print(budget1)
print(budget1.get_title())
print(budget1.get_amount())
print(budget1.get_parent_title())
print(budget1.get_parent_title() == None)
budget2 = Budget("Water", 102.2)
print(budget2)