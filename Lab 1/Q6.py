def read_english_maori_info(filename):
    fid = open(filename, 'r')
    Dump = fid.read().split("\n")
    List = []
    for i in Dump:
        English = ""
        Maori = ""
        j = 0
        while i[j] != " ":
            Maori = Maori + i[j]
            j += 1
        j += 2
        while i[j] != ")":
            English = English + i[j]
            j += 1
        List = List + [(English, Maori)]
    fid.close()
    return List

print(read_english_maori_info('words_list3.txt'))
