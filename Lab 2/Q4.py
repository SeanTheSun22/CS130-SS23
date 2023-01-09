def read_covid_data(filename):
    fid = open(filename, "r")
    contents = fid.read().split("\n")
    fid.close()
    return [(data.split(",")[0], int(data.split(",")[1])) for data in contents]


def build_covid_data(covid_dictionary, filenames):
    for filename in filenames:
        total_data = read_covid_data(filename)
        for data in total_data:
            if data[0] in covid_dictionary:
                covid_dictionary[data[0]] = covid_dictionary[data[0]] + data[1]


a_dict = {'Northland': 0, 'Waitemata': 0, 'Auckland': 0 }
build_covid_data(a_dict, ['12_01.txt'])
for key in sorted(a_dict):
    print(key, a_dict[key])

print()

a_dict = {'Northland': 0, 'Waitemata': 0, 'Auckland': 0, 'Counties Manukau': 0, 'Waikato': 0}
build_covid_data(a_dict, ['12_01.txt', '12_02.txt'])
for key in sorted(a_dict):
    print(key, a_dict[key])