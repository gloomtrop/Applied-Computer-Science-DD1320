from songClass import Song
from hashtable import Hashtable
import timeit


def readFile():
    songlist = list()
    with open("/Users/Axel Rooth/Desktop/KTH/Data/Tillda/Lab6/unique_tracks.txt", "r", encoding="utf8") as songfile:
        for rad in songfile:
            songinfo = rad.strip().split("<SEP>")
            songlist.append(Song(songinfo[0], songinfo[1], songinfo[2], songinfo[3] ))
    
    return songlist

def linsearch(songlist, testartist):
    count = 0
    for song in songlist:
        count +=1
        if song == testartist:
            # print(count)
            break
    
def binsearch(songlist, testartist):

    low = 0
    high = len(songlist)-1
    found = False
    count = 0
    while low <= high and not found:
        middle = (low + high)//2
        if songlist[middle].artist == testartist:
            found = True
        else:
            if testartist < songlist[middle].artist:
                high = middle - 1
            else:
                low = middle + 1
        count += 1
    # print(count)
    return found

def hashsearch(songlist, testartist):
       return htable.get(testartist) 
    
if __name__ == "__main__":
    
    songlist = readFile()
    songlist = songlist
    binlist = sorted(songlist)
    n = len(songlist)
    print("Antal element =", n)
    htable = Hashtable(n)

    for song in songlist:
        htable.put(song.artist, song)

    last = songlist[n-1]
    testartist = last.artist
    linartist = last

    # lintime = timeit.timeit(stmt = lambda: linsearch(songlist, linartist), number = 1000)
    bintime = timeit.timeit(stmt = lambda: binsearch(binlist, testartist), number = 1000)
    hashtime = timeit.timeit(stmt = lambda: hashsearch(songlist, testartist), number = 1000)

    # print("Linjärsökningen tog", round(lintime, 4) , "sekunder")
    print("Binärsökning tog", round(bintime, 10), "sekunder")
    print("Hashsökning tog", round(hashtime, 10), "sekunder")

    

