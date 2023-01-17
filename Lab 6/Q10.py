def insertion_single_pass(songs_list, index):
    temp = songs_list[index]
    index -= 1
    while (temp[2] < songs_list[index][2]) and (index >= 0):
        songs_list[index + 1] = songs_list[index]
        index -= 1
    songs_list[index + 1] = temp
    return

tuples = [('Something New', 'Wiz Khalifa', 200), ('See You Again', 'Wiz Khalifa', 229), ('Uptown Funk', 'Mark Ronson', 270), ('We Own It', 'Wiz Khalifa', 227), ('Find U Again', 'Mark Ronson', 176)]
insertion_single_pass(tuples, 3)
print(tuples)

tuples =  [('Something New', 'Wiz Khalifa', 200), ('We Own It', 'Wiz Khalifa', 227), ('See You Again', 'Wiz Khalifa', 229), ('Find U Again', 'Mark Ronson', 176), ('Gangnam Style', 'PSY', 219), ('New Face', 'PSY', 190), ('Uptown Funk', 'Mark Ronson', 270)]
insertion_single_pass(tuples, 3)
print(tuples)