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

    def get_total_duration(self):
        return sum(i.duration for i in self.songs)
    
    def __str__(self):
        if self.songs == []:
            return f"{self.get_full_name()} has not performed any songs yet."
        return f"{self.get_full_name()} has performed the following songs:\n" + "\n".join(f"{song}" for song in self.songs)

artist1 = Artist('Wiz', 'Khalifa')
print(artist1)
artist1.add_song('See You Again', 229)
print(artist1)
print(artist1.get_total_duration())

artist = Artist('Wiz', 'Khalifa')
artist.add_song('See You Again', 229)
artist.add_song('We Own It', 227)
artist.add_song('Something New', 200)
print(artist)
print(artist.get_total_duration())