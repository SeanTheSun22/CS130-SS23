class VowelAnalysis:
    def __init__(self, text):
        self.text = text.lower()
        dict = {vowel:0 for vowel in "aeiou"}
        for letter in self.text:
            if letter in dict:
                dict[letter] += 1
        self.vowels_count_dict = dict

sentence1 = VowelAnalysis("Hello world");
sentence2 = VowelAnalysis("Summer is over and the hot days are gone");
print(sentence1.text, sentence1.vowels_count_dict)
print(sentence2.text, sentence2.vowels_count_dict)
print(type(sentence1))
print(sentence1 == sentence2)