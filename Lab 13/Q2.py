def count_non_alphanumeric(word):
    if len(word) == 0:
        return 0
    if word[0].isalnum():
        return count_non_alphanumeric(word[1:])
    return 1 + count_non_alphanumeric(word[1:])

print(count_non_alphanumeric('(123)-[456]'))
print(count_non_alphanumeric('2rPTy5'))
print(count_non_alphanumeric('**hello world!?**'))