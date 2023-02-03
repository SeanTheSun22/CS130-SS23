class Covid19Data:
    def __init__(self, status = False, week_number = 1, number_of_new_cases = 0):
        self.status = status
        self.week_number = week_number
        self.number_of_new_cases = number_of_new_cases

    def set_number_of_new_cases(self, value):
        if value >= 0:
            self.number_of_new_cases = value

    def __str__(self):
        if self.status == True:
            return f"Real > week {self.week_number} : {self.number_of_new_cases}"
        return f"Predicted > week {self.week_number} : {self.number_of_new_cases}"
    
    def predict(self, ratio):
        return Covid19Data(False, self.week_number + 1, round(self.number_of_new_cases * ratio))
    
class Location:
    def __init__(self, name = ""):
        self.name = name
        self.data = []
    
    def add_case(self, week_number, number_of_new_cases):
        self.data.append(Covid19Data(True, week_number, number_of_new_cases))
    
    def get_total_number_of_new_cases(self):
        return sum(data.number_of_new_cases for data in self.data)

location1 = Location('Auckland')
location1.add_case(47, 2995)
location1.add_case(48, 3502)
location1.add_case(49, 4114)
print(location1.get_total_number_of_new_cases())
print(type(location1))
print(type(location1.data[0]))
location2 = Location('Northland')
print(len(location2.data))
location2.add_case(51, 1046)
print(len(location2.data))

location1 = Location('Auckland')
location1.add_case(47, 2995)
location2 = Location('Northland')
location2.add_case(51, 1046)
location2.add_case(50, 948)
print(location1.get_total_number_of_new_cases())
print(location2.get_total_number_of_new_cases())
print(location1 == location2)