class Song:
    def __init__(self, name = "", length = 0):
        self.song_name = name
        self.duration = length


song1 = Song('See You Again', 229)
print(song1.song_name, song1.duration)
song2 = Song('We Own It', 227)
print(song2.song_name, song2.duration)
print(type(song1))
print(song1 == song2)
song3 = Song()
print(song3.duration)