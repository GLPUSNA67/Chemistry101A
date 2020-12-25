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
    ''' Sample if main structure. '''
if __name__ == '__main__':
    A_Function()
    root.mainloop()

