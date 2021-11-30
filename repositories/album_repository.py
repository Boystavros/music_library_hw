from db.run_sql import run_sql

from models.album import Album
import repositories.artist_repository as album_repository

# CREATE

def save(album):
    sql = "INSERT INTO albums (title, "