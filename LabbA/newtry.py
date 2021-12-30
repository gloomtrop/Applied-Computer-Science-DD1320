
import operator
import sys
import time

def readExpression(q, layer, structures, count):
    if q[0] == "[":
        layer += 1
        x = q.pop(0)
        structures, count = readExpression(q, layer, structures, count)
        x = q.pop(0)
        structures, count = readExpression(q, layer,structures, count)
        x = q.pop(0)
        layer -= 1
    elif q[0].isdigit():
        structures, count = readWeight(q, layer, structures, count)

    return structures, count
   
def readWeight(q, layer, structures, count):
    count += 1
    number = q.pop(0)
    num_string = str(number)
    while True:
        if not q[0].isdigit():
            break
        number = q.pop(0)
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
 


start = time.time()

def main():
    s = """3
[[3,7],6]
40
[[2,3],[4,5]]

"""

    rows  = s.split("\n")
    j = 0
    for row in rows:
        layer = 0
        if j == 0:
            j+= 1
            continue
        if row == "":
            continue
        if not row[0].isdigit():
            count = 0
            structures = {}
            # s = WordQ()
            # q = storeSequence(row)
            
            structures, count = readExpression(list(row),layer,structures, count)
            max_matches = max(structures.items(), key=operator.itemgetter(1))[0]
            print(count -  structures[max_matches])
        else:
            print(0)
main()
end = time.time()
print(end - start)