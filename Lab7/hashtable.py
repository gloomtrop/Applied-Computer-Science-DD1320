class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Hashtable:
    def __init__(self, n):
        self.hashlist = [None]*2*n

    def store(self, key, data):
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

    def search(self, key):
        startslot = self.hashfunction(key, len(self.hashlist))
        atom = self.hashlist[startslot]
        if atom != None:
            found = False
            stop = False
            if atom.data.namn == key:
                return atom.data
            else:
                while not found and atom != None:
                    atom = atom.next 
                    if atom.data.namn == key:
                        return atom.data
        else:
            raise KeyError()

    def __contains__(self, key):
        if self.hashlist:
            return True
        else:
            return False

    def hashfunction(self, key, size):
        sum_of_string = 0
        for letter in key:
            sum_of_string = sum_of_string*32 + ord(letter)
        hashvalue = sum_of_string % size
        
        return hashvalue

    def exists(startslot):
        if self.hashlist[startslot] == None:
            return False
        else:
            return True
