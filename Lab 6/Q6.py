def bubble_single_pass(songs_list, index):
    for i in range(1, index + 1):
        if songs_list[i - 1][2] > songs_list[i][2]:
            temp = songs_list[i]
            songs_list[i] = songs_list[i - 1]
            songs_list[i - 1] = temp
    return

tuples = [('See You Again', 'Wiz Khalifa', 229), ('We Own It', 'Wiz Khalifa', 227), ('Something New', 'Wiz Khalifa', 200)]
bubble_single_pass(tuples, 2)
print(tuples)

tuples = [('We Own It', 'Wiz Khalifa', 227), ('See You Again', 'Wiz Khalifa', 229), ('Something New', 'Wiz Khalifa', 200), ('Find U Again', 'Mark Ronson', 176), ('Gangnam Style', 'PSY', 219), ('New Face', 'PSY', 190), ('Uptown Funk', 'Mark Ronson', 270)]
bubble_single_pass(tuples, 3)
print(tuples)