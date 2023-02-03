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


triangle1 = Triangle()
print(triangle1.side_length_a, triangle1.side_length_b, triangle1.side_length_c)
triangle2 = Triangle(18, 24, 30)
print(triangle2.side_length_a, triangle2.side_length_b, triangle2.side_length_c)
triangle1.set_side_length_a(-1)
print(triangle1.side_length_a)
triangle1.set_side_length_a(10)
print(triangle1.side_length_a)
triangle1.set_side_length_b(12)
print(triangle1.side_length_b)
triangle1.set_side_length_c(20)
print(triangle1.side_length_c)