
class Song:
    def __init__(self,trackid, songtime, artist, songtitle):
        self.trackid = trackid
        self.songtime = songtime
        self.artist = artist
        self.songtitle = songtitle

    def __lt__(self, other):
        return self.artist < other.artist
       


