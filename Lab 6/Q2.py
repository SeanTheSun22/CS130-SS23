def get_position_of_largest_duration(songs_list, index):
    max_index = 0
    for i in range(1, index + 1):
        if songs_list[max_index][2] < songs_list[i][2]:
            max_index = i
    return max_index


tuples = [('See You Again', 'Wiz Khalifa', 229), ('We Own It', 'Wiz Khalifa', 227), ('Something New', 'Wiz Khalifa', 200), ('Uptown Funk', 'Mark Ronson', 270), ('Find U Again', 'Mark Ronson', 176)]
print(get_position_of_largest_duration(tuples, 2))

tuples = [('See You Again', 'Wiz Khalifa', 229), ('We Own It', 'Wiz Khalifa', 227), ('Something New', 'Wiz Khalifa', 200), ('Uptown Funk', 'Mark Ronson', 270), ('Find U Again', 'Mark Ronson', 176)]
print(get_position_of_largest_duration(tuples , 4))

tuples = [('We Own It', 'Wiz Khalifa', 227), ('See You Again', 'Wiz Khalifa', 229), ('Something New', 'Wiz Khalifa', 200), ('Find U Again', 'Mark Ronson', 176), ('Gangnam Style', 'PSY', 219), ('New Face', 'PSY', 190), ('Uptown Funk', 'Mark Ronson', 270)]
print(get_position_of_largest_duration(tuples, 3))