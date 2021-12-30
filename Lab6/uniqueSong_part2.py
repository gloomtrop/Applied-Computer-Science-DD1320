from songClass import Song 
import timeit

def quicksort(data):
    sista = len(data) - 1
    qsort(data, 0, sista)

def qsort(data, low, high):
    pivotindex = (low+high)//2
    # flytta pivot till kanten
    data[pivotindex], data[high] = data[high], data[pivotindex]  
    
    # damerna först med avseende på pivotdata
    pivotmid = partitionera(data, low-1, high, data[high]) 
    
    # flytta tillbaka pivot
    data[pivotmid], data[high] = data[high], data[pivotmid]       
    
    if pivotmid-low > 1:
        qsort(data, low, pivotmid-1)
    if high-pivotmid > 1:
        qsort(data, pivotmid+1, high)

def partitionera(data, v, h, pivot):
    while True:
        v = v + 1
        while data[v] < pivot:
            v = v + 1
        h = h - 1
        while h != 0 and data[h] > pivot:
            h = h - 1
        data[v], data[h] = data[h], data[v]
        if v >= h: 
            break
    data[v], data[h] = data[h], data[v]
    return v

def bubblesort(songlist):
    for passnum in range(len(songlist)-1,0,-1):
        for i in range(passnum):
            if songlist[i].songtitle>songlist[i+1].songtitle:
                temp = songlist[i]
                songlist[i] = songlist[i+1]
                songlist[i+1] = temp
                # songlist[i], songlist[i+1] = songlist[i+1], songlist[i]

def readFile():
    songlist = list()
    with open("/Users/Axel Rooth/Desktop/KTH/Data/Tillda/Lab6/unique_tracks.txt", "r", encoding="utf8") as songfile:
        for rad in songfile:
            songinfo = rad.strip().split("<SEP>")
            songlist.append(Song(songinfo[0], songinfo[1], songinfo[2], songinfo[3] ))
    
    return songlist

if __name__ == "__main__":
    
    songlist = readFile()
    songlist = songlist[:10000]

    n = len(songlist)
    print("Antal element =", n)

    quicksorttime = timeit.timeit(stmt = lambda: quicksort(songlist), number = 1)
    bubblesorttime = timeit.timeit(stmt = lambda: bubblesort(songlist), number = 1)

    print("Quicksort tog", round(quicksorttime, 4) , "sekunder")
    print("Bubblesort tar", round(bubblesorttime, 4), "sekunder")

    