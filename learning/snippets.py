from tkinter import *  # get widget classes
from tkinter.ttk import Combobox #,Textbox
from tkinter.ttk import Entry
from tkinter.messagebox import *  # get standard dialogs
import tkinter as tk
import sqlite3
from sqlite3 import Error
root = tk.Tk()
root.title('Chemistry')
titlefont= ('Ariel', 14, 'bold')
labelfont= ('Ariel', 12)
''' the following 'list' as a space delimited string is needed to fill a combo box. '''
elements_symbols_list = "Ac Ag Al"
eci_1 = StringVar()
eci_1_col = IntVar()
eci_1_mass = DoubleVar()
''' the following fuction used the selected item from one combo box and a list to fill a different combo box. 
def select_eci_1_type(eventObject):
    cb_1_type = cb_Select_CB1.get() # use cb_1_type as a local variable to improve readability
    eci_db['eci_1']['eci_type'] = cb_Select_CB1.get()
    print("cb_1_type is ", cb_1_type)
    print("eci_db['eci_1']['eci_type'] is ", eci_db['eci_1']['eci_type'])
    print("eci_db['eci_1']['eci_type'] is ", cb_1_type)
    eci_db['eci_1']['eci_type'] = cb_1_type
    if cb_1_type == 'elements':
        cb_eci_1['values'] = elements_symbols_list
        cb_eci_1_N['values'] = elements_name_list
    elif cb_1_type == 'compounds':
        cb_eci_1['values'] = compound_symbols_list   #compound_values
        cb_eci_1_N['values'] = compound_names_list
    elif cb_1_type == 'ions':
        cb_eci_1['values'] = ion_symbols_list
        cb_eci_1_N['values'] = ion_names_list
    else: print("Error is select_eci_1_type")
'''
''' Sample if elif else structure. '''
def A_Function():
    print("Process selected is " , A_Function)
    if A_Function == "Acid_Base":
        pass
        # Do something
    elif A_Function == "Calculate":
        pass
       # Do something
    else: print("Error in A_Function process")
''' Sample label structure. '''
lbl_eci_1_qty = Label(root, text="ECI Qty 1", width=8)
lbl_eci_1_qty.grid(row=11, column=0)
lbl_eci_1_qty.config(font=labelfont)
''' Sample Entry structure. '''
eci_1_qty = 0
e_eci_1_qty = Entry(root, text="", textvariable=eci_1_qty, width=8)
e_eci_1_qty.grid(row=12, column=0)   #, padx=4)
e_eci_1_qty.config(font=labelfont)
''' Sample Combobox structure. '''
cb_eci_1 = Combobox(root, textvariable=eci_1, width=12) #, command=setClassItem
cb_eci_1.grid(row=12, column=2)   #, padx=4)
cb_eci_1.config(font=labelfont)
cb_eci_1['values'] = elements_symbols_list
cb_eci_1.bind("<<ComboboxSelected>>", A_Function)
''' Sample Text and Scrollbar structure. '''
e_Explanation = Text(root, height=6, width=100)
e_Explanation.grid(row=37, column=0, columnspan=6, sticky=W)
e_Explanation.config(font=labelfont)
e_Explanation.rowconfigure(99)
S = tk.Scrollbar(root)
S.grid(row=37, column=7, sticky=E)
S.config(command=e_Explanation.yview)
cb_eci_1.bind("<<ComboboxSelected>>", A_Function)

''' Sample dictionary structure. '''
AlC3 = dict(formula= 'AlC3', elements= 'AlC',name= 'aluminum_chloride')
AlC3 = dict(formula= 'AlC3', elements= 'AlC',name= 'aluminum_carbide')
c_db = {}
c_db['AlC3'] = AlC3
''' Sample dictionary structure. '''
class Compound:
    def __init__(self, formula, elements='',name= ''):
        self.formula = formula
        self.name = name
        self.elements = elements
Al4C3 = Compound(formula= 'Al4C3',name= 'aluminum_carbide', elements= 'AlC')
''' Sample conversion structure. '''
F = 1.00
def F_to_C(F):
    global C
    C = 5/9*(F- 32)
    print("C is", C)
''' To read a line of typed user input, use the input() function: '''
'''
name = input('Enter your name:')
print('Your name is', name)
'''
'''pass is also called a “no-op” statement. It does nothing. 
It serves as a placeholder for statements, possibly to be added later.
'''
'''
Floating point (float)
Use a decimal or exponential notation to specify a floating point value:
a = 37.45
b = 4e5 # 4 x 10**5 or 400,000
c = -1.345e-10

Common int/floatOperations:
x + y      Add
x - y      Subtract
x * y      Multiply
x / y      Divide
x // y     Floor Divide
x % y      Modulo
x ** y     Power
abs(x)     Absolute Value

Additional math functions are found in the math module.

import math
a = math.sqrt(x)
b = math.sin(x)
c = math.cos(x)
d = math.tan(x)
e = math.log(x)
Comparisons
The following comparison / relational operators work with numbers:

x < y      Less than
x <= y     Less than or equal
x > y      Greater than
x >= y     Greater than or equal
x == y     Equal to
x != y     Not equal to
You can form more complex boolean expressions using
and, or, not
Here are a few examples:
if b >= a and b <= c:
    print('b is between a and c')
if not (b < a or b > c):
    print('b is still between a and c')
    Converting Numbers
The type name can be used to convert values:

a = int(x)    # Convert x to integer
b = float(x)  # Convert x to float
Try it out.

>>> a = 3.14159
>>> int(a)
3
>>> b = '3.14159' # It also works with strings containing numbers
float(b)
3.14159
String Representation
Each character in a string is stored internally as a so-called Unicode “code-point” which is 
an integer. You can specify an exact code-point value using the following escape sequences:

a = '\xf1'          # a = 'ñ'
b = '\u2200'        # b = '∀'
c = '\U0001D122'    # c = '𝄢'
d = '\N{FOR ALL}'   # d = '∀'

String operations
Concatenation, length, membership and replication.

# Concatenation (+)
a = 'Hello' + 'World'   # 'HelloWorld'
b = 'Say ' + a          # 'Say HelloWorld'

# Length (len)
s = 'Hello'
len(s)                  # 5

# Membership test (`in`, `not in`)
t = 'e' in s            # True
f = 'x' in s            # False
g = 'hi' not in s       # True

# Replication (s * n)
rep = s * 5             # 'HelloHelloHelloHelloHello'
String methods
Strings have methods that perform various operations with the string data.

Example: stripping any leading / trailing white space.

s = '  Hello '
t = s.strip()     # 'Hello'
Example: Replacing text.

s = 'Hello world'
t = s.replace('Hello' , 'Hallo')   # 'Hallo world'

More string methods:
Strings have a wide variety of other methods for testing and manipulating the text data. 
This is a small sample of methods:

s.endswith(suffix)     # Check if string ends with suffix
s.find(t)              # First occurrence of t in s
s.index(t)             # First occurrence of t in s
s.isalpha()            # Check if characters are alphabetic
s.isdigit()            # Check if characters are numeric
s.islower()            # Check if characters are lower-case
s.isupper()            # Check if characters are upper-case
s.join(slist)          # Join a list of strings using s as delimiter
s.lower()              # Convert to lower case
s.replace(old,new)     # Replace text
s.rfind(t)             # Search for t from end of string
s.rindex(t)            # Search for t from end of string
s.split([delim])       # Split string into list of substrings
s.startswith(prefix)   # Check if string starts with prefix
s.strip()              # Strip leading/trailing space
s.upper()              # Convert to upper case

Raw Strings
Raw strings are string literals with an uninterpreted backslash. 
They are specified by prefixing the initial quote with a lowercase “r”.

>>> rs = r'c:\newdata\test' # Raw (uninterpreted backslash)
>>> rs
'c:\\newdata\\test'

f-Strings
A string with formatted expression substitution.

>>> name = 'IBM'
>>> shares = 100
>>> price = 91.1
>>> a = f'{name:>10s} {shares:10d} {price:10.2f}'
>>> a
'       IBM        100      91.10'
>>> b = f'Cost = ${shares*price:0.2f}'
>>> b
'Cost = $9110.00'

Exercise 1.17: f-strings
Sometimes you want to create a string and embed the values of variables into it.

To do that, use an f-string. For example:

>>> name = 'IBM'
>>> shares = 100
>>> price = 91.1
>>> f'{shares} shares of {name} at ${price:0.2f}'
'100 shares of IBM at $91.10'

Exercise 1.18: Regular Expressions
One limitation of the basic string operations is that they don’t support any kind of advanced pattern matching. For that, you need to turn to Python’s re module and regular expressions. Regular expression handling is a big topic, but here is a short example:

>>> text = 'Today is 3/27/2018. Tomorrow is 3/28/2018.'
>>> # Find all occurrences of a date
>>> import re
>>> re.findall(r'\d+/\d+/\d+', text)
['3/27/2018', '3/28/2018']
>>> # Replace all occurrences of a date with replacement text
>>> re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
'Today is 2018-3-27. Tomorrow is 2018-3-28.'
>>>
For more information about the re module, see the official documentation 
at https://docs.python.org/library/re.html.
Sometimes lists are created by other methods. For example, a string can be split into a list using the split() method:

>>> line = 'GOOG,100,490.10'
>>> row = line.split(',')
>>> row
['GOOG', '100', '490.10']
>>>
List operations
Lists can hold items of any type. Add a new item using append():

names.append('Murphy')    # Adds at end
names.insert(2, 'Aretha') # Inserts in middle
'''
''' Sample if main structure. '''
'''
if __name__ == '__main__':
    A_Function()
    root.mainloop()


#print('temp1 is ', temp1)
#print('temp len is ', len(temp))
#while not temp[-1]:
for i in range(0, 10):    #in range(0, len(temp1)):
    if c.find(str(i)):
        #if temp.find(str(i)).isdigit():
        temp1 = c.replace(str(i), "")
        temp = temp1
        print("temp1 is ", temp1)
        print("temp1 len is ", len(temp1))
        continue
except IndexError:
    print('IndexError: string index out of range')

print('temp is ', temp)
#new_list = compound_symbols_list.replace(2, "")
#print(new_list)

#line = 'AlC3, Ar2He2Kr2Ne2Xe2Rn2, BCl3, C14H30'
#row = line.split(',')
#print('row is ', row)

for c in row:   #compound_symbols_list:
    temp = ''

    # try:

    #elif temp1.find(str(3)):
#    temp1 = temp.replace(str(3), "")
#    print("temp1 is ", temp1)
#Use each item in the list as a key to look up 'elements' in its dictionary, and
#set temp1 to the value of that field

What I want to end up with is:
c_alpa_list = []
c_alpa_list = [AlC, AlCl, ArHeKrNeXeRn, Ar2He2Kr2Ne2Xe2Rn2, BCl, CH, CaHOP, CaI, CaHO, CaP, CdS, CsF, CHO, CO, CuS, BrH]
AlC = "AlC"
AlCl = "AlCl"
ArHeKrNeXeRn = "Ar2He2Kr2Ne2Xe2Rn2"
BCl = "BCl3"
CH = "CH4, C2H6, C3H8, C4H10, C4H10_M, C5H12, C6H14, C7H16, C8H18, C9H20, C10H22, C14H30, C18H38 "
CaHOP = "CaH2PO4"
CaI = "CaI"
CaHO = "CaOH2"
CaP = "Ca3P2"
CdS = "CdS"
CsF = "CsF"
CHO = "C6H8O7, CH3CO2H"
CO = "CO, CO2 "
CuS = "CuS"
BrH = "HBr_g, HBr_aq"
Common Idioms for Reading File Data
Read an entire file all at once as a string.

with open('foo.txt', 'rt') as file:
    data = file.read()
    # `data` is a string with all the text in `foo.txt`
Read a file line-by-line by iterating.

with open(filename, 'rt') as file:
    for line in file:
        # Process the line
Common Idioms for Writing to a File
Write string data.

with open('outfile', 'wt') as out:
    out.write('Hello World\n')
    ...
Redirect the print function.

with open('outfile', 'wt') as out:
    print('Hello World', file=out)
    To read a file line-by-line, use a for-loop like this:

>>> with open('Data/portfolio.csv', 'rt') as f:
        for line in f:
            print(line, end='')
>>> f = open('Data/portfolio.csv', 'rt')
>>> headers = next(f).split(',')
>>> headers
['name', 'shares', 'price\n']
>>> for line in f:
    row = line.split(',')
    print(row)

['"AA"', '100', '32.20\n']
['"IBM"', '50', '91.10\n']
...
>>> f.close()
Note: In these examples, f.close() is being called explicitly because the with statement isn’t being used.
to convert a string to an integer, use int(s). To convert a string to a floating point, use float(s).
To read a compressed file use:
import gzip
with gzip.open('Data/portfolio.csv.gz', 'rt') as f:
    for line in f:
        print(line, end='')
Note: Including the file mode of 'rt' is critical here. 
If you forget that, you’ll get byte strings instead of normal text strings.
total += n
n -= 1
import math
x = math.sqrt(10)

import urllib.request
u = urllib.request.urlopen('http://www.python.org/')
data = u.read()

To catch, use the try - except statement.
for line in f:
    fields = line.split()
    try:
        shares = int(fields[1])
    except ValueError:
        print("Couldn't parse", line)
        
def greeting(name):
    'Issues a greeting'
    print('Hello', name)
greeting('Guido')
Hello Guido
>>> greeting('Paula')
Hello Paula
>>>
If the first statement of a function is a string, it serves as documentation. 
Try typing a command such as help(greeting) to see it displayed.

sys.argv is a list that contains passed arguments on the command line (if any).

If you turn a dictionary into a list, you’ll get all of its keys:

>>> list(d)
['name', 'shares', 'price', 'date', 'account']
>>>

 A more elegant way to work with keys and values together is to use the items() method. 
>>> items = d.items()
>>> items
dict_items([('name', 'AA'), ('shares', 75), ('price', 32.2), ('date', (6, 11, 2007))])
>>> for k, v in d.items():
        print(k, '=', v)

name = AA
shares = 75
price = 32.2
date = (6, 11, 2007)
>>>
If you have tuples such as items, you can create a dictionary using the dict() function. Try it:

>>> items
dict_items([('name', 'AA'), ('shares', 75), ('price', 32.2), ('date', (6, 11, 2007))])
>>> d = dict(items)
>>> d
{'name': 'AA', 'shares': 75, 'price':32.2, 'date': (6, 11, 2007)}
An example populating the dict from the contents of a file.

prices = {} # Initial empty dict

with open('Data/prices.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        prices[row[0]] = float(row[1])

Sets
Sets are collection of unordered unique items.

tech_stocks = { 'IBM','AAPL','MSFT' }
# Alternative syntax
tech_stocks = set(['IBM', 'AAPL', 'MSFT'])
>>> tech_stocks
set(['AAPL', 'IBM', 'MSFT'])
>>> 'IBM' in tech_stocks
True

names = ['IBM', 'AAPL', 'GOOG', 'IBM', 'GOOG', 'YHOO']
unique = set(names)
Additional set operations:

names.add('CAT')        # Add an item
names.remove('YHOO')    # Remove an item

s1 | s2                 # Set union
s1 & s2                 # Set intersection
s1 - s2     

Keeping a History
Problem: We want a history of the last N things.

from collections import deque

history = deque(maxlen=N)
with open(filename) as f:
    for line in f:
        history.append(line)
Type Checking
How to tell if an object is a specific type.

if isinstance(a, list):
    print('a is a list')
    
def callback(eventObject):
    print(eventObject)

cbox.bind("<<ComboboxSelected>>", callback)

d2 = list(zip(compound_names_list,compound_symbols_list))
The following worked to create a dictionary of names to formulas
keys = ['aluminum_carbide', 'aluminum_chloride', 'air']
values = ['Al4C3', 'AlCl3', 'Ar2He2Kr2Ne2Xe2Rn2']
D3 = dict(zip(keys, values))

D3 = dict(zip(compound_names_list, compound_symbols_list))
compound_names_Dict = {}
for (k,v) in zip(compound_names_list, compound_symbols_list):
    compound_names_Dict[k] = v
    
'''
