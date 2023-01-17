def create_artist_dictionary(songs_list):
    artist_dictionary = {}
    for data in songs_list:
        artist = data[1]
        song_name = data[0]
        if artist not in artist_dictionary:
            artist_dictionary[artist]= [song_name]
        else:
            artist_dictionary[artist].append(song_name)
    for key, value in artist_dictionary.items():
        artist_dictionary[key] = sorted(value)
    return artist_dictionary


songs = [('See You Again', 'Wiz Khalifa'), ('We Own It', 'Wiz Khalifa'), ('Gangnam Style', 'PSY'), ('New Face', 'PSY'), ('Gentleman', 'PSY')]
a_dict = create_artist_dictionary(songs )
for key in sorted(a_dict.keys()):
    print(key, a_dict[key])

print()

songs =[('Sugar', 'Maroon 5'), ('Memories', 'Maroon 5')]
a_dict = create_artist_dictionary(songs )
for key in sorted(a_dict.keys()):
    print(key, a_dict[key])