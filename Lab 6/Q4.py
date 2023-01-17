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
    return

def my_selection_sort(songs_list):
    for i in range(len(songs_list) - 1, 0, -1):
        selection_single_pass(songs_list, i)
    return

tuples = [('See You Again', 'Wiz Khalifa', 229), ('We Own It', 'Wiz Khalifa', 227), ('Something New', 'Wiz Khalifa', 200)]
my_selection_sort(tuples)
print(tuples)