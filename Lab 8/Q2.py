from math import sqrt

class Triangle():
    def __init__(self, a = 1, b = 1, c = 1):
        self.side_length_a = a
        self.side_length_b = b
        self.side_length_c = c

    def set_side_length_a(self, a):
        if a > 0:
            self.side_length_a = a

    def set_side_length_b(self, b):
        if b > 0:
            self.side_length_b = b

    def set_side_length_c(self, c):
        if c > 0:
            self.side_length_c = c

    def get_perimeter(self):
        return round(self.side_length_a + self.side_length_b + self.side_length_c, 2)

    def get_area(self):
        return round(0.25 * sqrt((self.side_length_a + self.side_length_b + self.side_length_c)*(-self.side_length_a + self.side_length_b + self.side_length_c)*(self.side_length_a - self.side_length_b + self.side_length_c)*(self.side_length_a + self.side_length_b - self.side_length_c)), 2)

triangle1 = Triangle()
print(triangle1.get_perimeter(), triangle1.get_area())
triangle2 = Triangle(18, 24, 30)
print(triangle2.get_perimeter(), triangle2.get_area())
triangle = Triangle(6, 6, 6)
print(triangle.side_length_a, triangle.side_length_b, triangle.side_length_c)
print(triangle.get_perimeter(), triangle.get_area())