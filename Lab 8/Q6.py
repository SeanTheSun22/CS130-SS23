class Artist:
    def __init__(self, firstname, surname):
        self.first_name = firstname
        self.surname = surname
        self.songs = []

    def get_full_name(self):
        return f"{self.surname}, {self.first_name}"

artist1 = Artist('Wiz', 'Khalifa')
print(artist1.first_name, artist1.surname)
print(artist1.get_full_name())
print(len(artist1.songs))
artist2 = Artist('Mark', 'Ronson')
print(artist2.first_name, artist2.surname, artist2.get_full_name())
print(len(artist2.songs))
print(type(artist1))
print(artist1 == artist2)