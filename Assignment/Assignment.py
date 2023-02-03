import math
import random


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


class DartGame:
    def __init__(self, seed=30):
        self.print_banner()
        self.number_of_throws = self.input_number_of_throws()
        self.player1 = Player(self.input_player_name(1), seed)
        self.player2 = Player(self.input_player_name(2), seed)
        print()

    def print_banner(self):
        banner_text = "Welcome to the simplified dart game simulation!"
        banner_border = "*" * len(banner_text)
        print(f"{banner_border}\n{banner_text}\n{banner_border}")

    def input_number_of_throws(self):
        try:
            user_input = int(input("Enter the number of throws required: "))
            if user_input < 1 or user_input > 20:
                user_input = self.input_number_of_throws()
        except ValueError:
            print("ERROR: invalid number! Please enter again.")
            user_input = self.input_number_of_throws()
        return user_input

    def input_player_name(self, player_number):
        user_input = input(f"Enter player{player_number} name: ")
        while len(user_input) == 0:
            user_input = input(f"Enter player{player_number} name: ")
        return user_input
        
    def get_number_of_throws(self):
        return self.number_of_throws

    def get_first_player_name(self):
        return self.player1.get_name()

    def get_second_player_name(self):
        return self.player2.get_name()

    def play_game(self):
        for i in range(self.number_of_throws):
            self.player1.make_throw()
            self.player2.make_throw()
        print()
    
    def congratulate_player(self):
        scores = (self.player1.get_total_score(), 
                  self.player2.get_total_score())
                  
        if scores[0] == scores[1]:
            congratulate_text = "It's a tie!"
        elif scores[0] > scores[1]:
            congratulate_text = (f"Congratulations! The winner is "
                                 f"{self.get_first_player_name()}.")
        else:
            congratulate_text = (f"Congratulations! The winner is "
                                 f"{self.get_second_player_name()}.")
        congratulate_border = "*" * len(congratulate_text)

        print(congratulate_border, 
              congratulate_text, 
              congratulate_border, 
              sep = "\n")
        print()
        print(self.player1, 
              self.player2, 
              sep = "\n")


def test1():
    p1 = Point(1, 2)
    print(p1)
    print(p1.get_score())
    p2 = Point()
    print(p2)
    print(p2.get_score())
    print("-" * 7)
    p1 = Point(0, -2)
    print(p1)
    print(p1.get_score())
    p2 = Point(2, 0)
    print(p2)
    print(p2.get_score())
    print("-" * 7)

def test2():
    player1 = Player("Bob", 30)
    player1.make_throw()
    print(player1.get_score())
    print(player1)
    print("-" * 59)
    player1 = Player("Bob", 30)
    for i in range(5):
        player1.make_throw()
    print(player1.get_total_score())
    print(player1)
    print("-" * 59)

def test3():
    for i in range(5):
        game = DartGame(30)
        print(game.get_number_of_throws())
        print(game.get_first_player_name())
        print(game.get_second_player_name())
        print("-" * 47)
'''
2
Bob
Peter
Bob
2
Bob
Peter
2

Bob
Peter
101
2
Bob
Peter
21
20
Bob
Peter
'''

def test4():
    game = DartGame(30)
    game.play_game()
    game.congratulate_player()
    print("-" * 59)
    game = DartGame(90)
    game.play_game()
    game.congratulate_player()
    print("-" * 59)
'''
1
Bob
Peter
Bob
1

Bob

Peter
'''

def test5():
    game = DartGame(40)
    game.play_game()
    game.congratulate_player()
    print("-" * 60)
    game = DartGame(110)
    game.play_game()
    game.congratulate_player()
    print("-" * 60)
'''
5
Mary
Emma
Bob
2

Bob

Peter
'''

test4()