
import operator
import sys
import time

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

class WordQ:
    
    def __init__(self):
        self._first = None
        self._last = None
        
    def isEmpty(self):
        return self._first == None
    
    def enqueue(self, item):
        
        new_node = Node(item)
        if not self._first:
            self._first = new_node
        else:
            self._last.next = new_node
        self._last = new_node
    
    def size(self):
        current = self._first
        count = 0
        while current != None:
            count = count + 1
            current = current.next

        return count
    
    def peek(self):
        current = self._first
        if self._first == None:
            next_string = None
        else:
            next_string = current.data
        return next_string

    def look(self):
        current = self._first.next
        return current
    
    def dequeue(self):
        val = self._first.data
        self._first = self._first.next
        return val
    
    def __str__(self):
        return self._last.data


def readExpression(q, layer, structures, count):
    if q.peek() == "[":
        layer += 1
        x = q.dequeue()
        structures, count = readExpression(q, layer, structures, count)
        x = q.dequeue()
        structures, count = readExpression(q, layer,structures, count)
        x = q.dequeue()
        layer -= 1
    elif q.peek().isdigit():
        structures, count = readWeight(q, layer, structures, count)

    return structures, count
   
def readWeight(q, layer, structures, count):
    count += 1
    number = q.dequeue()
    num_string = str(number)
    while True:
        if not q.peek().isdigit():
            break
        number = q.dequeue()
        num_string = num_string + number
    structures = append2dict(num_string,layer, structures)
             
    return structures, count

def append2dict(num_string, layer, structures_d):
    
    matches = 0
    totweight = int(num_string)*2**(layer)

    if not structures_d:
        structures_d[str(totweight)] = 1
    else:
        
        if str(totweight) in structures_d:
            structures_d[str(totweight)] += 1
        else:
            structures_d[str(totweight)] = 1
    return structures_d
 

def storeSequence(sequence):
    q = WordQ()
    for letter in sequence:
        q.enqueue(letter)
    q.enqueue(".")
    return q

def appendQ(q):
    par = ""
    while q.peek() != ".":
        x = q.dequeue()
        par+= x + " "
    return par


def main():
    s = """3
[[3,7],6]
40
[[2,3],[4,5]]

"""

    rows  = s.split("\n")
    j = 0
    for row in sys.stdin:
        layer = 0
        if j == 0:
            j+= 1
            continue
        if row == "":
            continue
        count = 0
        structures = {}
        s = WordQ()
        q = storeSequence(row)
        structures, count = readExpression(q,layer,structures, count)
        max_matches = max(structures.items(), key=operator.itemgetter(1))[0]
        print(count -  structures[max_matches])
main()
