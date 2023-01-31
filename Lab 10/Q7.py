from Stack import Stack

def string_reversal(string):
    stack = Stack()
    for letter in string:
        stack.push(letter)
    return "".join([stack.pop() for letter in string])

string = "hello"
print(string)
print(string_reversal(string))

string = "Stacks are useful!"
print(string)
print(string_reversal(string))