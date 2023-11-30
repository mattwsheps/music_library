from lib.album import Album

class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        """
        Selecting all records.

        Executes the SQL query:
        SELECT * FROM albums;

        Arguments: None
        Returns: an array of Album objects
        """
        rows = self._connection.execute('SELECT * FROM albums')
        albums = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums
    
    def find(self, album_id):
        """
        Find a single album by its id.

        Executes the SQL query:
        SELECT title FROM albums WHERE id = album_id;

        Arguments: album_id
        Returns: an Album object
        """
        rows = self._connection.execute(
            'SELECT * FROM albums WHERE id = %s', [album_id])
        row = rows[0]
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])
    
    def create(self, album):
        """
        Add a single album to albums

        Executes the SQL query:
        INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s);

        Arguments: album
        Returns None
        """
        rows = self._connection.execute(
            'INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)',
            [album.title, album.release_year, album.artist_id]
        )
        return None
    
    def delete(self, album_id):
        """
        Deletes a single album from albums

        Executes the SQL query:
        DELETE FROM albums WHERE id = %s;

        Arguments: album_id
        Returns: None
        """
        rows = self._connection.execute(
            'DELETE FROM albums WHERE id = %s',
            [album_id]
        )
        return None