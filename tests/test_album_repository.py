from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When we call AlbumRepository#all
We get a list of Album objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection) # Create a new ArtistRepository

    albums = repository.all() # Get all artists

    # Assert on the results
    assert len(albums) == 12
    assert albums == [
        Album(1, "Doolittle", 1989, 1),
        Album(2, "Surfer Rosa", 1988, 1),
        Album(3, "Waterloo", 1974, 2),
        Album(4, "Super Trouper", 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2)
    ]

"""
When we call AlbumRepository#find
We get a single Album object reflecting the seed data.
"""
def test_get_single_album(db_connection):
    db_connection.seed('seeds/music_library.sql')
    repo = AlbumRepository(db_connection)

    album = repo.find(3)

    assert album == Album(3, 'Waterloo', 1974, 2)

"""
When we call AlbumRepository#create
We get a new album in the database.
"""
def test_album_create(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repo = AlbumRepository(db_connection)
    album = Album(None, 'Arrival', 1976, 2)
    repo.create(album)
    assert repo.all() == [
            Album(1, "Doolittle", 1989, 1),
            Album(2, "Surfer Rosa", 1988, 1),
            Album(3, "Waterloo", 1974, 2),
            Album(4, "Super Trouper", 1980, 2),
            Album(5, 'Bossanova', 1990, 1),
            Album(6, 'Lover', 2019, 3),
            Album(7, 'Folklore', 2020, 3),
            Album(8, 'I Put a Spell on You', 1965, 4),
            Album(9, 'Baltimore', 1978, 4),
            Album(10, 'Here Comes the Sun', 1971, 4),
            Album(11, 'Fodder on My Wings', 1982, 4),
            Album(12, 'Ring Ring', 1973, 2),
            Album(13, 'Arrival', 1976, 2)
        ]

"""
When we call AlbumRepository#delete
We remove an album from the database.
"""
def test_album_delete(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repo = AlbumRepository(db_connection)
    repo.delete(4)
    assert repo.all() == [
            Album(1, "Doolittle", 1989, 1),
            Album(2, "Surfer Rosa", 1988, 1),
            Album(3, "Waterloo", 1974, 2),
            Album(5, 'Bossanova', 1990, 1),
            Album(6, 'Lover', 2019, 3),
            Album(7, 'Folklore', 2020, 3),
            Album(8, 'I Put a Spell on You', 1965, 4),
            Album(9, 'Baltimore', 1978, 4),
            Album(10, 'Here Comes the Sun', 1971, 4),
            Album(11, 'Fodder on My Wings', 1982, 4),
            Album(12, 'Ring Ring', 1973, 2),
        ]
