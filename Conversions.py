F = 325
C = 25
K = 100
def F_to_C(F):
    global C
    C = 5/9*(F- 32)
    #return C
    print("C is", C)

def C_to_F(C):
    global F
    F = 9*C/5 + 32
    print("F is", F)

def K_to_C(K):
    global C
    C = K - 273.15
    print("C is", C)

def C_to_K(C):
    global K
    K = C + 273.15
    print("K is", K)

if __name__ == '__main__':
    #print("C is", C)
    #print("F is", F)
    F = 325
    F_to_C(F)
    C = 25
    C_to_F(C)
    K = 100
    K_to_C(K)
    C = 25
    C_to_K(C)
