class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Hashtable:
    def __init__(self, n):
        self.hashlist = [None]*2*n

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
        found = False
        stop = False
        if self.hashlist[startslot].data.artist == key:
            return self.hashlist[startslot]
        else:
            while not found and self.hashlist[startslot] != None:
                self.hashlist[startslot] = self.hashlist[startslot].next 
                if self.hashlist[startslot].data.artist == key:
                    return self.hashlist[startslot]

    def __contains__(self, key):
        pass    

    def hashfunction(self, key, size):
        sum_of_string = 0
        for letter in key:
            sum_of_string = sum_of_string*32 + ord(letter)
        hashvalue = sum_of_string % size
        
        return hashvalue
