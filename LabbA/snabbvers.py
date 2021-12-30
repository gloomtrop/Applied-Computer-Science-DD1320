import time
import sys
import operator


def readExpression(tree, layer, structures, count):
    while tree:
        if tree[0] in ("[,]"):
            if tree[0] == "[":
                layer += 1
            elif tree[0] == "]":
                layer -= 1
            tree.pop(0)
        elif tree[0].isdigit():
            count += 1
            num_string = ""
            while tree:
                if not tree[0].isdigit():
                    break
                number = tree.pop(0)
                num_string = f"{num_string}{number}"
            
            totweight = int(num_string)*2**(layer)

            if str(totweight) in structures:
                structures[str(totweight)] += 1
            else:
                structures[str(totweight)] = 1
    return structures, count

start = time.time()

def main():
    
    s = """3
[[3,7],6]
40
[[2,3],[4,[5,[1,6]]

"""

    rows  = s.split("\n")
    rows = list(filter(("").__ne__, rows))
    j = 0
    for row in rows:
        layer = 0
        if j is 0:
            j += 1
            continue
        if not row[0].isdigit():
            count = 0
            structures = {}
            row = list(row)
            # print(row)
            structures, count = readExpression(row,layer,structures, count)
            # print(structures)
            max_matches = max(structures, key=structures.get)
            # max_matches = max(structures.values())


            print(count -  structures[max_matches])
        else:
            print(0)
        # print(count - max_matches)

        end = time.time()
        print(end - start)
main()

