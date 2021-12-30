class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Hashtable:
    def __init__(self):
        self.hashlist = [None]*2*719

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.hashlist))
        if self.hashlist[hashvalue] == None:
            node = Node(data)
            self.hashlist[hashvalue] = node
        else:
            hashnode = self.hashlist[hashvalue]
            while hashnode.next != None:
                hashnode = hashnode.next
            node = Node(data)
            hashnode.next = node

    def get(self, key):
        startslot = self.hashfunction(key, len(self.hashlist))
        pokemon = self.hashlist[startslot]
        
        if pokemon != None:
            found = False
            stop = False
            if pokemon.data.namn == key:
                return pokemon
            else:
                while not found and pokemon != None:
                    pokemon = pokemon.next 
                    if pokemon.data.namn == key:
                        return pokemon
        else:
            raise Exception("Denna pokemon existerar inte")

    # def __contains__(self, key):
    #     return exists(key)

    def hashfunction(self, key, size):
        sum_of_string = 0
        for letter in key:
            sum_of_string = sum_of_string*32 + ord(letter)
        hashvalue = sum_of_string % size
        
        return hashvalue

    def exists(key):
        if self.hashlist[key] == None:
            return False
        else:
            return True
