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

    def assign(self, parent_title):
        self.parent_title = parent_title

    def unassign(self):
        self.parent_title = None

    def apply_inflation(self, inflation):
        self.amount += self.get_amount() *  inflation

