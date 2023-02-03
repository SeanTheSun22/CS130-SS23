def capitalise_words(words):
    if len(words) == 0:
        return []
    return [words[0][0].upper() + words[0][1:]] + capitalise_words(words[1:])

print(capitalise_words(['hello', 'world']))
