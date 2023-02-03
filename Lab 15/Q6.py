class LeibnizSeries:
    def __init__(self, number_of_terms = 10):
        self.__number_of_terms = number_of_terms

    def __iter__(self):
        return LeibnizSeriesIterator(self.__number_of_terms)
        
class LeibnizSeriesIterator:
    def __init__(self, n):
        self.n = n
        self.current = -1
    
    def __next__(self):
        self.current += 1
        if self.current == self.n:
            raise StopIteration("Error: all the items have been visited!")
        return (-1) ** self.current * 4 / (2 * self.current + 1)

series = LeibnizSeries(100)
sum_terms = 0
for term in series:
    sum_terms += term
print("Sum:", sum_terms)

series = LeibnizSeries()
sum_terms = 0
for term in series:
    sum_terms += term
    print(round(term,5))
print("Sum:", sum_terms)

series = LeibnizSeries(3)
series_iter = iter(series)
print(next(series_iter))
print(next(series_iter))
print(next(series_iter))
try:
    print(next(series_iter))
except StopIteration as err:
    print(err)