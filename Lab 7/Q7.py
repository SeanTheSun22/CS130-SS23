def linear_search_sorted(songs_list, target_song):
    comparisons_count = 0
    for item in songs_list:
        comparisons_count += 1
        if item[0] == target_song:
            return (True, comparisons_count)
        elif item[0] > target_song:
            return (False, comparisons_count)
    return (False, comparisons_count)

data = [('Find U Again', 'Mark Ronson', 176), ('Gangnam Style', 'PSY', 219), ('New Face', 'PSY', 190), ('Nothing Breaks Like a Heart', 'Mark Ronson', 217), ('Something New', 'Wiz Khalifa', 200), ('Sugar', 'Maroon 5', 235), ('We Own It', 'Wiz Khalifa', 227)]
result = linear_search_sorted(data, 'New Face')
print(result)

data = data = [('Find U Again', 'Mark Ronson', 176), ('Gangnam Style', 'PSY', 219), ('New Face', 'PSY', 190), ('Nothing Breaks Like a Heart', 'Mark Ronson', 217), ('Something New', 'Wiz Khalifa', 200)]
result = linear_search_sorted(data, 'Electricity')
print(result)

food = [('Find U Again', 'Mark Ronson', 176), ('Gangnam Style', 'PSY', 219), ('New Face', 'PSY', 190), ('Nothing Breaks Like a Heart', 'Mark Ronson', 217), ('Something New', 'Wiz Khalifa', 200), ('Sugar', 'Maroon 5', 235), ('We Own It', 'Wiz Khalifa', 227)]
result = linear_search_sorted(data, 'Standing in the Rain')
print(result)