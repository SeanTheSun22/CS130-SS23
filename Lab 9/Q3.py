class Song:
    def __init__(self, name = "", length = 0):
        self.song_name = name
        self.duration = length

    def set_duration(self, value):
        if value > 0:
            self.duration = value
    
    def __str__(self):
        return f"{self.song_name}({self.duration} seconds)"


class Artist:
    def __init__(self, first = "", surname = ""):
        self.first_name = first
        self.surname = surname
        self.songs = []

    def get_full_name(self):
        return f"{self.surname}, {self.first_name}"

    def add_song(self, song_name, duration):
        self.songs.append(Song(song_name, duration))

artist1 = Artist('Wiz', 'Khalifa')
print(artist1.get_full_name())
print(len(artist1.songs))
print(type(artist1))
artist1.add_song('See You Again', 229)
print(type(artist1.songs[0]))
print(artist1.songs[0])

artist = Artist('Wiz', 'Khalifa')
artist.add_song('See You Again', 229)
artist.add_song('We Own It', 227)
artist.add_song('Something New', 200)
for song in artist.songs:
    print(song)