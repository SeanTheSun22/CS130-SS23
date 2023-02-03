from Stack import Stack

def longest_mirror_pattern(string):
    string_stack = Stack()
    longest = 0
    length = 0
    for letter in string:
        if string_stack.is_empty():
            string_stack.push(letter)
            if longest < length:
                longest = length
            length = 0
        elif string_stack.peek() == letter:
            string_stack.pop()
            length += 2
        else:
            string_stack.push(letter)
            if longest < length:
                longest = length
            length = 0
    if longest < length:
        longest = length
    return longest

print(longest_mirror_pattern("ab"))
print(longest_mirror_pattern("aa"))
print(longest_mirror_pattern("aba")) 
print(longest_mirror_pattern("abb")) 
print(longest_mirror_pattern("abba"))
print(longest_mirror_pattern("cabba"))
