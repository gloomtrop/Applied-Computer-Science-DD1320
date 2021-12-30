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
            "Legendary: " + str(self.legendary))
