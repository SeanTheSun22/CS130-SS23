class VowelAnalysis:
    def __init__(self, text = ""):
        self.text = text.lower()
        dict = {vowel:0 for vowel in "aeiou"}
        for letter in self.text:
            if letter in dict:
                dict[letter] += 1
        self.vowels_count_dict = dict

    def __str__(self):
        if self.text == "":
            return "It is an empty string!"
        return f"{self.text}:\n" + "\n".join(f"{key} appears {self.vowels_count_dict[key]} time(s)." for key in self.vowels_count_dict.keys())

    def get_total_number_of_vowels(self):
        return sum(self.vowels_count_dict.values())

sentence1 = VowelAnalysis()
print(sentence1)
print(sentence1.get_total_number_of_vowels())
sentence2 = VowelAnalysis("Summer is over and the hot days are gone")
print(sentence2)
print(sentence2.get_total_number_of_vowels())