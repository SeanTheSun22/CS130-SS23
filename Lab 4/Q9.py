def read_word_start_with_vowel():
    word = input("Enter a word: ")
    if word[0].lower() in 'aeiou':
        return word
    else:
        raise ValueError(f"'{word}' does not start with a vowel")

print(read_word_start_with_vowel())
