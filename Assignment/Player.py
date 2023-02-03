from Point import Point
import random

class Player:
    def __init__(self, name, seed=30):
        self.name = name
        self.points = []
        random.seed(seed)

    def make_throw(self):
        x = random.randrange(-5, 6)
        y = random.randrange(-5, 6)
        self.points.append(Point(x, y))
        print(f"{self.name}: The score for a dart throw at position "
              f"{self.points[-1]} is {self.get_score()}.")
    
    def get_score(self):
        return self.points[-1].get_score()

    def get_total_score(self):
        return sum(point.get_score() for point in self.points)

    def get_name(self):
        return self.name
    
    def __str__(self):
        return (f"{self.name}'s total score is {self.get_total_score()}.\n"
                + "\n".join(f"The score for a dart throw at position {point} "
                f"is {point.get_score()}." for point in self.points))