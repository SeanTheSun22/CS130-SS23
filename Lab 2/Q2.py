def create_dictionary(locations):
    return {place:0 for place in locations}


a_dict = create_dictionary(['Northland', 'Waitemata'])
for key in sorted(a_dict):
    print(key, a_dict[key])

print()

a_dict = create_dictionary(['Northland', 'Waitemata', 'Auckland', 'Counties Manukau'])
for key in sorted(a_dict):
    print(key, a_dict[key])