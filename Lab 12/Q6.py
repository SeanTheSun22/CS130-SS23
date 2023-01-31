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

    def get_total_cost(self):
        sum = 0
        for budget in self.budgets:
            sum += budget.get_amount()
        return round(sum)

    def __str__(self):
        return f"{self.title}:\n" + "\n".join(str(budget) for budget in self.budgets) + f"\n=====\nTotal:${self.get_total_cost()}"

    def apply_inflation(self, rate):
        for budget in self.budgets:
            budget.apply_inflation(rate)

group1 = GroupBudget("Utility Bills")
budget1 = Budget("Electricity", 201.9)
budget2 = Budget("Water", 102.2)
budget3 = Budget("Internet", 120)
group1.add_budget(budget1)
group1.add_budget(budget2)
print(group1)
print(group1.get_total_cost())
group1.apply_inflation(0.073)
print("{:.1f}".format(budget1.get_amount()))
print("{:.1f}".format(budget2.get_amount()))
print(group1)