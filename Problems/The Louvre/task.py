class Painting:
    def __init__(self):
        self.title = input()
        self.artist = input()
        self.year = input()
        print(f'"{self.title}" by {self.artist} ({self.year}) hangs in the Louvre.')

painting = Painting()
