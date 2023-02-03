class Artist:
    def __init__(self, firstname, surname):
        self.first_name = firstname
        self.surname = surname
        self.songs = []

    def get_full_name(self):
        return f"{self.surname}, {self.first_name}"

    def add_song(self, name):
        self.songs.append(name)

    def __str__(self):
        if len(self.songs) == 0:
            return f"{self.get_full_name()} has not performed any songs yet."
        return f"{self.get_full_name()} has performed the following songs:\n" + "\n".join(self.songs)

artist1 = Artist('Wiz', 'Khalifa')
artist2 = Artist('Mark', 'Ronson')
artist1.add_song('See You Again')
artist1.add_song('We Own It')
artist1.add_song('Something New')
print(artist1)
print(artist2)