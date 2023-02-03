from Stack import Stack

def push_pop(a_stack, numbers):
    for number in numbers:
        if number % 2 == 0:
            for i in range(number):
                a_stack.push(number)
        else:
            for i in range(number):
                a_stack.pop()
    return


a_stack = Stack()
for value in [1, 2, 3 ,4]:
    a_stack.push(value)
push_pop(a_stack, [3, 6])
print(a_stack)

a_stack = Stack()
for value in [45, 123, 76, -3, 56, 13, -8, 9, 23, 3, 1, -9, -45]:
    a_stack.push(value)
push_pop(a_stack, [2, 7, 4, 5, 10, 9, 6])
print(a_stack)