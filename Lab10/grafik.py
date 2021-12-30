from molgrafik import *
import sys

class Ruta:
    def __init__(self, atom="( )", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None

class Node:

    def __init__(self, x, next = None):

        self.data = x
        self.next = next

class Wordstack:

    def __init__(self):
        self.first = None
    def enqueue(self, x):
        if self.first == None:
            new = Node(x)
            self.first = new
        else:
            new = Node(x)
            new.next = self.first
            self.first = new
    def dequeue(self):
        first = self.first
        self.first = self.first.next
        return first.data
    def isEmpty(self):
        if self.first == None:
            return True
        else:
            return False
    def peek(self):
        return self.first.data
    def overflow(self):
        print_list = []
        current = self.peek()
        while current.data != ".":
            print_list.append(current.data)
            current = current.next
            output_text = "".join(print_list)
        return output_text

class LwordQ:
    def __init__(self):
        self.first = None
        self.last = None
    def enqueue(self, x):
        if self.first == None:
            new = Node(x)
            self.first = new
            self.last = new
        else:
            new = Node(x)
            self.last.next = new
            self.last = new
    def dequeue(self):
        first = self.first
        self.first = self.first.next
        return first.data
    def isEmpty(self):
        if self.first == None:
            return True
        else:
            return False
    def peek(self):
        if self.first == None:
            return self.first
        else:
            return self.first.data
    def overflow(self):
        output_text = ""
        current = self.first
        if current.data != ".":
            output_text = " "
        while current.data != ".":
            output_text = output_text + current.data
            current = current.next
        return output_text
    def size(self):
        if self.first == None:
            leng = 0
        else: 
            current = self.first
            leng = 0
            while current != self.last:
                current = self.first.next
                leng = leng + 1
        return leng

class Syntaxfel(Exception):
    pass

def readFormula(q, atoms, p):               #<formel>::= <mol> \n
    formula = readMolecule(q, atoms, p, ruta = Ruta())     #returnerar hela formulfrekvens 
    # if mol.next != None and mol.down != None:
    #     mg = Molgrafik()
    #     mg.show(mol)                        #Visar hela formulan i med molgrafiken
    return formula

def readMolecule(q, atoms, p, ruta):  #<mol>   ::= <group> | <group><mol>
    if q.peek() == ".":
        if p.isEmpty():
            q.dequeue()
            return 
        else:
            raise Syntaxfel("Saknad högerparentes vid radslutet")
    formula = readGroup(q, atoms, p, ruta)        
    return formula
    
def readGroup(q, atoms, p, ruta = Ruta()):         #<group> ::= <atom> |<atom><num> | (<mol>) <num> 
    
    if q.peek() == "(":
        ruta.num = 4
        p.enqueue(q.dequeue())      #Tar bort ")" från kö och sätter den till först i stack
        ruta.down = readMolecule(q, atoms, p, ruta)   #Läser in molekyl om "(" är på g i kön  
    elif q.peek() == ")":           #Kollar om slutet på () är klar
        if p.isEmpty():
            raise Syntaxfel("Felaktig gruppstart vid radslutet" + q.overflow())
        else:
            if p.peek() == "(":
                q.dequeue()     
                p.dequeue()
                boolean, number = readNumber(q)     
                if boolean:       #Om nummer finns, läs in nästa molekylbindning
                    # ruta.num = int(number)
                    # ruta.down = readMolecule(q, atoms, p, ruta)
                    print("HEJ")
                else:
                    raise Syntaxfel("Saknad siffra vid radslutet" + q.overflow())
            else:
                raise Syntaxfel("Felaktig gruppstart vid radslutet" + q.overflow())
    else:
        ruta =  readAtom(q, atoms)
        ruta.next = readMolecule(q, atoms, p, ruta)

        return ruta

def readAtom(q, atoms):     #<atom>  ::= <LETTER> | <LETTER><letter>
    ruta = Ruta()
    atom_listed = list()
    atom_listed.append(readLETTER(q))
    atom_listed.extend(readletter(q))
    atom = "".join(atom_listed)
    if atom in atoms:
        ruta.atom = atom
        boolean, number = readNumber(q)
        if boolean:
            ruta.num = int(number)
        return ruta
    else:
        raise Syntaxfel("Okänd atom vid radslutet" + q.overflow())

def readLETTER(q):          #<LETTER>::= A | B | C | ... | Z
    letter = q.peek()
    if letter in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
        q.dequeue()
        return letter
    else:
        if letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            raise Syntaxfel("Saknad stor bokstav vid radslutet" + q.overflow())
        raise Syntaxfel("Felaktig gruppstart vid radslutet" + q.overflow())

def readletter(q):          #<letter>::= a | b | c | ... | z
    letter_list = list()
    if q.peek() in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
        letter_list.append(q.dequeue())
    return letter_list

def readNumber(q):          # <num>   ::= 2 | 3 | 4 | ...
    num = ""
    if q.peek().isdigit() == False:
        return False, None
    if q.peek() == "0":
        q.dequeue()
        raise Syntaxfel("För litet tal vid radslutet" + q.overflow())
    if q.peek()== "1":
        num += q.dequeue()
        if not q.peek().isdigit():
            raise Syntaxfel("För litet tal vid radslutet" + q.overflow())
    
    while q.peek().isdigit():
        num += q.dequeue()
    return True, num
     
def storeMolecule(molecule):        #Sparar molekylen i en länkad lista
    q = LwordQ()
    for letter in molecule:
        q.enqueue(letter)
    q.enqueue(".")
    return q

def checkStructure(molecule):      #Läser in formeln från användarinput
    stacker = Wordstack()
    q = storeMolecule(molecule)
    atoms = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg",
            "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr",
            "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr",
            "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd",
            "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
            "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf",
            "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po",
            "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm",
            "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh",
            "Hs", "Mt", "Ds", "Rg", "Cn", "Fl", "Lv"]
    try:
        formula = readFormula(q, atoms, stacker)
        mg = Molgrafik()
        mg.show(formula)
        return("Formeln är syntaktiskt korrekt")
    
    except Syntaxfel as fel:
        return str(fel)

def main():
    # while True:
    #     molecule = User()
    #     if molecule == "#":
    #         break

    molecule = input("Skriv in molekylformel: ") 
    # mg = Molgrafik()
    # mol = Ruta(atom = molecule)
    # mg.show(mol)
    result = checkStructure(molecule)
    print(result)

main()
