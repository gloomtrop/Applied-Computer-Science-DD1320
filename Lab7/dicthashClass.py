
class DictHash:
    def __init__(self):
        self.dicthash = dict()

    def store(self, key, data):
        self.dicthash = put(self.dicthash, key, data)

    def search(self, key):
        return find(self.dicthash, key)

    def __contains__(self, key):
        return exits(self.dicthash, key)

def put(hashlist, key, data):
    hashlist[key] = data
    return hashlist

def find(hashlist, key):
    if key in hashlist:
        return hashlist[key]
    else:
        raise Exception("Din pokemon finns inte i ditt pokedex")

def exits(hashlist, key):
    try:
        print(hashlist[key])
        return True
    except KeyError:
        return False
