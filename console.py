import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository

# artist_repository.delete_all()

artist1 = Artist("Prince")
artist_repository.save(artist1)

pdb.set_trace()