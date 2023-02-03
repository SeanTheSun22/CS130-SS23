class Song:
    def __init__(self, name = "", length = 0):
        self.song_name = name
        self.duration = length

    def set_duration(self, value):
        if value > 0:
            self.duration = value
    
    def __str__(self):
        return f"{self.song_name}({self.duration} seconds)"

song1 = Song('See You Again', 229)
print(song1.song_name, song1.duration)
song1.set_duration(-1)
print(song1.song_name, song1.duration)
song1.set_duration(190)
print(song1)
song3 = Song("Something New")
print(song3)
song3.set_duration(-100)
print(song3)
song3.set_duration(200)
print(song3)