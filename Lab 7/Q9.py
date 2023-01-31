def binary_search(sorted_list_of_songs, target_song):
    left = 0
    right = len(sorted_list_of_songs) - 1
    mid = (left + right) // 2
    mid_calculations = 1
    while sorted_list_of_songs[mid][0] != target_song and left <= right:
        print(f"left: {left}, right: {right}, mid: {mid}")
        if sorted_list_of_songs[mid][0] < target_song:
            left = mid + 1
        else:
            right = mid - 1
        mid_calculations += 1
        mid = (left + right) // 2
    if sorted_list_of_songs[mid][0] == target_song:
        print(f"left: {left}, right: {right}, mid: {mid}")
        return (mid, mid_calculations)
    return (-1, mid_calculations - 1)

food = [('Find U Again', 'Mark Ronson', 176), ('Gangnam Style', 'PSY', 219), ('New Face', 'PSY', 190), ('Nothing Breaks Like a Heart', 'Mark Ronson', 217), ('Something New', 'Wiz Khalifa', 200)]
print(binary_search(food, 'Gangnam Style'))

food = [('Find U Again', 'Mark Ronson', 176), ('Gangnam Style', 'PSY', 219), ('New Face', 'PSY', 190), ('Nothing Breaks Like a Heart', 'Mark Ronson', 217), ('Something New', 'Wiz Khalifa', 200), ('Sugar', 'Maroon 5', 235), ('We Own It', 'Wiz Khalifa', 227)]
print(binary_search(food, 'Electricity'))

food = [('Find U Again', 'Mark Ronson', 176), ('Gangnam Style', 'PSY', 219), ('New Face', 'PSY', 190), ('Nothing Breaks Like a Heart', 'Mark Ronson', 217), ('Something New', 'Wiz Khalifa', 200), ('Sugar', 'Maroon 5', 235), ('We Own It', 'Wiz Khalifa', 227)]
print(binary_search(food, 'Sugar'))