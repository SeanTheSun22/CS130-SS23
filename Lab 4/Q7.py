from queue import Empty


def get_valid_input():
    outputs = ["paper", "rock", "scissors"]
    while True:
        input_value = input("Enter a valid input (0 for paper, 1 for rock or 2 for scissors): ")
        try:
            if int(input_value) >= 0:
                return outputs[int(input_value)]
        except:
            pass

value = get_valid_input()
print('Valid input:', value)