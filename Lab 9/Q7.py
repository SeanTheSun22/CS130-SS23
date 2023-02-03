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

data1 = Covid19Data(True, 47, 2995)
print(data1)
data2 = Covid19Data(True, 48, 3502)
print(data2)
print(type(data1))
data3 = data1.predict(1.1)
print(type(data3))
print(data3)
data4 = Covid19Data()
print(data4)

data1 = Covid19Data(True, 49, 4114)
print(data1)
data2 = Covid19Data(False, 50, 4525)
print(data2)