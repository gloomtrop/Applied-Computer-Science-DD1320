
import operator

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



"""
On the first line one positive number: the number of testcases, at most 100. 
After that per testcase:
⟨expr⟩::=⟨weight⟩∣``[''⟨expr⟩``,''⟨expr⟩``]''

with ⟨weight⟩ a positive integer smaller than 109 indicating a 
weight and [⟨expr⟩,⟨expr⟩] indicating a rod with the two 
expressions at the ends of the rod. 
The total number of rods in the chain from a weight to the top 
of the mobile will be at most 16.

Sample Input 1:
3  #Number of testcases
[[3,7],6]
40
[[2,3],[4,5]]

Sample Output 1:
1
0
3
"""

# class Leave:
#     def __init__(self,value, level):
#         self.value = value
#         self.level = level'
#         self.count = 0

    
#The making of recursive algoritm, going in depth first


def readExpression(q, layer, levels, count):
    if q.peek() == "[":
        layer += 1
        x = q.dequeue()
        # print(x, end = " ") #"["
        levels, count = readExpression(q, layer, levels, count)
        x = q.dequeue()
        # print(x, end = " ") #","
        levels, count = readExpression(q, layer,levels, count)
        x = q.dequeue()
        # print(x, end = " ") #"]"
        layer -= 1
    elif q.peek().isdigit():
        levels, count = readWeight(q, layer, levels, count)
    
    # print(count)
    return levels, count
   

def readWeight(q, layer, levels, count):
    count += 1
    number = q.dequeue()
    num_string = str(number)
    # print(number, end = " ")
    while True:
        if not q.peek().isdigit():
            break
        number = q.dequeue()
        num_string = num_string + number
    levels = append2dict(num_string,layer, levels)
             
    return levels, count

def append2dict(num_string, layer, levels_d):
    

    if str(layer) in levels_d:
        pass
    else:
        levels_d[str(layer)] = {}

    if num_string in levels_d[str(layer)]:
        levels_d[str(layer)][num_string] += 1
    else:
        levels_d[str(layer)][num_string] = 1
    
    return levels_d

def checkMatch(levels_d):

    pass

def addMatches(levels_d):

    matches = {}
    # for i in range(16):
    #     matches[str(i)] = {}
    
    # for nivå, inre_dict in levels_d.items(): #Går igenom varje nivå 
    #     if not inre_dict:
    #         continue
    #     # print(inre_dict)
    #     for nyckel,leaf_count in levels_d[nivå].items(): #Går igenom varje startlöf för nivån att undersöka samband
    #         match_count = 0
    #         # print(inre_dict)
    #         # print(nyckel)
    #         # print(nyckel, end = " ")
    #         # print(leaf_count)

    #         for key, value in levels_d.items(): #Checking with every node if the values correlate with node
                
    #             if not value:
    #                 continue
    #             # print(value)
    #             leveldiff = int(key)-int(nivå)
    #             # print(leveldiff)
    #             if leveldiff != 0:
    #                 if int(max(value.items(), key=operator.itemgetter(1))[0]) < int(nyckel)*2**(leveldiff):
    #                     continue
    #             # max(nivåinre_dict.items(), key=operator.itemgetter(1))[0]
    #             for node, count in levels_d[key].items():
    #                 if node is nyckel:
    #                     pass
    #                     # print("Same", node)
    #                 else:
    #                     leveldiff = int(key)-int(nivå)
    #                     if leveldiff < 0:
    #                         if 2**abs(leveldiff) == (int(node)/int(nyckel)):
    #                             match_count += count*leaf_count
    #                     elif leveldiff> 0:
    #                         if 2**abs(leveldiff) == (int(nyckel)/int(node)):
    #                             match_count += count*leaf_count
    #                     else:
    #                         pass
    #         matches[nivå][nyckel] = match_count
    #         # print(match_count)  
    # print(matches)  
    return matches 

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
        # print(x, end = " ")
        par+= x + " "
    return par

def makeTree(seq):
    levels = dict()
    for i in range(1,12):
        levels[str(i)] = []
    layer = 0
    i = 0
    while True:
        # print(seq[i], end = " ")
        if seq[i] == "[":
            layer += 1
            if seq[i+1].isnumeric():
                levels[layer] = seq[i+1]
                i+=1
                # print(i)
                if seq[i+2].isnumeric():
                    levels[layer] = levels[layer],seq[i+2]  
                    i+= 2      
      
        elif seq[i] == "]":
            # print(seq[i])
            layer -= 1
            if i != len(seq)-1:
                # print("Hej" + seq[i+1])
                if seq[i+2].isnumeric():
                    levels[layer] = seq[i+2]
                    i+=2
        
        # print(layer)
        i += 1
        if len(seq) == i:
            break
    return levels

def main():
    s = """3
[[3,7],6]
40
[[2,3],[4,5]]

"""

    rows  = s.split("\n")
    j = 0
    for row in rows:

        if j == 0:
            j+= 1
            continue
        if row == "":
            continue
        count = 0
        # tree = makeTree(seq)
        # print(tree)
        layer = 0
        levels = {}
        # for i in range(16):
        #     levels[str(i)] = {}
        s = WordQ()
        # n = WordQ()
        q = storeSequence(row)
        levels, count = readExpression(q,layer,levels, count)
        matches = addMatches(levels)
        # print("\n")
        # print(levels)
        max_matches = 0
        for nivå, nivåinre_dict in matches.items():
            if not nivåinre_dict:
                continue
            maxinre_dict = max(nivåinre_dict.items(), key=operator.itemgetter(1))[0]
            if int(nivåinre_dict[maxinre_dict])> max_matches:
                max_matches = int(nivåinre_dict[maxinre_dict])
            # print(max(nivåinre_dict.items(), key=operator.itemgetter(1))[0])
            
        print(count - 1 - max_matches)


        # max_matches = 0
        #     for matchnode in matches:
        #         if matchnode.matches >= max_matches:
        #             max_matches = matchnode.matches

        #     print(b.leavecount-1-max_matches)
    # s.enqueue(".")
    # n.enqueue(".")
    # # print(s.overflow())
    # s_par = appendQ(s)
    # n_par = appendQ(n)
    # print("\n")
    # print(s_par)
    # print(n_par)

    # b = Bintree()
    # b.put("[]")
    # b.put("3")

    # b.put(3)
    # b.put(4)
    # b.put(5)
    # b.write()
   
    

main()