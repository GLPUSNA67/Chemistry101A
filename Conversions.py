F = 1.00
C = 1.00
K = 100
oz = 1.00
g = 1.00
inch = 1.00
cm = 1.00
Torr = 1.00
mm_hg = 1.00
atm = 1.00
N_m_2 = 1.00
Pa = 1.00   #Pascal = kg m-1 s_2 = N_m\u207B2
#print('Pascal = kg m-1 s_2 = N m\u207B2')
quart = 1.00
liter = 1.00
joule = 1.00
cal = 1.00

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
def inch_to_cm(inch):
    global cm
    cm = 2.54*inch
    print("cms are", cm)
def cm_to_inch(cm):
    global inch
    inch = cm/2.54
    print("inchs are", inch)
def oz_to_g(oz):
    global g
    g = oz/28.35
    print("grams are", g)
def g_to_oz(g):
    global oz
    oz = 28.35*g
    print("ounces are", oz)
def Torr_to_mm_hg(Torr):
    global mm_hg
    mm_hg = Torr
    print("mm_hg are", mm_hg)
def mm_hg_to_Torr(mm_hg):
    global Torr
    Torr = mm_hg
    print("Torr are", Torr)
def atm_to_Torr(atm):
    global Torr
    Torr =760*atm
    print("Torr are", Torr)
def Torr_to_atm(Torr):
    global atm
    atm = atm/760
    print("atm are", atm)
def atm_to_mm_hg(atm):
    global mm_hg
    mm_hg =760*atm
    print("mm_hg are", mm_hg)
def mm_hg_to_atm(mm_hg):
    global atm
    atm = atm/760
    print("atm are", atm)
def quart_to_liter(quart):
    global liter
    liter =quart/0.9463
    print("liter are", liter)
def liter_to_quart(liter):
    global quart
    quart = 0.9463*liter
    print("quarts are",quart)
def joule_to_cal(joule):
    global cal
    cal = 4.184*joule
    print("liter are", liter)
def cal_to_joule(cal):
    global joule
    joule = cal/4.184
    print("joules are", joule)
''' Functional program example of recursion factorial. '''
def f_factorial(n): # Excessive recursion calls can crash the program.
    return 1 if n == 0 else n*f_factorial(n-1)
''' Procedural program example of factorial. '''
def p_factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= 1
    return f
def vol_from_prt():
    ''' Calculate volume given pressure, R constant, and temperature. pv = nRt'''
    n= 0.54
    R = 0.08206 # R value for these units
    T = 288   # Temp in K
    P = .967    # P in atm
    vol = n*R*T/P
    print(vol)

def p_from_vrt():
    ''' Calculate pressure given volume, R constant, and temperature. pv = nRt'''
    n= 10.5
    R = 0.08206 # R value for these units
    T = 273.15 + 452   # Temp in K
    V = 565    # P in atm
    P = n*R*T/V
    print(P)

#print(f_factorial(0))
#print(f_factorial(2))
#print(f_factorial(4))
#print(f_factorial(0))
#print(f_factorial(2))
#print(f_factorial(4))
''' lambda expressions do not with if statements.'''
''' example of lambda expression with if expressions.'''
# (lambda gp: 'good' if gp > 7 else 'satisfactory' if gp > 7 else 'insufficient')(6)

if __name__ == '__main__':
    #print("C is", C)
    #print("F is", F)
    F = 325
    #F_to_C(F)
    C = 25
    #C_to_F(C)
    K = 100
    #K_to_C(K)
    C = 25
    #C_to_K(C)
    #f_factorial(3)
    #vol_from_prt()
    vol_from_prt()
