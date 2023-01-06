def get_sum_evens(filename):
    fid = open(filename, 'r')
    Line = fid.readline()
    List = []
    while Line:
        Numbers = Line.split()
        Sum = 0
        for i in Numbers:
            if int(i) % 2 == 0:
                Sum += int(i)
        List.append(Sum)
        Line = fid.readline()
    fid.close()
    return(List)

filename = "numbers0.txt"
print(get_sum_evens(filename))