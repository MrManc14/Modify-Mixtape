class MixtapeModifier():

    def __init__(self, mixtape, changes):
        self.mixtape = mixtape
        self.changes = changes


    def apply_changes(self):
	for key, value in self.changes.items():
            if key == 'add':
                self.add_to_mixtape(value)
	    elif key == 'delete':
		self.delete_from_mixtape(value)
	    elif key == 'update':
		self.update_mixtape(value)


    def add_to_mixtape(self, changes):
        for change in changes:
	    if change.get('playlist'):
		playlist = change.get('playlist')
		user_id = playlist.get('user_id')
		if user_id:
		    song_ids = playlist.get('song_ids', [])
		    new_playlist = {"id": "4", "user_id": user_id, "song_ids": song_ids}
		    new_playlists = self.mixtape['playlists']
		    new_playlists.append(new_playlist)
		    self.mixtape['playlists'] = new_playlists


    def delete_from_mixtape(self, changes):
	for change in changes:
	    if change.get('playlist'):
	        playlist = change.get('playlist')
		id = playlist.get('id')
		if id:
		    self.mixtape['playlists'].pop(int(id)-1)


    def update_mixtape(self, changes):
	for change in changes:
            if change.get('playlist'):
                playlist = change.get('playlist')
                id = playlist.get('id')
                if id:
		    if playlist.get('add'):
			song_ids = playlist['add'].get('song_ids', [])
			for song in song_ids:
                            self.mixtape['playlists'][int(id)-1]['song_ids'].append(song)

    def get_mixtape(self):
        return self.mixtape
