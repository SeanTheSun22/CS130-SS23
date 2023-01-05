def create_english_maori_dictionary(english_words, maori_words):
    a_dict = dict()
    for i in range(len(english_words)):
        a_dict[english_words[i]] = maori_words[i]
    return a_dict

words1 = ['love', 'river', 'walk', 'love']
words2 = ['aroha', 'awa', 'hikoi', 'aroha']
a_dict = create_english_maori_dictionary(words1, words2)
for key in sorted(a_dict.keys()):
    print(key, a_dict[key])