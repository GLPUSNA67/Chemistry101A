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
from Udemy Zero to Hero 110
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
# Driver code
#print(mySum(1, 2, 3, 4, 5))
#print(mySum(10, 20))

''' Example of a function that modifies an attribute. '''
class Simple():
    def __init__(self,value):
        self.value = value
    def add_to_value(self,amount):
        self.value = self.value + amount
        print('We just added {} to your value'.format(amount) ) # or
        print(f'We just added {amount} to your value'.format(amount) )

try:
    f = open('testfile', 'w')
    f.write("Write a test line.")
except TypeError:
    print("There was a type error.")
except:
    print("All other errors.")
else:
    print("Runs when there is no error.")
finally:
    print("I always run.")

def ask_for_int():
    while True: #always requires a break statememt
        try:
            result = int(input("Please provide an integer."))
        except:
            print("Your input was not an integer.")
            continue
        else:
            print("Thanks for the integer")
            break
        finally:
            print("End of try/except/finally.")
            print("I will always run at the end.")


# pyLint installed

''' Card class example of class, dictionary and reference to dictionary value'''
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9,
          'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

two_hearts = Card("Hearts", "Two")
three_hearts = Card("Hearts", "Three")

