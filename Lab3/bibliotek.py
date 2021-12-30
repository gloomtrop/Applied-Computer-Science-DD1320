from bintree import Bintree


def readFiles(svenska):
    count = 0
    with open("/Users/Axel Rooth/Desktop/KTH/Data/Tillda/Lab3/word3.txt", "r", encoding = "utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()           # Ett trebokstavsord per rad
            if ordet in svenska:
                print(ordet, end = " ") 
            else:
                svenska.put(ordet)
                count += 1


    nodes = svenska.size()
    print("\n")
    print("Det finns " + str(nodes) + " noder i trädet")
    print("Antal ord som försöktes att läggas in i trädet är " + str(count))
    print("\n")
        
   

def readFilesE(engelska, svenska):
    count = 0
    with open("/Users/Axel Rooth/Desktop/KTH/Data/Tillda/Lab3/engelska.txt", "r", encoding = "utf-8") as engelskfil:
        for rad in engelskfil:
            listaword = rad.split()
            for ordet in listaword:
                ordet = ordet.strip(",").strip("!").strip(".").strip('"').strip("'")
                if ordet in engelska:
                    pass
                else:
                    engelska.put(ordet)
                    count += 1
                    if ordet in svenska:
                        print(ordet, end = " ")
    
    nodes = engelska.size()
    print("\n")
    print("Det finns " + str(nodes) + " noder i trädet")
    print("Antal ord som försöktes att läggas in i trädet är " + str(count))
    print("\n")
    
        
                            # in i sökträdet
        

def main():
    svenska = Bintree()
    engelska = Bintree()
    readFiles(svenska)
    readFilesE(engelska, svenska)
    
    
    # svenska.write()


main()
