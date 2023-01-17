def bubble_single_pass(songs_list, index):
    for i in range(1, index + 1):
        if songs_list[i - 1][2] > songs_list[i][2]:
            temp = songs_list[i]
            songs_list[i] = songs_list[i - 1]
            songs_list[i - 1] = temp
    return

def my_bubble_sort(songs_list):
    for i in range(len(songs_list) - 1, 0, -1):
        bubble_single_pass(songs_list, i)
    return


tuples = [('See You Again', 'Wiz Khalifa', 229), ('We Own It', 'Wiz Khalifa', 227), ('Something New', 'Wiz Khalifa', 200)]
my_bubble_sort(tuples)
print(tuples)