import math

def read_sum_of_squares(filename):
    try:
        fid = open(filename, 'r')
    except FileNotFoundError:
        print("ERROR: The file '", filename, "' does not exist.", sep = "")
        return 0
    data = fid.read().split()
    fid.close()

    sum = 0

    for value in data:
        try:
            if math.sqrt(float(value)).is_integer():
                sum += int(value)
        except:
            pass
            
    return sum

print(read_sum_of_squares("fie.txt"))
