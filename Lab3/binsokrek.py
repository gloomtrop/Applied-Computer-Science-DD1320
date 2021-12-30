def binsok(listan, nyckel):
    if len(listan) == 0:
        return False
    else:
        mitten = len(listan)//2
        if listan[mitten] == nyckel:
            return True
        else:
            if nyckel < listan[mitten]:
                return binsok(listan[:mitten], nyckel)
            else:
                return binsok(listan[mitten+1:], nyckel)


x = [1,3,4,6,7]
key = 2

bins = binsok(x, key)
print(bins)