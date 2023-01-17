def get_position_of_largest_duration(songs_list, index):
    max_index = 0
    for i in range(1, index + 1):
        if songs_list[max_index][2] < songs_list[i][2]:
            max_index = i
    return max_index

def selection_single_pass(songs_list, index):
    swap_index = get_position_of_largest_duration(songs_list, index)
    temp = songs_list[index]
    songs_list[index] = songs_list[swap_index]
    songs_list[swap_index] = temp
    return songs_list

tuples = [('See You Again', 'Wiz Khalifa', 229), ('We Own It', 'Wiz Khalifa', 227), ('Something New', 'Wiz Khalifa', 200)]
selection_single_pass(tuples, 2)
print(tuples)

tuples = [('We Own It', 'Wiz Khalifa', 227), ('See You Again', 'Wiz Khalifa', 229), ('Something New', 'Wiz Khalifa', 200), ('Find U Again', 'Mark Ronson', 176), ('Gangnam Style', 'PSY', 219), ('New Face', 'PSY', 190), ('Uptown Funk', 'Mark Ronson', 270)]
selection_single_pass(tuples, 3)
print(tuples)