def read_locations(filename):
    fid = open(filename, "r")
    locations = fid.read().split("\n")
    fid.close()
    return locations


data = read_locations("locations.txt")
print(data)
print(type(data))