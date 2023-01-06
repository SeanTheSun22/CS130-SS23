def create_list_of_tuples(words_list):
    return [(Word,len(Word)) for Word in words_list if Word[0] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]]


print(create_list_of_tuples(['Hello', 'world', 'good', 'job', 'well', 'done']))
print(create_list_of_tuples(['Abby', 'Bella', 'abby']))
print(create_list_of_tuples([]))