from bintreeMod import Bintree
from linkedQFile import LinkedQ

import string


def readFiles(svenska):
    with open("/Users/Axel Rooth/Desktop/KTH/Data/Tillda/Lab4/word3.txt", "r", encoding = "utf-8") as svenskfil:
            for rad in svenskfil:
                ordet = rad.strip() 
                svenska.put(ordet)


def userinput():
    userfirst = input("Vad är ditt startord?: ")
    userlast = input("Vad är ditt slutord?: ")
    return userfirst, userlast

def makechildren(q, nod, last_word, svenska, gamla):

    gamla.put(nod)
    word_list = list(nod)
    alphabet = 
    l = ["å", "ä" ,"ö"]
    
    for i in range(0,3): alphabet.append(l[i])
    
    index = 0
    word_listcopy = word_list
    for letter in word_list:
        for j in alphabet:
            word_list.remove(letter)
            word_list.insert(index, j)
            word = ""
            for i in word_list: 
                word += i
            if word in svenska:
                if word not in gamla:
                    q.enqueue(word)
                    gamla.put(word)
                    if word == last_word:
                        return word
                        
            word_list = list(nod)
        index += 1
        

if __name__ == "__main__":

    q = LinkedQ()
    svenska = Bintree()
    gamla = Bintree()

    readFiles(svenska)
    first_word, last_word = userinput()

    q.enqueue(first_word)
    foundchain = None
    while not q.isEmpty():
        nod = q.dequeue()
        foundchain = makechildren(q, nod, last_word, svenska, gamla)
        if foundchain != None:
            break
    
    if foundchain == None:
        print("Det finns inte en väg till ", last_word)
    else:
        print("Det finns en väg till ", last_word)
        
