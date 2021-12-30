from wordqueueClassL import Wordqueue
from molgrafik import *
from hashtest import *
from hashtable import *
# from bintree import Bintree
# ["`","~","!","@","#","$","%","^","&","*","(","_","-","+","=","{","[","}","}","|",":",";","'","<,,,>",".","?","/"]
import string
import sys

class Ruta:
    def __init__(self, atom="( )", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None

class Syntaxfel(Exception):
    pass

def readFormula(q): #<formel>::= <mol> \n
    ruta = Ruta()
    if q.peek() == ".":
        word = dequeuer(q)
        raise Syntaxfel("Felaktig gruppstart vid radslutet" + word)
    ruta = readMolecule(q, ruta)
    if q.peek() == ")":
        word = dequeuer(q)
        raise Syntaxfel("Felaktig gruppstart vid radslutet" + word)
    return ruta
    
def readMolecule(q, ruta): #<mol>   ::= <group> | <group><mol>
    ruta = readGroup(q, ruta)
    if q.peek() == "." and q.look() == None: 
        return ruta
    elif q.peek() != ")":
        ruta.next = Ruta()
        ruta.next = readMolecule(q, ruta.next)
        return ruta
    return ruta

def readGroup(q, ruta): #<group> ::= <atom> |<atom><num> | (<mol>) <num>    
    if q.peek() == "(":
        q.dequeue()
        ruta.down = Ruta()
        ruta.down = readMolecule(q, ruta.down)
        if q.peek() ==")":
            q.dequeue()
            if q.peek().isdigit():
                number = readNumber(q)
                ruta.num = int(number)
                return ruta
            else:
                word = dequeuer(q)
                raise Syntaxfel("Saknad siffra vid radslutet" + word)
        else:
            word = dequeuer(q)
            raise Syntaxfel("Saknad högerparentes vid radslutet" + word)
    elif q.peek() != ")" and q.peek().isalpha() :
        ruta = readAtom(q, ruta)
        if q.peek().isdigit():
            number = readNumber(q)
            ruta.num = int(number)
    else:
        word = dequeuer(q)
        raise Syntaxfel("Felaktig gruppstart vid radslutet" + word)
    
    return ruta
            
def readAtom(q, ruta): #<atom>  ::= <LETTER> | <LETTER><letter>   
    atoms = readfile()
    # print(atoms)
    letter = readLETTER(q)
    mol = letter + q.peek()
    if q.peek() in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
        readletter(q)
        letter = mol
        if letter not in atoms:
            word = dequeuer(q)
            raise Syntaxfel("Okänd atom vid radslutet" + word)
        ruta.atom = letter
        return ruta
    if q.peek() in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
        if letter not in atoms:
            word = dequeuer(q)
            raise Syntaxfel("Okänd atom vid radslutet" + word)
    if letter not in atoms and q.peek().isdigit():
        word = dequeuer(q)
        raise Syntaxfel("Okänd atom vid radslutet" + word)
    else:
        ruta.atom = letter
        return ruta

def readLETTER(q):
    letter = q.peek()
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if letter in alphabet:
        q.dequeue()
        return letter

    word = dequeuer(q)
    raise Syntaxfel("Saknad stor bokstav vid radslutet" + word)

def readletter(q):
    letter = q.dequeue()
    word = ""
    return

def readNumber(q):

    number = q.dequeue()
    num_string = number
    if int(number) < 1:
        word = dequeuer(q)
        raise Syntaxfel("För litet tal vid radslutet" + word)

    while True:
        if not q.peek().isdigit():
            break
        number = q.dequeue()
        num_string = num_string + number

    if int(num_string) > 1:
        return num_string
    
    word = dequeuer(q)
    raise Syntaxfel("För litet tal vid radslutet" + word)

def storeMolecule(formula):
    q = Wordqueue()
    formula = list(formula)
    for letter in formula:
        q.enqueue(letter)
    q.enqueue(".")
    return q

def checkStructure(formula):
    q = storeMolecule(formula)
    try:
        formula = readFormula(q)
        mg = Molgrafik()
        mg.show(formula)
        atomlista = skapaAtomlista()
        hashtabell = lagraHashtabell(atomlista)
        weight= calcWeight(formula, hashtabell)
        print("Molekylen väger " + str(weight))
        return "Formeln är syntaktiskt korrekt"
        
    except Syntaxfel as fel:
        return str(fel)

def calcWeight(formula, hashtabell):

    if formula:     #Om det finns en molekylformel
        if formula.down: #Vid parenteser kollas rutträdets down pekare, alltså grupp
            gvikt = float(calcWeight(formula.down, hashtabell))*float(formula.num)
            return gvikt + float(calcWeight(formula.next, hashtabell)) #Adderar ihop de rekursiva vikterna och returnerar
        else:       #Kollar nästa atom
            atom_obj = hashtabell.search(formula.atom)
            vikt = float(atom_obj.vikt) * float(formula.num)
            return vikt + float(calcWeight(formula.next, hashtabell))
    return 0

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def dequeuer(q):
    word = " "
    if q.peek() == "." and q.look() ==None:
        return ""
    if q.peek() == "." and q.look() ==".":
        for let in range(0, q.size()-1):
            word += q.dequeue()
        raise Syntaxfel("Felaktig gruppstart vid radslutet" + word) 
        

    for let in range(0, q.size()-1):
        word += q.dequeue() 
    return word

def readfile():
    atoms = list()
    
    with open("/Users/Axel Rooth/Desktop/KTH/Data/Tillda/Lab9/molekyler.txt", "r", encoding="utf8") as moleculefile:
        for rad in moleculefile:
            list_of_atoms = rad.split()
            for atom in list_of_atoms:
                atoms.append(atom.strip("\n"))
    
    return atoms

def main(): 
    formula = input("Skriv in din formula här: ")
    result = checkStructure(formula)
    print(result)
        
if __name__ == "__main__":
    main()