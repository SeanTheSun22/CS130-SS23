def get_longest_length(words):
    if len(words) == 0:
        return 0
    if len(words[0]) > get_longest_length(words[1:]):
        return len(words[0])
    return get_longest_length(words[1:])

list_words = ['This', 'is', 'a', 'computer', 'science', 'test']
print(get_longest_length(list_words))