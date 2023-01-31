class Covid19Data:
    def __init__(self, status = False, week_number = 1, number_of_new_cases = 0):
        self.status = status
        self.week_number = week_number
        self.number_of_new_cases = number_of_new_cases

    def set_number_of_new_cases(self, value):
        if value >= 0:
            self.number_of_new_cases = value

data1 = Covid19Data(True, 47, 2995)
print(data1.status, data1.week_number, data1.number_of_new_cases)
data2 = Covid19Data(True, 48, 3502)
print(data2.status, data2.week_number, data2.number_of_new_cases)
print(type(data1))
print(data1 == data2)
data1.set_number_of_new_cases(-1)
print(data1.number_of_new_cases)
data1.set_number_of_new_cases(500)
print(data1.number_of_new_cases)
data3 = Covid19Data()
print(data3.status, data3.week_number, data3.number_of_new_cases)

data1 = Covid19Data(True, 49, 4114)
print(data1.status, data1.week_number, data1.number_of_new_cases)
data2 = Covid19Data(False, 50, 4525)
print(data2.status, data2.week_number, data2.number_of_new_cases)