from bintree import Bintree
from linkedQFile import LinkedQ

import string

class Parentnode:
    def __init__(self, word, parent = None ):
        self.word = word
        self.parent = parent


def makechildren(q, ordet):

    gamla.put(ordet.word)
    # print(gamla.size())
    word_list = list(ordet.word)
    wordet = ordet.word
    alphabet = list(string.ascii_lowercase)
    l = ["å", "ä" ,"ö"]

    for i in range(0,3): alphabet.append(l[i])

    index = 0
    for letter_index in range(0, len(word_list)):     
        for j in alphabet: 
            test_ord =  wordet[:letter_index]+j+wordet[letter_index+1:]   
            if test_ord in svenska and test_ord not in gamla:
                nod = Parentnode(test_ord, ordet)
                q.enqueue(nod)
                gamla.put(test_ord)     
         
        index += 1


def writechain(endnode):
    if endnode.parent != None:
        writechain(endnode.parent)
        print(endnode.word)
    else:
        print(endnode.word)



if __name__ == "__main__":

    q = LinkedQ()
    svenska = Bintree()
    gamla = Bintree()

    with open("/Users/Axel Rooth/Desktop/KTH/Data/Tillda/Lab5/word3.txt", "r", encoding = "utf-8") as svenskfil:
            for rad in svenskfil:
                ordet = rad.strip() 
                if ordet in svenska:
                    pass
                else:
                    svenska.put(ordet)

    first_word = input("Vad är ditt startord?: ")
    last_word = input("Vad är ditt slutord?: ")

    parent = Parentnode(first_word)
    makechildren(q, parent)

    while not q.isEmpty():
        ordet = q.dequeue()
        makechildren(q, ordet)
        if ordet.word == last_word:
            writechain(ordet)
            print("Det finns en väg till ", last_word)
            break
        elif ordet.word != last_word and q.isEmpty():
            print("Det finns inte en väg till", last_word)
            

            
    
    
        
