from tkinter import *  # get widget classes
from tkinter.ttk import Combobox  # ,Textbox
from tkinter.ttk import Entry
from MessageBoxes import *
from tkinter.messagebox import *  # get standard dialogs
import tkinter as tk
import sqlite3
from sqlite3 import Error
from ElementsDict import *
from CompoundsDict import *
from ionDict import *
from eciDict import *
from Conversions import *

root = tk.Tk()
root.title('Chemistry')
titlefont = ('Ariel', 14, 'bold')
labelfont = ('Ariel', 14)  # , 'bold')
buttonfont = ('Ariel', 12)  # , 'bold')
entryfont = ('Ariel', 12)  # , 'bold')


def select_eci_1_type(eventObject):
    cb_1_type = cb_Select_CB1.get()  # use cb_1_type as a local variable to improve readability
    eci_d['eci_1']['eci_type'] = cb_Select_CB1.get()
    # print("cb_1_type is ", cb_1_type)
    ''' Both of the assignments below work. '''
    # print("eci_db['eci_1']['eci_type'] is ", eci_db['eci_1']['eci_type'])
    # print("eci_db['eci_1']['eci_type'] is ", cb_1_type)
    eci_d['eci_1']['eci_type'] = cb_1_type
    if cb_1_type == 'elements':
        cb_eci_1['values'] = elements_symbols_list
        cb_eci_1_N['values'] = elements_name_list
    elif cb_1_type == 'compounds':
        cb_eci_1['values'] = compound_symbols_list
        cb_eci_1_N['values'] = compound_names_list
    elif cb_1_type == 'ions':
        cb_eci_1['values'] = ion_symbols_list
        cb_eci_1_N['values'] = ion_names_list
    else:
        print("Error is select_eci_1_type")
