class Song:
    # Class attributes for global tracking
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Set instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update total song count
        Song.count += 1

        # Track unique artists
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

        # Track unique genres
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

        # Update per-genre counts
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

        # Update per-artist counts
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1

    @classmethod
    def get_total_songs(cls):
        return cls.count

    @classmethod
    def get_artists(cls):
        return cls.artists

    @classmethod
    def get_genres(cls):
        return cls.genres

    @classmethod
    def get_genre_count(cls):
        return cls.genre_count

    @classmethod
    def get_artist_count(cls):
        return cls.artist_count
