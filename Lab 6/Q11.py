def my_insertion_sort(songs_list):
    for index in range(1, len(songs_list)):
        temp = songs_list[index]
        index -= 1
        while (temp[2] < songs_list[index][2]) and (index >= 0):
            songs_list[index + 1] = songs_list[index]
            index -= 1
        songs_list[index + 1] = temp
    return

tuples = [('See You Again', 'Wiz Khalifa', 229), ('We Own It', 'Wiz Khalifa', 227), ('Something New', 'Wiz Khalifa', 200)]
my_insertion_sort(tuples)
print(tuples)