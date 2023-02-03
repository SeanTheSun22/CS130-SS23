from Player import Player

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