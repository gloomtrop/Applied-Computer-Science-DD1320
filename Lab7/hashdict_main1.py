from pokemonClass import Pokemon
from dicthashClass import DictHash



def readfiles(hashlist):
    
    with open("/Users/Axel Rooth/Desktop/KTH/Data/Tillda/Lab7/pokemon.txt", "r", encoding="utf8") as pokemonfile:
        i = 0
        for rad in pokemonfile:
            if i == 0:
                pass
            else:
                L = rad.split(",")

                hashlist.store(L[1].lower(), Pokemon(L[1].lower(),L[2],L[3],L[4],L[5],L[6],L[7],L[8],L[9],L[10],L[11],L[12].strip("\n")))
            i += 1

if __name__ == "__main__":
    hashlist = DictHash()
    readfiles(hashlist)

    user_input = input("Vilken pokemon letar du efter? ").lower()

    x = hashlist.search(user_input)
    

