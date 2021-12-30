# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
from scipy import stats
import pandas as pd
#%%

# Mersenne Twister, Source: https://github.com/james727/MTP/blob/master/mersenne_twister.py
class mersenne_rng(object):
    def __init__(self, seed = 5489):
        #Förbestämda konstanter utifrån MT1997 specifikation
        self.state = [0]*624 #lagrar statusen för generatorn med 624 antal upprepningar
        self.f = 1812433253
        self.m = 397 #Mittenvärde
        self.u = 11 # additional Mersenne Twister tempering bit shifts/masks
        self.s = 7 #TGFSR(R) tempering bit shifts
        self.b = 0x9D2C5680 #TGFSR(R) tempering bitmasks
        self.t = 15 #TGFSR(R) tempering bit shifts
        self.c = 0xEFC60000 #TGFSR(R) tempering bitmasks
        self.l = 18 #additional Mersenne Twister tempering bit shifts/masks
        self.index = 624
        self.lower_mask = (1<<31)-1
        self.upper_mask = 1<<31

        # initialisera generatorn med seedet
        self.state[0] = seed
        for i in range(1,624): 
            #Skapar den lägsta 32 biten av funktionen som är invärde av int_32
            #Funktionen använder sig av xor/^ (sätter varje bit till 1 om en bit av bitarna är 1) 
            # och en shift/>> (pushar kopior av den mest vänstra biten från vänster och låter 
            # den mest högra biten tappas)
            self.state[i] = self.int_32(self.f*(self.state[i-1]^(self.state[i-1]>>30)) + i)
    
    #Genererar de nästa 624 värdena från serien av värden till temp
    # och adresserar varje nytt värde till self.state
    def twist(self):
        for i in range(624):
            temp = self.int_32((self.state[i]&self.upper_mask)+(self.state[(i+1)%624]&self.lower_mask))
            temp_shift = temp>>1 #temp*A
            if temp%2 != 0: #Gör en xor på matrisen om temp inte är ett tal av faktor 2
                temp_shift = temp_shift^0x9908b0df
            self.state[i] = self.state[(i+self.m)%624]^temp_shift #Sparar det nya värdet i state
        self.index = 0
    #Genererar slumptalet m.h.a av 4 xorshifts
    # och om hela state-listan är gjord ska en twist göras för varje tal 
    # i state-listan.
    def get_random_number(self):
        if self.index >= 624:
            self.twist()
        y = self.state[self.index]
        y = y^(y>>self.u)
        y = y^((y<<self.s)&self.b)
        y = y^((y<<self.t)&self.c)
        y = y^(y>>self.l)
        self.index+=1
        return self.int_32(y)

    #Gör ett heltal som är tillåtet inom ramen av de 32 bitarna
    def int_32(self, number):
        return int(0xFFFFFFFF & number)
#LCG - Linear Congruential Generator
def lcg(x0, a, c, m, n):
    period = 0
    string = ""
    it = 0
    #Skapar första värdet av den linjära funktionen
    x1 = (a*x0 + c)%m
    #Itererar genom godtyckligt antal gånger 
    #För att lösa in i fil samt undersöka periodens längd
    for i in range(n):
        for j in range(n):
            x1 = (a*x1 + c)%m
            string += str(x1) + " "
            it += 1
            if x0 == x1 and period == 0:
                period = it

        string += "\n"
    write("lcg",string)
    return period
    """
    Xn+1 = (a*Xn + c)*mod(m)
    Xo, a , c <= m are all positive real values
    """
    """
    Rules for choosing constants (Hull–Dobell Theorem):
    --------------------------------------------------
    When c ≠ 0, correctly chosen parameters allow a period equal to m, 
    for all seed values. This will occur if and only if:[2]:17—19

        1.m and c are relatively prime,
        2.a − 1 is divisible by all prime factors of m ,
        3.a − 1 is divisible by 4 if m is divisible by 4.
    """
        
# Mersenne twister call

def mersenne(n):
    string = ""
    period = 0
    it = 0
    seed =1131464071 #Använder mig av ett invärde med få 0:or
    rng = mersenne_rng(1131464071)
    for i in range(n):
        for j in range(n):
            x1 = rng.get_random_number()
            string += str(x1) + " "
            it += 1
            if seed == x1 and period == 0:
                period = it
        string += "\n"
    write("mers",string)
    return period

# Chi-Square goodness of fit test
def chitest(M):

    
    arr = np.asarray(M)
    
    unique_elements, count_elements = np.unique(arr, return_counts=True)
    onesarr = np.ones(len(count_elements))
    chi2_stat, p_val = scipy.stats.chisquare(count_elements, onesarr)

    return chi2_stat, p_val

def makelist(M):
    x = np.matrix.tolist(M)
    matrix_list = list()
    index_list = list()
    j = 0
    for l in x:
        for i in l:
            matrix_list.append(i)
            index_list.append(j)
            j += 1
    return matrix_list, index_list
def basicstats(M):
    arr_m = np.asarray(M)


#Write to file
def write(name, string):
    text_file = open(name +".txt", "w")
    text_file.write(string)
    text_file.close()

#Read from file
def read(filename, n):
    it = 0
    matrix = np.zeros((n, n))
    """KOM PÅ NÅGOT SMART"""
    with open(filename + '.txt','r') as f:
        for line in f:
            row = line.strip().split(" ")
            for i in range(0, len(row)-1):
                row[i] = int(row[i])
            matrix[it] = row
            it += 1
    f.close()
    return matrix

def main():
    it = 0
    out_df = pd.DataFrame(columns=["Matrixsize", "LCG: chi2_val",
                                 "LCG: P_val","LCG: Period",
                                 "MT:chi2_val", "MT: P_val",
                                 "MT: Period"])
    it_vec = [500]
    #LCG vals
    x0l = 3
    al = 13
    cl = 1
    ml = 2**32-1

    #Mersenne vals initialized
    
    for i in it_vec:
        n = i
        #Make random matrices
        period_lcg = lcg(x0l, al, cl, ml, n)
        period_mers = mersenne(n)

        #Read and plot lcg matrix
        M_lcg = read("lcg", n)
        plt.matshow(M_lcg, cmap=plt.cm.gray)
        plt.title("LCG")
        plt.colorbar()
        plt.show()
        
        #Make and plot Mersenne Twister matrix
        M_mers = read("mers", n)
        plt.matshow(M_mers, cmap=plt.cm.gray)
        plt.title("Mersenne Twister")
        plt.colorbar()
        plt.show()

        fig = plt.figure()
        #Make LCG list and scatterplot
        lcg_list, lcg_index = makelist(M_lcg)
        # ax_lcg = fig.add_subplot(221)
        # ax_lcg.scatter(lcg_index, lcg_list)
        # ax_lcg.title.set_text("LCG Scatter")

        #Make Mers list and scatterplot
        mers_list, mers_index = makelist(M_mers)
        # ax_mers = fig.add_subplot(222)
        # ax_mers.scatter(mers_index, mers_list)
        # ax_mers.title.set_text("MT Scatter")
        # plt.show()

        #LCG basic stats
        desc_lcg = stats.describe(lcg_list)
        print(desc_lcg)

        #MT basics stats
        desc_mers = stats.describe(mers_list)
        print(desc_mers)
        #Test for distribution using chi-test
        #For LCG
        chi2_lcg, p_val_lcg = chitest(M_lcg)
        #For Mersenne
        chi2_mers, p_val_mers = chitest(M_mers)

        #Output

        out_df.loc[it] = [i, chi2_lcg, p_val_lcg, period_lcg,
                            chi2_mers, p_val_mers, period_mers]
                       
        it += 1
    display(out_df)
  
main()

# %%
