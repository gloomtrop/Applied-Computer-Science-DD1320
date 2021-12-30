from bintreeMod import Bintree
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

def makechildren(first_word, svenska, gamla):

    gamla.put(first_word)
    print(gamla.size())
    word_list = list(first_word)
    alphabet = list(string.ascii_lowercase)
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
                    print(word)
                    gamla.put(word)
            word_list = list(first_word)
        index += 1


    print(gamla.size())
            




if __name__ == "__main__":


    svenska = Bintree()
    gamla = Bintree()

    readFiles(svenska)
    first_word, last_word = userinput()
    makechildren(first_word, svenska, gamla)


