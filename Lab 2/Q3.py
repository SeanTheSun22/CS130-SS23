def read_covid_data(filename):
    fid = open(filename, "r")
    contents = fid.read().split("\n")
    fid.close()
    return [(data.split(",")[0], int(data.split(",")[1])) for data in contents]


data = read_covid_data("12_01.txt")
print(data)
print(type(data))
print(type(data[0][0]), type(data[0][1]))

print()

print(read_covid_data("12_04.txt"))