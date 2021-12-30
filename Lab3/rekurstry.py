def siffersumma(n):
      if n == 0:  
         return 0
      else:               
         return n%10 + siffersumma(n//10)

for i in range(0,11):
    siffersum = siffersumma(i)
    print(siffersumma)


