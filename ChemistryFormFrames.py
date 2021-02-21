''' The program is designed to solve non-graphic problems in a first year general chemistry book.
There are three environments. In the laboratory environment, anything can be created or 'deconstructed'
and each step of the process should be recorded and displayed to verify the process and to aid a student
learning general chemistry.
The industrial and nature environments only describes industrial and natural processes.
There is no experimentation in these environments and the level of detail in explanations varies.
The main part of the program is the laboratory process in which a process is selected, all the appropriate field
values are entered, calculations are made, results are presented, and a record of the process is stored. Later,
that record can be retrieved and used to recreate the process for verification and learning.
The ideal is that every important aspect of each process should be described and explained.
Especially, each step in the process, the equipment and energy used, the side effects and by-products.
'''
import sys
from tkinter import *  # get widget classes
from tkinter.ttk import Combobox, Entry, Label
#import ttk
import logging
logging.basicConfig(
    filename = 'app.log',            # Name of the log file (omit to use stderr)
    filemode = 'w',                  # File mode (use 'a' to append)
    level    = logging.WARNING,      # Logging level (DEBUG, INFO, WARNING, ERROR, or CRITICAL)
)
import tkinter as tk
#import sqlite3
#from sqlite3 import Error
import pdb
from tkinter import messagebox as mb #*  # get standard dialogs
from MessageBoxes import *
from tkinter import messagebox as mb
from tkinter import font
from ElementsDict import *
from CompoundsDict import *
from ionDict import *
from eciDict import *
from ConVarFunEtc import *
from collections import defaultdict
#import defaultdict

#from Conversions import *
# This file sets up basic configuration of the logging module.
# Change settings here to adjust logging output as needed.
#r = Tk()
#r.option_add('*Dialog.msg.font', 'Helvetica 12')

''' ['Al', '4', 'C', '3'] ['C', 1, 'H', '3', 'C', 1, 'O', '2'] ['H', 1, 'C', 2, 'H', 3, 'O', 2]'''
''' Function should yield ['Al', '4', 'C', '3'] ['C', 2, 'H', '3', 'O', '2'] ['H', 4, 'C', 2, 'O', 2]'''
''' CH3CH2CH2CH3 --> ['C', 1, 'H', 3, 'C', 1, 'H', 2, 'C', 1, 'H', 2, 'C', 1, 'H', 3] --> ['C', 4, 'H', 10'''
#s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
#[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

#e = [('C', 1), ('H', 3), ('C', 1), ('H', 2), ('C', 1), ('H', 2), ('C', 1), ('H', 3)]
#d = defaultdict(list)
#for k, v in e:
#    d[k].append(v)
#sorted(d.items())
#[('C', [1, 1, 1, 1]), ('H', [3, 2, 2, 3])]
''' Now I need to add the numbers in the above lists. '''

root = tk.Tk()
root.title('Chemistry')

#titlefont = ('Ariel', 14, 'bold')
#labelfont = ('Ariel', 14)  # , 'bold')
#uttonfont = ('Ariel', 12)  # , 'bold')
#entryfont = ('Ariel', 12)  # , 'bold')
font1 = font.Font(name='TkCaptionFont', exists=True)
font1.config(family='courier new', size=20)
winInstructions = Toplevel()
e_Instructions = Text(winInstructions, height=20, width=50)
e_Instructions.grid(row=0, column=0) #, columnspan=6, sticky=W)
e_Instructions.config(font=entryfont)
e_Instructions.insert(tk.END, "Program instructions will be provided in this window. \n")
e_Instructions.insert(tk.END, "Move this window so it is always visible, or minimize it are resize it as needed. \n")
e_Instructions.insert(tk.END, "Process instructions will be provided in this window. \n")


#e_Instructions.rowconfigure(99)
''' *** e_eci_1_qty.insert(0, eci_1_M_qty) WORKS to insert a value into an entry box !!! *** '''
''' fahrenheit = [((9/5)*temp + 32) for temp in celsius '''

# *** Start constants and variables
''' All the element, compound and ion lists have been moved to the ConVarFunEtc module'''

''' 
Text with unicode can be included in combo boxes. Such use requires setting up a dictionary
to associate the text with elements that have quantities different from the standard.

Not all the elements and their attributes have been added to the database. H\u2082 works for H2 subscript'''
''' The following are not lists, but have list in the title because the string lists the items.'''


''' Process documentation 
 A des_list is a dictionary and list. The dictionary key is an alphabetical list of elements 
 in a compound. When elements are selected in various combo boxes and user chooses a process to perform,
 an alphabetic string is made of the list of elements in the combo boxes. Then a procedure will use 
 the alphabetic string as a key to the dictionary. The values returned are a list of compounds which
 have those elements. That list is used to fill a compound combo box. User will then be prompted to
 confirm a single item or to select an item from the list as the goal compound to use in the process.
 An additional function will be needed to fill the names combo box with the names associated with 
 the compoounds. This will help a user who knows the name of the compound desired, but not the formula.
 des_lists need to be recreated for compounds and ions when a compound or ion is added to the database.
 '''

#c_alpa_list = "AlC, AlCl, ArHeKrNeXeRn, Ar2He2Kr2Ne2Xe2Rn2, BCl, CH, CaHOP, CaI, CaHO, CaP, CdS, CsF, CHO, CO, CuS, BrH"

record_name = ""  # This is a placeholder for a record name to store the process in the database.
''' The following are lists of variables to fill various combo boxes until proper lists are made. '''
process_list = "Balance_Equation Set_default_T_and_P Parse_Reactants Parse_Products Acid_Base Calculate Oxidation_Reduction Oxidation_Rate Precipitation Synthesis Decompose Refine Metathesis "
equipment = "refinery blah1 blah2"
energy_type = "heat electricity"
catalyst = "blah1 blah2 blah3 blah4"
side_effects = "air_polution water_polution land_polution"
by_products = "CO CO2 NO NO2"
variables = "Av Bv Cv Kv"  # Variable names cannot conflict with element symbols like B C H K etc
''' Variables to hold the selected items of combo boxes. '''
#process_selected = ""
equipment_selected = ""
energy_type_selected = ""
catalyst_selected = ""
side_effect_selected = ""
by_product_selected = ""
variable_selected = ""
variable_value = DoubleVar()
Init_default_T_and_P = FALSE
Av = DoubleVar()
Bv = DoubleVar()
Cv = DoubleVar()
Kv = DoubleVar()

''' Miscellaneous variables to use until proper variables are created. '''
valences = "7 6 5 4 3 2 1 0 -1 -2 -3 -4"
#element1 = StringVar()

''' *** Program and data structure notes follow. ***
*** The following lines describes the structure of the eci frame dictionaries. ***
The eci frame is where all frame related process variables are stored and used for process calculations.
eci_1_d['eci'] is a reference to an eci in the frame dictionary for the first eci frame
The fields of the eci frame are shown below.
eci_1_d = dict(eci = 'eci_1', eci_type = "", name ="", column = "", electronegativity = "", _group = "",
             display_qty = "", qty = "", M_qty = "" , mass = "", Oxidation_State ="", display_units = "", units = "", valence = "",
             display_temp_units= "", display_temp_qty="", display_press_units= "", display_press_qty= "",
             temp_units= "", temp_qty="", press_units= "", press_qty= "")
Usage: db[eci_1]['name'] is a reference to a dictionary or dictionaries. 
       It uses eci_1 to find the right dictionary and 'name' as the key to look up an element field value.
       eci_1_d['eci'] is a reference to a eci in the frame dictionary for the first eci frame
       The db dictionary of dictionaries holds the field values of elements. 
       The other dictionaries hold the field values of compounds and ions.
       These dictionaries are created from the SQL database and may be used to update the database. 
       db[eci_1]['name'] is used to look up field values in the elements dictionary
       c_db[eci_1]['name'] is used to look up field values in the compound dictionary -- note the c_ prefix
       i_db[eci_1]['name'] is used to look up field values in the ion dictionary -- the note i_ prefix
       eci_d['eci_1']['name']
'''
''' Many of the variables below are needed because they record selection of items in combo boxes. 
The extraneous ones will be deleted as they are identified. '''
#def create_variables():
default_temp_units = StringVar()
default_temp_qty = DoubleVar()
default_press_units = StringVar()
default_press_qty = DoubleVar()
eci_1 = StringVar()
eci_2 = StringVar()
eci_3 = StringVar()
eci_4 = StringVar()
eci_5 = StringVar()
eci_6 = StringVar()
eci_1_col = IntVar()
eci_2_col = IntVar()
eci_3_col = IntVar()
eci_4_col = IntVar()
eci_5_col = IntVar()
eci_6_col = IntVar()
eci_1_electronegativity = ""
eci_2_electronegativity = ""
eci_3_electronegativity = ""
eci_4_electronegativity = ""
eci_5_electronegativity = ""
eci_6_electronegativity = ""
eci_1_group = StringVar()
eci_2_group = StringVar()
eci_3_group = StringVar()
eci_4_group = StringVar()
eci_5_group = StringVar()
eci_6_group = StringVar()
eci_1_M_qty = StringVar()
eci_2_M_qty = StringVar()
eci_3_M_qty = StringVar()
eci_4_M_qty = StringVar()
eci_5_M_qty = StringVar()
eci_6_M_qty = StringVar()
eci_1_mass = DoubleVar()
eci_2_mass = DoubleVar()
eci_3_mass = DoubleVar()
eci_4_mass = DoubleVar()
eci_5_mass = DoubleVar()
eci_6_mass = DoubleVar()
eci_1_name = StringVar()
eci_2_name = StringVar()
eci_3_name = StringVar()
eci_4_name = StringVar()
eci_5_name = StringVar()
eci_6_name = StringVar()
eci_1_Oxidation_State = StringVar()
eci_2_Oxidation_State = StringVar()
eci_3_Oxidation_State = StringVar()
eci_4_Oxidation_State = StringVar()
eci_5_Oxidation_State = StringVar()
eci_6_Oxidation_State = StringVar()
eci_1_qty = DoubleVar()
eci_2_qty = StringVar()
eci_3_qty = StringVar()
eci_4_qty = StringVar()
eci_5_qty = StringVar()
eci_6_qty = StringVar()
eci_1_type = StringVar()
eci_2_type = StringVar()
eci_3_type = StringVar()
eci_4_type = StringVar()
eci_5_type = StringVar()
eci_6_type = StringVar()
eci_1_units = StringVar()
eci_2_units = StringVar()
eci_3_units = StringVar()
eci_4_units = StringVar()
eci_5_units = StringVar()
eci_6_units = StringVar()
eci_1_valence = StringVar()
eci_2_valence = StringVar()
eci_3_valence = StringVar()
eci_4_valence = StringVar()
eci_5_valence = StringVar()
eci_6_valence = StringVar()
eci_1_temp_units = StringVar()
eci_2_temp_units = StringVar()
eci_3_temp_units = StringVar()
eci_4_temp_units = StringVar()
eci_5_temp_units = StringVar()
eci_6_temp_units = StringVar()
eci_temp_1_qty = DoubleVar()
eci_temp_2_qty = DoubleVar()
eci_temp_3_qty = DoubleVar()
eci_temp_4_qty = DoubleVar()
eci_temp_5_qty = DoubleVar()
eci_temp_6_qty = DoubleVar()
eci_1_press_units = StringVar()
eci_2_press_units = StringVar()
eci_3_press_units = StringVar()
eci_4_press_units = StringVar()
eci_5_press_units = StringVar()
eci_6_press_units = StringVar()
eci_press_1_qty = DoubleVar()
eci_press_2_qty = DoubleVar()
eci_press_3_qty = DoubleVar()
eci_press_4_qty = DoubleVar()
eci_press_5_qty = DoubleVar()
eci_press_6_qty = DoubleVar()
energy_amount = DoubleVar()

def Initialize_default_T_and_P():
    ''' Set the initial values for temperature and pressure used
    to determine if an eci starts as a solid, liquid, or gas. '''
    cb_1_Temp_Units.set("C")
    e_Temp_Qty_1.delete(0, END)
    e_Temp_Qty_1.insert(0, 25)
    cb_1_Press_Units.set("ATM")
    e_Press_Qty_1.delete(0, END)
    e_Press_Qty_1.insert(0, 1.000)
    Init_default_T_and_P = TRUE

def Set_default_T_and_P():
    ''' User should re-set the initial values for temperature and pressure
    used to determine if an eci starts as a solid, liquid, or gas. '''
    print('Input the default units and quantities you want to use.')
    default_temp_units = cb_1_Temp_Units.get()
    default_temp_qty = e_Temp_Qty_1.get()
    default_press_units = cb_1_Press_Units.get()
    default_press_qty = e_Press_Qty_1.get()
    #print('default_temp_units are ', default_temp_units)
    #print('default_temp_qty is ', default_temp_qty)
    #print('default_press_units are ', default_press_units)
    #print('default_press_qty is ', default_press_qty)


''' Initialize values -- because I have need to do that in other programs. '''
cb_1_type = ""  # elements compounds ions
cb_2_type = ""
cb_3_type = ""
cb_4_type = ""
cb_5_type = ""
cb_6_type = ""

# *** End constants and variables

# *** Start function descriptions
def describe_eci_frame():
    ''' An eci refers to an item that is either an element, a compound, or an ion.
    A frame refers to a group of eci related widgets and the variables associated with an eci.
    There are six eci frames in the program that are used to gather, store, and display information
    about each eci. Each eci also has a related dictionary that stores variables that are displayed,
    used for calculations, and used to create a record of a selected process.
    Some dictionary variables will have display units and quantities that differ from the units and quantities
    actually used in equations to calculate other values which will be displayed in other widgets.
    For example, user may enter Temperature units as F, but the program uses C to calculate values. '''

def describe_record_structure():
    ''' A record is used to store and retrieve informamtion about a step in a process.
    A whole process will consist of a series of steps.
    Each record will include information about a compound, a process, an environment,
    all the non-null information in each of the six eci_frames, information about
    equipment, energy, catalysts, side effects, a description of information used to perform
    the step of the process (a history of intermediate steps),
    and other information relevant to the process.
    '''

def describe_environments():
    ''' There are three environments.
    In the laboratory environment, almost anything is possible, and everything needs to be explained.
    In the industry environment, only existing industrial processes are described.
    In the nature environment, only existing natural processes are described.
    '''
def describe_other_variables():
    ''' Every process uses ecergy and has side effects.
    Almost all processes use equipment and tools, have products and by-products.
    Many chemical processes use catalysts.
    All the information about these variables needs to be included in each process record.
    '''

''' All the select_eci_type functions work. User selects the type eci and 
the function loads the appropriate elements,compounds or ions in the symbol/formula
combo boxes and their names in the names combo boxes. '''

def select_eci_1_type(eventObject):
    '''
    Use these comboboxes to load the correct symbols/formulae and names
    in the associated comboboxes
    '''
    cb_1_type = cb_Select_CB1.get()  # use cb_1_type as a local variable to improve readability
    eci_d['eci_1']['eci_type'] = cb_Select_CB1.get()
    print("eci_d['eci_1']['eci_type'] is ", eci_d['eci_1']['eci_type'])
    print("cb_1_type is ", cb_1_type)
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


def select_eci_2_type(eventObject):
    cb_2_type = cb_Select_CB2.get()
    print("cb_2_type is ", cb_2_type)
    eci_d['eci_2']['eci_type'] = cb_Select_CB2.get()
    if cb_2_type == 'elements':
        cb_eci_2['values'] = elements_symbols_list
        cb_eci_2_N['values'] = elements_name_list
    elif cb_2_type == 'compounds':
        cb_eci_2['values'] = compound_symbols_list
        cb_eci_2_N['values'] = compound_names_list
    elif cb_2_type == 'ions':
        cb_eci_2['values'] = ion_symbols_list
        cb_eci_2_N['values'] = ion_names_list
    else:
        print("Error is select_eci_2_type")


def select_eci_3_type(eventObject):
    cb_3_type = cb_Select_CB3.get()
    print("cb_3_type is ", cb_3_type)
    eci_d['eci_3']['eci_type'] = cb_Select_CB3.get()
    if cb_3_type == 'elements':
        cb_eci_3['values'] = elements_symbols_list
        cb_eci_3_N['values'] = elements_name_list
    elif cb_3_type == 'compounds':
        cb_eci_3['values'] = compound_symbols_list
        cb_eci_3_N['values'] = compound_names_list
    elif cb_3_type == 'ions':
        cb_eci_3['values'] = ion_symbols_list
        cb_eci_3_N['values'] = ion_names_list
    else:
        print("Error is select_eci_3_type")


def select_eci_4_type(eventObject):
    cb_4_type = cb_Select_CB4.get()
    print("cb_4_type is ", cb_4_type)
    eci_d['eci_4']['eci_type'] = cb_Select_CB4.get()
    if cb_4_type == 'elements':
        cb_eci_4['values'] = elements_symbols_list
        cb_eci_4_N['values'] = elements_name_list
    elif cb_4_type == 'compounds':
        cb_eci_4['values'] = compound_symbols_list
        cb_eci_4_N['values'] = compound_names_list
    elif cb_4_type == 'ions':
        cb_eci_4['values'] = ion_symbols_list
        cb_eci_4_N['values'] = ion_names_list
    else:
        print("Error is select_eci_4_type")


def select_eci_5_type(eventObject):
    cb_5_type = cb_Select_CB5.get()
    print("cb_5_type is ", cb_5_type)
    eci_d['eci_5']['eci_type'] = cb_Select_CB5.get()
    if cb_5_type == 'elements':
        cb_eci_5['values'] = elements_symbols_list
        cb_eci_5_N['values'] = elements_name_list
    elif cb_5_type == 'compounds':
        cb_eci_5['values'] = compound_symbols_list
        cb_eci_5_N['values'] = compound_names_list
    elif cb_5_type == 'ions':
        cb_eci_5['values'] = ion_symbols_list
        cb_eci_5_N['values'] = ion_names_list
    else:
        print("Error is select_eci_5_type")


def select_eci_6_type(eventObject):
    cb_6_type = cb_Select_CB6.get()
    print("cb_6_type is ", cb_6_type)
    eci_d['eci_6']['eci_type'] = cb_Select_CB6.get()
    if cb_6_type == 'elements':
        cb_eci_6['values'] = elements_symbols_list
        cb_eci_6_N['values'] = elements_name_list
    elif cb_6_type == 'compounds':
        cb_eci_6['values'] = compound_symbols_list
        cb_eci_6_N['values'] = compound_names_list
    elif cb_6_type == 'ions':
        cb_eci_6['values'] = ion_symbols_list
        cb_eci_6_N['values'] = ion_names_list
    else:
        print("Error is select_eci_6_type")


''' Start defining process and chemistry related functions '''


def create_record():
    ''' print("Pressed create_record button") '''


def get_record():
    ''' print("Pressed get_record button") '''


def retrieve_record():
    ''' print("Pressed retrieve_record button") '''


def previous_record():
    ''' print("Pressed previous_record button") '''


def next_record():
    ''' print("Pressed next_record button") '''


def update_record():
    ''' print("Pressed update_record button") '''


def process_selected(eventObject):
    """ print("process_selected") """
    # if process_selected == Calculate:
    # Change the following message to a window with instructions.
    #showinfo(title=None, message="To calculate eci variables, enter an element type and symbol and a mole quantity.")
    #tkMessageBox.showinfo(message='Hello')

def check_entry_changes():
    '''
    When an entry is made, check the value and assign it to an eci dictionary field.
    '''
    '''eci_1_d = dict(eci = 'eci_1', eci_type = "", name ="", column = "", electronegativity = "", _group = "",
                 display_qty = "", qty = "", M_qty = "" , mass = "", Oxidation_State ="", display_units = "", units = "", valence = "",
                 display_temp_units= "", display_temp_qty="", display_press_units= "", display_press_qty= "",
                 temp_units= "", temp_qty="", press_units= "", press_qty= "")
    '''
    print("In check_entry_changes")

    eci_1_type = cb_Select_CB1.get()
    eci_1 = cb_eci_1.get()
    eci_1_qty = e_eci_1_qty.get()
    eci_1_units = cb_eci_1_units.get()
    eci_d['eci_1']['eci'] = eci_1
    eci_d['eci_1']['type'] = eci_1_type
    if eci_1_units == "":
        cb_eci_1_units.set('grams')
    eci_d['eci_1']['display_units'] = cb_eci_1_units.get()
    eci_d['eci_1']['display_temp_units'] = cb_1_Temp_Units.get()
    eci_d['eci_1']['display_temp_qty'] = e_Temp_Qty_1.get()
    eci_d['eci_1']['display_press_units'] = cb_1_Press_Units.get()
    eci_d['eci_1']['display_press_qty'] = e_Press_Qty_1.get()
    if eci_1_type == 'elements':
        eci_1_mass = getdouble(db[eci_1]['mass'])   # Get element mass from the dictionary of element dictionaries
        eci_d['eci_1']['mass'] = getdouble(db[eci_1]['mass'])   #set the eci_frame mass field to the element mass
        ''' Need to move the following to a separate function because qty may be input or calculated
            or qualify it as an imput or a calculated value. Won't it normally be a calculated value? '''
        eci_d['eci_1']['display_qty'] = e_eci_1_qty.get()

        #eci_1_M_qty = getdouble(db[eci_1]['mass'])  # don't use float due to precision errors
        eci_1_M_qty = getdouble(e_eci_1_M_qty.get())
        m_mass = eci_1_M_qty * getdouble(db[eci_1]['mass'])
        e_eci_1_qty.insert(0, m_mass)   #eci_1_mass)
        print("m_mass is ", m_mass)
        print("m_mass is ",  getdouble(eci_1_M_qty) * getdouble(db[eci_1]['mass'])) #getdouble(e_eci_1_M_qty.get()) eci_1_M_qty


    elif eci_1_type == 'compounds':
        pass
        ''' Compounds and ions don't currently have a mass property '''
        #eci_1_mass = getdouble(c_db[eci_1]['mass'])
        #e_eci_1_qty.insert(0, eci_1_mass)
    elif eci_1_type == 'ions':
        pass
        ''' Compounds and ions don't currently have a mass property '''
        #eci_1_mass = getdouble(i_db[eci_1]['mass'])
        #e_eci_1_qty.insert(0, eci_1_mass)

    #print("e_eci_1_qty.get() is ", e_eci_1_qty.get())
    #print("eci_db['eci_1']['qty'] is ", eci_d['eci_1']['qty'])
    #print("e_eci_1_M_qty.get() is ", e_eci_1_M_qty.get())
    #print("eci_1_qty is ", e_eci_1_qty.get())  # eci_1_qty is  PY_VAR54
    #print("eci_db['eci_1']['qty'] is ", eci_1_qty)


    #The following works.
    '''
    total_mass = getdouble(e_eci_1_qty.get()) * eci_1_mass  # float(db[eci_1]['mass'])
    print("total_mass is ", total_mass)
    eci_d['eci_1']['qty'] = total_mass
    print("eci_db['eci_1']['qty'] ", eci_d['eci_1']['qty'])
    '''

def Continue():
    ''' A button/function to continue whatever process was selected. '''
    process_selected = cb_Select_Process.get()
    print("Process selected is ", process_selected)
    # check_entry_changes()
    #
    if process_selected == "Acid_Base":
        ''' Continue the Acid_Base process '''
        Acid_Base()
    elif process_selected == "Balance_Equation":
        Balance_Equation()
    elif process_selected == "Calculate":
        ''' Continue the Calculate process '''
        check_entry_changes()
        #calculate()
    elif process_selected == "Decompose":
        """ Continue the Decompose process """
        Decompose()
    elif process_selected == "Set_default_T_and_P":
        """ Continue the Initialize_default_T_and_P process """
        #if Init_default_T_and_P == FALSE:
        #    pdb.set_trace()
        #    Initialize_default_T_and_P()
        #    Init_default_T_and_P == TRUE
        set_t_and_p_inst = "Set the default temperature and pressure settings you want to use" \
                           "for the current process. Select Set_default_T_and_P from the Process " \
                           "combobox, then select/set the temperature and pressure units and quantities" \
                           "in the first eci frame. Then press the Continue button. After you have set these" \
                           "defaults, select the next process. "
        e_Explanation.insert(END, set_t_and_p_inst)
        Set_default_T_and_P()
    elif process_selected == "Oxidation_Reduction":
        """ Continue the Oxidation_Reduction process """
        Oxidation_Reduction()
    elif process_selected == "Metathesis":
        """ Continue the Metathesis process """
        Metathesis()
    elif process_selected == "Oxidation_Rate":
        """ Continue the Oxidation_Rate process """
        Oxidation_Rate()
    elif process_selected == "Parse_Reactants":
        ''' There is a general procedure used to prove parse works,
        and a procedure tied to the eci_1 combobox. '''
        Parse_Reactants()
    elif process_selected == "Parse_Products":
        ''' There is a general procedure used to prove parse works,
        and a procedure tied to the eci_1 combobox. '''
        Parse_Products()
    elif process_selected == "Precipitation":
        """ Continue the Precipitation process """
        Precipitation()
    elif process_selected == "Reduction":
        """ Continue the Reduction process """
        Reduction()
    elif process_selected == "Refine":
        """ Continue the Refine process """
        Refine()
    elif process_selected == "Synthesis":
        """ Continue the Synthesis process """
        Synthesis()
    else:
        print("No process has been selected in Continue selection of process")
    # CountElements()
    # AlphabetizeElements()
    # eci_1 = cb_eci_1.get()
    # print("Process selected is " , process_selected)
    # print('eci_1 = ', eci_1)
    # print("Pressed Continue button")

def Balance_Equation():
    be = ""
    print("Started Balance_Equation")
    e_Explanation.insert(END, "Started Balance_Equation")
    e_Explanation.insert(END, '\n')
    e_Explanation.insert(END, "Step 1: ")
    if cb_eci_1.get() != "":
        be = cb_eci_1.get()
        print("cb_eci_1 is ", be)
        #e_Explanation.insert(END, cb_eci_1.get())
    if cb_eci_2.get() != "":
        be = be + " + " + cb_eci_2.get()
        print("cb_eci_2 is ", be)
        #e_Explanation.insert(END, be)
    if cb_eci_3.get() != "":
        be = be + " + " + cb_eci_3.get()
        print("cb_eci_3 is ", be)
        #e_Explanation.insert(END, be)
    if cb_eci_4.get() != "":
        be = be + " --> " + cb_eci_4.get()
        print("cb_eci_4 is ", be)
        #e_Explanation.insert(END, be)
    if cb_eci_5.get() != "":
        be = be + " + " + cb_eci_5.get()
        print("cb_eci_5 is ", be)
        #e_Explanation.insert(END, be)
    if cb_eci_6.get() != "":
        be = be + " + " + cb_eci_6.get()
        print("cb_eci_6 is ", be)
    e_Explanation.insert(END, be)

def calculate():
    ''' A step toward performing general chemistry related calculations.
    There will be many calculations done by the program.
    They will be separated into separate functions as they are developed.'''
    #Message.config(font, titlefont)
    #showinfo.__setattr__(font, 'Helvetica 12') # Doesn't work
    #mb.Dialog.show(title=None, message="To calculate eci variable, senter an element type and symbol and a mole quantity.")
    #showinfo(title=None, message="To calculate eci variables, enter an element type and symbol and a mole quantity.")
    #check_entry_changes()
    calculate_eci_variables()


def calculate_eci_variables():
    print('In process calculate_eci_variables')
    '''
    A step toward calculating variables associated with an eci.
    This one simply gets an element symbol, retrieves the atomic mass,
    and the mole quantity, calculates the quantity in grams, and
    inserts that quantity into the eci quantity entry box.
    '''
    '''msg_Calculate_eci_variables = Label(text=showinfo(title=None, message=None, **options), enter an element type and symbol and a mole quantity.")
    msg_Calculate_eci_variables.config(font=labelfont)
    msg_Calculate_eci_variables.grid(row=8, column=0)
    '''
    ''' What will standard calculation units be? Set them in the eci frame dictionary.
    If a temp or press units or quantity changes, change the value in the eci frame dictionary.
    If there is a mole quantity, assume it is correct and change the regular quantity.
    Implement controlled changes in mole and regular quantities. For example,if a mole quantity 
    changes, calculate the regular quantity. If that quantity already exists in the quantity box,
    do not change it. Otherwise change it. Likewise, if the mole quantity is the same, do not change it.
    After each change, the values in the dicionary need to be set. Check the logic, it may be better
    to verify changes in the dictionary values and then change the mole and regular quantities
    rather than delegating the change control to the widgets. Widgets changes update the directory 
    and the directory updates the widgets.
    '''
    ''' The following process currently only works for eci_1'''
    check_entry_changes()
    print('In process calculate_eci_variables after check_entry_changes')
    #eci_1 = cb_eci_1.get()
    #print('eci_1 is ', eci_1)
    #eci_1_M_qty = e_eci_1_M_qty.get()
    ''' e_eci_1_qty.insert(0, eci_1_M_qty) WORKS!!! '''
    #print('eci_1_M_qty is ', eci_1_M_qty)
    #eci_1_units = cb_eci_1_units.get()
    #print('eci_1_units are ', eci_1_units)
    if eci_1_units == 'liters(l)' or eci_1_units == 'liters(g)' or eci_1_units == 'ml(l)' or eci_1_units == 'ml(g)':
            #and not eci_1_M_qty == 0.0:
        vol_from_prt()

    #else:
    #if eci_1_units == 'grams' and not eci_1_M_qty == "":
    ''' eci_1_mass = DoubleVar() '''
    #eci_1_mass = getdouble(db[eci_1]['mass'])
    #eci_1_mass = db[eci_1]['mass'].get()  #eci_1('mass')   #
    eci_1_M_qty = getdouble(e_eci_1_M_qty.get())
    #print('eci_1_mass = ', getdouble(db[eci_1]['mass']))   #eci_1('mass'))    #eci_1_mass)
    print('eci_1_M_qty = ', getdouble(e_eci_1_M_qty.get()))
    #m_mass = eci_1_M_qty * 26    #getdouble(db[eci_1]['mass'])  #26   #eci_1_mass getdouble(db[eci_1]['mass'])
    #e_eci_1_qty.delete(0, END)
    #e_eci_1_qty.insert(0, m_mass)
    #e_Explanation.insert(END, m_mass)
    #print('m_mass is ', m_mass)

    #if not eci_1_M_qty == "":  ''' Have not yet incorporated temp and press into calculate

    #    eci_1_temp_units = cb_1_Temp_Units.get()
    #    print('eci_1_temp_units are ', eci_1_temp_units)
    #    eci_1_press_units_units = cb_1_Press_Units.get()
    #    print('eci_1_press_units_units are ', eci_1_press_units_units)
        #eci_1_temp_units = cb_1_Temp_Units.get()
        #e_Temp_Qty_1.delete(0, END)
        #e_Temp_Qty_1.insert(0, 288)
        #eci_1_press_units = "ATM"
        #e_Press_Qty_1.delete(0, END)
        #e_Press_Qty_1.insert(0, 0.967)
        # vol_from_prt()    ''' Not yet ready to incorporate gas calculations into calculate process

def Oxidation_Reduction():
    """This function has been entered after elements have been selected and the Continue button pressed."""
    #e_Explanation.insert(tk.END, "Oxidation_Reduction process entered\n")
    count = CountElements()
    if count == 3:
        e_Explanation.insert(tk.END, "Oxidation_Rate can't currently process three elements.\n")
    elif count == 2:
        Oxidation_Rate_Two_Elements()
        #cb_1_type = cb_Select_CB1.get()
        #cb_2_type = cb_Select_CB2.get()
    else: e_Explanation.insert(tk.END, "Oxidation_Rate failed at count equal two elements.\n")

    ''' The following will not be used until compound, ions, or three elements are being considered
    if cb_1_type == 'elements' and cb_2_type == 'elements' and cb_3_type == 'elements' or cb_3_type == "":
        Oxidation_Rate_Two_Elements()
    elif cb_1_type == 'compounds' or cb_2_type == 'compounds' and cb_3_type == 'compounds':
        e_Explanation.insert(tk.END, "Oxidation_Rate can't currently process compounds.\n")
        #Oxidation_Rate_Compounds()
    elif cb_1_type == 'ions' or cb_2_type == 'ions' and cb_3_type == 'ions':
        e_Explanation.insert(tk.END, "Oxidation_Rate can't currently process ions.\n")
        Oxidation_Rate_Ions()
    else:
        e_Explanation.insert(tk.END, "Oxidation_Rate process failed.\n")
    '''
    '''
    Oxidation_Rate()
    cb_1_type = cb_Select_CB1.get()  # Get the selected type of: element, compound, or ion
    print('eci_1_type = ', cb_1_type)
    eci_1 = cb_eci_1.get()
    print('eci_1 = ', eci_1)
    if cb_1_type == 'elements':
        ''''''  *** The following works! ''''''

        # eci_db['eci_1']['name']
        eci_d['eci_1']['name'] = db[eci_1]['name']
        # eci_db[eci_1]['name'] = db[eci_1]['name']
        print("eci_db['eci_1']['name'] is ", eci_d['eci_1']['name'])
        eci_1_name = db[eci_1]['name']
        print("db[eci_1]['name'] is ", eci_1_name)

        eci_1_col = db[eci_1]['column']
        eci_1_mass = db[eci_1]['mass']
        eci_1_valence = db[eci_1]['valence']
        eci_d['eci_1']['column'] = db[eci_1]['column']
        eci_d['eci_1']['mass'] = db[eci_1]['mass']
        eci_d['eci_1']['valence'] = db[eci_1]['valence']
        print("eci_db['eci_1']['column'] is ", eci_d['eci_1']['column'])
        print("eci_db['eci_1']['mass'] is ", eci_d['eci_1']['mass'])
        print("eci_db['eci_1']['valence'] is ", eci_d['eci_1']['valence'])
        # print("db[eci_1]['name'] is ", eci_1_name)
        # print("db[eci_1]['column'] is ", eci_1_col)
        # print("db[eci_1]['mass'] is ", eci_1_mass)
        # print("db[eci_1]['valence'] is ", eci_1_valence)
        # print(eci_1_valence)   # Prints out the variable #str(eci_1).affinity
    elif cb_1_type == 'compounds':
        # eci_1 = cb_eci_1.get()
        # print('eci_1 = ', eci_1)
        e_Explanation.insert(tk.END, "Oxidation_Reduction can't process compounds entered\n")
        print("Oxidation_Reduction eci_1 can't process compounds yet")
    elif cb_1_type == 'ions':
        # eci_1 = cb_eci_1.get()
        # print('eci_1 = ', eci_1)
        e_Explanation.insert(tk.END, "Error in Oxidation_Reduction eci_1 can't process compounds yet")
    else:
        print("Oxidation_Reduction process eci_1 else clause")
    cb_2_type = cb_Select_CB2.get()  # Get the selected type of: element, compound, or ion
    print('eci_2_type = ', cb_2_type)
    if cb_2_type == 'elements':
        eci_2 = cb_eci_2.get()
        print('eci_2 = ', eci_2)
        ''''''  *** The following works! ''''''
        eci_2_name = db[eci_2]['name']
        eci_2_col = db[eci_2]['column']
        eci_2_mass = db[eci_2]['mass']
        eci_2_valence = db[eci_2]['valence']
        print("db[eci_2]['name'] is ", eci_2_name)
        print("db[eci_2]['column'] is ", eci_2_col)
        print("db[eci_2]['mass'] is ", eci_2_mass)
        print("db[eci_2]['valence'] is ", eci_2_valence)
        # print(eci_1_valence)   # Prints out the variable #str(eci_1).affinity
    elif cb_2_type == 'compounds':
        # eci_2 = cb_eci_2.get()
        # print('eci_2 = ', eci_2)
        print("Error in Oxidation_Reduction eci_2 can't process compounds yet")
    elif cb_2_type == 'ions':
        # eci_2 = cb_eci_2.get()
        # print('eci_2 = ', eci_2)
        print("Error in Oxidation_Reduction eci_2 can't process ions yet")
    else:
        print("Error in Oxidation_Reduction process eci_2 else clause")
    cb_3_type = cb_Select_CB3.get()  # Get the selected type of: element, compound, or ion
    print('eci_3_type = ', cb_3_type)
    eci_3 = cb_eci_3.get()
    print('eci_3 = ', eci_3)
    if cb_3_type == 'elements':
        # eci_3 = cb_eci_3.get()
        # print('eci_3 = ', eci_3)
        ''''''  *** The following works! ''''''
        eci_3_name = db[eci_3]['name']
        eci_3_col = db[eci_3]['column']
        eci_3_mass = db[eci_3]['mass']
        eci_3_valence = db[eci_3]['valence']
        print("db[eci_3]['name'] is ", eci_3_name)
        print("db[eci_3]['column'] is ", eci_3_col)
        print("db[eci_3]['mass'] is ", eci_3_mass)
        print("db[eci_3]['valence'] is ", eci_3_valence)
        # print(eci_1_valence)   # Prints out the variable #str(eci_1).affinity
    elif cb_3_type == 'compounds':
        # eci_3 = cb_eci_3.get()
        # print('eci_3 = ', eci_3)
        print("Error in Oxidation_Reduction eci_3 can't process compounds yet")
    elif cb_3_type == 'ions':
        # eci_3 = cb_eci_3.get()
        # print('eci_3 = ', eci_3)
        print("Error in Oxidation_Reduction eci_3 can't process ions yet")
    elif cb_3_type == "":
        pass
    else:
        e_Explanation.insert(tk.END, "Error in Oxidation_Reduction process eci_3 else clause\n")

    # if cb_eci_1.get() == 'elements':
    #    eci_1 = cb_eci_1.get()
    #    print('eci_1 = ', eci_1)
    #    print('eci_1_type = ', cb_eci_1.get())
    '''

def Precipitation():
    """ print("Pressed update_record button") """
    e_Explanation.insert(tk.END, "Precipitation process entered\n")
    # print("Precipitation process entered")


def Oxidation_Rate():   #Based on eci type, call appropriate Oxidation_Rate function
    ''' Synthesize elements into compounds or ions '''
    count = CountElements()
    if count == 3:
        e_Explanation.insert(tk.END, "Oxidation_Rate can't currently process three elements.\n")
    elif count == 2:
        cb_1_type = cb_Select_CB1.get()
        cb_2_type = cb_Select_CB2.get()
        #cb_3_type = cb_Select_CB3.get()
    else: e_Explanation.insert(tk.END, "Oxidation_Rate failed at count equal two elements.\n")

    ''' The following will not be used until compound, ions, or three elements are being considered '''
    if cb_1_type == 'elements' and cb_2_type == 'elements' and cb_3_type == 'elements' or cb_3_type == "":
        e_Explanation.insert(tk.END, "Oxidation_Rate can't currently process three elements.\n")
        #Oxidation_Rate_Three_Elements()
    elif cb_1_type == 'compounds' or cb_2_type == 'compounds' and cb_3_type == 'compounds':
        e_Explanation.insert(tk.END, "Oxidation_Rate can't currently process compounds.\n")
        #Oxidation_Rate_Compounds()
    elif cb_1_type == 'ions' or cb_2_type == 'ions' and cb_3_type == 'ions':
        e_Explanation.insert(tk.END, "Oxidation_Rate can't currently process ions.\n")
        #Oxidation_Rate_Ions()
    else:
        e_Explanation.insert(tk.END, "Oxidation_Rate process failed.\n")


''' Oxidation_Rate_Compounds and Oxidation_Rate_Ions are placeholders for future use as needed. '''


def Oxidation_Rate_Compounds():
    e_Explanation.insert(tk.END, "Entered Oxidation_Rate_Compounds has not yet been programmed.\n")


def Oxidation_Rate_Ions():
    e_Explanation.insert(tk.END, "Entered Oxidation_Rate_Ions has not yet been programmed.\n")


def Oxidation_Rate_Two_Elements():
    ''' This function has been entered after elements have been selected and the Continue button pressed.
    Each item is an element. Compounds and ions use a different function.
    It is necessary to get the valence and electronegativity values because the valence of some
    elements is determined by the relative electronegativity of the other elements.'''
    #e_Explanation.insert(tk.END, "Oxidation_Rate_Elements process entered\n")

    '''
    cb_1_type = cb_Select_CB1.get()
    cb_2_type = cb_Select_CB2.get()
    '''
    eci_1 = cb_eci_1.get()
    eci_2 = cb_eci_2.get()

    ''' if eci_db['eci_1']['eci_type'] == 'elements': is no longer needed because 
    all non-elements have been moved to another function. '''
    eci_1_valence = db[eci_1]['valence']
    eci_2_valence = db[eci_2]['valence']
    eci_1_electronegativity = db[eci_1]['electronegativity']
    eci_2_electronegativity = db[eci_2]['electronegativity']
    print('eci_1_valence is ', eci_1_valence)
    print('eci_2_valence is ', eci_2_valence)
    print("db[eci_1]['eci_1_electronegativity'] is ", eci_1_electronegativity)
    print("db[eci_2]['eci_2_electronegativity'] is ", eci_2_electronegativity)
    if eci_1_valence.isnumeric():
        ''' This section of code only works for metals that have single valence values. '''
        ''' Set the dictionary values. 
        Oxidation_State only has one value that is set for this case. 
        Other elements have multiple valence values, these will be dealt with later.
        '''
        eci_1_Oxidation_State = eci_1_valence
        db[eci_1]['valence'] = eci_1_valence
        db[eci_1]['Oxidation_State'] = eci_1_valence
        print("eci_1_Oxidation_State is ", eci_1_Oxidation_State)
        print("db[eci_1]['valence'] is numeric ", eci_1_valence)
        ''' eci_db['eci_2']['eci_type'] == 'elements': '''
        eci_2_valence = db[eci_2]['valence']
        if eci_2_valence.isnumeric() or eci_2_valence == "-1":
            ''' Now we can solve for the valences'''
            Solve_Two_Single_Valence_Compound(eci_1, eci_1_valence, eci_2, eci_2_valence)
        elif not eci_2_valence.isnumeric():
            print("In elif not eci_2_valence.isnumeric")
            eci_2_group = db[eci_2]['_group']
            if eci_2_group == "7A":
                print("db[eci_2]['_group'] is ", eci_2_group)
                #eci_1_electronegativity = db[eci_1]['electronegativity']
                #eci_2_electronegativity = db[eci_2]['electronegativity']
                #print("db[eci_1]['eci_1_electronegativity'] is ", eci_1_electronegativity)
                #print("db[eci_2]['eci_2_electronegativity'] is ", eci_2_electronegativity)
                if eci_1_electronegativity < eci_2_electronegativity:
                    eci_2_valence = -1
                    Solve_Two_Single_Valence_Compound(eci_1, eci_1_valence, eci_2, eci_2_valence)
                    eci_2_Oxidation_State = eci_2_valence
                    db[eci_2]['Oxidation_State'] = eci_2_Oxidation_State
                    print("eci_2_Oxidation_State is ", eci_2_Oxidation_State)
                    ''' The following can be moved to synthesis. '''
                    eci_1_M_qty = 1
                    e_eci_1_M_qty.delete(0)
                    e_eci_1_M_qty.insert(0, eci_1_M_qty)
                    eci_2_M_qty = eci_1_valence  # This is correct. Cross assign valences to quantities
                    e_eci_2_M_qty.delete(0, END)
                    e_eci_2_M_qty.insert(0, eci_2_M_qty)
                    ''' Set the type and value of the compound.'''
                    ''' These functions will be moved to other processes when they are defined. 
                    Oxidation_Rate_Elements will only store the oxidation states in the frame directories. '''
                    cb_4_type = "compound"
                    eci_4_type = "compound"
                    ''' Set a temporary variable to hold the formula variable
                    because the formula assumes quantity is 1, so it doen't need to be shown'''
                    eci_1a = eci_1
                    eci_2a = eci_2
                    if eci_2_valence == -1:
                        eci_1a = eci_1
                    elif not eci_2_valence == -1:
                        eci_1a = eci_1 + str(eci_2_valence)
                    if eci_1_valence == '1':
                        eci_2a = eci_2
                        print('eci_2a is ', eci_2a)
                    elif not eci_1_valence == '1':
                        eci_2a = eci_2 + str(eci_1_valence)
                    eci_4 = eci_1a + eci_2a
                    ''' *** Set cb_eci_4 selected item to eci_4 *** '''
                    cb_eci_4.set(eci_4)
                    e_eci_4_M_qty.delete(0, END)
                    e_eci_4_M_qty.insert(0, 1)
                    print("eci_4 is ", eci_4)
                    print("e_eci_1_M_qty is ", e_eci_1_M_qty.get())
                    print("e_eci_2_M_qty is ", e_eci_2_M_qty.get())
                elif eci_1_electronegativity > eci_2_electronegativity:
                    print(
                        "In Oxidation_Rate_Elements eci_2 group 7A -- eci_1_electronegativity > eci_2_electronegativity")
            elif eci_2_group == "6A":  # Will need to exclude Oxygen for some compounds
                print("In Oxidation_Rate_Elements eci_2_group == 6A.")
                db[eci_2]['_group'] = eci_2_group
                print("db[eci_2]['_group'] is ", eci_2_group)
                print("db[eci_1]['eci_1_electronegativity'] is ", eci_1_electronegativity)
                print("db[eci_2]['eci_2_electronegativity'] is ", eci_2_electronegativity)
                if eci_1_electronegativity < eci_2_electronegativity:
                    eci_2_valence = -2
                    eci_1_M_qty = -eci_2_valence
                    eci_2_M_qty = eci_1_valence
                    eci_2_Oxidation_State = eci_2_valence
                    print("eci_2_Oxidation_State is ", eci_2_Oxidation_State)
                    if eci_2_valence == -2 and eci_1_valence == "1":
                        print("if eci_2_valence == -2 and eci_1_valence == 1:")
                        print("eci_1 is", eci_1, "eci_2_valence is", eci_2_valence, "eci_2 is", eci_2)
                        eci_4 = eci_1 + str(abs(eci_2_valence)) + eci_2
                        e_eci_1_M_qty.delete(0)
                        e_eci_1_M_qty.insert(0, eci_1_M_qty)
                        eci_2_M_qty = eci_1_valence  # This is correct. Cross assign valences to quantities
                        e_eci_2_M_qty.delete(0, END)
                        e_eci_2_M_qty.insert(0, eci_2_M_qty)
                    elif -int(eci_2_valence) == int(eci_1_valence):
                        print("-eci_2_valence is", -eci_2_valence)
                        eci_4 = eci_1 + eci_2
                        e_eci_1_M_qty.delete(0)
                        e_eci_1_M_qty.insert(0, 1)
                        e_eci_2_M_qty.delete(0, END)
                        e_eci_2_M_qty.insert(0, 1)
                    elif not -int(eci_2_valence) == int(eci_1_valence):
                        eci_4 = eci_1 + str(-eci_2_valence) + eci_2 + str(eci_1_valence)
                        print("-int(eci_2_valence) is", -int(eci_2_valence))
                        print("int(eci_1_valence) is", int(eci_1_valence))
                        # eci_4 = eci_1 + eci_2 + eci_1_valence
                        e_eci_1_M_qty.delete(0)
                        e_eci_1_M_qty.insert(0, eci_1_M_qty)
                        eci_2_M_qty = eci_1_valence  # This is correct. Cross assign valences to quantities
                        e_eci_2_M_qty.delete(0, END)
                        e_eci_2_M_qty.insert(0, eci_2_M_qty)
                    ''' *** Set cb_eci_4 selected item to eci_4 *** '''
                    cb_eci_4.set(eci_4)
                    e_eci_4_M_qty.delete(0, END)
                    e_eci_4_M_qty.insert(0, 1)
                    print("eci_4 is ", eci_4)
                    eci_1_massa = float(eci_1_M_qty) * float(eci_1_mass)
                    print("eci_1_massa is ", eci_1_massa)
                    e_eci_1_qty.delete(0)
                    e_eci_1_qty.insert(0, eci_1_massa)
                    e_eci_2_qty.delete(0)
                    e_eci_2_qty.insert(0, float(eci_2_M_qty) * float(eci_2_mass))
                    # eci_1_M_qty = 1

            elif not eci_2_group == "6A" and not eci_2_group == "7A":
                print("In Oxidation_Rate_Elements not eci_2_group == 6A or 7A.")
                e_Explanation.insert(tk.END, "In Oxidation_Rate_Elements not eci_2_group == 6A or 7A.\n")
            elif eci_1_electronegativity > eci_1_electronegativity:
                e_Explanation.insert(tk.END, "In Oxidation_Rate_Elements eci_1_electronegativity > eci_1_electronegativity.\n")
    elif not eci_1_valence.isnumeric():  # if eci_1_valence is a string of valence values
        e_Explanation.insert(tk.END, "In Oxidation_Rate_Elements elif not eci_1_valence.isnumeric().\n")
        print("In Oxidation_Rate_Elements not eci_1_valence.isnumeri.")
    else:
        e_Explanation.insert(tk.END, "In Oxidation_Rate_Elements else clause -- no processing option worked.\n")
        e_Explanation.insert(tk.END, "In Oxidation_Rate process else clause\n")

def Solve_Two_Single_Valence_Compound(eci_1, eci_1_valence, eci_2, eci_2_valence):
    print('Entered Solve_Two_Single_Valence_Compound ', eci_1, eci_1_valence, eci_2, eci_2_valence)
    ''' Set the values in the eci frame dictionary. '''
    ''' The following demonstrate the direct assignments of values
    from the element dictionary to the frame dictionary. '''
    eci_d['eci_1']['eci'] = cb_eci_1.get()
    eci_d['eci_2']['eci'] = cb_eci_2.get()
    eci_d['eci_1']['eci_type'] = cb_Select_CB1.get()
    eci_d['eci_2']['eci_type'] = cb_Select_CB2.get()
    eci_1_name = db[eci_1]['name']
    eci_1_mass = db[eci_1]['mass']
    eci_1_group = db[eci_1]['_group']
    eci_1_valence = db[eci_1]['valence']
    eci_1_Oxidation_State = eci_1_valence
    eci_1_electronegativity = db[eci_1]['electronegativity']
    print("eci_db['eci_1']['eci'] is ", eci_d['eci_1']['eci'])
    print("eci_db['eci_2']['eci'] is ", eci_d['eci_2']['eci'])
    print("db[eci_1]['name'] is ", eci_1_name)
    print("db[eci_1]['mass'] is ", eci_1_mass)
    print("db[eci_1]['_group'] is ", eci_1_group)
    print("db[eci_1]['valence'] is ", eci_1_valence)
    print("eci_1_Oxidation_State is ", eci_1_Oxidation_State)
    print("db[eci_1]['electronegativity'] is ", eci_1_electronegativity)
    eci_2_name = db[eci_2]['name']
    eci_2_mass = db[eci_2]['mass']
    eci_2_group = db[eci_2]['_group']
    eci_2_valence = db[eci_2]['valence']
    eci_2_Oxidation_State = eci_2_valence
    db[eci_2]['valence'] = eci_2_valence
    db[eci_2]['Oxidation_State'] = eci_2_Oxidation_State
    eci_2_electronegativity = db[eci_2]['electronegativity']
    print("db[eci_2]['name'] is ", eci_2_name)
    print("db[eci_2]['_group'] is ", eci_2_group)
    print("db[eci_2]['valence'] is ", eci_2_valence)
    print("db[eci_2]['electronegativity'] is ", eci_2_electronegativity)
    print("db[eci_2]['valence'] is numeric ", eci_2_valence)
    print("eci_2_Oxidation_State is ", eci_2_Oxidation_State)
    eci_1_M_qty = 1
    e_eci_1_M_qty.delete(0)
    e_eci_1_M_qty.insert(0, eci_1_M_qty)
    eci_2_M_qty = eci_1_valence  # This is correct. Cross assign valences to quantities
    e_eci_2_M_qty.delete(0, END)
    e_eci_2_M_qty.insert(0, eci_2_M_qty)
    cb_4_type = "compound"
    eci_4_type = "compound"
    eci_1a = eci_1
    eci_2a = eci_2
    if eci_2_valence == "-1":
        eci_1a = eci_1
    elif not eci_2_valence == "-1":
        eci_1a = eci_1 + str(eci_2_valence)
    if eci_1_valence == '1':
        eci_2a = eci_2
        print('eci_2a is ', eci_2a)
    elif not eci_1_valence == '1':
        eci_2a = eci_2 + str(eci_1_valence)
    eci_4 = eci_1a + eci_2a
    ''' *** Set cb_eci_4 selected item to eci_4 *** '''
    cb_eci_4.set(eci_4)
    e_eci_4_M_qty.delete(0, END)
    e_eci_4_M_qty.insert(0, 1)
    print("eci_4 is ", eci_4)
    print("e_eci_1_M_qty is ", e_eci_1_M_qty.get())
    print("e_eci_2_M_qty is ", e_eci_2_M_qty.get())

def Oxidation_Rate_Three_Elements():
    ''' This function has been entered after elements have been selected and the Continue button pressed.
    Each item is an element. Compounds and ions use a different function.
    It is necessary to get the valence and electronegativity values because the valence of some
    elements is determined by the relative electronegativity of the other elements.'''
    #cb_eci_1_units.set('grams')
    #cb_eci_2_units.set('grams')
    #cb_eci_4_units.set('grams')

    #e_Explanation.insert(tk.END, "Oxidation_Rate_Elements process entered\n")

    '''
    cb_1_type = cb_Select_CB1.get()
    cb_2_type = cb_Select_CB2.get()
    cb_3_type = cb_Select_CB3.get()
    '''
    eci_1 = cb_eci_1.get()
    eci_2 = cb_eci_2.get()
    #eci_3 = cb_eci_3.get()
    ''' Set the values in the eci frame dictionary. '''
    #   What was this about? eci_1_temp_units = cb_1_Temp_Units.get()
    eci_d['eci_1']['eci'] = cb_eci_1.get()
    eci_d['eci_2']['eci'] = cb_eci_2.get()
    eci_d['eci_3']['eci'] = cb_eci_3.get()
    ''' The following demonstrate the direct assignments of frame values 
    from the element dictionary. '''
    eci_d['eci_1']['eci_type'] = cb_Select_CB1.get()
    eci_d['eci_2']['eci_type'] = cb_Select_CB2.get()
    eci_d['eci_3']['eci_type'] = cb_Select_CB3.get()
    print("eci_db['eci_1']['eci'] is ", eci_d['eci_1']['eci'])
    print("eci_db['eci_2']['eci'] is ", eci_d['eci_2']['eci'])
    print("eci_db['eci_3']['eci'] is ", eci_d['eci_3']['eci'])

    ''' if eci_db['eci_1']['eci_type'] == 'elements': is no longer needed
    because all non-elements have been moved to another function. '''
    ''' These lines get values of the element from the element dictionary. '''
    eci_1_name = db[eci_1]['name']
    eci_1_mass = db[eci_1]['mass']
    eci_1_group = db[eci_1]['_group']
    eci_1_valence = db[eci_1]['valence']
    eci_1_electronegativity = db[eci_1]['electronegativity']
    print("db[eci_1]['name'] is ", eci_1_name)
    print("db[eci_1]['mass'] is ", eci_1_mass)
    print("db[eci_1]['_group'] is ", eci_1_group)
    print("db[eci_1]['valence'] is ", eci_1_valence)
    print("db[eci_1]['electronegativity'] is ", eci_1_electronegativity)
    ''' if eci_db['eci_2']['eci_type'] == 'elements':  in no longer needed. '''
    eci_2_name = db[eci_2]['name']
    eci_2_mass = db[eci_2]['mass']
    eci_2_group = db[eci_2]['_group']
    eci_2_valence = db[eci_2]['valence']
    eci_2_electronegativity = db[eci_2]['electronegativity']
    print("db[eci_2]['name'] is ", eci_2_name)
    print("db[eci_2]['_group'] is ", eci_2_group)
    print("db[eci_2]['valence'] is ", eci_2_valence)
    print("db[eci_2]['electronegativity'] is ", eci_2_electronegativity)
    if eci_d['eci_3']['eci_type'] == 'elements':
        eci_3_name = db[eci_3]['name']
        eci_3_group = db[eci_3]['_group']
        eci_3_valence = db[eci_3]['valence']
        eci_3_electronegativity = db[eci_3]['electronegativity']
        print("db[eci_3]['name'] is ", eci_3_name)
        print("db[eci_3]['_group'] is ", eci_3_group)
        print("db[eci_3]['valence'] is ", eci_3_valence)
        print("db[eci_3]['electronegativity'] is ", eci_3_electronegativity)
        print("In Oxidation_Rate_Elements. Function does not yet work for 3 elements.")
    if eci_1_valence.isnumeric():
        ''' This process only works for metals that have single valence values. '''
        ''' Set the dictionary values. Valence may have multiple values. In these cases, it has only one value.
        Oxidation_State only has one value that is set for this case. '''
        eci_1_Oxidation_State = eci_1_valence
        db[eci_1]['valence'] = eci_1_valence
        db[eci_1]['Oxidation_State'] = eci_1_valence
        print("eci_1_Oxidation_State is ", eci_1_Oxidation_State)
        print("db[eci_1]['valence'] is numeric ", eci_1_valence)
        ''' eci_db['eci_2']['eci_type'] == 'elements': '''
        if eci_2_valence.isnumeric():
            eci_2_Oxidation_State = eci_2_valence
            db[eci_2]['valence'] = eci_2_valence
            db[eci_2]['Oxidation_State'] = eci_2_Oxidation_State
            print("db[eci_2]['valence'] is numeric ", eci_2_valence)
            print("eci_1_Oxidation_State is ", eci_1_Oxidation_State)
            ''' Now we can solve for the valences'''
        elif not eci_2_valence.isnumeric():
            print("In elif not eci_2_valence.isnumeric")
            if eci_2_group == "7A":
                print("db[eci_2]['_group'] is ", eci_2_group)
                if eci_1_electronegativity < eci_2_electronegativity:
                    eci_2_valence = -1
                    eci_2_Oxidation_State = eci_2_valence
                    db[eci_2]['Oxidation_State'] = eci_2_Oxidation_State
                    print("eci_2_Oxidation_State is ", eci_2_Oxidation_State)
                    ''' The following can be moved to synthesis. '''
                    eci_1_M_qty = 1
                    e_eci_1_M_qty.delete(0)
                    e_eci_1_M_qty.insert(0, eci_1_M_qty)
                    eci_2_M_qty = eci_1_valence  # This is correct. Cross assign valences to quantities
                    e_eci_2_M_qty.delete(0, END)
                    e_eci_2_M_qty.insert(0, eci_2_M_qty)
                    ''' Set the type and value of the compound.'''
                    ''' These functions will be moved to other processes when they are defined. 
                    Oxidation_Rate_Elements will only store the oxidation states in the frame directories. '''
                    cb_4_type = "compound"
                    eci_4_type = "compound"
                    ''' Set a temporary variable to hold the formula variable
                    because the formula assumes quantity is 1, so it doen't need to be shown'''
                    eci_1a = eci_1
                    eci_2a = eci_2
                    if eci_2_valence == -1:
                        eci_1a = eci_1
                    elif not eci_2_valence == -1:
                        eci_1a = eci_1 + str(eci_2_valence)
                    if eci_1_valence == '1':
                        eci_2a = eci_2
                        print('eci_2a is ', eci_2a)
                    elif not eci_1_valence == '1':
                        eci_2a = eci_2 + str(eci_1_valence)
                    eci_4 = eci_1a + eci_2a
                    ''' *** Set cb_eci_4 selected item to eci_4 *** '''
                    cb_eci_4.set(eci_4)
                    e_eci_4_M_qty.delete(0, END)
                    e_eci_4_M_qty.insert(0, 1)
                    print("eci_4 is ", eci_4)
                    print("e_eci_1_M_qty is ", e_eci_1_M_qty.get())
                    print("e_eci_2_M_qty is ", e_eci_2_M_qty.get())
                elif eci_1_electronegativity > eci_2_electronegativity:
                    print(
                        "In Oxidation_Rate_Elements eci_2 group 7A -- eci_1_electronegativity > eci_2_electronegativity")
            elif eci_2_group == "6A":  # Will need to exclude Oxygen for some compounds
                print("In Oxidation_Rate_Elements eci_2_group == 6A.")
                db[eci_2]['_group'] = eci_2_group
                print("db[eci_2]['_group'] is ", eci_2_group)
                if eci_1_electronegativity < eci_2_electronegativity:
                    eci_2_valence = -2
                    eci_1_M_qty = -eci_2_valence
                    eci_2_M_qty = eci_1_valence
                    eci_2_Oxidation_State = eci_2_valence
                    print("eci_2_Oxidation_State is ", eci_2_Oxidation_State)
                    if eci_2_valence == -2 and eci_1_valence == "1":
                        print("if eci_2_valence == -2 and eci_1_valence == 1:")
                        print("eci_1 is", eci_1, "eci_2_valence is", eci_2_valence, "eci_2 is", eci_2)
                        eci_4 = eci_1 + str(abs(eci_2_valence)) + eci_2
                        e_eci_1_M_qty.delete(0)
                        e_eci_1_M_qty.insert(0, eci_1_M_qty)
                        eci_2_M_qty = eci_1_valence  # This is correct. Cross assign valences to quantities
                        e_eci_2_M_qty.delete(0, END)
                        e_eci_2_M_qty.insert(0, eci_2_M_qty)
                    elif -int(eci_2_valence) == int(eci_1_valence):
                        print("-eci_2_valence is", -eci_2_valence)
                        eci_4 = eci_1 + eci_2
                        e_eci_1_M_qty.delete(0)
                        e_eci_1_M_qty.insert(0, 1)
                        e_eci_2_M_qty.delete(0, END)
                        e_eci_2_M_qty.insert(0, 1)
                    elif not -int(eci_2_valence) == int(eci_1_valence):
                        eci_4 = eci_1 + str(-eci_2_valence) + eci_2 + str(eci_1_valence)
                        print("-int(eci_2_valence) is", -int(eci_2_valence))
                        print("int(eci_1_valence) is", int(eci_1_valence))
                        # eci_4 = eci_1 + eci_2 + eci_1_valence
                        e_eci_1_M_qty.delete(0)
                        e_eci_1_M_qty.insert(0, eci_1_M_qty)
                        eci_2_M_qty = eci_1_valence  # This is correct. Cross assign valences to quantities
                        e_eci_2_M_qty.delete(0, END)
                        e_eci_2_M_qty.insert(0, eci_2_M_qty)
                    ''' *** Set cb_eci_4 selected item to eci_4 *** '''
                    cb_eci_4.set(eci_4)
                    e_eci_4_M_qty.delete(0, END)
                    e_eci_4_M_qty.insert(0, 1)
                    print("eci_4 is ", eci_4)
                    eci_1_massa = float(eci_1_M_qty) * float(eci_1_mass)
                    print("eci_1_massa is ", eci_1_massa)
                    e_eci_1_qty.delete(0)
                    e_eci_1_qty.insert(0, eci_1_massa)
                    e_eci_2_qty.delete(0)
                    e_eci_2_qty.insert(0, float(eci_2_M_qty) * float(eci_2_mass))
                    # eci_1_M_qty = 1

            elif not eci_2_group == "6A" and not eci_2_group == "7A":
                print("In Oxidation_Rate_Elements not eci_2_group == 6A or 7A.")
                e_Explanation.insert(tk.END, "In Oxidation_Rate_Elements not eci_2_group == 6A or 7A.\n")
            elif eci_1_electronegativity > eci_1_electronegativity:
                e_Explanation.insert(tk.END, "In Oxidation_Rate_Elements eci_1_electronegativity > eci_1_electronegativity.\n")
    elif not eci_1_valence.isnumeric():  # if eci_1_valence is a string of valence values
        e_Explanation.insert(tk.END, "In Oxidation_Rate_Elements elif not eci_1_valence.isnumeric().\n")
        print("In Oxidation_Rate_Elements not eci_1_valence.isnumeri.")
    else:
        e_Explanation.insert(tk.END, "In Oxidation_Rate_Elements else clause -- no processing option worked.\n")
        e_Explanation.insert(tk.END, "In Oxidation_Rate process else clause\n")

def Acid_Base():
    e_Explanation.insert(tk.END, "Acid_Base process entered\n")


def Decompose():
    e_Explanation.insert(tk.END, "Decompose process entered\n")


def Refine():
    e_Explanation.insert(tk.END, "Refine process entered\n")


def Metathesis():
    e_Explanation.insert(tk.END, "Metathesis process entered\n")


def Oxidization():
    e_Explanation.insert(tk.END, "Oxidization process entered\n")


def Reduction():
    e_Explanation.insert(tk.END, "Reduction process entered\n")


def Synthesis():
    '''
    Option 1. The user will select a product and the program will determine the reactants
    and the by-products.
    Option 2. The user will start by entering compounds and or elements in the left side of the
    GUI. Since there are so many possibilities, the user will need to specify the reactants and
    the primary product. Any other products will be considered by-products.
    Start by counting the number if reactants, alphabetize them, look up all the products
    that have any combination of those reactant elements, and fill the product combo box
    with that list. Since the program will not know which items will be products and which
    will be by-products, the list must contain all the compounds that have any of the reactants.
    All products that do not have those elements can be eliminated from the products box --
    even catalysts can be eliminated because they will be specified in a separate combo box.
    When a primary product has been selected, start the synthesis process by calculating the
    oxidation status, then

    '''
    e_Explanation.insert(tk.END, "Synthesis process entered\n")
    print("Synthesis process entered")
    CountElements()
    AlphabetizeElements()
    Oxidation_Rate()
    ''' Consider starting with a compound formula or name.'''

    cb_1_type = cb_Select_CB1.get()  # Get the selected type of: element, compound, or ion
    cb_2_type = cb_Select_CB2.get()
    cb_3_type = cb_Select_CB3.get()

    print("cb_1_type is", cb_1_type, "cb_2_type is", cb_2_type)

    # e_Explanation.insert(tk.END, "cb_1_type = cb_Select_CB1.get() step\n")

    eci_1 = cb_eci_1.get()
    eci_2 = cb_eci_2.get()
    # if cb_1_type == 'elements':
    #    eci_1_valence = db[eci_1]['valence']
    #    eci_2_valence = db[eci_2]['valence']
    #    print("eci_1 is", eci_1, "eci_2 is", eci_2)
    # eci_3 = cb_eci_3.get()
    # and eci_1 != ''
    # eci_1_valence = db[eci_1]['valence']
    # eci_3_group = db[eci_3]['_group']
    '''
    Cut out code that determines oxidation rate for elements.
    '''
    if cb_1_type == 'compounds':
        eci_1 = cb_eci_1.get()
        print('eci_1 is ', eci_1)
        eci_1_name = c_db[eci_1]['name']
        # eci_1_name = c_db[eci_1]['name']
        print('eci_1_name is ', eci_1_name)
        # e_Explanation.insert(tk.END, "In Synthesis, compounds.\n")


'''
        if eci_1_valence < eci_2_valence:
            balance = eci_2_valence / eci_1_valence
            print('Synthesis balance is:' ,balance)
        elif eci_2_valence > eci_1_valence:
            pass
        elif eci_2_valence == eci_1_valence:
            balance = 1
            print('Synthesis balance is:' ,balance)
'''


def setClassItem(eventObject):
    ''' If eci_1 or eci_2 are elements, set their quantity and name variables. '''
    e_Explanation.insert(tk.END, "setClassItem process entered\n")
    # print("setClassItem process entered")
    eci_1 = cb_eci_1.get()
    # print('eci_1 is', eci_1)
    # *** The following works!
    if cb_1_type == 'elements':
        eci_temp_1_qty = db[eci_1]['mass']
        eci_1_name = db[eci_1]['name']
        e_Explanation.insert(tk.END, "db[eci_1]['mass'] is ", eci_temp_1_qty, '\n')
        print("db[eci_1]['mass'] is ", eci_temp_1_qty)
        print("db[eci_1]['name'] is ", eci_1_name)
    elif cb_1_type == 'compounds':
        eci_1 = cb_eci_1.get()
        eci_1_name = c_db[eci_1]['name']
        print('eci_1 = ', eci_1)
        print("In setClassItem at elif compounds")


def setSelectedItemName(ComboboxSelected):
    cb_1_type = cb_Select_CB1.get()
    cb_2_type = cb_Select_CB2.get()
    cb_3_type = cb_Select_CB3.get()
    cb_4_type = cb_Select_CB4.get()
    cb_5_type = cb_Select_CB5.get()
    cb_6_type = cb_Select_CB6.get()
    eci_1 = cb_eci_1.get()
    eci_2 = cb_eci_2.get()
    eci_3 = cb_eci_3.get()
    eci_4 = cb_eci_4.get()
    eci_5 = cb_eci_5.get()
    eci_6 = cb_eci_6.get()
    eci_1_name = cb_eci_1_N.get()
    eci_2_name = cb_eci_2_N.get()
    eci_3_name = cb_eci_3_N.get()
    eci_4_name = cb_eci_4_N.get()
    eci_5_name = cb_eci_5_N.get()
    eci_6_name = cb_eci_6_N.get()
    # print("eci_1_name is ", eci_1_name)
    if cb_1_type == 'elements':
        try:
            if not eci_1_name == db[eci_1]['name']:
                cb_eci_1_N.set(db[eci_1]['name'])   # This works
                eci_1_d['eci'] = cb_eci_1.get()
                eci_1_d['name'] = db[eci_1]['name'] #cb_eci_1_N.get()
                eci_d['eci_1']['eci'] = eci_1
                eci_d['eci_1']['name'] = db[eci_1]['name'] #eci_1_name
                #print("eci_db['eci_1']['eci'] is ", eci_db['eci_1']['eci'])
                #print("eci_db['eci_1']['name'] is ", eci_db['eci_1']['name'])
                #print("eci_1_d['eci'] is ", eci_1_d['eci'])
                #print("eci_1_d['name'] is ", eci_1_d['name'])
        except KeyError:
            cb_eci_1_N.set("not a valid key")
    elif cb_1_type == 'compounds':
        try:
            if not eci_1_name == c_db[eci_1]['name']:
                cb_eci_1_N.set(c_db[eci_1]['name'])
                eci_1_d['eci'] = cb_eci_1.get()
                eci_1_d['name'] = eci_1_name
        except KeyError:
            cb_eci_1_N.set("not a valid key")
    elif cb_1_type == 'ions':
        try:
            if not eci_1_name == i_db[eci_1]['name']:
                cb_eci_1_N.set(i_db[eci_1]['name'])
                eci_1_d['eci'] = cb_eci_1.get()
                eci_1_d['name'] = eci_1_name
        except KeyError:
            cb_eci_1_N.set("not a valid key")
    if cb_2_type == 'elements':
        try:
            if not eci_2_name == db[eci_2]['name']:
                cb_eci_2_N.set(db[eci_2]['name'])
                eci_2_d['eci'] = cb_eci_2.get()
                eci_2_d['name'] = eci_2_name
        except KeyError:
            cb_eci_2_N.set("not a valid key")
    elif cb_2_type == 'compounds':
        try:
            if not eci_2_name == c_db[eci_2]['name']:
                cb_eci_2_N.set(c_db[eci_2]['name'])
                eci_2_d['eci'] = cb_eci_2.get()
                eci_2_d['name'] = eci_2_name
        except KeyError:
            cb_eci_2_N.set("not a valid key")
    elif cb_2_type == 'ions':
        try:
            if not eci_2_name == i_db[eci_2]['name']:
                cb_eci_2_N.set(i_db[eci_2]['name'])
                eci_2_d['eci'] = cb_eci_2.get()
                eci_2_d['name'] = eci_2_name
        except KeyError:
            cb_eci_2_N.set("not a valid key")
    if cb_3_type == 'elements':
        try:
            if not eci_3_name == db[eci_3]['name']:
                cb_eci_3_N.set(db[eci_3]['name'])
                eci_3_d['eci'] = cb_eci_3.get()
                eci_3_d['name'] = eci_3_name
        except KeyError:
            cb_eci_3_N.set("not a valid key")
    elif cb_3_type == 'compounds':
        try:
            if not eci_3_name == c_db[eci_3]['name']:
                cb_eci_3_N.set(c_db[eci_3]['name'])
                eci_3_d['eci'] = cb_eci_3.get()
                eci_3_d['name'] = eci_3_name
        except KeyError:
            cb_eci_3_N.set("not a valid key")
    elif cb_3_type == 'ions':
        try:
            if not eci_3_name == i_db[eci_3]['name']:
                cb_eci_3_N.set(i_db[eci_3]['name'])
                eci_3_d['eci'] = cb_eci_3.get()
                eci_3_d['name'] = eci_3_name
        except KeyError:
            cb_eci_3_N.set("not a valid key")
    if cb_4_type == 'elements':
        try:
            if not eci_4_name == db[eci_4]['name']:
                cb_eci_4_N.set(db[eci_4]['name'])
                eci_4_d['eci'] = cb_eci_4.get()
                eci_4_d['name'] = eci_4_name
        except KeyError:
            cb_eci_4_N.set("not a valid key")
    elif cb_4_type == 'compounds':
        try:
            if not eci_4_name == c_db[eci_4]['name']:
                cb_eci_4_N.set(c_db[eci_4]['name'])
                eci_4_d['eci'] = cb_eci_4.get()
                eci_4_d['name'] = eci_4_name
        except KeyError:
            cb_eci_4_N.set("not a valid key")
    elif cb_4_type == 'ions':
        try:
            if not eci_4_name == i_db[eci_4]['name']:
                cb_eci_4_N.set(i_db[eci_4]['name'])
                eci_4_d['eci'] = cb_eci_4.get()
                eci_4_d['name'] = eci_4_name
        except KeyError:
            cb_eci_4_N.set("not a valid key")
    if cb_5_type == 'elements':
        try:
            if not eci_5_name == db[eci_5]['name']:
                cb_eci_5_N.set(db[eci_5]['name'])
                eci_5_d['eci'] = cb_eci_5.get()
                eci_5_d['name'] = eci_5_name
        except KeyError:
            cb_eci_5_N.set("not a valid key")
    elif cb_5_type == 'compounds':
        try:
            if not eci_5_name == c_db[eci_5]['name']:
                cb_eci_5_N.set(c_db[eci_5]['name'])
                eci_5_d['eci'] = cb_eci_5.get()
                eci_5_d['name'] = eci_5_name
        except KeyError:
            cb_eci_5_N.set("not a valid key")
    elif cb_5_type == 'ions':
        try:
            if not eci_5_name == i_db[eci_5]['name']:
                cb_eci_5_N.set(i_db[eci_5]['name'])
                eci_5_d['eci'] = cb_eci_5.get()
                eci_5_d['name'] = eci_5_name
        except KeyError:
            cb_eci_5_N.set("not a valid key")
    if cb_6_type == 'elements':
        try:
            if not eci_6_name == db[eci_6]['name']:
                cb_eci_6_N.set(db[eci_6]['name'])
                eci_6_d['eci'] = cb_eci_6.get()
                eci_6_d['name'] = eci_6_name
        except KeyError:
            cb_eci_6_N.set("not a valid key")
    elif cb_6_type == 'compounds':
        try:
            if not eci_6_name == c_db[eci_6]['name']:
                cb_eci_6_N.set(c_db[eci_6]['name'])
                eci_6_d['eci'] = cb_eci_6.get()
                eci_6_d['name'] = eci_6_name
        except KeyError:
            cb_eci_6_N.set("not a valid key")
    elif cb_6_type == 'ions':
        try:
            if not eci_6_name == i_db[eci_6]['name']:
                cb_eci_6_N.set(i_db[eci_6]['name'])
                eci_6_d['eci'] = cb_eci_6.get()
                eci_6_d['name'] = eci_6_name
        except KeyError:
            cb_eci_6_N.set("not a valid key")
    else:
        pass  # print('In else clause of setSelectedItemName.')


def setSelectedItemFormula(ComboboxSelected):
    eci_1_N = cb_eci_1_N.get()
    eci_2_N = cb_eci_2_N.get()
    eci_3_N = cb_eci_3_N.get()
    eci_4_N = cb_eci_4_N.get()
    eci_5_N = cb_eci_5_N.get()
    eci_6_N = cb_eci_6_N.get()
    cb_1_type = cb_Select_CB1.get()
    cb_2_type = cb_Select_CB2.get()
    cb_3_type = cb_Select_CB3.get()
    cb_4_type = cb_Select_CB4.get()
    cb_5_type = cb_Select_CB5.get()
    cb_6_type = cb_Select_CB6.get()
    if cb_1_type == 'elements':
        if not eci_1 == element_names_Dict[cb_eci_1_N.get()]:
            cb_eci_1.set(element_names_Dict[cb_eci_1_N.get()])
    elif cb_1_type == 'compounds':
        if not eci_1 == compounds_names_dict[cb_eci_1_N.get()]:
            cb_eci_1.set(compounds_names_dict[cb_eci_1_N.get()])
        else:
            print('eci_1 is already correct and doesn\'t need to be reset')
    elif cb_1_type == 'ions':
        if not eci_1 == ion_names_dict[cb_eci_1_N.get()]:
            cb_eci_1.set(ion_names_dict[cb_eci_1_N.get()])
    if cb_2_type == 'elements':
        if not eci_2 == element_names_Dict[cb_eci_2_N.get()]:
            cb_eci_2.set(element_names_Dict[cb_eci_2_N.get()])
    elif cb_2_type == 'compounds':
        if not eci_2 == compounds_names_dict[cb_eci_2_N.get()]:
            cb_eci_2.set(compounds_names_dict[cb_eci_2_N.get()])
    elif cb_2_type == 'ions':
        if not eci_2 == ion_names_dict[cb_eci_2_N.get()]:
            cb_eci_2.set(ion_names_dict[cb_eci_2_N.get()])
    if cb_3_type == 'elements':
        if not eci_3 == element_names_Dict[cb_eci_3_N.get()]:
            cb_eci_3.set(element_names_Dict[cb_eci_3_N.get()])
    elif cb_3_type == 'compounds':
        if not eci_3 == compounds_names_dict[cb_eci_3_N.get()]:
            cb_eci_3.set(compounds_names_dict[cb_eci_3_N.get()])
    elif cb_3_type == 'ions':
        if not eci_3 == ion_names_dict[cb_eci_3_N.get()]:
            cb_eci_3.set(ion_names_dict[cb_eci_3_N.get()])
    if cb_4_type == 'elements':
        if not eci_4 == element_names_Dict[cb_eci_4_N.get()]:
            cb_eci_4.set(element_names_Dict[cb_eci_4_N.get()])
    elif cb_4_type == 'compounds':
        if not eci_4 == compounds_names_dict[cb_eci_4_N.get()]:
            cb_eci_4.set(compounds_names_dict[cb_eci_4_N.get()])
    elif cb_4_type == 'ions':
        if not eci_4 == ion_names_dict[cb_eci_4_N.get()]:
            cb_eci_4.set(ion_names_dict[cb_eci_4_N.get()])
    if cb_5_type == 'elements':
        if not eci_5 == element_names_Dict[cb_eci_5_N.get()]:
            cb_eci_5.set(element_names_Dict[cb_eci_5_N.get()])
    elif cb_5_type == 'compounds':
        if not eci_5 == compounds_names_dict[cb_eci_5_N.get()]:
            cb_eci_5.set(compounds_names_dict[cb_eci_5_N.get()])
    elif cb_5_type == 'ions':
        if not eci_5 == ion_names_dict[cb_eci_5_N.get()]:
            cb_eci_5.set(ion_names_dict[cb_eci_5_N.get()])
    if cb_6_type == 'elements':
        if not eci_6 == element_names_Dict[cb_eci_6_N.get()]:
            cb_eci_6.set(element_names_Dict[cb_eci_6_N.get()])
    elif cb_6_type == 'compounds':
        if not eci_6 == compounds_names_dict[cb_eci_6_N.get()]:
            cb_eci_6.set(compounds_names_dict[cb_eci_6_N.get()])
    elif cb_6_type == 'ions':
        if not eci_6 == ion_names_dict[cb_eci_6_N.get()]:
            cb_eci_6.set(ion_names_dict[cb_eci_6_N.get()])


def eci_units_selected(*arg):
    ''' If gas units are selected, the user needs to fill in temperature and pressure
    units and amounts. This procedure sets default values.
    The user can reset the displayed units and quantities, but they will be converted into
    the units and quantities actually used to calculate quantities used by the program.  '''
    print("In process eci_units_selected")
    #print("cb_eci_1_units.get() is ", cb_eci_1_units.get())

    eci_1_units = cb_eci_1_units.get()
    eci_2_units = cb_eci_2_units.get()
    eci_3_units = cb_eci_3_units.get()
    eci_4_units = cb_eci_4_units.get()
    eci_5_units = cb_eci_5_units.get()
    eci_6_units = cb_eci_6_units.get()
    eci_d['eci_1']['display_units'] = cb_eci_1_units.get()
    eci_d['eci_2']['display_units'] = cb_eci_2_units.get()
    eci_d['eci_3']['display_units'] = cb_eci_3_units.get()
    eci_d['eci_4']['display_units'] = cb_eci_4_units.get()
    eci_d['eci_5']['display_units'] = cb_eci_5_units.get()
    eci_d['eci_6']['display_units'] = cb_eci_6_units.get()
    if eci_1_units == 'liters(l)' or eci_1_units == 'ml(l)' or eci_1_units == 'liters(g)' or eci_1_units == 'ml(g)':    #liters(l) liters(g) ml(l) ml(g
        if cb_1_Temp_Units.get() == "":
            eci_1_temp_units = cb_1_Temp_Units.set('K')
        if cb_1_Press_Units.get() == "":
            eci_1_press_units = cb_1_Press_Units.set('ATM')
    # elif not eci_1_units == 'liters(g)' and not eci_1_units == 'ml(g)':
    #     print('cb_eci_1_units are ', eci_1_units)
    if eci_2_units == 'liters(l)' or eci_2_units == 'ml(l)' or eci_2_units == 'liters(g)' or eci_2_units == 'ml(g)':
        if cb_2_Temp_Units.get() == "":
            eci_2_temp_units = cb_2_Temp_Units.set('K')
        if cb_2_Press_Units.get() == "":
            eci_2_press_units = cb_2_Press_Units.set('ATM')
    if eci_3_units == 'liters(l)' or eci_3_units == 'ml(l)' or eci_3_units == 'liters(g)' or eci_3_units == 'ml(g)':
        if cb_3_Temp_Units.get() == "":
            eci_3_temp_units = cb_3_Temp_Units.set('K')
        if cb_3_Press_Units.get() == "":
            eci_3_press_units = cb_3_Press_Units.set('ATM')
    if eci_4_units == 'liters(l)' or eci_4_units == 'ml(l)' or eci_4_units == 'liters(g)' or eci_4_units == 'ml(g)':
        if cb_4_Temp_Units.get() == "":
            eci_4_temp_units = cb_4_Temp_Units.set('K')
        if cb_4_Press_Units.get() == "":
            eci_4_press_units = cb_4_Press_Units.set('ATM')
    if eci_5_units == 'liters(l)' or eci_5_units == 'ml(l)' or eci_5_units == 'liters(g)' or eci_5_units == 'ml(g)':
        if cb_5_Temp_Units.get() == "":
            eci_5_temp_units = cb_5_Temp_Units.set('K')
        if cb_4_Press_Units.get() == "":
            eci_5_press_units = cb_5_Press_Units.set('ATM')
    if eci_6_units == 'liters(l)' or eci_6_units == 'ml(l)' or eci_6_units == 'liters(g)' or eci_6_units == 'ml(g)':
        if cb_6_Temp_Units.get() == "":
            eci_6_temp_units = cb_6_Temp_Units.set('K')
        if cb_6_Press_Units.get() == "":
            eci_6_press_units = cb_6_Press_Units.set('ATM')
    eci_d['eci_1']['display_temp_units'] = cb_1_Temp_Units.get()
    eci_d['eci_2']['display_temp_units'] = cb_2_Temp_Units.get()
    eci_d['eci_3']['display_temp_units'] = cb_3_Temp_Units.get()
    eci_d['eci_4']['display_temp_units'] = cb_4_Temp_Units.get()
    eci_d['eci_5']['display_temp_units'] = cb_5_Temp_Units.get()
    eci_d['eci_6']['display_temp_units'] = cb_6_Temp_Units.get()
    eci_d['eci_1']['display_press_units'] = cb_1_Press_Units.get()
    eci_d['eci_2']['display_press_units'] = cb_2_Press_Units.get()
    eci_d['eci_3']['display_press_units'] = cb_3_Press_Units.get()
    eci_d['eci_4']['display_press_units'] = cb_4_Press_Units.get()
    eci_d['eci_5']['display_press_units'] = cb_5_Press_Units.get()
    eci_d['eci_6']['display_press_units'] = cb_6_Press_Units.get()
    #print("eci_db['eci_1']['display_temp_units'] are ", eci_db['eci_1']['display_temp_units'])
    #print("eci_db['eci_1']['display_press_units'] are ", eci_db['eci_1']['display_press_units'])

''' I want to write separate lambda expressions for each entry and combobox
    that will update the associated dictionary field.
    Can I rewrite set_eci_db_eci_1_qty(qty) as a lambda expression such as:
    set_eci_db_eci_1_qty = e_eci_1_qty.get() for each entry and combobox
    so I don't have to write separate functions for each.
    Or, is it better to use eci_units_selected to check and set every dictionary variable
    everytime one of them is changed. set_quantity = tkinter
'''

def set_eci_db_eci_1_qty(qty):
    set_eci_db_eci_1_qty = qty
    print('set_eci_db_eci_1_qty is ', set_eci_db_eci_1_qty)

def vol_from_prt():
    print('In process vol_from_prt')
    ''' Calculate volume given pressure, R constant, and temperature. pv = nRt'''
    n = float(eci_1_M_qty.get())    # getdouble
    #n= 0.54
    R = 0.08206 # R value for these units
    #T = 288
    #P = .967
    if eci_1_temp_units.get() == 'C':
        T = 273.15 + float(e_Temp_Qty_1.get())  #C_to_K(float(e_Temp_Qty_1.get())) got TypeError: unsupported operand type(s) for *: 'float' and 'NoneType'
    elif eci_1_temp_units.get() == 'K':
        T = float(e_Temp_Qty_1.get())
    if eci_1_press_units.get() == 'ATM':
        P = float(e_Press_Qty_1.get())
    elif eci_1_press_units.get() == 'torr':
        P = float(e_Temp_Qty_1.get()) * 760

    try:
        vol = n*R*T/P
        e_eci_1_qty.delete(0, 'end')
        e_eci_1_qty.insert(0, vol)
        print(n, T, P, vol)
    except: print('Error in vol = n*R*T/P')

''' function may not be needed
def eci_1_qty_changed(eventObject):    #callback
    eci_1_qty = e_eci_1_qty.get()   #e_eci_1_qty
    print('eci_1_qty is ', eci_1_qty)'''


def callback_set_temp_units(eventObject):
    ''' Whenever a temperature units combo box is selected, update the eci_db variable. '''
    eci_1_temp_units = cb_1_Temp_Units.get()
    eci_2_temp_units = cb_2_Temp_Units.get()
    eci_3_temp_units = cb_3_Temp_Units.get()
    eci_4_temp_units = cb_4_Temp_Units.get()
    eci_5_temp_units = cb_5_Temp_Units.get()
    eci_6_temp_units = cb_6_Temp_Units.get()
    eci_d['eci_1']['display_temp_units'] = cb_1_Temp_Units.get()
    eci_d['eci_2']['display_temp_units'] = cb_2_Temp_Units.get()
    eci_d['eci_3']['display_temp_units'] = cb_3_Temp_Units.get()
    eci_d['eci_4']['display_temp_units'] = cb_4_Temp_Units.get()
    eci_d['eci_5']['display_temp_units'] = cb_5_Temp_Units.get()
    eci_d['eci_6']['display_temp_units'] = cb_6_Temp_Units.get()


def callback_set_press_units(eventObject):
    ''' Whenever a temperature units combo box is selected, update the eci_db variable. '''
    eci_1_press_units = cb_1_Press_Units.get()
    eci_2_press_units = cb_2_Press_Units.get()
    eci_3_press_units = cb_3_Press_Units.get()
    eci_4_press_units = cb_4_Press_Units.get()
    eci_5_press_units = cb_5_Press_Units.get()
    eci_6_press_units = cb_6_Press_Units.get()
    eci_d['eci_1']['display_press_units'] = cb_1_Press_Units.get()
    eci_d['eci_2']['display_press_units'] = cb_2_Press_Units.get()
    eci_d['eci_3']['display_press_units'] = cb_3_Press_Units.get()
    eci_d['eci_4']['display_press_units'] = cb_4_Press_Units.get()
    eci_d['eci_5']['display_press_units'] = cb_5_Press_Units.get()
    eci_d['eci_6']['display_press_units'] = cb_6_Press_Units.get()


'''
def callback_eci_1(eventObject):
    eci_1 = cb_eci_1.get()
    print(eci_1)
'''
'''
set_temp_and_press_settings() has been superceded by callback_set_temp_units and callback_set_press_units.
def set_temp_and_press_settings():
    eci_1_temp_units = cb_1_Temp_Units.set('C')
    eci_2_temp_units = cb_2_Temp_Units.set('C')
    eci_3_temp_units = cb_3_Temp_Units.set('C')
    eci_4_temp_units = cb_4_Temp_Units.set('C')
    eci_5_temp_units = cb_5_Temp_Units.set('C')
    eci_6_temp_units = cb_6_Temp_Units.set('C')
    eci_db['eci_1']['display_temp_units'] = cb_1_Temp_Units.get()
    eci_db['eci_2']['display_temp_units'] = cb_2_Temp_Units.get()
    eci_db['eci_3']['display_temp_units'] = cb_3_Temp_Units.get()
    eci_db['eci_4']['display_temp_units'] = cb_4_Temp_Units.get()
    eci_db['eci_5']['display_temp_units'] = cb_5_Temp_Units.get()
    eci_db['eci_6']['display_temp_units'] = cb_6_Temp_Units.get()
    #print("eci_db['eci_1']['display_temp_units']", cb_1_Temp_Units.get())
    eci_1_press_units = cb_1_Press_Units.set('torr')
    eci_2_press_units = cb_2_Press_Units.set('torr')
    eci_3_press_units = cb_3_Press_Units.set('torr')
    eci_4_press_units = cb_4_Press_Units.set('torr')
    eci_5_press_units = cb_5_Press_Units.set('torr')
    eci_6_press_units = cb_6_Press_Units.set('torr')
    eci_db['eci_1']['display_press_units'] = cb_1_Press_Units.get()
    eci_db['eci_2']['display_press_units'] = cb_2_Press_Units.get()
    eci_db['eci_3']['display_press_units'] = cb_3_Press_Units.get()
    eci_db['eci_4']['display_press_units'] = cb_4_Press_Units.get()
    eci_db['eci_5']['display_press_units'] = cb_5_Press_Units.get()
    eci_db['eci_6']['display_press_units'] = cb_6_Press_Units.get()
'''
def Reset_Product_Boxes():
    #cb_eci_2.set("")
    #cb_eci_2_N.set("")
    #e_eci_2_M_qty.delete(0, END)
    #cb_eci_3.set("")
    #cb_eci_3_N.set("")
    #e_eci_3_M_qty.delete(0, END)
    cb_eci_4.set("")
    cb_eci_4_N.set("")
    e_eci_4_M_qty.delete(0, END)
    cb_eci_5.set("")
    cb_eci_5_N.set("")
    e_eci_5_M_qty.delete(0, END)
    cb_eci_6.set("")
    cb_eci_6_N.set("")
    e_eci_6_M_qty.delete(0, END)

def Reset_Reactant_Boxes():
    cb_eci_1.set("")
    cb_eci_1_N.set("")
    e_eci_1_M_qty.delete(0, END)
    cb_eci_2.set("")
    cb_eci_2_N.set("")
    e_eci_2_M_qty.delete(0, END)
    cb_eci_3.set("")
    cb_eci_3_N.set("")
    e_eci_3_M_qty.delete(0, END)
    #cb_eci_5.set("")
    #cb_eci_5_N.set("")
    #e_eci_5_M_qty.delete(0, END)
    #cb_eci_6.set("")
    #cb_eci_6_N.set("")
    #e_eci_6_M_qty.delete(0, END)

def Parse_Reactants():  # 'He2SO4'
    ''' I need to parse for number, uppercase, and lowercase. Leading number always applies to an element or formula,
    later numbers are assumed to apply to the preceeding element.
    '''
    e_Explanation.insert(tk.END, "Parse_Reactants process entered\n")
    #Reset_Product_Boxes()
    if cb_Select_CB1.get() == 'compounds':
        eci_1 = cb_eci_1.get()
        compound = cb_eci_1.get()
        print('Parse_Reactants compound is ', compound)

    elif not cb_Select_CB1.get() == 'compounds':
        print('In Parse_Reactants, but compound type is not a set')
        e_Explanation.insert(tk.END, "Parse_Compounds process entered, but compound type is not a set\n")

    else: print("Parse_Reactants process entered", cb_eci_1.get())


    #print('Parse_Reactants compound is ', compound)
    ''' Start with a normal compound which does not start with an integer.'''
    # For example: compound = 'Na2SO4'
    if compound == "":
        e_Explanation.insert(tk.END, "Parse_Reactants process entered, but compound is empty string. \n")
    elif compound[0].isdigit():
        ''' If the leading character is a number, apply it to the whole formula. '''
        compound_formula_qty = compound[0]
        ''' Reset the compound to the string after the intial digit. '''
        compound = compound[1:]
        print('Parse_Reactants compound first character is integer ', compound[0])
        ''' The first character is not a number. '''
    elif not compound[0].isdigit():
        print('Pass to Parse_Compound') #Parse_Compound_ECI_1
        parsed_compound = Parse_Compound(compound)
        Display_Parsed_Reactant(parsed_compound)
        # Parse_Compound_ECI_1()
    else:
        print('In else clause of Parse_Compounds')
    # print(' If the leading character is a number, '
    #      'need to add it to the result of Parse_Compounds_1(compound).')

def Parse_Products():  # 'He2SO4'
    ''' I need to parse for number, uppercase, and lowercase. Leading number always applies to an element or formula,
    later numbers are assumed to apply to the preceeding element.
    '''
    e_Explanation.insert(tk.END, "Parse_Products process entered\n")
    if cb_Select_CB4.get() == 'compounds':
        eci_1 = cb_eci_4.get()
        compound = cb_eci_4.get()
        print('Parse_Products compound is ', compound)

    elif not cb_Select_CB4.get() == 'compounds':
        print('In Parse_Products, but compound type is not a set')
        e_Explanation.insert(tk.END, "Parse_Compounds process entered, but compound type is not a set\n")

    else: print("Parse_Products process entered", cb_eci_4.get())

    ''' Start with a normal compound which does not start with an integer.'''
    if compound == "":
        e_Explanation.insert(tk.END, "Parse_Products process entered, but compound is empty string. \n")
    elif compound[0].isdigit():
        ''' If the leading character is a number, apply it to the whole formula. '''
        compound_formula_qty = compound[0]
        ''' Reset the compound to the string after the intial digit. '''
        compound = compound[1:]
        print('Parse_Products compound first character is integer ', compound[0])
        ''' The first character is not a number. '''
    elif not compound[0].isdigit():
        print('Pass to Parse_Products') #Parse_Compound_ECI_1
        parsed_compound = Parse_Compound(compound)
        Display_Parsed_Product(parsed_compound)
        # Parse_Compound_ECI_1()
    else:
        print('In else clause of Parse_Compounds')
    # print(' If the leading character is a number, '
    #      'need to add it to the result of Parse_Compounds_1(compound).')

def Parse_Compound(compound):
    ''' Got a compound from eci_1. Parse it. '''
    print('In Parse_Compound(compound): compound = ', compound)
    len_compound = len(compound)
    current_compound = []
    # print('len_compound is ', len_compound)
    while len(compound) >= 3:
        # print('len(compound) is ', len_compound)
        if compound[0].isupper() and compound[1].islower() and compound[2].isdigit():  # and compound[3].isupper():
            print(
                'In compound[0].isupper() and compound[1].islower() and compound[2].isdigit()')  # Re,removed  and compound[3].isupper()
            current_element_multiplier = 1
            current_element = compound[:2]
            current_element_multiplier = int(compound[2:3])
            current_compound.append(current_element)
            current_compound.append(current_element_multiplier)
            compound = compound[3:]
            print('elif compound[0].isupper() and compound[1].isdigit() and compound[2].isupper(): compound = ',
                  compound)
            print('current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
            print('current_compound is ', current_compound)
        elif compound[0].isupper() and compound[1].islower() and compound[2].isdigit():  # and compound[3].isdigit()
            print('In compound[0].isupper() and compound[1].islower() and compound[2].isdigit()')
            print("Don't know if there are any of these.")
        elif compound[0].isupper() and compound[1].isupper():
            print('In compound[0].isupper() and compound[1].isupper()')
            current_element_multiplier = 1
            current_element = compound[0]
            current_compound.append(current_element)
            current_compound.append(current_element_multiplier)
            compound = compound[1:]
            print('In elif compound[1].isupper() and len(compound) > 1: compound = ', compound)
            print('current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
            print('current_compound is ', current_compound)
        elif compound[0].isupper() and compound[1].islower() and compound[2].isupper():
            print('In compound[0].isupper() and compound[1].islower() and compound[2].isupper()')
            current_element_multiplier = 1
            current_element = compound[:2]
            current_element_multiplier = 1
            current_compound.append(current_element)
            current_compound.append(current_element_multiplier)
            compound = compound[2:]
            len_compound = len(compound)
            print('elif compound[0].isupper() and compound[1].islower() and compound[2].isupper(): compound = ',
                  compound)
            print('current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
            print('current_compound, and length are ', current_compound, len_compound)
        elif compound[0].isupper() and compound[1].isdigit() and compound[2].isupper():
            print('In compound[0].isupper() and compound[1].isdigit() and compound[2].isupper()')
            current_element_multiplier = 1
            current_element = compound[:1]
            current_element_multiplier = int(compound[1:2])
            current_compound.append(current_element)
            current_compound.append(current_element_multiplier)
            compound = compound[2:]
            print('elif compound[0].isupper() and compound[1].isdigit() and compound[2].isupper(): compound = ',
                  compound)
            print('current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
            print('current_compound is ', current_compound)
        elif compound[0].isupper() and compound[1].isdigit() and compound[2].isdigit():
            print('In compound[0].isupper() and compound[1].isdigit() and compound[2].isdigit()')
            current_element_multiplier = 1
            current_element = compound[:1]
            current_element_multiplier = int(compound[1:3])
            current_compound.append(current_element)
            current_compound.append(current_element_multiplier)
            if len(compound) > 2:
                compound = compound[3:]
            else:
                compound = ""
            print('elif compound[0].isupper() and compound[1].isdigit() and compound[2].isupper(): compound = ',
                  compound)
            print('current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
            print('current_compound is ', current_compound)

    if len(compound) < 3:
        print('if len(compound) < 3:')
        while len(compound) > 0:
            if compound[0] == '_':
                compound = ""
                print("In if compound[0] == '_':")
            elif len(compound) == 1:
                if compound[0].isupper():
                    print('In compound[0].isupper()')
                    current_element_multiplier = 1
                    current_element = compound[0]
                    current_compound.append(current_element)
                    current_compound.append(current_element_multiplier)
                    print('In if compound[0].isupper():: compound = ', compound)
                    print('current_element is ', current_element, ' current_element_multiplier is ',
                          current_element_multiplier)
                    print('current_compound is ', current_compound)
                    compound = ""
            elif len(compound) == 2:
                if compound[0].isupper() and compound[1].isupper():
                    print('In compound[0].isupper() and compound[1].isupper()')
                    current_element_multiplier = 1
                    current_element = compound[0]
                    current_compound.append(current_element)
                    current_compound.append(current_element_multiplier)
                    compound = compound[1:]
                    print('In elif compound[1].isupper() and len(compound) > 1: compound = ', compound)
                    print('current_element is ', current_element, ' current_element_multiplier is ',
                          current_element_multiplier)
                    print('current_compound is ', current_compound)
                elif compound[0].isupper() and compound[1].islower():
                    print('In compound[0].isupper() and compound[1].islower()')
                    current_element_multiplier = 1
                    current_element = compound[0:1]
                    current_compound.append(current_element)
                    current_compound.append(current_element_multiplier)
                    compound = ""
                    print('In if compound[0].isupper() and compound[1].islower():: compound = ', compound)
                    print('current_element is ', current_element, ' current_element_multiplier is ',
                          current_element_multiplier)
                    print('current_compound is ', current_compound)
                elif compound[0].isupper() and compound[1].isdigit():
                    print('In compound[0].isupper() and compound[1].isdigit()')
                    current_element_multiplier = 1
                    current_element = compound[0]
                    current_element_multiplier = int(compound[1])
                    current_compound.append(current_element)
                    current_compound.append(current_element_multiplier)
                    compound = ""
                    print('In if compound[0].isupper() and compound[1].islower():: compound = ', compound)
                    print('current_element is ', current_element, ' current_element_multiplier is ',
                          current_element_multiplier)
                    print('current_compound is ', current_compound)
        print('compound =  ', compound)
        compound = ""
        return current_compound
        #Display_Parsed_Reactant(current_compound)


def Display_Parsed_Reactant(parsed_compound):
    print('Entering Display_Parsed_Compound')
    print(parsed_compound)
    ''' Need to reset all possible product boxes to empty strings'''
    Reset_Product_Boxes()
    e_eci_1_M_qty.delete(0, END)
    e_eci_1_M_qty.insert(0, 1)
    cb_Select_CB4.set('elements')
    element_1 = parsed_compound[0]
    print('element_1 is ', element_1)
    cb_eci_4.set("")
    cb_eci_4_N.set("")
    cb_eci_4.set(element_1)
    moles_1 = parsed_compound[1]
    print('moles_1 is ', moles_1)
    e_eci_4_M_qty.delete(0, END)
    e_eci_4_M_qty.insert(0, moles_1)

    cb_Select_CB5.set('elements')
    element_2 = parsed_compound[2]
    print('element_2 is ', element_2)
    cb_eci_5.set("")
    cb_eci_5_N.set("")
    cb_eci_5.set(element_2)
    moles_2 = parsed_compound[3]
    e_eci_5_M_qty.delete(0, END)
    e_eci_5_M_qty.insert(0, moles_2)

    try:
        if parsed_compound[4]:
            print('parsed_compound[4] is ', parsed_compound[4])
            cb_Select_CB6.set('elements')
            element_3 = parsed_compound[4]
            print('element_3 is ', element_3)
            cb_eci_6.set("")
            cb_eci_6_N.set("")
            cb_eci_6.set(element_3)
            moles_3 = parsed_compound[5]
            e_eci_6_M_qty.delete(0, END)
            e_eci_6_M_qty.insert(0, moles_3)
        if parsed_compound[6]:
            cb_Select_CB3.set('elements')
            element_4 = parsed_compound[6]
            print('element_4 is ', element_4)
            cb_eci_3.set("")
            cb_eci_3_N.set("")
            cb_eci_3.set(element_4)
            moles_4 = parsed_compound[7]
            e_eci_3_M_qty.delete(0, END)
            e_eci_3_M_qty.insert(0, moles_4)
    except:
        pass

def Display_Parsed_Product(parsed_compound):
    print('Entering Display_Parsed_Compound')
    print(parsed_compound)
    ''' Need to reset all possible product boxes to empty strings'''
    Reset_Reactant_Boxes()
    e_eci_4_M_qty.delete(0, END)
    e_eci_4_M_qty.insert(0, 1)

    cb_Select_CB1.set('elements')
    element_1 = parsed_compound[0]
    print('element_1 is ', element_1)
    cb_eci_1.set("")
    cb_eci_1_N.set("")
    cb_eci_1.set(element_1)
    moles_4 = parsed_compound[1]
    print('moles_1 is ', moles_4)
    e_eci_1_M_qty.delete(0, END)
    e_eci_1_M_qty.insert(0, moles_4)

    cb_Select_CB2.set('elements')
    element_2 = parsed_compound[2]
    print('element_2 is ', element_2)
    cb_eci_2.set("")
    cb_eci_2_N.set("")
    cb_eci_2.set(element_2)
    moles_2 = parsed_compound[3]
    e_eci_2_M_qty.delete(0, END)
    e_eci_2_M_qty.insert(0, moles_2)

    try:
        if parsed_compound[4]:
            print('parsed_compound[4] is ', parsed_compound[4])
            cb_Select_CB3.set('elements')
            element_3 = parsed_compound[4]
            print('element_3 is ', element_3)
            cb_eci_3.set("")
            cb_eci_3_N.set("")
            cb_eci_3.set(element_3)
            moles_3 = parsed_compound[5]
            e_eci_3_M_qty.delete(0, END)
            e_eci_3_M_qty.insert(0, moles_3)
        if parsed_compound[6]:
            cb_Select_CB6.set('elements')
            element_4 = parsed_compound[6]
            print('element_4 is ', element_4)
            cb_eci_6.set("")
            cb_eci_6_N.set("")
            cb_eci_6.set(element_4)
            moles_4 = parsed_compound[7]
            e_eci_6_M_qty.delete(0, END)
            e_eci_6_M_qty.insert(0, moles_4)
    except:
        pass

''' Use decimal instead of float in order to eliminate floating point errors. '''
def Parse_Compound_Logic():
    ''' Identify the logical steps in parsing compounds'''
    print('In Parse_Compound_Logic')
    ''' Get len(compound'''
    ''' If len(compound < 3'''
    ''' If len(compound >= 3 -- there is only one four item pattern, so include it with 3 item pattern. '''
    ''' Patterns that allow the first element to be identified and separated are:'''
    ''' Upper, upper -- compound[0].isupper() and compound[1].isupper()'''
    ''' Upper, lower, upper -- compound[0].isupper() and compound[1].islower() and compound[2].isupper() '''
    ''' Upper, digit, upper -- compound[0].isupper() and compound[1].isdigit() and compound[2].isupper() '''
    ''' Upper, lower, digit -- compound[0].isupper() and compound[1].islower() and compound[2].isdigit() '''
    ''' Patterns that allow the subsequent element or digits to be identified and separated are:'''
    ''' same as above'''
    ''' Upper, upper -- compound[0].isupper() and compound[1].isupper()'''
    ''' Upper, lower, upper -- compound[0].isupper() and compound[1].islower() and compound[2].isupper() '''
    ''' Upper, digit, upper -- compound[0].isupper() and compound[1].isdigit() and compound[2].isupper() '''

    ''' *** Not valid *** Upper, lower, digit -- compound[0].isupper() and compound[1].islower() and compound[2].isdigit() '''
    ''' new patterns'''
    ''' Upper, digit, digit -- compound[0].isupper() and compound[1].isdigit() and compound[2].isdigit() '''
    ''' Upper, lower, digit, digit -- compound[0].isupper() and compound[1].islower() and compound[2].isdigit()  and compound[3].isdigit()'''
    ''' digit, upper -- compound[0].isdigit() and compound[1].isupper() '''
    ''' digit, digit, upper -- compound[0].isdigit() and compound[1].isdigit() and compound[2].isupper() '''
    ''' final patterns'''
    ''' If len(compound < 3'''
    ''' All the above where length is 2, 1, or 0. '''


def CountElements():  # The following does not work. Need valid test for value
    e_Explanation.insert(tk.END, "CountElements process entered\n")
    intElementCount = 0
    eci_1 = cb_eci_1.get()
    eci_2 = cb_eci_2.get()
    eci_3 = cb_eci_3.get()
    if eci_1 == "":  # cb_eci_1
        pass
    else:
        intElementCount = 1
    if eci_2 == "":
        pass
    else:
        intElementCount = intElementCount + 1
    if eci_3 == "":
        pass
    else:
        intElementCount = intElementCount + 1
    print('element count is', intElementCount)
    return intElementCount
    # rtb_Explanation.Text = rtb_Explanation.Text & intElementCount

def AlphabetizeElements():  # TypeError: '<' not supported between instances of 'StringVar' and 'StringVar'
    e_Explanation.insert(tk.END, "AlphabetizeElements process entered\n")
    strAlphaElements = ""
    eci_1 = cb_eci_1.get()
    eci_2 = cb_eci_2.get()
    eci_3 = cb_eci_3.get()

    if eci_1 < eci_2 and eci_1 < eci_3:
        if eci_2 < eci_3:
            strAlphaElements = eci_1 + eci_2 + eci_3
        elif eci_3 < eci_2:
            strAlphaElements = eci_1 + eci_3 + eci_2
    elif eci_2 < eci_1 and eci_2 < eci_3:
        if eci_1 < eci_3:
            strAlphaElements = eci_2 + eci_1 + eci_3
        elif eci_3 < eci_1:
            strAlphaElements = eci_2 + eci_3 + eci_1
    elif eci_3 < eci_1 and eci_3 < eci_2:
        if eci_1 < eci_2:
            strAlphaElements = eci_3 + eci_1 + eci_2
        elif eci_2 < eci_1:
            strAlphaElements = eci_3 + eci_2 + eci_1
    else:
        e_Explanation.insert(tk.END, 'Error:Fell to else clause in AlphabetizeElements\n')
    # e_Explanation.insert(tk.END, 'strAlphaElements is %', strAlphaElements) #How do I insert arguments?
    print('strAlphaElements is ', strAlphaElements)

# Make new dictionaries of elements, compounds and ions to ensure they are current.
# Also, if the data is changed in a dictionary, it needs to be changed in the database.
# Current, data will be changed in a dictionary and then changed in the database.
# Make new alpha lists of compounds and ions to ensure they are current.
# An alpha dictionary/list is a list of compound (or ion) elements in alphabetic order and a list of the compounds or ions 
# that have the same list of elements. After a set of elements have been chosen and alphabetized, these lists will be used
#  to determine which compounds have these elements, and that list will be used to fill the appropriate combo box
def make_element_dictionary():
    pass
    # print("In make_element_dictionary")

def make_compound_dictionary():
    pass


def make_ion_dictionary():
    pass


def make_compound_alpha_list():
    pass


def make_ion_alpha_list():
    pass
    # a_list = [eci_1, eci_2, eci_3]
    # alpha = (sorted(a_list)) #Does not concatenate
    # beta = alpha(0) + alpha(1) + alpha(2)
    # print('In AlphabetizeElements', alpha)
    # print('In AlphabetizeElements', sorted(alpha))

def show_hide_instructions():
    if btn_show_instructions.text == 'Show Instructions':
        ''' What code changes button text? '''
        popup()
        btn_show_instructions.text == 'Hide Instructions'
        ''' Code to show the window with instructions. '''
    else:
        popup()
        btn_show_instructions.text == 'Show Instructions'
        ''' Code to hide the window with instructions. '''
'''
def makePopup():
    window = Toplevel()
    window.title("Instructions and History")
    okButton = Button(root, text="OK")
    #window
    #okButton.config(pack())
'''
class popupWindow(object):
    def __init__(self,master):
        top=self.top=Toplevel(master)
        self.l=Label(top,text="Hello World")
        self.l.pack()
        self.e=Entry(top)
        self.e.pack()
        self.b=Button(top,text='Ok',command=self.cleanup)
        self.b.pack()
    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()

def popup():
        w=popupWindow(root)
        #self.b["state"] = "disabled"
        #self.master.wait_window(self.w.top)
        #self.b["state"] = "normal"

''' *** Learn to send text and variables to the explanation textbox. *** '''

''' *** End function descriptions. *** '''

''' *** Start GUI layout. *** '''
'''
#def mcf(): #make_main_chemistry_form
main_frame = Frame(root)
main_frame.pack(fill = BOTH, expand = 1)
main_canvas = Canvas(main_frame)
main_canvas.pack(side=LEFT, fill=BOTH, expand = 1)
sb = Scrollbar(main_frame, orient=VERTICAL,command=main_canvas.yview)
sb.pack(side=RIGHT, fill=Y)
main_canvas.configure(yscrollcommand=sb.set)
main_canvas.bind('<Configure>', lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all")))
#sb.pack( side = RIGHT, fill = Y )
#sb.grid(row = 1, rowspan = 30, column = 12)
#sb.grid(rowspan = 30)
#sb.grid_anchor(anchor='e')
'''
lbl_Title = Label(root, text="Chemistry")
lbl_Title.grid(row=0, column=3)
lbl_Title.config(font=titlefont)

lbl_blank = Label(root, text="")
lbl_blank.grid(row=1, column=0)
lbl_blank.config(font=labelfont)

lbl_record_create = Label(text="Create record:")
lbl_record_create.grid(row=2, column=0)
lbl_record_create.config(font=labelfont)
e_recordname = Entry(root, text="")
e_recordname.grid(row=2, column=1, columnspan=2)
e_recordname.config(font=labelfont)
btn_create_record = Button(root, text='Create Record', command=create_record)
btn_create_record.grid(row=2, column=3)
btn_create_record.config(font=buttonfont)
btn_create_record.bind("<<ComboboxSelected>>", create_record())
btn_update_record = Button(root, text='Update Record', command=update_record)
btn_update_record.grid(row=2, column=4)
btn_update_record.config(font=buttonfont)
btn_update_record.bind("<<ComboboxSelected>>", update_record)
btn_Continue = Button(root, text='* Continue *', command=Continue)
btn_Continue.grid(row=2, column=5)
btn_Continue.config(font=titlefont)
# btn_Continue.bind("<<ComboboxSelected>>", Continue())

lbl_record_ops = Label(text="Get record:")
lbl_record_ops.grid(row=3, column=0)
lbl_record_ops.config(font=labelfont)
cb_RecordName: Combobox = Combobox(root, values="", width=12)
cb_RecordName.grid(row=3, column=1)
cb_RecordName.config(font=entryfont)
cb_RecordName.bind("<<ComboboxSelected>>", retrieve_record)
# e_recordname = Entry(root, text="")   #, width=30)
# e_recordname.grid(row=3, column=3)
# e_recordname.config(font=labelfont)
btn_create_record = Button(root, text='Get Record', command=get_record)
btn_create_record.grid(row=3, column=2)
btn_create_record.config(font=buttonfont)
btn_create_record.bind("<<ComboboxSelected>>", retrieve_record)
btn_create_record = Button(root, text='Previous Record', command=get_record)
btn_create_record.grid(row=3, column=3)
btn_create_record.config(font=buttonfont)
btn_create_record.bind("<<ComboboxSelected>>", previous_record)
btn_create_record = Button(root, text='Next Record', command=get_record)
btn_create_record.grid(row=3, column=4)
btn_create_record.config(font=buttonfont)
btn_create_record.bind("<<ComboboxSelected>>", next_record)
btn_show_instructions = Button(root, text='Show Instructions', command=get_record)
btn_show_instructions.grid(row=2, column=6)
btn_show_instructions.config(font=labelfont)
btn_show_instructions.bind("<<ComboboxSelected>>", show_hide_instructions)

lbl_LU_Compound = Label(text="   Look up compound:")
lbl_LU_Compound.grid(row=6, column=0)
lbl_LU_Compound.config(font=labelfont)
cb_LU_Compound = Combobox(root, values=compound_symbols_list, width=12)
cb_LU_Compound.grid(row=6, column=1)
cb_LU_Compound.config(font=entryfont)

# Create a search for and retrieve a compount
lbl_LU_Process = Label(text="   Look up process:")
lbl_LU_Process.grid(row=6, column=2)
lbl_LU_Process.config(font=labelfont)
cb_LU_Process = Combobox(root, values=process_list, width=12)
cb_LU_Process.grid(row=6, column=3)
cb_LU_Process.config(font=entryfont)
# Create a search for and retrieve a process
lbl_LU_Environment = Label(text="   Look up environment:", width=22)
lbl_LU_Environment.grid(row=6, column=4)
lbl_LU_Environment.config(font=labelfont)
cb_LU_Environment = Combobox(root, values=environment, width=12)
cb_LU_Environment.grid(row=6, column=5)
cb_LU_Environment.config(font=entryfont)
# Create a search for and retrieve a environment

lbl_Select_Process = Label(text="Select process", width=13)
lbl_Select_Process.grid(row=7, column=2)
lbl_Select_Process.config(font=titlefont)
cb_Select_Process: Combobox = Combobox(root, values=process_list, textvariable=process_selected, width=12)
cb_Select_Process.grid(row=7, column=3)
cb_Select_Process.config(font=entryfont)
cb_Select_Process.bind("<<ComboboxSelected>>", process_selected)
lbl_Select_Environment = Label(text="   Select environment:", width=22)
lbl_Select_Environment.grid(row=7, column=4)
lbl_Select_Environment.config(font=titlefont)
cb_Select_Environment: Combobox = Combobox(root, values=environment, width=12)
cb_Select_Environment.grid(row=7, column=5)
cb_Select_Environment.config(font=entryfont)

lbl_blank = Label(root, text="")
lbl_blank.grid(row=8, column=0)

lbl_eci_1 = Label(root, text="   Select Element, Compound or Ion for ComboBox 1")
lbl_eci_1.grid(row=9, column=0, columnspan=3, sticky=W)
lbl_eci_1.config(font=labelfont)
cb_Select_CB1: Combobox = Combobox(root, values=eci_cb_values, width=10)
cb_Select_CB1.grid(row=9, column=3, sticky=W)
cb_Select_CB1.config(font=entryfont)
cb_Select_CB1.bind("<<ComboboxSelected>>", select_eci_1_type)
# cb_Select_CB1.bind("<<ComboboxSelected>>", callback1)
# cb_Process = Combobox(root, values=process_list, width=20)
# cb_Process.grid(row=9, column=3) # , columnspan=2
# cb_Process.config(font=entryfont)
lbl_eci_4 = Label(root, text="Select Element, Compound or Ion for ComboBox 4")
lbl_eci_4.grid(row=9, column=4, columnspan=3, sticky=W)
lbl_eci_4.config(font=labelfont)
cb_Select_CB4 = Combobox(root, values=eci_cb_values, width=10)
cb_Select_CB4.grid(row=9, column=6)
cb_Select_CB4.config(font=entryfont)
cb_Select_CB4.bind("<<ComboboxSelected>>", select_eci_4_type)

lbl_eci_1_qty = Label(root, text="ECI Qty 1", width=8)
lbl_eci_1_qty.grid(row=11, column=0)
lbl_eci_1_qty.config(font=labelfont)
lbl_eci_1_units = Label(root, text="Units 1", width=10)
lbl_eci_1_units.grid(row=11, column=1, sticky=W)
lbl_eci_1_units.config(font=labelfont)
lbl_eci_1 = Label(root, text="ECI 1", width=10)
lbl_eci_1.grid(row=11, column=2, sticky=W)
lbl_eci_1.config(font=labelfont)
lbl_eci_1_valence = Label(root, text="Valence 1", width=10)
lbl_eci_1_valence.grid(row=11, column=3, sticky=W)
lbl_eci_1_valence.config(font=labelfont)
lbl_eci_4_qty = Label(root, text="ECI Qty 4", width=8)
lbl_eci_4_qty.grid(row=11, column=4)
lbl_eci_4_qty.config(font=labelfont)
lbl_eci_4_units = Label(root, text="Units 4", width=10)
lbl_eci_4_units.grid(row=11, column=5, sticky=W)
lbl_eci_4_units.config(font=labelfont)
lbl_eci_4 = Label(root, text="ECI 4", width=10)
lbl_eci_4.grid(row=11, column=6, sticky=W)
lbl_eci_4.config(font=labelfont)
lbl_eci_4_valence = Label(root, text="Valence 4", width=10)
lbl_eci_4_valence.grid(row=11, column=7, sticky=W)
lbl_eci_4_valence.config(font=labelfont)

e_eci_1_qty = Entry(root, text="", textvariable=eci_1_qty, width=8)
e_eci_1_qty.grid(row=12, column=0)
e_eci_1_qty.config(font=entryfont)
''' Can I generalize the following to: set_eci_db_eci_1_qty = e_eci_1_qty.get()'''
#e_eci_1_qty.bind('<FocusOut>', lambda event: set_eci_db_eci_1_qty(e_eci_1_qty.get()))
cb_eci_1_units: Combobox = Combobox(root, values=unit_values, textvariable=eci_1_units, width=10)
cb_eci_1_units.grid(row=12, column=1)
cb_eci_1_units.config(font=entryfont)
cb_eci_1_units.bind("<<ComboboxSelected>>", eci_units_selected)
cb_eci_1: Combobox = Combobox(root, textvariable=eci_1, width=12)
cb_eci_1.grid(row=12, column=2)
cb_eci_1.config(font=labelfont)
cb_eci_1['values'] = elements_symbols_list
cb_eci_1.bind("<<ComboboxSelected>>", setSelectedItemName)

cb_eci_1_valence: Combobox = Combobox(root, textvariable=eci_1_valence, width=8)
cb_eci_1_valence.grid(row=12, column=3)
cb_eci_1_valence.config(font=entryfont)
cb_eci_1_valence['values'] = valences
e_eci_4_qty = Entry(root, text="", textvariable=eci_4_qty, width=8)
e_eci_4_qty.grid(row=12, column=4)
e_eci_4_qty.config(font=entryfont)
cb_eci_4_units: Combobox = Combobox(root, values=unit_values, textvariable=eci_4_units, width=10)
cb_eci_4_units.grid(row=12, column=5)
cb_eci_4_units.config(font=entryfont)
cb_eci_4_units.bind("<<ComboboxSelected>>", eci_units_selected)
# cb_eci_4_units.bind("<<ComboboxSelected>>", callback_eci_4_units)
cb_eci_4: Combobox = Combobox(root, textvariable=eci_4, width=12)
cb_eci_4.grid(row=12, column=6)
cb_eci_4.config(font=entryfont)
cb_eci_4['values'] = compound_symbols_list
cb_eci_4.bind("<<ComboboxSelected>>", setSelectedItemName)
cb_eci_4_valence: Combobox = Combobox(root, textvariable=eci_4_valence, width=5)
cb_eci_4_valence.grid(row=12, column=7)
cb_eci_4_valence.config(font=entryfont)
cb_eci_4_valence['values'] = valences

e_eci_1_M_qty = Entry(root, text="", textvariable=eci_1_M_qty, width=8)
e_eci_1_M_qty.grid(row=13, column=0)
e_eci_1_M_qty.config(font=entryfont)
e_eci_1_M_qty.bind('<FocusOut>', (lambda event: check_entry_changes()))  # '''  does not work'''
lbl_eci_1_units_M = Label(root, text="Moles", width=12)
lbl_eci_1_units_M.grid(row=13, column=1)
lbl_eci_1_units_M.config(font=labelfont)
# cb_Elements1 = Combobox(root, values=elements, width=30)
cb_eci_1_N: Combobox = Combobox(root, textvariable=eci_1_name, width=12)
cb_eci_1_N.grid(row=13, column=2)
cb_eci_1_N.config(font=entryfont)
cb_eci_1_N['values'] = compound_names_list
cb_eci_1_N.bind("<<ComboboxSelected>>", setSelectedItemFormula)

e_eci_4_M_qty = Entry(root, text="", textvariable=eci_4_M_qty, width=8)
e_eci_4_M_qty.grid(row=13, column=4)
e_eci_4_M_qty.config(font=entryfont)
lbl_eci_4_units_M = Label(root, text="Moles", width=10)
lbl_eci_4_units_M.grid(row=13, column=5)
lbl_eci_4_units_M.config(font=labelfont)
cb_eci_4_N: Combobox = Combobox(root, values=compound_symbols_list, textvariable=eci_4_name, width=12)
cb_eci_4_N.grid(row=13, column=6)
cb_eci_4_N.config(font=entryfont)
cb_eci_4_N.bind("<<ComboboxSelected>>", setSelectedItemFormula)

lbl_Temp_Units_1 = Label(root, text="Temp Units", width=10)
lbl_Temp_Units_1.grid(row=14, column=0)
lbl_Temp_Units_1.config(font=labelfont)
lbl_Temp_Qty_1 = Label(root, text="Temp Qty", width=10)
lbl_Temp_Qty_1.grid(row=14, column=1)
lbl_Temp_Qty_1.config(font=labelfont)
lbl_Press_Units_1 = Label(root, text="Press Units", width=10)
lbl_Press_Units_1.grid(row=14, column=2, sticky=W)
lbl_Press_Units_1.config(font=labelfont)
lbl_Press_Qty_1 = Label(root, text="Press Qty", width=10)
lbl_Press_Qty_1.grid(row=14, column=3, sticky=W)
lbl_Press_Qty_1.config(font=labelfont)
lbl_Temp_Units_4 = Label(root, text="Temp Units", width=10)
lbl_Temp_Units_4.grid(row=14, column=4)
lbl_Temp_Units_4.config(font=labelfont)
lbl_Temp_Qty_4 = Label(root, text="Temp Qty", width=10)
lbl_Temp_Qty_4.grid(row=14, column=5, sticky=W)
lbl_Temp_Qty_4.config(font=labelfont)
lbl_Press_Units_4 = Label(root, text="Press Units", width=10)
lbl_Press_Units_4.grid(row=14, column=6, sticky=W)
lbl_Press_Units_4.config(font=labelfont)
lbl_Press_Qty_4 = Label(root, text="Press Qty", width=10)
lbl_Press_Qty_4.grid(row=14, column=7, sticky=W)
lbl_Press_Qty_4.config(font=labelfont)

cb_1_Temp_Units: Combobox = Combobox(root, values=temp_units, textvariable=eci_1_temp_units,
                                     width=10)  # eci_temp_1_units
cb_1_Temp_Units.grid(row=15, column=0)
cb_1_Temp_Units.config(font=entryfont)
cb_1_Temp_Units.bind("<<ComboboxSelected>>", eci_units_selected) #callback_set_temp_units)
e_Temp_Qty_1 = Entry(root, text="", textvariable=eci_temp_1_qty, width=8)
e_Temp_Qty_1.grid(row=15, column=1)
e_Temp_Qty_1.config(font=entryfont)
cb_1_Press_Units: Combobox = Combobox(root, values=press_units, textvariable=eci_1_press_units, width=10)
cb_1_Press_Units.grid(row=15, column=2)  # , padx=4)
cb_1_Press_Units.config(font=entryfont)
cb_1_Press_Units.bind("<<ComboboxSelected>>", eci_units_selected) #callback_set_press_units)
e_Press_Qty_1 = Entry(root, text="", textvariable=eci_press_1_qty, width=8)
e_Press_Qty_1.grid(row=15, column=3)
e_Press_Qty_1.config(font=entryfont)
cb_4_Temp_Units: Combobox = Combobox(root, values=temp_units, textvariable=eci_4_temp_units, width=10)
cb_4_Temp_Units.grid(row=15, column=4)
cb_4_Temp_Units.config(font=entryfont)
cb_4_Temp_Units.bind("<<ComboboxSelected>>", eci_units_selected)
e_Temp_Qty_4 = Entry(root, text="", textvariable=eci_temp_4_qty, width=8)
e_Temp_Qty_4.grid(row=15, column=5, sticky=W)
e_Temp_Qty_4.config(font=entryfont)
cb_4_Press_Units: Combobox = Combobox(root, values=press_units, textvariable=eci_4_press_units, width=10)
cb_4_Press_Units.grid(row=15, column=6)
cb_4_Press_Units.config(font=entryfont)
cb_4_Press_Units.bind("<<ComboboxSelected>>", eci_units_selected)
e_Press_Qty_4 = Entry(root, text="", textvariable=eci_press_4_qty, width=8)
e_Press_Qty_4.grid(row=15, column=7)
e_Press_Qty_4.config(font=entryfont)

'''lbl_blank = Label(root, text="")
lbl_blank.grid(row=16, column=0)
lbl_blank.config(font=labelfont)'''

lbl_eci_2 = Label(root, text="   Select Element, Compound or Ion for ComboBox 2")
lbl_eci_2.grid(row=17, column=0, columnspan=3, sticky=W)
lbl_eci_2.config(font=labelfont)
cb_Select_CB2: Combobox = Combobox(root, values=eci_cb_values, width=10)
cb_Select_CB2.grid(row=17, column=3, sticky=W)
cb_Select_CB2.config(font=entryfont)
cb_Select_CB2.bind("<<ComboboxSelected>>", select_eci_2_type)
# btn_Select_CB2 = Button(root, command=Synthesis(variables), text = 'Elements')
# btn_Select_CB2.grid(row=17, column=2)
# btn_Select_CB2.config(font=buttonfont)
lbl_eci_5 = Label(root, text="Select Element, Compound or Ion for ComboBox 5")
lbl_eci_5.grid(row=17, column=4, columnspan=2, sticky=W)
lbl_eci_5.config(font=labelfont)
cb_Select_CB5: Combobox = Combobox(root, values=eci_cb_values, width=10)  # , width=20)
cb_Select_CB5.grid(row=17, column=6)
cb_Select_CB5.config(font=entryfont)
cb_Select_CB5.bind("<<ComboboxSelected>>", select_eci_5_type)

lbl_eci_2_qty = Label(root, text="ECI Qty 2", width=10)
lbl_eci_2_qty.grid(row=19, column=0)
lbl_eci_2_qty.config(font=labelfont)
lbl_eci_2_units = Label(root, text="Units 2", width=10)
lbl_eci_2_units.grid(row=19, column=1, sticky=W)
lbl_eci_2_units.config(font=labelfont)
lbl_eci_2 = Label(root, text="ECI 2")
lbl_eci_2.grid(row=19, column=2, sticky=W)
lbl_eci_2.config(font=labelfont)
lbl_eci_2_valence = Label(root, text="Valence 2", width=10)
lbl_eci_2_valence.grid(row=19, column=3, sticky=W)
lbl_eci_2_valence.config(font=labelfont)
lbl_eci_5_qty = Label(root, text="ECI Qty 5", width=10)
lbl_eci_5_qty.grid(row=19, column=4)
lbl_eci_5_qty.config(font=labelfont)
lbl_eci_5_units = Label(root, text="Units 5", width=10)
lbl_eci_5_units.grid(row=19, column=5)
lbl_eci_5_units.config(font=labelfont)
lbl_eci_5 = Label(root, text="ECI 5", width=10)
lbl_eci_5.grid(row=19, column=6)
lbl_eci_5.config(font=labelfont)
lbl_eci_5_valence = Label(root, text="Valence 5", width=10)
lbl_eci_5_valence.grid(row=19, column=7, sticky=W)
lbl_eci_5_valence.config(font=labelfont)

e_eci_2_qty = Entry(root, text="", textvariable=eci_2_qty, width=8)
e_eci_2_qty.grid(row=20, column=0)
e_eci_2_qty.config(font=entryfont)
# cb_Elements1.bind("<<ComboboxSelected>>", callback_E1)
cb_eci_2_units: Combobox = Combobox(root, values=unit_values, textvariable=eci_2_units, width=10)
cb_eci_2_units.grid(row=20, column=1)
cb_eci_2_units.config(font=entryfont)
cb_eci_2_units.bind("<<ComboboxSelected>>", eci_units_selected)
cb_eci_2: Combobox = Combobox(root, textvariable=eci_2, width=12)
cb_eci_2.grid(row=20, column=2)
cb_eci_2.config(font=entryfont)
cb_eci_2['values'] = elements_symbols_list
cb_eci_2.bind("<<ComboboxSelected>>", setSelectedItemName)
cb_eci_2_valence: Combobox = Combobox(root, textvariable=eci_2_valence, width=8)
cb_eci_2_valence.grid(row=20, column=3)
cb_eci_2_valence.config(font=entryfont)
cb_eci_2_valence['values'] = valences
e_eci_5_qty = Entry(root, text="", textvariable=eci_5_qty, width=8)
e_eci_5_qty.grid(row=20, column=4)
e_eci_5_qty.config(font=entryfont)
cb_eci_5_units: Combobox = Combobox(root, values=unit_values, textvariable=eci_5_units, width=10)
cb_eci_5_units.grid(row=20, column=5)
cb_eci_5_units.config(font=entryfont)
cb_eci_5_units.bind("<<ComboboxSelected>>", eci_units_selected)
cb_eci_5: Combobox = Combobox(root, values=compound_symbols_list, textvariable=eci_5, width=12)
cb_eci_5.grid(row=20, column=6)
cb_eci_5.config(font=entryfont)
cb_eci_5.bind("<<ComboboxSelected>>", setSelectedItemName)
cb_eci_5_valence: Combobox = Combobox(root, textvariable=eci_5_valence, width=5)
cb_eci_5_valence.grid(row=20, column=7)
cb_eci_5_valence.config(font=entryfont)
cb_eci_5_valence['values'] = valences

'''    e_eci_2_M_qty.delete(0)
UnboundLocalError: local variable 'e_eci_2_M_qty' referenced before assignment
'''
# e_eci_2_M_qty = Entry(root, text="", textvariable=eci_2_M_qty, width=8)
# e_eci_1_M_qty.grid(row=13, column=0)
# e_eci_1_M_qty.config(font=entryfont)
e_eci_2_M_qty = Entry(root, text="", textvariable=eci_2_M_qty, width=8)
e_eci_2_M_qty.grid(row=21, column=0)
e_eci_2_M_qty.config(font=entryfont)
lbl_eci_2_units_M = Label(root, text="Moles", width=10)
lbl_eci_2_units_M.grid(row=21, column=1)
lbl_eci_2_units_M.config(font=labelfont)
cb_eci_2_N: Combobox = Combobox(root, values=elements_name_list, textvariable=eci_2_name, width=12)
cb_eci_2_N.grid(row=21, column=2)
cb_eci_2_N.config(font=entryfont)
cb_eci_2_N.bind("<<ComboboxSelected>>", setSelectedItemFormula)
e_eci_5_M_qty = Entry(root, text="CompoundQty 5", textvariable=eci_5_M_qty, width=8)
e_eci_5_M_qty.grid(row=21, column=4)
e_eci_5_M_qty.config(font=entryfont)
lbl_eci_5_units_M = Label(root, text="Moles", width=10)
lbl_eci_5_units_M.grid(row=21, column=5)
lbl_eci_5_units_M.config(font=labelfont)
cb_eci_5_N: Combobox = Combobox(root, values=compound_names_list, textvariable=eci_5_name, width=12)
cb_eci_5_N.grid(row=21, column=6)
cb_eci_5_N.config(font=entryfont)
cb_eci_5_N.bind("<<ComboboxSelected>>", setSelectedItemFormula)

lbl_Temp_Units_2 = Label(root, text="Temp Units", width=10)
lbl_Temp_Units_2.grid(row=22, column=0)
lbl_Temp_Units_2.config(font=labelfont)
lbl_Temp_Qty_2 = Label(root, text="Temp Qty", width=10)
lbl_Temp_Qty_2.grid(row=22, column=1)
lbl_Temp_Qty_2.config(font=labelfont)
lbl_Press_Units_2 = Label(root, text="Press Units", width=10)
lbl_Press_Units_2.grid(row=22, column=2)
lbl_Press_Units_2.config(font=labelfont)
lbl_Press_Qty_2 = Label(root, text="Press Qty", width=10)
lbl_Press_Qty_2.grid(row=22, column=3)
lbl_Press_Qty_2.config(font=labelfont)
lbl_Temp_Units_5 = Label(root, text="Temp Units", width=10)
lbl_Temp_Units_5.grid(row=22, column=4)
lbl_Temp_Units_5.config(font=labelfont)
lbl_Temp_Qty_5 = Label(root, text="Temp Qty", width=10)
lbl_Temp_Qty_5.grid(row=22, column=5, sticky=W)
lbl_Temp_Qty_5.config(font=labelfont)
lbl_Press_Units_5 = Label(root, text="Press Units", width=10)
lbl_Press_Units_5.grid(row=22, column=6)
lbl_Press_Units_5.config(font=labelfont)
lbl_Press_Qty_5 = Label(root, text="Press Qty", width=10)
lbl_Press_Qty_5.grid(row=22, column=7)
lbl_Press_Qty_5.config(font=labelfont)

cb_2_Temp_Units: Combobox = Combobox(root, values=temp_units, textvariable=eci_2_temp_units, width=10)
cb_2_Temp_Units.grid(row=23, column=0)
cb_2_Temp_Units.config(font=entryfont)
cb_2_Temp_Units.bind("<<ComboboxSelected>>", eci_units_selected)
e_Temp_Qty_2 = Entry(root, text="", textvariable=eci_temp_2_qty, width=8)
e_Temp_Qty_2.grid(row=23, column=1)
e_Temp_Qty_2.config(font=entryfont)
cb_2_Press_Units: Combobox = Combobox(root, values=press_units, textvariable=eci_2_press_units, width=10)
cb_2_Press_Units.grid(row=23, column=2)
cb_2_Press_Units.config(font=entryfont)
cb_2_Press_Units.bind("<<ComboboxSelected>>", eci_units_selected)
e_Press_Qty_2 = Entry(root, text="", textvariable=eci_press_2_qty, width=8)
e_Press_Qty_2.grid(row=23, column=3)
e_Press_Qty_2.config(font=entryfont)
cb_5_Temp_Units: Combobox = Combobox(root, values=temp_units, textvariable=eci_5_temp_units, width=10)
cb_5_Temp_Units.grid(row=23, column=4)
cb_5_Temp_Units.config(font=entryfont)
cb_5_Temp_Units.bind("<<ComboboxSelected>>", eci_units_selected)
e_Temp_Qty_5 = Entry(root, text="", textvariable=eci_temp_2_qty, width=8)
e_Temp_Qty_5.grid(row=23, column=5, sticky=W)
e_Temp_Qty_5.config(font=entryfont)
cb_5_Press_Units: Combobox = Combobox(root, values=press_units, textvariable=eci_5_press_units, width=10)
cb_5_Press_Units.grid(row=23, column=6)
cb_5_Press_Units.config(font=entryfont)
cb_5_Press_Units.bind("<<ComboboxSelected>>", eci_units_selected)
e_Press_Qty_5 = Entry(root, text="", textvariable=eci_press_5_qty, width=8)
e_Press_Qty_5.grid(row=23, column=7)
e_Press_Qty_5.config(font=entryfont)

lbl_blank = Label(root, text="")
lbl_blank.grid(row=24, column=0)
lbl_blank.config(font=labelfont)

lbl_eci_3 = Label(root, text="   Select Element, Compound or Ion for ComboBox 3")
lbl_eci_3.grid(row=26, column=0, columnspan=3, sticky=W)
lbl_eci_3.config(font=labelfont)
cb_Select_CB3: Combobox = Combobox(root, values=eci_cb_values, width=10)
cb_Select_CB3.grid(row=26, column=3, sticky=W)
cb_Select_CB3.config(font=entryfont)
cb_Select_CB3.bind("<<ComboboxSelected>>", select_eci_3_type)
lbl_eci_6 = Label(root, text="Select Element, Compound or Ion for ComboBox 6 ")
lbl_eci_6.grid(row=26, column=4, columnspan=2, sticky=W)
lbl_eci_6.config(font=labelfont)
cb_Select_CB6: Combobox = Combobox(root, values=eci_cb_values, width=10)
cb_Select_CB6.grid(row=26, column=6, sticky=W)
cb_Select_CB6.config(font=entryfont)
cb_Select_CB6.bind("<<ComboboxSelected>>", select_eci_6_type)

lbl_eci_3_qty = Label(root, text="ECI Qty 3", width=8)
lbl_eci_3_qty.grid(row=27, column=0)
lbl_eci_3_qty.config(font=labelfont)
lbl_eci_3_units = Label(root, text="Units 3", width=6)
lbl_eci_3_units.grid(row=27, column=1, sticky=W)
lbl_eci_3_units.config(font=labelfont)
lbl_eci_3 = Label(root, text="ECI 3")
lbl_eci_3.grid(row=27, column=2, sticky=W)
lbl_eci_3.config(font=labelfont)
lbl_eci_3_valence = Label(root, text="Valence 3", width=10)
lbl_eci_3_valence.grid(row=27, column=3, sticky=W)
lbl_eci_3_valence.config(font=labelfont)
lbl_eci_6_qty = Label(root, text="ECI Qty 6", width=8)
lbl_eci_6_qty.grid(row=27, column=4)
lbl_eci_6_qty.config(font=labelfont)
lbl_eci_6_units = Label(root, text="Units 6", width=8)
lbl_eci_6_units.grid(row=27, column=5, sticky=W)
lbl_eci_6_units.config(font=labelfont)
lbl_eci_6 = Label(root, text="ECI 6", width=10)
lbl_eci_6.grid(row=27, column=6, sticky=W)
lbl_eci_6.config(font=labelfont)
lbl_eci_6_valence = Label(root, text="Valence 6", width=10)
lbl_eci_6_valence.grid(row=27, column=7, sticky=W)
lbl_eci_6_valence.config(font=labelfont)

e_eci_3_qty = Entry(root, text="", textvariable=eci_3_qty, width=8)
e_eci_3_qty.grid(row=28, column=0)
e_eci_3_qty.config(font=entryfont)
# cb_Elements1.bind("<<ComboboxSelected>>", callback_E1)
cb_eci_3_units: Combobox = Combobox(root, values=unit_values, textvariable=eci_3_units, width=8)
cb_eci_3_units.grid(row=28, column=1, sticky=W)
cb_eci_3_units.config(font=entryfont)
cb_eci_3_units.bind("<<ComboboxSelected>>", eci_units_selected)
cb_eci_3: Combobox = Combobox(root, textvariable=eci_3, width=12)
cb_eci_3.grid(row=28, column=2, sticky=W)
cb_eci_3.config(font=entryfont)
cb_eci_3['values'] = elements_symbols_list
cb_eci_3.bind("<<ComboboxSelected>>", setSelectedItemName)
cb_eci_3_valence: Combobox = Combobox(root, textvariable=eci_3_valence, width=8)
cb_eci_3_valence.grid(row=28, column=3)
cb_eci_3_valence.config(font=entryfont)
cb_eci_3_valence['values'] = valences
e_eci_6_qty = Entry(root, text="", textvariable=eci_6_qty, width=8)
e_eci_6_qty.grid(row=28, column=4)
e_eci_6_qty.config(font=entryfont)
cb_eci_6_units: Combobox = Combobox(root, values=unit_values, textvariable=eci_6_units, width=8)
cb_eci_6_units.grid(row=28, column=5)
cb_eci_6_units.config(font=entryfont)
cb_eci_6_units.bind("<<ComboboxSelected>>", eci_units_selected)
cb_eci_6: Combobox = Combobox(root, values=compound_symbols_list, textvariable=eci_6, width=12)
cb_eci_6.grid(row=28, column=6)
cb_eci_6.config(font=entryfont)
cb_eci_6.bind("<<ComboboxSelected>>", setSelectedItemName)
cb_eci_6_valence: Combobox = Combobox(root, textvariable=eci_6_valence, width=5)
cb_eci_6_valence.grid(row=28, column=7)
cb_eci_6_valence.config(font=entryfont)
cb_eci_6_valence['values'] = valences

e_eci_3_M_qty = Entry(root, text=" ", width=8)
e_eci_3_M_qty.grid(row=29, column=0)
e_eci_3_M_qty.config(font=entryfont, textvariable=eci_3_M_qty)
lbl_eci_3_units_M = Label(root, text="Moles", width=8)
lbl_eci_3_units_M.grid(row=29, column=1)
lbl_eci_3_units_M.config(font=labelfont)
cb_eci_3_N: Combobox = Combobox(root, values=elements_name_list, textvariable=eci_3_name, width=12)
cb_eci_3_N.grid(row=29, column=2)
cb_eci_3_N.config(font=entryfont)
cb_eci_3_N.bind("<<ComboboxSelected>>", setSelectedItemFormula)
e_eci_6_M_qty = Entry(root, text="CompoundQty 6", textvariable=eci_6_M_qty, width=8)
e_eci_6_M_qty.grid(row=29, column=4)
e_eci_6_M_qty.config(font=entryfont)
lbl_eci_6_units_M = Label(root, text="Moles", width=8)
lbl_eci_6_units_M.grid(row=29, column=5)
lbl_eci_6_units_M.config(font=labelfont)
cb_eci_6_N: Combobox = Combobox(root, values=compound_names_list, textvariable=eci_6_name, width=12)
cb_eci_6_N.grid(row=29, column=6)
cb_eci_6_N.config(font=entryfont)
cb_eci_6_N.bind("<<ComboboxSelected>>", setSelectedItemFormula)

lbl_Temp_Units_3 = Label(root, text="Temp Units", width=10)
lbl_Temp_Units_3.grid(row=30, column=0)
lbl_Temp_Units_3.config(font=labelfont)
lbl_Temp_Qty_3 = Label(root, text="Temp Qty", width=10)
lbl_Temp_Qty_3.grid(row=30, column=1)
lbl_Temp_Qty_3.config(font=labelfont)
lbl_Press_Units_3 = Label(root, text="Press Units", width=10)
lbl_Press_Units_3.grid(row=30, column=2)
lbl_Press_Units_3.config(font=labelfont)
lbl_Press_Qty_3 = Label(root, text="Press Qty", width=10)
lbl_Press_Qty_3.grid(row=30, column=3)
lbl_Press_Qty_3.config(font=labelfont)
lbl_Temp_Units_6 = Label(root, text="Temp Units", width=10)
lbl_Temp_Units_6.grid(row=30, column=4)
lbl_Temp_Units_6.config(font=labelfont)
lbl_Temp_Qty_6 = Label(root, text="Temp Qty", width=10)
lbl_Temp_Qty_6.grid(row=30, column=5)
lbl_Temp_Qty_6.config(font=labelfont)
lbl_Press_Units_6 = Label(root, text="Press Units", width=10)
lbl_Press_Units_6.grid(row=30, column=6)
lbl_Press_Units_6.config(font=labelfont)
lbl_Press_Qty_6 = Label(root, text="Press Qty", width=10)
lbl_Press_Qty_6.grid(row=30, column=7)
lbl_Press_Qty_6.config(font=labelfont)

cb_3_Temp_Units: Combobox = Combobox(root, values=temp_units, textvariable=eci_3_temp_units, width=10)
cb_3_Temp_Units.grid(row=31, column=0)
cb_3_Temp_Units.config(font=entryfont)
cb_3_Temp_Units.bind("<<ComboboxSelected>>", eci_units_selected)
e_Temp_Qty_3 = Entry(root, text="", textvariable=eci_temp_3_qty, width=8)
e_Temp_Qty_3.grid(row=31, column=1)
e_Temp_Qty_3.config(font=entryfont)
cb_3_Press_Units: Combobox = Combobox(root, values=press_units, textvariable=eci_3_press_units, width=10)
cb_3_Press_Units.grid(row=31, column=2)
cb_3_Press_Units.config(font=entryfont)
cb_3_Press_Units.bind("<<ComboboxSelected>>", eci_units_selected)
e_Press_Qty_3 = Entry(root, text="", textvariable=eci_press_3_qty, width=8)
e_Press_Qty_3.grid(row=31, column=3)
e_Press_Qty_3.config(font=entryfont)
cb_6_Temp_Units: Combobox = Combobox(root, values=temp_units, textvariable=eci_6_temp_units, width=10)
cb_6_Temp_Units.grid(row=31, column=4)
cb_6_Temp_Units.config(font=entryfont)
cb_6_Temp_Units.bind("<<ComboboxSelected>>", eci_units_selected)
e_Temp_Qty_6 = Entry(root, text="", textvariable=eci_temp_6_qty, width=8)
e_Temp_Qty_6.grid(row=31, column=5)
e_Temp_Qty_6.config(font=entryfont)
cb_6_Press_Units: Combobox = Combobox(root, values=press_units, textvariable=eci_6_press_units, width=10)
cb_6_Press_Units.grid(row=31, column=6)
cb_6_Press_Units.config(font=entryfont)
cb_6_Press_Units.bind("<<ComboboxSelected>>", eci_units_selected)
e_Press_Qty_6 = Entry(root, text="", textvariable=eci_press_6_qty, width=8)
e_Press_Qty_6.grid(row=31, column=7)
e_Press_Qty_6.config(font=entryfont)

lbl_blank = Label(root, text="")
lbl_blank.grid(row=32, column=0)
lbl_blank.config(font=labelfont)

lbl_Equipment = Label(root, text="Equipment", width=10)
lbl_Equipment.grid(row=33, column=0)
lbl_Equipment.config(font=labelfont)
lbl_Energy_type = Label(root, text="Energy type", width=10)
lbl_Energy_type.grid(row=33, column=1, sticky=W)
lbl_Energy_type.config(font=labelfont)
lbl_Energy_amount = Label(root, text="Energy amount", width=12)
lbl_Energy_amount.grid(row=33, column=2, sticky=W)
lbl_Energy_amount.config(font=labelfont)
lbl_Catalyst = Label(root, text="Catalyst", width=10)
lbl_Catalyst.grid(row=33, column=3, sticky=W)
lbl_Catalyst.config(font=labelfont)
lbl_Side_effects = Label(root, text="Side effects", width=12)
lbl_Side_effects.grid(row=33, column=4)
lbl_Side_effects.config(font=labelfont)
lbl_By_products = Label(root, text="By-products", width=10)
lbl_By_products.grid(row=33, column=5, sticky=W)
lbl_By_products.config(font=labelfont)
lbl_Variables = Label(root, text="Variables")
lbl_Variables.grid(row=33, column=6, sticky=W)
lbl_Variables.config(font=labelfont)
lbl_Variables = Label(root, text="Values", width=10)
lbl_Variables.grid(row=33, column=7, sticky=W)
lbl_Variables.config(font=labelfont)

cb_Equipment: Combobox = Combobox(root, values=equipment, textvariable=equipment_selected, width=12)
cb_Equipment.grid(row=34, column=0)
cb_Equipment.config(font=entryfont)
cb_Energy_type: Combobox = Combobox(root, values=energy_type, textvariable=energy_type_selected, width=12)
cb_Energy_type.grid(row=34, column=1, sticky=W)
cb_Energy_type.config(font=entryfont)
e_Energy_amount = Entry(root, text="", textvariable=energy_amount, width=12)
e_Energy_amount.grid(row=34, column=2)
e_Energy_amount.config(font=entryfont)
cb_Catalyst: Combobox = Combobox(root, values=catalyst, textvariable=catalyst_selected, width=12)
cb_Catalyst.grid(row=34, column=3, sticky=W)
cb_Catalyst.config(font=entryfont)
cb_Side_effects: Combobox = Combobox(root, values=side_effects, textvariable=side_effect_selected, width=12)
cb_Side_effects.grid(row=34, column=4)
cb_Side_effects.config(font=entryfont)
cb_By_products: Combobox = Combobox(root, values=by_products, textvariable=by_product_selected, width=12)
cb_By_products.grid(row=34, column=5, sticky=W)
cb_By_products.config(font=entryfont)
cb_Variables: Combobox = Combobox(root, values=variables, textvariable=variable_selected, width=12)
cb_Variables.grid(row=34, column=6, sticky=W)
cb_Variables.config(font=entryfont)
e_Variable_Value = Entry(root, text="", textvariable=variable_value, width=8)
e_Variable_Value.grid(row=34, column=7)
e_Variable_Value.config(font=entryfont)

lbl_Explanation = Label(root, text="Explanation", width=10)
lbl_Explanation.grid(row=35, column=0)
lbl_Explanation.config(font=labelfont)
lbl_Explanation = Label(root, text="Super subscript ", width=12)
lbl_Explanation.grid(row=35, column=1)
lbl_Explanation.config(font=labelfont)
lbl_LU_Process = Label(text='360\u2070 \u2070C H\u2082O')  # C2H3O2-
lbl_LU_Process.grid(row=35, column=2)
lbl_LU_Process.config(font=labelfont)
'''
unicode numbers. degrees: \u2070 subscript 2: \u2082 subscript 3: \u2083 subscript e: \u2091
superscript 2:\u00B2 superscript 3:\u00B3 superscript 4: \u2074 superscript -: \u207B
'''
lbl_LU_Process = Label(text='X\u2074 + X\u00B2 = 0')
lbl_LU_Process.grid(row=35, column=3)
lbl_LU_Process.config(font=labelfont)
lbl_LU_Process = Label(text='C\u2082H\u2083O\u2082\u207B C\u2082H\u2083O\u00B2\u207B')
# lbl_LU_Process = Label(text='C\u00B2\u207A Fe\u00B3\u207A Cl\u207B e\u207B')
lbl_LU_Process.grid(row=35, column=4)
lbl_LU_Process.config(font=labelfont)
lbl_LU_Process = Label(text='Cl\u2091 Fe\u00B3\u207A ')
lbl_LU_Process.grid(row=35, column=5)
lbl_LU_Process.config(font=labelfont)
e_Explanation = Text(root, height=6, width=100)
e_Explanation.grid(row=36, column=0, columnspan=6, sticky=W)
e_Explanation.config(font=entryfont)
e_Explanation.rowconfigure(99)

# e_Explanation.insert(1, 'Fe\u00B2\u207A Fe\u00B3\u207A Cl\u207B e\u207B')
S = tk.Scrollbar(root)
S.grid(row=36, column=7, sticky=E)
S.config(command=e_Explanation.yview)

lbl_blank = Label(root, text="")
lbl_blank.grid(row=40, column=0, columnspan=2)
lbl_blank.config(font=labelfont)
lbl_blank = Label(root, text="")
lbl_blank.grid(row=41, column=0, columnspan=2)
lbl_blank.config(font=labelfont)
lbl_blank = Label(root, text="")
lbl_blank.grid(row=42, column=0, columnspan=2)
lbl_blank.config(font=labelfont)
# *** End GUI layout

if __name__ == '__main__':
    #create_variables()
    #mcf()
    # set_temp_and_press_settings()
    # make_element_dictionary()
    # make_compound_dictionary()
    # make_ion_dictionary()
    # make_compound_alpha_list()
    # make_ion_alpha_list()
    root.mainloop()

    # print(element)

''' *** e_eci_1_qty.bind('<FocusOut>', (lambda event: check_entry_changes())) ***'''
