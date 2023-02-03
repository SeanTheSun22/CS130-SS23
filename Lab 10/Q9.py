from Stack import Stack

def evaluate_postfix(postfix):
    stack = Stack()
    list = postfix.split(" ")
    for item in list:
        if item in "+-*/":
            a = stack.pop()
            b = stack.pop()
            stack.push(compute(b, a, item))
        else:
            stack.push(int(item))
    return stack.pop()
            

def compute(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    else:
        return number1 // number2

print(evaluate_postfix('21 9 +'))

print(evaluate_postfix('2 4 3 * -'))

print(evaluate_postfix('9 4 2 - 10 * + 13 -'))
