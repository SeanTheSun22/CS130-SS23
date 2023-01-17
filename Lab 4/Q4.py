def get_maori_word(word_dictionary, english_word):
    try:
        if english_word == "":
            return "ERROR: Invalid word!"
        else:
            return word_dictionary[english_word]
    except KeyError:
        return "ERROR: " + english_word + " is not available."
    except:
        return "ERROR: Invalid input!"
        
dictionary = {'love': 'aroha', 'river': 'awa', 'walk': 'hikoi', 'gathering': 'hui'}

print(get_maori_word(dictionary, 'house'))

print()

print(get_maori_word(dictionary, 'love'))

print()

print(get_maori_word(dictionary, ''))

print()

print(get_maori_word(dictionary, ['house', 'love']))