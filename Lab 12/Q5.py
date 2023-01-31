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

class GroupBudget:
    def __init__(self, title):
        self.title = title
        self.budgets = []

    def get_number_of_budgets(self):
        return len(self.budgets)

    def add_budget(self, budget):
        budget.assign(self.title)
        self.budgets.append(budget)

    def remove_budget(self, budget):
        budget.unassign()
        self.budgets.remove(budget)

group1 = GroupBudget("Utility Bills")
budget1 = Budget("Electricity", 201.9)
budget2 = Budget("Water", 102.2)
budget3 = Budget("Internet", 120)
group1.add_budget(budget1)
group1.add_budget(budget2)
print(group1.get_number_of_budgets())
print(budget1.get_parent_title())
print(budget2.get_parent_title())
print(budget3.get_parent_title())
group1.remove_budget(budget1)
print(group1.get_number_of_budgets())
print(budget1.get_parent_title())