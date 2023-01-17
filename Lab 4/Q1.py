def is_eligible(age_input):
    try:
        age = int(age_input)
        if age >= 7:
            return (True, age)
        else:
            return (False, age)
    except ValueError:
        return (False, 'ValueError')
    except TypeError:
        return (False, 'TypeError')


print(is_eligible('7'))

print()

print(is_eligible('abc'))

print()

print(is_eligible([1, 2, 3]))

print()

print(is_eligible('33'))