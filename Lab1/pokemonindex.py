import random

class Pokemon:

    def __init__(self, namn, typ1, typ2, total, hp, attack, defense, spAtk, spDef, speed, generation, legendary):
        self.namn = namn
        self.typ1 = typ1
        self.typ2 = typ2
        self.total = total
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.spAtk = spAtk
        self.spDef = spDef
        self.speed = speed
        self.generation = generation
        self.legendary = legendary

    def attackDmg(self):
        return self.attack + random.randint(0,1)*self.spAtk
    
    def health(self, attack_by_enemy):
        return self.hp - attack_by_enemy + random.randint(0,1)*self.defense

    def __str__(self):
        return ("Din pokemon heter " + self.namn.title() + " och har dessa attributer\n" +
            "Typ1: " + self.typ1 + "\n" +
            "Typ2: " + self.typ2 + "\n" +
            "Total: " + self.total + "\n" +
            "HP: " + self.hp + "\n" +
            "Attack: " + self.attack + "\n" +
            "Defense: " + self.defense + "\n" +
            "Sp. Atk: " + self.spAtk + "\n" + 
            "Sp. Def: " + self.spDef + "\n" +
            "Speed: " + self.speed + "\n" +
            "Generation: " + self.generation + "\n"
            "Legendary: " + self.legendary)


def readFiles():

    pokemonList = list()
    fil = open("/Users/Axel Rooth/Desktop/KTH/Data/Tillda/Lab1/pokemon.txt", "r") 
    textFile = fil.readlines()
    fil.close()
    for line in textFile:
        pokL = line.split(",")
        pokemonList.append(
            Pokemon(pokL[1].lower(), pokL[2], pokL[3], pokL[4], pokL[5], pokL[6], pokL[7], pokL[8], pokL[9], pokL[10], pokL[11], pokL[12])
            )    
    
    return pokemonList

def search(pokemonList, user_search):
    pos = 0
    found = False

    while pos< len(pokemonList) and not found:
        if pokemonList[pos].namn == user_search:
            found = True
            print((pokemonList[pos]))
        else:
            pos += 1


def main():
    pokemonList = readFiles()
    del pokemonList[0]
    
    user_search = input("What pokemon do you want to search for? ").lower()
    search(pokemonList, user_search)
    
    #Hej
main()



