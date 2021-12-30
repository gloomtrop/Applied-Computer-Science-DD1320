from molgrafik import *

class Ruta:
    def __init__(self, atom="( )", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None
mol = Ruta(atom = "Cl", num = 2)
mol.next =Ruta(num = 2)
mol1 =mol.next
mol1.down = Ruta(atom = "A", num = 2)
mg = Molgrafik()
mg.show(mol)
