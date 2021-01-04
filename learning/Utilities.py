import time

''' Functional program example of recursion factorial. '''
def l_factorial(n): # Excessive recursion calls can crash the program.
    return 1 if n == 0 else n*l_factorial(n-1)
''' Procedural program example of factorial. '''
def p_factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= 1
    return f

def timer(fnc, arg):
    t0 = time.time()
    fnc(arg)
    t1 = time.time()
    print('t0 is ', t0)
    print('t1 is ', t1)
    return t1-t0
#print('Took: %.5f s' % timer(l_factorial, 900))

l_timestamp = lambda fnc, arg: (time.time(), fnc(arg)), (time.time())
l_diff = lambda t0, retval, t1: t1-t0
''' Error with the following. TypeError: 'tuple' object is not callable
course said * would unpack tuple'''
l_timer = lambda fnc, arg: l_diff(*l_timestamp(fnc, arg))
#print('Took: %.5f s' % l_timer(l_factorial, 900))

''' * is an unpacking function. Look it up. '''

def mySum(*args):
    sum = 0
    for i in range(0, len(args)):
        sum = sum + args[i]
    return sum

# Driver code
#print(mySum(1, 2, 3, 4, 5))
#print(mySum(10, 20))

