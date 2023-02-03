def linear_search(songs_list, target_song):
    comparisons_count = 0
    for item in songs_list:
        comparisons_count += 1
        if item[0] == target_song:
            return (True, comparisons_count)
    return (False, comparisons_count)

tuples = [('Something New', 'Wiz Khalifa', 200), ('We Own It', 'Wiz Khalifa', 227), ('Uptown Funk', 'Mark Ronson', 270), ('See You Again', 'Wiz Khalifa', 229), ('Find U Again', 'Mark Ronson', 176)]
result = linear_search(tuples, 'See You Again')
print(result)

tuples = [('Something New', 'Wiz Khalifa', 200), ('We Own It', 'Wiz Khalifa', 227), ('Uptown Funk', 'Mark Ronson', 270), ('See You Again', 'Wiz Khalifa', 229), ('Find U Again', 'Mark Ronson', 176)]
result = linear_search(tuples, 'New Face')
print(result)
