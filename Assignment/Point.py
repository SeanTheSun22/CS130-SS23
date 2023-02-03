import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        distance = self.distance_from_zero()
        
        if distance <= 1:
            self.score = 100
        elif distance <= 2:
            self.score = 50
        elif distance <= 3:
            self.score = 20
        elif distance <= 4:
            self.score = 10
        else:
            self.score = 0

    def distance_from_zero(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_score(self):
        return self.score

    def __str__(self):
        return f"({self.x}, {self.y})"