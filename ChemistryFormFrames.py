# Time to refactor
from tkinter import *  # get widget classes
from tkinter.ttk import Combobox #,Textbox
from tkinter.ttk import Entry
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
titlefont= ('Ariel', 14, 'bold')
labelfont= ('Ariel', 14) #, 'bold')
buttonfont= ('Ariel', 12) #, 'bold')
entryfont= ('Ariel', 12) #, 'bold')

''' *** e_eci_1_qty.insert(0, eci_1_M_qty) WORKS to insert a value into an entry box !!! *** '''

# *** Start constants and variables
''' The element list below has been superceded and will be deleted when it has been confirmed to be
unnecessary. '''
elements = "Ac Ag Al Am Ar As At Au B Ba Be Bi Bk Br C Ca Cd Ce Cf Cl Cm Co Cr Cs Cu Dy Er Es Eu " \
 "F Fe Fm Fr Ga Gd Ge H He Hf Hg Ho I In Ir K Kr La Li Lu Md Mn Mo N Na Nb Nd Ne Ni Np O Os " \
 "P Pa Pb Pd Pm Po Pr Pt Pu Ra Rb Re Rh Rn  Ru S Sb Sc Se Si Sm Sn Sr Ta Tb Tc Te Th Ti Tl Tm" \
 "U V W Xe Y Yb Zn Zr "
''' The following is a list of all elements that are likely to be used, and a few more. 

Text with unicode can be included in combo boxes. Such use requires setting up a dictionary
to associate the text with elements that have quantities different from the standard.

Not all the elements and their attributes have been added to the database. H\u2082 works for H2 subscript'''
elements_symbols_list = "Ac Ag Al Am Ar As At Au B Ba Be Bi Bk Br C Ca Cd Ce Cf Cl Cm Co Cr Cs Cu Dy Er Es Eu " \
 "F Fe Fm Fr Ga Gd Ge H He Hf Hg Ho I In Ir K Kr La Li Lu Md Mn Mo N Na Nb Nd Ne Ni Np O Os " \
 "P Pa Pb Pd Pm Po Pr Pt Pu Ra Rb Re Rh Rn  Ru S Sb Sc Se Si Sm Sn Sr Ta Tb Tc Te Th Ti Tl Tm" \
 "U V W Xe Y Yb Zn Zr "
''' An element name list is used to fill the element name combo box to help the user who knows 
the name of an element, but not the symbols. '''
elements_name_list = "Actinium Silver Aluminum Americium Argon Arsenic Astatine Gold Boron Barium Beryllium " \
    "Bismuth Berkelium Bromine Carbon Calcium Cadmium Cerium Californium Chlorine Curium Cobalt Chromium " \
    "Cesium Copper Dysprosium Erbium Einsteinium Europium Fluorine Iron Fermium Francium Gallium Gadolinium "\
    "Germanium Hydrogen Helium Hafnium Mercury Holmium Iodine Indium Iridium Potassium Krypton " \
    "Lanthanum Lithium Lutetium Mendelevium Manganese Molybdenum Nitrogen Na Niobium Neodymium Neon Nickel " \
    "Neptunium Oxygen Osmium Phosphorus Protactinium Lead Palladium Promethium Polonium Praseodymium " \
    "Platnum Plutonium Radium Rubidium Rhenium Rhodium Radon Rutherfordium Sulfur Antimony Scandium Selenium Silicon " \
    "Samarium Tin Strontium Tantalum Terbium Technetium Tellurium Thorium Titanium " \
    "Thallium Thulium Uranium Vanadium Tungsten Xenon Yttrium Ytterbium Zinc Zirconium "
''' This list of elements and names will help retrieve names from symbols. '''
#element = zip(elements_symbols_list, elements_name_list)
element_names_Dict = {'Actinium': 'Ac', 'Silver': 'Ag', 'Aluminum': 'Al', 'Americium': 'Am', 'Argon': 'Ar',
                      'Arsenic': 'As', 'Astatine': 'At', 'Gold': 'Au', 'Boron': 'B', 'Barium': 'Ba',
                      'Beryllium': 'Be', 'Bismuth': 'Bi', 'Berkelium': 'Bk', 'Bromine': 'Br', 'Carbon': 'C',
                      'Calcium': 'Ca', 'Cadmium': 'Cd', 'Cerium': 'Ce', 'Californium': 'Cf', 'Chlorine': 'Cl',
                      'Curium': 'Cm', 'Cobalt': 'Co', 'Chromium': 'Cr', 'Cesium': 'Cs', 'Copper': 'Cu',
                      'Dysprosium': 'Dy', 'Erbium': 'Er', 'Einsteinium': 'Es', 'Europium': 'Eu', 'Fluorine': 'F',
                      'Iron': 'Fe', 'Fermium': 'Fm', 'Francium': 'Fr', 'Gallium': 'Ga', 'Gadolinium': 'Gd',
                      'Germanium': 'Ge', 'Hydrogen': 'H', 'Helium': 'He', 'Hafnium': 'Hf', 'Mercury': 'Hg',
                      'Holmium': 'Ho', 'Iodine': 'I', 'Indium': 'In', 'Iridium': 'Ir', 'Potassium': 'K',
                      'Krypton': 'Kr', 'Lanthanum': 'La', 'Lithium': 'Li', 'Lutetium': 'Lu', 'Mendelevium': 'Md',
                      'Manganese': 'Mn', 'Molybdenum': 'Mo', 'Nitrogen': 'N', 'Na': 'Na', 'Niobium': 'Nb',
                      'Neodymium': 'Nd', 'Neon': 'Ne', 'Nickel': 'Ni', 'Neptunium': 'Np', 'Oxygen': 'O',
                      'Osmium': 'Os', 'Phosphorus': 'P', 'Protactinium': 'Pa', 'Lead': 'Pb', 'Palladium': 'Pd',
                      'Promethium': 'Pm', 'Polonium': 'Po', 'Praseodymium': 'Pr', 'Platnum': 'Pt', 'Plutonium': 'Pu',
                      'Radium': 'Ra', 'Rubidium': 'Rb', 'Rhenium': 'Re', 'Rhodium': 'Rh', 'Radon': 'Rn',
                      'Rutherfordium': 'Ru', 'Sulfur': 'S', 'Antimony': 'Sb', 'Scandium': 'Sc', 'Selenium': 'Se',
                      'Silicon': 'Si', 'Samarium': 'Sm', 'Tin': 'Sn', 'Strontium': 'Sr', 'Tantalum': 'Ta',
                      'Terbium': 'Tb', 'Technetium': 'Tc', 'Tellurium': 'Te', 'Thorium': 'Th', 'Titanium': 'Ti',
                      'Thallium': 'Tl', 'Thulium': 'Tm', 'Uranium': 'U', 'Vanadium': 'V', 'Tungsten': 'W',
                      'Xenon': 'Xe', 'Yttrium': 'Y', 'Ytterbium': 'Yb', 'Zinc': 'Zn', 'Zirconium': 'Zr'}
''' Tried to change symbols to use subscripts, but the Compound Dictionary would not accept 
a subscripted formula as a valid key'''
compound_symbols_list = "Al4C3 AlCl3 Ar2He2Kr2Ne2Xe2Rn2 BCl3 CH4 C2H6 C3H8 C4H10 C4H10, C5H12 C6H14 C7H16 C8H18 " \
                        "C9H20 C10H22 C14H30 C18H38 CaH2PO4 CaI CaOH2 Ca3P2 CdS CsF C6H8O7 CH3CO2H C2H4COH " \
                        "CO CO2 HBr HC2H3O2 HCl HClO4 HCN H2CO3 HF HI " \
                        "HNO2 HNO3 H3PO4 H2S H2SO3 H2SO4 IF7 KBr KOH LiCl Mg3N2 NaCl NaHCO3 Na2O NaOH " \
                        "Na2SO4 NH3 N2H4 NO NO2 N2O4 N2O N2O5 PF5 SO2 SO3 "

compound_names_list = "aluminum_carbide aluminum_chloride air boron_trichloride methane ethane propane butane 2-methylpropane" \
                      " pentane hexane heptane octane nonane decane tetradecane octadecane calcium_dihydrogen_phosphate" \
                      " calcium_iodide calcium_hydroxide calcium_phosphide cadmium_sulfide cesium_fluoride citric_acid" \
                      " acetic_acid acetic_acid carbon_monoxide carbon_dioxide hydrogen_bromide " \
                      " acetic_acid hydrogen_chloride hydrochloric_acid perchloric_acid hydrogen_cyanide" \
                      " carbonic_acid hydrogen_fluoride hydrofluoric_acid hydrogen_iodide nitrous_acid" \
                      " nitric_acid phosphoric_acid hydrogen_suflide sulfurous_acid sulfuric_acid" \
                      " iodine_heptafluoride potassium_bromide potassium_hydroxide lithium_chloride magnesium_nitride" \
                      " sodium_chloride bicarbonate_of_soda sodium_oxide sodium_hydroxide sodium_sulfate ammonia hydrazine nitric_oxide" \
                      " nitorgen_dioxide dinitrogen_tetroxide nitrous_oxide dinitrogen_pentoxide phosphorus_pentafluoride" \
                      " sulfur_dioxide sulfur_trioxide"
''' This list of compounds and names will help retrieve names from formulas. Doesn't work. Why? '''
compounds_names_dict = {'aluminum_carbide': 'Al4C3', 'aluminum_chloride': 'AlCl3', 'air': 'Ar2He2Kr2Ne2Xe2Rn2',
                        'boron_trichloride': 'BCl3', 'methane': 'CH4', 'ethane': 'C2H6', 'propane': 'C3H8',
                        'butane': 'C4H10', '2-methylpropane': 'C4H10_M', 'pentane': 'C5H12', 'hexane': 'C6H14',
                        'heptane': 'C7H16', 'octane': 'C8H18', 'nonane': 'C9H20', 'decane': 'C10H22',
                        'tetradecane': 'C14H30', 'octadecane': 'C18H38', 'calcium_dihydrogen_phosphate': 'CaH2PO4',
                        'calcium_iodide': 'CaI', 'calcium_hydroxide': 'CaOH2', 'calcium_phosphide': 'Ca3P2',
                        'cadmium_sulfide': 'CdS', 'cesium_fluoride': 'CsF', 'citric_acid': 'C6H8O7',
                        'acetic_acid': 'HC2H3O2', 'carbon_monoxide': 'CO', 'carbon_dioxide': 'CO2',
                        'hydrogen_bromide': 'HBr',
                        'hydrochloric_acid': 'HCl', 'perchloric_acid': 'HClO4', 'hydrogen_cyanide': 'HCN',
                        'carbonic_acid': 'H2CO3', 'hydrofluoric_acid': 'HF',
                        'hydroiodic_acid': 'HI', 'nitrous_acid': 'HNO2',
                        'nitric_acid': 'HNO3', 'phosphoric_acid': 'H3PO4',
                        'hydrosulfuric_acid': 'H2S', 'sulfurous_acid': 'H2SO3', 'sulfuric_acid': 'H2SO4',
                        'iodine_heptafluoride': 'IF7', 'potassium_bromide': 'KBr', 'potassium_hydroxide': 'KOH',
                        'lithium_chloride': 'LiCl', 'magnesium_nitride': 'Mg3N2', 'sodium_chloride': 'NaCl',
                        'bicarbonate_of_soda': 'NaHCO3', 'sodium_oxide': 'Na2O', 'sodium_hydroxide': 'NaOH',
                        'sodium_sulfate': 'Na2SO4', 'ammonia': 'NH3', 'hydrazine': 'N2H4', 'nitric_oxide': 'NO',
                        'nitorgen_dioxide': 'NO2', 'dinitrogen_tetroxide': 'N2O4', 'nitrous_oxide': 'N2O',
                        'dinitrogen_pentoxide': 'N2O5', 'phosphorus_pentafluoride': 'PF5', 'sulfur_dioxide': 'SO2',
                        'sulfur_trioxide': 'SO3'}
ion_names_dict = {'acetate': 'C2H3O2', 'chlorite': 'ClO2', 'chlorate': 'ClO3', 'perchlorate': 'ClO4',
                   'cyanide': 'CN', 'carbonate': 'CO32', 'copper_(II)_sulfide': 'CuS', 'iron_(II)_chloride': 'FeCl2',
                   'iron_(III)_chloride': 'FeCl3','dihydrogen_phosphate': 'H2PO4','hydrogen_carbonate': 'HCO3',
                   'mercury_(I)_oxide': 'Hg2O','mercury_(II)_oxide': 'HgO', 'hydronium': 'H3O',
                   'hydrogen_phosphate': 'HPO42','hydrogen_sulfate': 'HSO4','hydroxide': 'OH',
                   'ammonium': 'NH4', 'nitrate': 'NO3','nitrite': 'NO2',
                   'permanganate': 'MnO4','peroxide': 'H2O22','sulfate': 'SO42',
                   'sulfite': 'SO32', 'phosphate': 'PO43'}

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

''' An initial list of ions and names to fill the combo boxes until a proper list can be made. '''

#ion_names_list = "hydroxide sulfate"

ion_names_list = "acetate chlorite chlorate perchlorate cyanide carbonate copper_(II)_sulfide " \
                 "iron_(II)_chloride iron_(III)_chloride dihydrogen_phosphate hydrogen_carbonate " \
                 "mercury_(I)_oxide mercury_(II)_oxide hydronium hydrogen_phosphate hydrogen_sulfate " \
                 "hydroxide ammonium nitrate nitrite permanganate peroxide sulfate sulfite phosphate "
unit_values = "Moles grams kilograms ounces pounds liters(l) liters(g) ml(l) ml(g)"
eci_cb_values = "elements compounds ions"
environment = "Laboratory Industry Nature"
temp_umits = "K F C"
press_umits = "ATM torr psi hg"
ion_symbols_list = "C2H3O2 ClO2 ClO3 ClO4 CN CO32 CuS FeCl2 FeCl3 H2PO4 HCO3 Hg2O HgO H3O HPO42 HSO4 OH NH4 NO3 NO2 MnO4 O22 SO42 SO32 PO43"

c_alpa_list = "AlC, AlCl, ArHeKrNeXeRn, Ar2He2Kr2Ne2Xe2Rn2, BCl, CH, CaHOP, CaI, CaHO, CaP, CdS, CsF, CHO, CO, CuS, BrH"

record_name = ""    # This is a placeholder for a record name to store the process in the database.
''' The following are lists of variables to fill various combo boxes until proper lists are made. '''
process_list = "Parse_Compounds Acid_Base Calculate Oxidation_Reduction Oxidation_Rate Precipitation Synthesis Decompose Refine Metathesis "
equipment = "refinery blah1 blah2"
energy_type = "heat electricity"
catalyst = "blah1 blah2 blah3 blah4"
side_effects = "air_polution water_polution land_polution"
by_products = "CO CO2 NO NO2"
variables ="Av Bv Cv Kv"     # Variable names cannot conflict with element symbols like B C H K etc
''' Variables to hold the selected items of combo boxes. '''
process_selected = ""
equipment_selected = ""
energy_type_selected = ""
catalyst_selected = ""
side_effect_selected = ""
by_product_selected = ""
variable_selected = ""
variable_value = DoubleVar()
Av = DoubleVar()
Bv = DoubleVar()
Cv = DoubleVar()
Kv = DoubleVar()

''' Miscellaneous variables to use until proper variables are created. '''
valences = "7 6 5 4 3 2 1 0 -1 -2 -3 -4"
element1 = StringVar()
'''
*** The following line describes the structure of the eci dictionary. ***
d_eci_1 = dict(eci='', eci_type= '', name= '', column= '', electronegativity = "", _group = "", 
            qty = "", M_qty = "" , mass = "", Oxidation_State ="", units = "", valence = "",
            temp_units= "", temp_qty="", press_units= "", press_qty= "")
'''
''' Many of the variables below are needed because they record selection of items in combo boxes. 
The extraneous ones will be deleted as they are identified. '''
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
eci_1_electronegativity = DoubleVar()
eci_2_electronegativity = DoubleVar()
eci_3_electronegativity = DoubleVar()
eci_4_electronegativity = DoubleVar()
eci_5_electronegativity = DoubleVar()
eci_6_electronegativity = DoubleVar()
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
''' Initialize values -- because I have need to do that in other programs. '''
cb_1_type = ""  # elements compounds ions
cb_2_type = ""
cb_3_type = ""
cb_4_type = ""
cb_5_type = ""
cb_6_type = ""

 # *** End constants and variables

# *** Start function descriptions
''' All the select_eci_type functions work. User selects the type eci 
and the function loads the appropriate elements,compounds or ions in the symbol/formula
combo boxes and their names in the names combo boxes. '''
def select_eci_1_type(eventObject):
    cb_1_type = cb_Select_CB1.get() # use cb_1_type as a local variable to improve readability
    eci_db['eci_1']['eci_type'] = cb_Select_CB1.get()
    #print("cb_1_type is ", cb_1_type)
    ''' Both of the assignments below work. '''
    #print("eci_db['eci_1']['eci_type'] is ", eci_db['eci_1']['eci_type'])
    #print("eci_db['eci_1']['eci_type'] is ", cb_1_type)
    eci_db['eci_1']['eci_type'] = cb_1_type
    if cb_1_type == 'elements':
        cb_eci_1['values'] = elements_symbols_list
        cb_eci_1_N['values'] = elements_name_list
    elif cb_1_type == 'compounds':
        cb_eci_1['values'] = compound_symbols_list
        cb_eci_1_N['values'] = compound_names_list
    elif cb_1_type == 'ions':
        cb_eci_1['values'] = ion_symbols_list
        cb_eci_1_N['values'] = ion_names_list
    else: print("Error is select_eci_1_type")
def select_eci_2_type(eventObject):
    cb_2_type = cb_Select_CB2.get()
    print("cb_2_type is ", cb_2_type)
    eci_db['eci_2']['eci_type'] = cb_Select_CB2.get()
    if cb_2_type == 'elements':
        cb_eci_2['values'] = elements_symbols_list
        cb_eci_2_N['values'] = elements_name_list
    elif cb_2_type == 'compounds':
        cb_eci_2['values'] = compound_symbols_list
        cb_eci_2_N['values'] = compound_names_list
    elif cb_2_type == 'ions':
        cb_eci_2['values'] = ion_symbols_list
        cb_eci_2_N['values'] = ion_names_list
    else: print("Error is select_eci_2_type")
def select_eci_3_type(eventObject):
    cb_3_type = cb_Select_CB3.get()
    print("cb_3_type is ", cb_3_type)
    eci_db['eci_3']['eci_type'] = cb_Select_CB3.get()
    if cb_3_type == 'elements':
        cb_eci_3['values'] = elements_symbols_list
        cb_eci_3_N['values'] = elements_name_list
    elif cb_3_type == 'compounds':
        cb_eci_3['values'] = compound_symbols_list
        cb_eci_3_N['values'] = compound_names_list
    elif cb_3_type == 'ions':
        cb_eci_3['values'] = ion_symbols_list
        cb_eci_3_N['values'] = ion_names_list
    else: print("Error is select_eci_3_type")
def select_eci_4_type(eventObject):
    cb_4_type = cb_Select_CB4.get()
    print("cb_4_type is ", cb_4_type)
    eci_db['eci_4']['eci_type'] = cb_Select_CB4.get()
    if cb_4_type == 'elements':
        cb_eci_4['values'] = elements_symbols_list
        cb_eci_4_N['values'] = elements_name_list
    elif cb_4_type == 'compounds':
        cb_eci_4['values'] = compound_symbols_list
        cb_eci_4_N['values'] = compound_names_list
    elif cb_4_type == 'ions':
        cb_eci_4['values'] = ion_symbols_list
        cb_eci_4_N['values'] = ion_names_list
    else: print("Error is select_eci_4_type")
def select_eci_5_type(eventObject):
    cb_5_type = cb_Select_CB5.get()
    print("cb_5_type is ", cb_5_type)
    eci_db['eci_5']['eci_type'] = cb_Select_CB5.get()
    if cb_5_type == 'elements':
        cb_eci_5['values'] = elements_symbols_list
        cb_eci_5_N['values'] = elements_name_list
    elif cb_5_type == 'compounds':
        cb_eci_5['values'] = compound_symbols_list
        cb_eci_5_N['values'] = compound_names_list
    elif cb_5_type == 'ions':
        cb_eci_5['values'] = ion_symbols_list
        cb_eci_5_N['values'] = ion_names_list
    else: print("Error is select_eci_5_type")
def select_eci_6_type(eventObject):
    cb_6_type = cb_Select_CB6.get()
    print("cb_6_type is ", cb_6_type)
    eci_db['eci_6']['eci_type'] = cb_Select_CB6.get()
    if cb_6_type == 'elements':
        cb_eci_6['values'] = elements_symbols_list
        cb_eci_6_N['values'] = elements_name_list
    elif cb_6_type == 'compounds':
        cb_eci_6['values'] = compound_symbols_list
        cb_eci_6_N['values'] = compound_names_list
    elif cb_6_type == 'ions':
        cb_eci_6['values'] = ion_symbols_list
        cb_eci_6_N['values'] = ion_names_list
    else: print("Error is select_eci_6_type")

''' Start defining process and chemistry related functions '''
def create_record():
    print("Pressed create_record button")
def get_record():
    pass
    #print("Pressed Get Record button")
def retrieve_record():
    pass
    #print("Pressed Retrieve Record button")
def previous_record():
    pass
    #print("Pressed Previous Record button")
def next_record():
    pass
    #print("Pressed Next Record button")
def update_record():
    #pass
    print("Pressed Update Record button")

def check_entry_changes():
    eci_1 = cb_eci_1.get()
    eci_1_qty = e_eci_1_qty.get()
    eci_1_mass = float(db[eci_1]['mass']) #float( temp_entry.get() )
    eci_db['eci_1']['qty'] = eci_1_qty
    print("e_eci_1_qty.get() is ", e_eci_1_qty.get())
    print("eci_1_qty is ", e_eci_1_qty.get())   #eci_1_qty is  PY_VAR54
    print("eci_db['eci_1']['qty'] is ", eci_1_qty)
    print("eci_1_mass is ", eci_1_mass)
    ''' The following works. '''
    total_mass = float(e_eci_1_qty.get()) * eci_1_mass  #float(db[eci_1]['mass'])
    print("total_mass is ", total_mass)

def Continue():
    process_selected = cb_Select_Process.get()
    print("Process selected is " , process_selected)
    #check_entry_changes()

    if process_selected == "Acid_Base":
        #print("Synthesis process entered")
        Acid_Base()
    elif process_selected == "Calculate":
        #print("Decompose process entered")
       Calculate()
    elif process_selected == "Decompose":   #Calculate()
        #print("Decompose process entered")
        Decompose()
    elif process_selected == "Oxidation_Reduction":
        #print("Decompose process entered")
        Oxidation_Reduction()
    elif process_selected == "Metathesis":  #Oxidation_Rate
        Metathesis()
        #print("Decompose process entered")
    elif process_selected == "Oxidation_Rate": #
        Oxidation_Rate()
    elif process_selected == "Parse_Compounds":
        ''' There is a general procedure used to prove parse works,
        and a procedure tied to the eci_1 combobox. '''
        Parse_Compounds()
    elif process_selected == "Precipitation":
        Precipitation()
    elif process_selected == "Reduction":
        Reduction()
    elif process_selected == "Refine":
        Refine()
    elif process_selected == "Synthesis":
        Synthesis()
    else: print("No process has been selected in Continue selection of process")
    #CountElements()
    #AlphabetizeElements()
    #eci_1 = cb_eci_1.get()
    #print("Process selected is " , process_selected)
    #print('eci_1 = ', eci_1)
    #print("Pressed Continue button")
def Calculate():
    ''' a step toward calculating variables associated with an eci. '''
    eci_1 = cb_eci_1.get()
    #print('eci_1 is ', eci_1)
    eci_1_M_qty = e_eci_1_M_qty.get()
    ''' e_eci_1_qty.insert(0, eci_1_M_qty) WORKS!!! '''
    #print('eci_1_M_qty is ', eci_1_M_qty)
    if not eci_1_M_qty == "":
        eci_1_mass = (db[eci_1]['mass'])
        #print('eci_1_mass = ', eci_1_mass)
        m_mass =  float(eci_1_M_qty) * float(eci_1_mass)
        e_eci_1_qty.insert(0, m_mass)
        e_Explanation.insert(END, m_mass)
        print('m_mass is ', m_mass)

def Oxidation_Reduction():
    ''' This function has been entered after elements have been selected and the COntinue button pressed'''
    e_Explanation.insert(tk.END, "Oxidation_Reduction process entered\n")
    Oxidation_Rate()
    cb_1_type = cb_Select_CB1.get()   # Get the selected type of: element, compound, or ion
    print('eci_1_type = ', cb_1_type)
    eci_1 = cb_eci_1.get()
    print('eci_1 = ', eci_1)
    if cb_1_type == 'elements':
        '''  *** The following works! '''

        #eci_db['eci_1']['name']
        eci_db['eci_1']['name'] = db[eci_1]['name']
        #eci_db[eci_1]['name'] = db[eci_1]['name']
        print("eci_db['eci_1']['name'] is ", eci_db['eci_1']['name'])
        eci_1_name = db[eci_1]['name']
        print("db[eci_1]['name'] is ", eci_1_name)

        eci_1_col = db[eci_1]['column']
        eci_1_mass = db[eci_1]['mass']
        eci_1_valence = db[eci_1]['valence']
        eci_db['eci_1']['column'] = db[eci_1]['column']
        eci_db['eci_1']['mass'] = db[eci_1]['mass']
        eci_db['eci_1']['valence'] = db[eci_1]['valence']
        print("eci_db['eci_1']['column'] is ", eci_db['eci_1']['column'])
        print("eci_db['eci_1']['mass'] is ", eci_db['eci_1']['mass'])
        print("eci_db['eci_1']['valence'] is ", eci_db['eci_1']['valence'])
        #print("db[eci_1]['name'] is ", eci_1_name)
        #print("db[eci_1]['column'] is ", eci_1_col)
        #print("db[eci_1]['mass'] is ", eci_1_mass)
        #print("db[eci_1]['valence'] is ", eci_1_valence)
        #print(eci_1_valence)   # Prints out the variable #str(eci_1).affinity
    elif cb_1_type == 'compounds':
        #eci_1 = cb_eci_1.get()
        #print('eci_1 = ', eci_1)
        e_Explanation.insert(tk.END, "Oxidation_Reduction process entered\n")
        print("Error in Oxidation_Reduction eci_1 can't process compounds yet")
    elif cb_1_type == 'ions':
        #eci_1 = cb_eci_1.get()
        #print('eci_1 = ', eci_1)
        e_Explanation.insert(tk.END, "Error in Oxidation_Reduction eci_1 can't process compounds yet")
    else: print("Error in Oxidation_Reduction process eci_1 else clause")
    cb_2_type = cb_Select_CB2.get()   # Get the selected type of: element, compound, or ion
    print('eci_2_type = ', cb_2_type)
    if cb_2_type == 'elements':
        eci_2 = cb_eci_2.get()
        print('eci_2 = ', eci_2)
        '''  *** The following works! '''
        eci_2_name = db[eci_2]['name']
        eci_2_col = db[eci_2]['column']
        eci_2_mass = db[eci_2]['mass']
        eci_2_valence = db[eci_2]['valence']
        print("db[eci_2]['name'] is ", eci_2_name)
        print("db[eci_2]['column'] is ", eci_2_col)
        print("db[eci_2]['mass'] is ", eci_2_mass)
        print("db[eci_2]['valence'] is ", eci_2_valence)
        #print(eci_1_valence)   # Prints out the variable #str(eci_1).affinity
    elif cb_2_type == 'compounds':
        #eci_2 = cb_eci_2.get()
        #print('eci_2 = ', eci_2)
        print("Error in Oxidation_Reduction eci_2 can't process compounds yet")
    elif cb_2_type == 'ions':
        #eci_2 = cb_eci_2.get()
        #print('eci_2 = ', eci_2)
        print("Error in Oxidation_Reduction eci_2 can't process ions yet")
    else: print("Error in Oxidation_Reduction process eci_2 else clause")
    cb_3_type = cb_Select_CB3.get()   # Get the selected type of: element, compound, or ion
    print('eci_3_type = ', cb_3_type)
    eci_3 = cb_eci_3.get()
    print('eci_3 = ', eci_3)
    if cb_3_type == 'elements':
        #eci_3 = cb_eci_3.get()
        #print('eci_3 = ', eci_3)
        '''  *** The following works! '''
        eci_3_name = db[eci_3]['name']
        eci_3_col = db[eci_3]['column']
        eci_3_mass = db[eci_3]['mass']
        eci_3_valence = db[eci_3]['valence']
        print("db[eci_3]['name'] is ", eci_3_name)
        print("db[eci_3]['column'] is ", eci_3_col)
        print("db[eci_3]['mass'] is ", eci_3_mass)
        print("db[eci_3]['valence'] is ", eci_3_valence)
        #print(eci_1_valence)   # Prints out the variable #str(eci_1).affinity
    elif cb_3_type == 'compounds':
        #eci_3 = cb_eci_3.get()
        #print('eci_3 = ', eci_3)
        print("Error in Oxidation_Reduction eci_3 can't process compounds yet")
    elif cb_3_type == 'ions':
        #eci_3 = cb_eci_3.get()
        #print('eci_3 = ', eci_3)
        print("Error in Oxidation_Reduction eci_3 can't process ions yet")
    elif cb_3_type == "":
        pass
    else: e_Explanation.insert(tk.END, "Error in Oxidation_Reduction process eci_3 else clause\n")

    #if cb_eci_1.get() == 'elements':
    #    eci_1 = cb_eci_1.get()
    #    print('eci_1 = ', eci_1)
    #    print('eci_1_type = ', cb_eci_1.get())
def Precipitation():
    e_Explanation.insert(tk.END, "Precipitation process entered\n")
    #print("Precipitation process entered")

def Oxidation_Rate():
    cb_1_type = cb_Select_CB1.get()
    cb_2_type = cb_Select_CB2.get()
    cb_3_type = cb_Select_CB3.get()
    if cb_1_type == elements and cb_2_type == elements and cb_3_type == elements or cb_3_type == "":
        Oxidation_Rate_Elements()
    elif cb_1_type == 'compounds' or cb_2_type == 'compounds' and cb_3_type == 'compounds':
        Oxidation_Rate_Compounds()
    elif cb_1_type == 'ions' or cb_2_type == 'ions' and cb_3_type == 'ions':
        Oxidation_Rate_Ions()
    else: e_Explanation.insert(tk.END, "Oxidation_Rate process fell through to else clause\n")
''' Oxidation_Rate_Compounds and Oxidation_Rate_Ions are placeholders for future use as needed. '''
def Oxidation_Rate_Compounds():
    e_Explanation.insert(tk.END, "Entered Oxidation_Rate_Compounds process\n")
def Oxidation_Rate_Ions():
    e_Explanation.insert(tk.END, "Entered Oxidation_Rate_Ions process\n")

def Oxidation_Rate_Elements():
    ''' This function has been entered after elements have been selected and the Continue button pressed'''
    cb_eci_1_units.set('grams')
    cb_eci_2_units.set('grams')
    cb_eci_4_units.set('grams')

    e_Explanation.insert(tk.END, "Oxidation_Rate_Elements process entered\n")

    '''  Each item is an element. Compounds and ions use a different function.
    It is necessary to get the valence and electronegativity values because the valence of some
    elements is determined by the relative electronegativity of the other elements. '''
    '''
    cb_1_type = cb_Select_CB1.get()
    cb_2_type = cb_Select_CB2.get()
    cb_3_type = cb_Select_CB3.get()
    '''
    eci_1 = cb_eci_1.get()
    eci_2 = cb_eci_2.get()
    eci_3 = cb_eci_3.get()
    ''' Set the values in the eci frame dictionary. '''
    eci_db['eci_1']['eci'] = cb_eci_1.get()
    eci_db['eci_2']['eci'] = cb_eci_2.get()
    eci_db['eci_3']['eci'] = cb_eci_3.get()
    ''' The following demonstrate the direct assignments of frame values 
    from the element dictionary. '''
    eci_db['eci_1']['eci_type'] = cb_Select_CB1.get()
    eci_db['eci_2']['eci_type'] = cb_Select_CB2.get()
    eci_db['eci_3']['eci_type'] = cb_Select_CB3.get()
    print("eci_db['eci_1']['eci'] is ", eci_db['eci_1']['eci'])
    print("eci_db['eci_2']['eci'] is ", eci_db['eci_2']['eci'])
    print("eci_db['eci_3']['eci'] is ", eci_db['eci_3']['eci'])

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
    if eci_db['eci_3']['eci_type'] == 'elements':
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
                    eci_2_M_qty = eci_1_valence #This is correct. Cross assign valences to quantities
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
                    ''' Need to set cb_eci_4 selected item to eci_4'''
                    cb_eci_4.set(eci_4)
                    e_eci_4_M_qty.delete(0, END)
                    e_eci_4_M_qty.insert(0, 1)
                    print("eci_4 is ", eci_4)
                    print("e_eci_1_M_qty is ", e_eci_1_M_qty.get())
                    print("e_eci_2_M_qty is ", e_eci_2_M_qty.get())
                elif eci_1_electronegativity > eci_2_electronegativity:
                    print("In Oxidation_Rate_Elements eci_2 group 7A -- eci_1_electronegativity > eci_2_electronegativity")
            elif eci_2_group == "6A":   # Will need to exclude Oxygen for some compounds
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
                        print("eci_1 is", eci_1, "eci_2_valence is", eci_2_valence, "eci_2 is", eci_2 )
                        eci_4 = eci_1 + str(abs(eci_2_valence)) + eci_2
                        e_eci_1_M_qty.delete(0)
                        e_eci_1_M_qty.insert(0, eci_1_M_qty)
                        eci_2_M_qty = eci_1_valence #This is correct. Cross assign valences to quantities
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
                        #eci_4 = eci_1 + eci_2 + eci_1_valence
                        e_eci_1_M_qty.delete(0)
                        e_eci_1_M_qty.insert(0, eci_1_M_qty)
                        eci_2_M_qty = eci_1_valence #This is correct. Cross assign valences to quantities
                        e_eci_2_M_qty.delete(0, END)
                        e_eci_2_M_qty.insert(0, eci_2_M_qty)
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
                    #eci_1_M_qty = 1

            elif not eci_2_group == "6A"and not eci_2_group == "7A":
                print("In Oxidation_Rate_Elements not eci_2_group == 6A or 7A.")
            elif eci_1_electronegativity > eci_1_electronegativity:
                pass
    elif not eci_1_valence.isnumeric():   # if eci_1_valence is a string of valence values
        print("In Oxidation_Rate_Elements not eci_1_valence.isnumeri.")
    else: e_Explanation.insert(tk.END, "In Oxidation_Rate process else clause\n")

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
    Option 1. The user will select a product and the progrtam will determine the reactants
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
    When a pirmary product has been selected, start the synthesis process by calculating the
    ozidation status, then

    '''
    e_Explanation.insert(tk.END, "Synthesis process entered\n")
    print("Synthesis process entered")
    CountElements()
    AlphabetizeElements()
    Oxidation_Rate()
    ''' Consider starting with a compound formula or name.'''

    cb_1_type = cb_Select_CB1.get()   # Get the selected type of: element, compound, or ion
    cb_2_type = cb_Select_CB2.get()
    cb_3_type = cb_Select_CB3.get()
    #if cb_3_type == 'elements':
    #    cb_3_type = cb_Select_CB3.get()

    print("cb_1_type is", cb_1_type, "cb_2_type is", cb_2_type)
    #cb_3_type = cb_Select_CB3.get()
    #e_Explanation.insert(tk.END, "cb_1_type = cb_Select_CB1.get() step\n")
    #print('eci_1_type = ', cb_1_type)
    eci_1 = cb_eci_1.get()
    eci_2 = cb_eci_2.get()
    #if cb_1_type == 'elements':
    #    eci_1_valence = db[eci_1]['valence']
    #    eci_2_valence = db[eci_2]['valence']
    #    print("eci_1 is", eci_1, "eci_2 is", eci_2)
    #eci_3 = cb_eci_3.get()
     # and eci_1 != ''
    #eci_1_valence = db[eci_1]['valence']
    #eci_3_group = db[eci_3]['_group']
    '''
    Cut out code that determines oxidation rate for elements.
    '''
    if cb_1_type == 'compounds':
        eci_1 = cb_eci_1.get()
        print('eci_1 is ', eci_1)
        eci_1_name = c_db[eci_1]['name']
        #eci_1_name = c_db[eci_1]['name']
        print('eci_1_name is ', eci_1_name)
        #e_Explanation.insert(tk.END, "In Synthesis, compounds.\n")

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
    e_Explanation.insert(tk.END, "setClassItem process entered\n")
    #print("setClassItem process entered")
    eci_1 = cb_eci_1.get()
    #print('eci_1 is', eci_1)
    #*** The following works!
    if cb_1_type == 'elements':
        eci_temp_1_qty = db[eci_1]['mass']
        eci_1_name = db[eci_1]['name']
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
    #print("eci_1_name is ", eci_1_name)
    if cb_1_type == 'elements':
        try:
            if not eci_1_name == db[eci_1]['name']:
                cb_eci_1_N.set(db[eci_1]['name'])
        except KeyError:
            cb_eci_1_N.set("not a valid key")
    elif cb_1_type == 'compounds':
        try:
            if not eci_1_name == c_db[eci_1]['name']:
                cb_eci_1_N.set(c_db[eci_1]['name'])
        except KeyError:
            cb_eci_1_N.set("not a valid key")
    elif cb_1_type == 'ions':
        try:
            if not eci_1_name == i_db[eci_1]['name']:
                cb_eci_1_N.set(i_db[eci_1]['name'])
        except KeyError:
            cb_eci_1_N.set("not a valid key")
    if cb_2_type == 'elements':
        try:
            if not eci_2_name == db[eci_2]['name']:
                cb_eci_2_N.set(db[eci_2]['name'])
        except KeyError:
            cb_eci_2_N.set("not a valid key")
    elif cb_2_type == 'compounds':
        try:
            if not eci_2_name == c_db[eci_2]['name']:
                cb_eci_2_N.set(c_db[eci_2]['name'])
        except KeyError:
            cb_eci_2_N.set("not a valid key")
    elif cb_2_type == 'ions':
        try:
            if not eci_2_name == i_db[eci_2]['name']:
                cb_eci_2_N.set(i_db[eci_2]['name'])
        except KeyError:
            cb_eci_2_N.set("not a valid key")
    if cb_3_type == 'elements':
        try:
            if not eci_3_name == db[eci_3]['name']:
                cb_eci_3_N.set(db[eci_3]['name'])
        except KeyError:
            cb_eci_3_N.set("not a valid key")
    elif cb_3_type == 'compounds':
        try:
            if not eci_3_name == c_db[eci_3]['name']:
                cb_eci_3_N.set(c_db[eci_3]['name'])
        except KeyError:
            cb_eci_3_N.set("not a valid key")
    elif cb_3_type == 'ions':
        try:
            if not eci_3_name == i_db[eci_3]['name']:
                cb_eci_3_N.set(i_db[eci_3]['name'])
        except KeyError:
            cb_eci_3_N.set("not a valid key")
    if cb_4_type == 'elements':
        try:
            if not eci_4_name == db[eci_4]['name']:
                cb_eci_4_N.set(db[eci_4]['name'])
        except KeyError:
            cb_eci_4_N.set("not a valid key")
    elif cb_4_type == 'compounds':
        try:
            if not eci_4_name == c_db[eci_4]['name']:
                cb_eci_4_N.set(c_db[eci_4]['name'])
        except KeyError:
            cb_eci_4_N.set("not a valid key")
    elif cb_4_type == 'ions':
        try:
            if not eci_4_name == i_db[eci_4]['name']:
                cb_eci_4_N.set(i_db[eci_4]['name'])
        except KeyError:
            cb_eci_4_N.set("not a valid key")
    if cb_5_type == 'elements':
        try:
            if not eci_5_name == db[eci_5]['name']:
                cb_eci_5_N.set(db[eci_5]['name'])
        except KeyError:
            cb_eci_5_N.set("not a valid key")
    elif cb_5_type == 'compounds':
        try:
            if not eci_5_name == c_db[eci_5]['name']:
                cb_eci_5_N.set(c_db[eci_5]['name'])
        except KeyError:
            cb_eci_5_N.set("not a valid key")
    elif cb_5_type == 'ions':
        try:
            if not eci_5_name == i_db[eci_5]['name']:
                cb_eci_5_N.set(i_db[eci_5]['name'])
        except KeyError:
            cb_eci_5_N.set("not a valid key")
    if cb_6_type == 'elements':
        try:
            if not eci_6_name == db[eci_6]['name']:
                cb_eci_6_N.set(db[eci_6]['name'])
        except KeyError:
            cb_eci_6_N.set("not a valid key")
    elif cb_6_type == 'compounds':
        try:
            if not eci_6_name == c_db[eci_6]['name']:
                cb_eci_6_N.set(c_db[eci_6]['name'])
        except KeyError:
            cb_eci_6_N.set("not a valid key")
    elif cb_6_type == 'ions':
        try:
            if not eci_6_name == i_db[eci_6]['name']:
                cb_eci_6_N.set(i_db[eci_6]['name'])
        except KeyError:
            cb_eci_6_N.set("not a valid key")
    else: pass #print('In else clause of setSelectedItemName.')

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
         if not eci_1 ==element_names_Dict[cb_eci_1_N.get()]:
            cb_eci_1.set(element_names_Dict[cb_eci_1_N.get()])
    elif cb_1_type == 'compounds':
        if not eci_1 ==compounds_names_dict[cb_eci_1_N.get()]:
            cb_eci_1.set(compounds_names_dict[cb_eci_1_N.get()])
        else: print('eci_1 is already correct and doesn\'t need to be reset')
    elif cb_1_type == 'ions':
        if not eci_1 ==ion_names_dict[cb_eci_1_N.get()]:
            cb_eci_1.set(ion_names_dict[cb_eci_1_N.get()])
    if cb_2_type == 'elements':
         if not eci_2 ==element_names_Dict[cb_eci_2_N.get()]:
            cb_eci_2.set(element_names_Dict[cb_eci_2_N.get()])
    elif cb_2_type == 'compounds':
        if not eci_2 ==compounds_names_dict[cb_eci_2_N.get()]:
            cb_eci_2.set(compounds_names_dict[cb_eci_2_N.get()])
    elif cb_2_type == 'ions':
        if not eci_2 ==ion_names_dict[cb_eci_2_N.get()]:
            cb_eci_2.set(ion_names_dict[cb_eci_2_N.get()])
    if cb_3_type == 'elements':
         if not eci_3 ==element_names_Dict[cb_eci_3_N.get()]:
            cb_eci_3.set(element_names_Dict[cb_eci_3_N.get()])
    elif cb_3_type == 'compounds':
        if not eci_3 ==compounds_names_dict[cb_eci_3_N.get()]:
            cb_eci_3.set(compounds_names_dict[cb_eci_3_N.get()])
    elif cb_3_type == 'ions':
        if not eci_3 ==ion_names_dict[cb_eci_3_N.get()]:
            cb_eci_3.set(ion_names_dict[cb_eci_3_N.get()])
    if cb_4_type == 'elements':
         if not eci_4 ==element_names_Dict[cb_eci_4_N.get()]:
            cb_eci_4.set(element_names_Dict[cb_eci_4_N.get()])
    elif cb_4_type == 'compounds':
        if not eci_4 ==compounds_names_dict[cb_eci_4_N.get()]:
            cb_eci_4.set(compounds_names_dict[cb_eci_4_N.get()])
    elif cb_4_type == 'ions':
        if not eci_4 ==ion_names_dict[cb_eci_4_N.get()]:
            cb_eci_4.set(ion_names_dict[cb_eci_4_N.get()])
    if cb_5_type == 'elements':
         if not eci_5 ==element_names_Dict[cb_eci_5_N.get()]:
            cb_eci_5.set(element_names_Dict[cb_eci_5_N.get()])
    elif cb_5_type == 'compounds':
        if not eci_5 ==compounds_names_dict[cb_eci_5_N.get()]:
            cb_eci_5.set(compounds_names_dict[cb_eci_5_N.get()])
    elif cb_5_type == 'ions':
        if not eci_5 ==ion_names_dict[cb_eci_5_N.get()]:
            cb_eci_5.set(ion_names_dict[cb_eci_5_N.get()])
    if cb_6_type == 'elements':
         if not eci_6 ==element_names_Dict[cb_eci_6_N.get()]:
            cb_eci_6.set(element_names_Dict[cb_eci_6_N.get()])
    elif cb_6_type == 'compounds':
        if not eci_6 ==compounds_names_dict[cb_eci_6_N.get()]:
            cb_eci_6.set(compounds_names_dict[cb_eci_6_N.get()])
    elif cb_6_type == 'ions':
        if not eci_6 ==ion_names_dict[cb_eci_6_N.get()]:
            cb_eci_6.set(ion_names_dict[cb_eci_6_N.get()])

def eci_units_selected(*arg):
    ''' If gas units are selected, the user needs to fill in temperature and pressure
    units and amounts. This procedure sets default values.
    The user can reset the displayed units and quantities, but they will be converted into
    the units and quantities actually used to calculate quantities used by the program.  '''
    print("In process eci_units_selected")
    print("cb_eci_1_units.get() is ", cb_eci_1_units.get())
    eci_1_units = cb_eci_1_units.get()
    eci_2_units = cb_eci_2_units.get()
    eci_3_units = cb_eci_3_units.get()
    eci_4_units = cb_eci_4_units.get()
    eci_5_units = cb_eci_5_units.get()
    eci_6_units = cb_eci_6_units.get()
    eci_db['eci_1']['display_units'] = cb_eci_1_units.get()
    eci_db['eci_2']['display_units'] = cb_eci_2_units.get()
    eci_db['eci_3']['display_units'] = cb_eci_3_units.get()
    eci_db['eci_4']['display_units'] = cb_eci_4_units.get()
    eci_db['eci_5']['display_units'] = cb_eci_5_units.get()
    eci_db['eci_6']['display_units'] = cb_eci_6_units.get()
    if eci_1_units == 'liters(g)' or eci_1_units == 'ml(g)':
        if cb_1_Temp_Units.get() == "":
            eci_1_temp_units = cb_1_Temp_Units.set('C')
            e_Temp_Qty_1.delete(0, 'end')
            e_Temp_Qty_1.insert(0, '25')
        if cb_1_Press_Units.get() == "":
            eci_1_press_units = cb_1_Press_Units.set('torr')
            e_Press_Qty_1.delete(0, 'end')
            e_Press_Qty_1.insert(0, '760')
        #print('cb_eci_1_units are ', eci_1_units)
    #elif not eci_1_units == 'liters(g)' and not eci_1_units == 'ml(g)':
    #     print('cb_eci_1_units are ', eci_1_units)
    if eci_2_units == 'liters(g)' or eci_2_units == 'ml(g)':
        if cb_2_Temp_Units.get() == "":
            eci_2_temp_units = cb_2_Temp_Units.set('C')
            e_Temp_Qty_2.delete(0, 'end')
            e_Temp_Qty_2.insert(0, '25')
        if cb_2_Press_Units.get() == "":
            eci_2_press_units = cb_2_Press_Units.set('torr')
            e_Press_Qty_2.delete(0, 'end')
            e_Press_Qty_2.insert(0, '760')
    if eci_3_units == 'liters(g)' or eci_3_units == 'ml(g)':
        if cb_3_Temp_Units.get() == "":
            eci_3_temp_units = cb_3_Temp_Units.set('C')
            e_Temp_Qty_3.delete(0, 'end')
            e_Temp_Qty_3.insert(0, '25')
        if cb_3_Press_Units.get() == "":
            eci_3_press_units = cb_3_Press_Units.set('torr')
            e_Press_Qty_3.delete(0, 'end')
            e_Press_Qty_3.insert(0, '760')
    if eci_4_units == 'liters(g)' or eci_4_units == 'ml(g)':
        if cb_4_Temp_Units.get() == "":
            eci_4_temp_units = cb_4_Temp_Units.set('C')
            e_Temp_Qty_4.delete(0, 'end')
            e_Temp_Qty_4.insert(0, '25')
        if cb_4_Press_Units.get() == "":
            eci_4_press_units = cb_4_Press_Units.set('torr')
            e_Press_Qty_4.delete(0, 'end')
            e_Press_Qty_4.insert(0, '760')
    if eci_5_units == 'liters(g)' or eci_5_units == 'ml(g)':
        if cb_5_Temp_Units.get() == "":
            eci_5_temp_units = cb_5_Temp_Units.set('C')
            e_Temp_Qty_5.delete(0, 'end')
            e_Temp_Qty_5.insert(0, '25')
        if cb_4_Press_Units.get() == "":
            eci_5_press_units = cb_5_Press_Units.set('torr')
            e_Press_Qty_5.delete(0, 'end')
            e_Press_Qty_5.insert(0, '760')
    if eci_6_units == 'liters(g)' or eci_6_units == 'ml(g)':
        if cb_6_Temp_Units.get() == "":
            eci_6_temp_units = cb_6_Temp_Units.set('C')
            e_Temp_Qty_6.delete(0, 'end')
            e_Temp_Qty_6.insert(0, '25')
        if cb_6_Press_Units.get() == "":
            eci_6_press_units = cb_6_Press_Units.set('torr')
            e_Press_Qty_6.delete(0, 'end')
            e_Press_Qty_6.insert(0, '760')
        #print("eci_db['eci_1']['display_units'] are ", eci_db['eci_1']['display_units'])

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
    eci_db['eci_1']['display_temp_units'] = cb_1_Temp_Units.get()
    eci_db['eci_2']['display_temp_units'] = cb_2_Temp_Units.get()
    eci_db['eci_3']['display_temp_units'] = cb_3_Temp_Units.get()
    eci_db['eci_4']['display_temp_units'] = cb_4_Temp_Units.get()
    eci_db['eci_5']['display_temp_units'] = cb_5_Temp_Units.get()
    eci_db['eci_6']['display_temp_units'] = cb_6_Temp_Units.get()

def callback_set_press_units(eventObject):
    ''' Whenever a temperature units combo box is selected, update the eci_db variable. '''
    eci_1_press_units = cb_1_Press_Units.get()
    eci_2_press_units = cb_2_Press_Units.get()
    eci_3_press_units = cb_3_Press_Units.get()
    eci_4_press_units = cb_4_Press_Units.get()
    eci_5_press_units = cb_5_Press_Units.get()
    eci_6_press_units = cb_6_Press_Units.get()
    eci_db['eci_1']['display_press_units'] = cb_1_Press_Units.get()
    eci_db['eci_2']['display_press_units'] = cb_2_Press_Units.get()
    eci_db['eci_3']['display_press_units'] = cb_3_Press_Units.get()
    eci_db['eci_4']['display_press_units'] = cb_4_Press_Units.get()
    eci_db['eci_5']['display_press_units'] = cb_5_Press_Units.get()
    eci_db['eci_6']['display_press_units'] = cb_6_Press_Units.get()

'''
def callback_eci_1(eventObject):
    eci_1 = cb_eci_1.get()
    print(eci_1)
'''
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

def Parse_Compounds(): #'He2SO4'
    ''' I need to parse for number, uppercase, and lowercase. Leading number always applies to an element or formula,
    later numbers are assumed to apply to the preceeding element.
    '''
    eci_1 = cb_eci_1.get()
    compound = cb_eci_1.get()
    #compound = 'H2O'    #'He2SO4'
    e_Explanation.insert(tk.END, "Parse_Compounds process entered\n")
    if compound == "":
        pass
    else: print("Parse_Compounds process entered", compound)
    compound_formula_qty = 1
    element_1 = ''
    current_element = ""
    current_element_multiplier = 1
    #e_Explanation.
    print('Parse_Compounds compound is ', compound)
    ''' Start with a normal compound which does not start with an integer.'''
     # For example: compound = 'Na2SO4'
    if compound == "":
        pass
    elif compound[0].isdigit():
        ''' If the leading character is a number, apply it to the whole formuls. '''
        compound_formula_qty =  compound[0]
        ''' Reset the compound to the string after the intial digit. '''
        compound = compound[1:]
        print('Parse_Compounds compound first character is integer ', compound[0] )
        ''' The first character is not a number. '''
    elif not compound[0].isdigit():
        print('Pass to Parse_Compound_ECI_1')
        Parse_Get_Compound()
        #Parse_Compound_ECI_1()
    else:  Parse_Compound_Method()
    #print(' If the leading character is a number, '
    #      'need to add it to the result of Parse_Compounds_1(compound).')

def Parse_Get_Compound():
    ''' Get a compound from eci_1. Call a function to parse.. '''
    print('In Parse_Get_Compound():')
    compound = ""
    compound = eci_1.get()
    print('Finish Parse_Get_Compound(): compound = ', compound)
    Parse_Compound(compound)

def Parse_Compound(compound):
    ''' Got a compound from eci_1. Parse it. '''
    print('In Parse_Compound(compound): compound = ', compound)
    len_compound = len(compound)
    current_compound =[]
    #print('len_compound is ', len_compound)
    while len(compound) >= 3:
        #print('len(compound) is ', len_compound)
        if compound[0].isupper() and compound[1].islower() and compound[2].isdigit(): # and compound[3].isupper():
            print('In compound[0].isupper() and compound[1].islower() and compound[2].isdigit()') # Re,removed  and compound[3].isupper()
            current_element_multiplier = 1
            current_element = compound[:2]
            current_element_multiplier = compound[2:3]
            current_compound.append(current_element)
            current_compound.append(current_element_multiplier)
            compound = compound[3:]
            print('elif compound[0].isupper() and compound[1].isdigit() and compound[2].isupper(): compound = ', compound)
            print('current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
            print('current_compound is ', current_compound)
        elif compound[0].isupper() and compound[1].islower() and compound[2].isdigit(): #   and compound[3].isdigit()
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
            print('elif compound[0].isupper() and compound[1].islower() and compound[2].isupper(): compound = ', compound)
            print('current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
            print('current_compound, and length are ', current_compound, len_compound)
        elif compound[0].isupper() and compound[1].isdigit() and compound[2].isupper():
            print('In compound[0].isupper() and compound[1].isdigit() and compound[2].isupper()')
            current_element_multiplier = 1
            current_element = compound[:1]
            current_element_multiplier = compound[1:2]
            current_compound.append(current_element)
            current_compound.append(current_element_multiplier)
            compound = compound[2:]
            print('elif compound[0].isupper() and compound[1].isdigit() and compound[2].isupper(): compound = ', compound)
            print('current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
            print('current_compound is ', current_compound)
        elif compound[0].isupper() and compound[1].isdigit() and compound[2].isdigit():
            print('In compound[0].isupper() and compound[1].isdigit() and compound[2].isdigit()')
            current_element_multiplier = 1
            current_element = compound[:1]
            current_element_multiplier = compound[1:3]
            current_compound.append(current_element)
            current_compound.append(current_element_multiplier)
            if len(compound) > 2:
                compound = compound[3:]
            else: compound = ""
            print('elif compound[0].isupper() and compound[1].isdigit() and compound[2].isupper(): compound = ', compound)
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
                    print('current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
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
                    print('current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
                    print('current_compound is ', current_compound)
                elif compound[0].isupper() and compound[1].islower():
                    print('In compound[0].isupper() and compound[1].islower()')
                    current_element_multiplier = 1
                    current_element = compound[0:1]
                    current_compound.append(current_element)
                    current_compound.append(current_element_multiplier)
                    compound = ""
                    print('In if compound[0].isupper() and compound[1].islower():: compound = ', compound)
                    print('current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
                    print('current_compound is ', current_compound)
                elif compound[0].isupper() and compound[1].isdigit():
                    print('In compound[0].isupper() and compound[1].isdigit()')
                    current_element_multiplier = 1
                    current_element = compound[0]
                    current_element_multiplier = compound[1]
                    current_compound.append(current_element)
                    current_compound.append(current_element_multiplier)
                    compound = ""
                    print('In if compound[0].isupper() and compound[1].islower():: compound = ', compound)
                    print('current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
                    print('current_compound is ', current_compound)
        print('compound =  ', compound)
        compound = ""
        Display_Parsed_Compound(current_compound)

def Display_Parsed_Compound(parsed_compound):
    print('Entering Display_Parsed_Compound')
    print(parsed_compound)
    e_eci_1_M_qty.delete(0, END)
    e_eci_1_M_qty.insert(0,1)

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

    if parsed_compound[3]:
        cb_Select_CB6.set('elements')
        element_3 = parsed_compound[4]
        print('element_3 is ', element_3)
        cb_eci_6.set("")
        cb_eci_6_N.set("")
        cb_eci_6.set(element_3)
        moles_3 = parsed_compound[5]
        e_eci_6_M_qty.delete(0, END)
        e_eci_6_M_qty.insert(0, moles_3)
    if parsed_compound[4]:
        cb_Select_CB3.set('elements')
        element_4 = parsed_compound[6]
        print('element_4 is ', element_4)
        cb_eci_3.set("")
        cb_eci_3_N.set("")
        cb_eci_3.set(element_4)
        moles_4 = parsed_compound[7]
        e_eci_3_M_qty.delete(0, END)
        e_eci_3_M_qty.insert(0, moles_4)

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


def CountElements():    # The following does not work. Need valid test for value
    e_Explanation.insert(tk.END, "CountElements process entered\n")
    intElementCount = 0
    eci_1 = cb_eci_1.get()
    eci_2 = cb_eci_2.get()
    eci_3 = cb_eci_3.get()
    if eci_1 == "" :     #cb_eci_1
        pass
    else: intElementCount = 1
    if eci_2 == "" :
        pass
    else: intElementCount = intElementCount + 1
    if eci_3 == "" :
        pass
    else: intElementCount = intElementCount + 1
    print('element count is', intElementCount)
    #rtb_Explanation.Text = rtb_Explanation.Text & intElementCount
    
def AlphabetizeElements():   #TypeError: '<' not supported between instances of 'StringVar' and 'StringVar'
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
    else: e_Explanation.insert(tk.END, 'Error:Fell to else clause in AlphabetizeElements\n')
    #e_Explanation.insert(tk.END, 'strAlphaElements is %', strAlphaElements) #How do I insert arguments?
    print('strAlphaElements is ', strAlphaElements)

# Make new dictionaries of elements, compounds and ions to ensure they are current.
# Also, if the data is changed in a dictionary, it needs to be changed in the database.
# Current, data will be changed in a dictionary and then changed in the database.
# Make new alpha lists of compounds and ions to ensure they are current.
# An alpha dictionary/list is a list of compound (or ion) elements in alphabetic order and a list of the compounds or ions 
# that have the same list of elements. After a set of elements have been chosen and alphabetized, these lists will be used
#  to determine which compounds have these elements, and that list will be used to fill the appropriate combo box
def make_element_dictionary():
    print("In make_element_dictionary")
def make_compound_dictionary():
    pass    
def make_ion_dictionary():
    pass
def make_compound_alpha_list():
    pass
def make_ion_alpha_list():
    pass
    #a_list = [eci_1, eci_2, eci_3]
    #alpha = (sorted(a_list)) #Does not concatenate
    #beta = alpha(0) + alpha(1) + alpha(2)
    #print('In AlphabetizeElements', alpha)
    #print('In AlphabetizeElements', sorted(alpha))
''' *** Learn to sent text and variables to the explanation textbox. *** '''
    #rtb_Explanation.Text = rtb_Explanation.Text & strAlphaElement

''' *** End function descriptions. *** '''

''' *** Start GUI layout. *** '''
lbl_Title = Label(root, text="Chemistry")
lbl_Title.grid(row=0, column=3)
lbl_Title.config(font=titlefont)

lbl_blank = Label(root, text="")
lbl_blank.grid(row=1, column=0) #, columnspan=1)
lbl_blank.config(font=labelfont)

lbl_record_create = Label(text="Create record:")
lbl_record_create.grid(row=2, column=0)
lbl_record_create.config(font=labelfont)
e_recordname = Entry(root, text="")  #, width=14)
e_recordname.grid(row=2, column=1, columnspan=2)
e_recordname.config(font=labelfont)
btn_create_record = Button(root, text = 'Create Record', command=create_record)
btn_create_record.grid(row=2, column=3)
btn_create_record.config(font=buttonfont)
btn_create_record.bind("<<ComboboxSelected>>", create_record())
btn_update_record = Button(root, text = 'Update Record', command=update_record)
btn_update_record.grid(row=2, column=4)
btn_update_record.config(font=buttonfont)
btn_update_record.bind("<<ComboboxSelected>>", update_record)
btn_Continue = Button(root, text = '* Continue *', command=Continue)   #, command=callback_print_vars)
btn_Continue.grid(row=2, column=5)
btn_Continue.config(font=titlefont) # Continue()
#btn_Continue.bind("<<ComboboxSelected>>", Continue())

lbl_record_ops = Label(text="Get record:")
lbl_record_ops.grid(row=3, column=0)   #, columnspan=1)
lbl_record_ops.config(font=labelfont)
cb_RecordName: Combobox = Combobox(root, values="", width=12)
cb_RecordName.grid(row=3, column=1)  #, columnspan=2)
cb_RecordName.config(font=entryfont)
cb_RecordName.bind("<<ComboboxSelected>>", retrieve_record)
#e_recordname = Entry(root, text="")   #, width=30)
#e_recordname.grid(row=3, column=3)
#e_recordname.config(font=labelfont)
btn_create_record = Button(root, text = 'Get Record', command=get_record)
btn_create_record.grid(row=3, column=2)
btn_create_record.config(font=buttonfont)
btn_create_record.bind("<<ComboboxSelected>>", retrieve_record)
btn_create_record = Button(root, text = 'Previous Record', command=get_record)
btn_create_record.grid(row=3, column=3)
btn_create_record.config(font=buttonfont)
btn_create_record.bind("<<ComboboxSelected>>", previous_record)
btn_create_record = Button(root, text = 'Next Record', command=get_record)
btn_create_record.grid(row=3, column=4)
btn_create_record.config(font=buttonfont)
btn_create_record.bind("<<ComboboxSelected>>", next_record)

lbl_LU_Compound = Label(text="   Look up compound:")
lbl_LU_Compound.grid(row=6, column=0)   #, columnspan=1)
lbl_LU_Compound.config(font=labelfont)
cb_LU_Compound = Combobox(root, values=compound_symbols_list, width=12)
cb_LU_Compound.grid(row=6, column=1)  #, columnspan=1)
cb_LU_Compound.config(font=entryfont)

# Create a search for and retrieve a compount
lbl_LU_Process = Label(text="   Look up process:")
lbl_LU_Process.grid(row=6, column=2)  #, columnspan=1)
lbl_LU_Process.config(font=labelfont)
cb_LU_Process = Combobox(root, values=process_list, width=12)   #, width=30)
cb_LU_Process.grid(row=6, column=3)   #, columnspan=2)
cb_LU_Process.config(font=entryfont)
# Create a search for and retrieve a process
lbl_LU_Environment = Label(text="   Look up environment:", width=22)
lbl_LU_Environment.grid(row=6, column=4)
lbl_LU_Environment.config(font=labelfont)
cb_LU_Environment = Combobox(root, values=environment, width=12)   #, width=30)
cb_LU_Environment.grid(row=6, column=5)   #, columnspan=2)
cb_LU_Environment.config(font=entryfont)
# Create a search for and retrieve a environment

lbl_Select_Process = Label(text="Select process", width=12)
lbl_Select_Process.grid(row=7, column=2)   #, columnspan=2)
lbl_Select_Process.config(font=titlefont)
cb_Select_Process: Combobox = Combobox(root, values=process_list, textvariable=process_selected, width=12)   #, width=30)
cb_Select_Process.grid(row=7, column=3)   #, columnspan=2)
cb_Select_Process.config(font=entryfont)
cb_Select_Process.bind("<<ComboboxSelected>>", process_selected)
lbl_Select_Environment = Label(text="   Select environment:", width=22)
lbl_Select_Environment.grid(row=7, column=4)
lbl_Select_Environment.config(font=titlefont)
cb_Select_Environment: Combobox = Combobox(root, values=environment, width=12)   #, width=30)
cb_Select_Environment.grid(row=7, column=5)   #, columnspan=2)
cb_Select_Environment.config(font=entryfont)

lbl_blank = Label(root, text="")
lbl_blank.grid(row=8, column=0) #, columnspan=2)
lbl_blank.config(font=labelfont)

lbl_eci_1 = Label(root, text="   Select Element, Compound or Ion for ComboBox 1")
lbl_eci_1.grid(row=9, column=0, columnspan=3, sticky=W)
lbl_eci_1.config(font=labelfont)
cb_Select_CB1: Combobox = Combobox(root, values=eci_cb_values, width=10)
cb_Select_CB1.grid(row=9, column=3, sticky=W)
cb_Select_CB1.config(font=entryfont)
cb_Select_CB1.bind("<<ComboboxSelected>>", select_eci_1_type) #select_eci_1_type
#cb_Select_CB1.bind("<<ComboboxSelected>>", callback1)
#cb_Process = Combobox(root, values=process_list, width=20)
#cb_Process.grid(row=9, column=3) # , columnspan=2
#cb_Process.config(font=entryfont)
lbl_eci_4 = Label(root, text="Select Element, Compound or Ion for ComboBox 4")   #Element, Compound or Ion number 4
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
lbl_eci_4_qty.grid(row=11, column=4)   #, , sticky=W  padx=4)
lbl_eci_4_qty.config(font=labelfont)
lbl_eci_4_units = Label(root, text="Units 4", width=10)
lbl_eci_4_units.grid(row=11, column=5, sticky=W)   #, padx=4)
lbl_eci_4_units.config(font=labelfont)
lbl_eci_4 = Label(root, text="ECI 4", width=10)
lbl_eci_4.grid(row=11, column=6, sticky=W)   #, padx=4)
lbl_eci_4.config(font=labelfont)
lbl_eci_4_valence = Label(root, text="Valence 4", width=10)
lbl_eci_4_valence.grid(row=11, column=7, sticky=W)
lbl_eci_4_valence.config(font=labelfont)

e_eci_1_qty = Entry(root, text="", textvariable=eci_1_qty, width=8)
e_eci_1_qty.grid(row=12, column=0)
e_eci_1_qty.config(font=entryfont)
e_eci_1_qty.bind('<FocusOut>', (lambda event: check_entry_changes())) #'''  does not work'''
cb_eci_1_units: Combobox = Combobox(root, values=unit_values, textvariable=eci_1_units, width=10)
cb_eci_1_units.grid(row=12, column=1)   #, padx=4)
cb_eci_1_units.config(font=entryfont)
cb_eci_1_units.bind("<<ComboboxSelected>>", eci_units_selected)
cb_eci_1: Combobox = Combobox(root, textvariable=eci_1, width=12) #, command=setClassItem
cb_eci_1.grid(row=12, column=2)   #, padx=4)
cb_eci_1.config(font=labelfont)
cb_eci_1['values'] = elements_symbols_list
cb_eci_1.bind("<<ComboboxSelected>>", setSelectedItemName)

cb_eci_1_valence: Combobox = Combobox(root, textvariable=eci_1_valence, width=8)
cb_eci_1_valence.grid(row=12, column=3)   #, padx=4)
cb_eci_1_valence.config(font=entryfont)
cb_eci_1_valence['values'] = valences
e_eci_4_qty = Entry(root, text="", textvariable=eci_4_qty, width=8)
e_eci_4_qty.grid(row=12, column=4)   #, padx=4)
e_eci_4_qty.config(font=entryfont)
cb_eci_4_units: Combobox = Combobox(root, values=unit_values, textvariable=eci_4_units, width=10)
cb_eci_4_units.grid(row=12, column=5)   #, padx=4)
cb_eci_4_units.config(font=entryfont)
cb_eci_4_units.bind("<<ComboboxSelected>>", eci_units_selected)
#cb_eci_4_units.bind("<<ComboboxSelected>>", callback_eci_4_units)
cb_eci_4: Combobox = Combobox(root, textvariable=eci_4, width=12)   # , values=compound_values
cb_eci_4.grid(row=12, column=6)   #, padx=4)
cb_eci_4.config(font=entryfont)
cb_eci_4['values'] = compound_symbols_list
cb_eci_4.bind("<<ComboboxSelected>>", setSelectedItemName)
cb_eci_4_valence: Combobox = Combobox(root, textvariable=eci_4_valence, width=5)
cb_eci_4_valence.grid(row=12, column=7)   #, padx=4)
cb_eci_4_valence.config(font=entryfont)
cb_eci_4_valence['values'] = valences

e_eci_1_M_qty = Entry(root, text="", textvariable=eci_1_M_qty, width=8)
e_eci_1_M_qty.grid(row=13, column=0)   #, padx=4)
e_eci_1_M_qty.config(font=entryfont)
lbl_eci_1_units_M = Label(root, text="Moles", width=12)
lbl_eci_1_units_M.grid(row=13, column=1)   #, padx=4)
lbl_eci_1_units_M.config(font=labelfont)
# cb_Elements1 = Combobox(root, values=elements, width=30)
cb_eci_1_N: Combobox = Combobox(root,  textvariable=eci_1_name, width=12)
cb_eci_1_N.grid(row=13, column=2)   #, padx=4)
cb_eci_1_N.config(font=entryfont)
cb_eci_1_N['values'] = compound_names_list
cb_eci_1_N.bind("<<ComboboxSelected>>", setSelectedItemFormula)

e_eci_4_M_qty = Entry(root, text="", textvariable=eci_4_M_qty, width=8)
e_eci_4_M_qty.grid(row=13, column=4)   #, padx=4)
e_eci_4_M_qty.config(font=entryfont)
lbl_eci_4_units_M = Label(root, text="Moles", width=10)
lbl_eci_4_units_M.grid(row=13, column=5)   #, padx=4)
lbl_eci_4_units_M.config(font=labelfont)
cb_eci_4_N: Combobox = Combobox(root, values=compound_symbols_list, textvariable=eci_4_name, width=12)
cb_eci_4_N.grid(row=13, column=6)   #, padx=4)
cb_eci_4_N.config(font=entryfont)
cb_eci_4_N.bind("<<ComboboxSelected>>", setSelectedItemFormula)

lbl_Temp_Units_1 = Label(root, text="Temp Units", width=10)
lbl_Temp_Units_1.grid(row=14, column=0)
lbl_Temp_Units_1.config(font=labelfont)
lbl_Temp_Qty_1 = Label(root, text="Temp Qty", width=10)
lbl_Temp_Qty_1.grid(row=14, column=1)   #, sticky=W
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

cb_1_Temp_Units: Combobox = Combobox(root, values=temp_umits, textvariable=eci_1_temp_units, width=10) # eci_temp_1_units
cb_1_Temp_Units.grid(row=15, column=0)   #, padx=4) eci_temp_1_units
cb_1_Temp_Units.config(font=entryfont)
cb_1_Temp_Units.bind("<<ComboboxSelected>>", callback_set_temp_units)
e_Temp_Qty_1 = Entry(root, text="", textvariable=eci_temp_1_qty, width=8)   #, width=12)
e_Temp_Qty_1.grid(row=15, column=1)   #, padx=4)
e_Temp_Qty_1.config(font=entryfont)
cb_1_Press_Units: Combobox = Combobox(root, values=press_umits, textvariable=eci_1_press_units, width=10)   #, width=12)
cb_1_Press_Units.grid(row=15, column=2)  #, padx=4)
cb_1_Press_Units.config(font=entryfont)
cb_1_Press_Units.bind("<<ComboboxSelected>>", callback_set_press_units)
e_Press_Qty_1 = Entry(root, text="", textvariable=eci_press_1_qty, width=8)   #, width=12)
e_Press_Qty_1.grid(row=15, column=3)   #, padx=4)
e_Press_Qty_1.config(font=entryfont)
cb_4_Temp_Units: Combobox = Combobox(root, values=temp_umits, textvariable=eci_4_temp_units, width=10)
cb_4_Temp_Units.grid(row=15, column=4)   #, padx=4)
cb_4_Temp_Units.config(font=entryfont)
cb_4_Temp_Units.bind("<<ComboboxSelected>>", callback_set_temp_units)
e_Temp_Qty_4 = Entry(root, text="", textvariable=eci_temp_4_qty, width=8)   #, width=12)
e_Temp_Qty_4.grid(row=15, column=5, sticky=W)  #, padx=4)
e_Temp_Qty_4.config(font=entryfont)
cb_4_Press_Units: Combobox = Combobox(root, values=press_umits, textvariable=eci_4_press_units, width=10)   #, width=12)
cb_4_Press_Units.grid(row=15, column=6)   #, padx=4)
cb_4_Press_Units.config(font=entryfont)
cb_4_Press_Units.bind("<<ComboboxSelected>>", callback_set_press_units)
e_Press_Qty_4 = Entry(root, text="", textvariable=eci_press_4_qty, width=8)   #, width=12)
e_Press_Qty_4.grid(row=15, column=7)   #, padx=4)
e_Press_Qty_4.config(font=entryfont)

lbl_blank = Label(root, text="")
lbl_blank.grid(row=16, column=0)   #, columnspan=2)
lbl_blank.config(font=labelfont)

lbl_eci_2 = Label(root, text="   Select Element, Compound or Ion for ComboBox 2")
lbl_eci_2.grid(row=17, column=0, columnspan=3, sticky=W)
lbl_eci_2.config(font=labelfont)
cb_Select_CB2: Combobox = Combobox(root, values=eci_cb_values, width=10)
cb_Select_CB2.grid(row=17, column=3, sticky=W) # , columnspan=2
cb_Select_CB2.config(font=entryfont)
cb_Select_CB2.bind("<<ComboboxSelected>>", select_eci_2_type)
#btn_Select_CB2 = Button(root, command=Synthesis(variables), text = 'Elements')
#btn_Select_CB2.grid(row=17, column=2)
#btn_Select_CB2.config(font=buttonfont)
lbl_eci_5 = Label(root, text="Select Element, Compound or Ion for ComboBox 5")
lbl_eci_5.grid(row=17, column=4, columnspan=2, sticky=W)
lbl_eci_5.config(font=labelfont)
cb_Select_CB5: Combobox = Combobox(root, values=eci_cb_values, width=10)   #, width=20)
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
lbl_eci_5_qty.grid(row=19, column=4)   #, padx=4)
lbl_eci_5_qty.config(font=labelfont)
lbl_eci_5_units = Label(root, text="Units 5", width=10)
lbl_eci_5_units.grid(row=19, column=5)   #, padx=4)
lbl_eci_5_units.config(font=labelfont)
lbl_eci_5 = Label(root, text="ECI 5", width=10)
lbl_eci_5.grid(row=19, column=6)   #, padx=4)
lbl_eci_5.config(font=labelfont)
lbl_eci_5_valence = Label(root, text="Valence 5", width=10)
lbl_eci_5_valence.grid(row=19, column=7, sticky=W)
lbl_eci_5_valence.config(font=labelfont)

e_eci_2_qty = Entry(root, text="", textvariable=eci_2_qty, width=8)
e_eci_2_qty.grid(row=20, column=0)   #, padx=4)
e_eci_2_qty.config(font=entryfont)
# cb_Elements1.bind("<<ComboboxSelected>>", callback_E1)
cb_eci_2_units: Combobox = Combobox(root, values=unit_values, textvariable=eci_2_units, width=10)   #, width=8)
cb_eci_2_units.grid(row=20, column=1)   #, padx=4)
cb_eci_2_units.config(font=entryfont)
cb_eci_2_units.bind("<<ComboboxSelected>>", eci_units_selected)
cb_eci_2: Combobox = Combobox(root,  textvariable=eci_2, width=12)    #, values=elements, width=30)
cb_eci_2.grid(row=20, column=2)   #, padx=4)
cb_eci_2.config(font=entryfont)
cb_eci_2['values'] = elements_symbols_list
cb_eci_2.bind("<<ComboboxSelected>>", setSelectedItemName)
cb_eci_2_valence: Combobox = Combobox(root, textvariable=eci_2_valence, width=8)
cb_eci_2_valence.grid(row=20, column=3)   #, padx=4)
cb_eci_2_valence.config(font=entryfont)
cb_eci_2_valence['values'] = valences
e_eci_5_qty = Entry(root, text="", textvariable=eci_5_qty, width=8)
e_eci_5_qty.grid(row=20, column=4)    #, padx=4)
e_eci_5_qty.config(font=entryfont)
cb_eci_5_units: Combobox = Combobox(root, values=unit_values, textvariable=eci_5_units, width=10)
cb_eci_5_units.grid(row=20, column=5)   #, padx=4)
cb_eci_5_units.config(font=entryfont)
cb_eci_5_units.bind("<<ComboboxSelected>>", eci_units_selected)
cb_eci_5: Combobox = Combobox(root, values=compound_symbols_list, textvariable=eci_5, width=12)   #, width=30)
cb_eci_5.grid(row=20, column=6)   #, padx=4)
cb_eci_5.config(font=entryfont)
cb_eci_5.bind("<<ComboboxSelected>>", setSelectedItemName)
cb_eci_5_valence: Combobox = Combobox(root, textvariable=eci_5_valence, width=5)
cb_eci_5_valence.grid(row=20, column=7)   #, padx=4)
cb_eci_5_valence.config(font=entryfont)
cb_eci_5_valence['values'] = valences

'''    e_eci_2_M_qty.delete(0)
UnboundLocalError: local variable 'e_eci_2_M_qty' referenced before assignment
'''
#e_eci_2_M_qty = Entry(root, text="", textvariable=eci_2_M_qty, width=8)
#e_eci_1_M_qty.grid(row=13, column=0)   #, padx=4)
#e_eci_1_M_qty.config(font=entryfont)
e_eci_2_M_qty = Entry(root, text="", textvariable = eci_2_M_qty, width=8)
e_eci_2_M_qty.grid(row=21, column=0)   #, padx=4)
e_eci_2_M_qty.config(font=entryfont)
lbl_eci_2_units_M = Label(root, text="Moles", width=10)
lbl_eci_2_units_M.grid(row=21, column=1)   #, padx=4)
lbl_eci_2_units_M.config(font=labelfont)
cb_eci_2_N: Combobox = Combobox(root, values=elements_name_list,  textvariable=eci_2_name, width=12)   #, width=30)
cb_eci_2_N.grid(row=21, column=2)   #, padx=4)
cb_eci_2_N.config(font=entryfont)
cb_eci_2_N.bind("<<ComboboxSelected>>", setSelectedItemFormula)
e_eci_5_M_qty = Entry(root, text="CompoundQty 5", textvariable=eci_5_M_qty, width=8)   #, width=8)
e_eci_5_M_qty.grid(row=21, column=4)   #, padx=4)
e_eci_5_M_qty.config(font=entryfont)
lbl_eci_5_units_M = Label(root, text="Moles", width=10)
lbl_eci_5_units_M.grid(row=21, column=5)   #, padx=4)
lbl_eci_5_units_M.config(font=labelfont)
cb_eci_5_N: Combobox = Combobox(root, values=compound_names_list, textvariable=eci_5_name, width=12)   #, width=30)
cb_eci_5_N.grid(row=21, column=6)   #, padx=4)
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
lbl_Temp_Units_5 = Label(root, text="Temp Units", width=10) #, textvariable=eci_temp_5_units
lbl_Temp_Units_5.grid(row=22, column=4)
lbl_Temp_Units_5.config(font=labelfont)
lbl_Temp_Qty_5 = Label(root, text="Temp Qty", width=10) #, textvariable=eci_temp_5_qty
lbl_Temp_Qty_5.grid(row=22, column=5, sticky=W)
lbl_Temp_Qty_5.config(font=labelfont)
lbl_Press_Units_5 = Label(root, text="Press Units", width=10) #, textvariable=eci_press_5_units
lbl_Press_Units_5.grid(row=22, column=6)
lbl_Press_Units_5.config(font=labelfont)
lbl_Press_Qty_5 = Label(root, text="Press Qty", width=10) #, textvariable=eci_press_5_qty
lbl_Press_Qty_5.grid(row=22, column=7)
lbl_Press_Qty_5.config(font=labelfont)

cb_2_Temp_Units: Combobox = Combobox(root, values=temp_umits, textvariable=eci_2_temp_units, width=10)
cb_2_Temp_Units.grid(row=23, column=0)   #, padx=4)
cb_2_Temp_Units.config(font=entryfont)
cb_2_Temp_Units.bind("<<ComboboxSelected>>", callback_set_temp_units)
e_Temp_Qty_2 = Entry(root, text="", textvariable=eci_temp_2_qty, width=8)  #eci_temp_2_qty
e_Temp_Qty_2.grid(row=23, column=1)   #, padx=4)
e_Temp_Qty_2.config(font=entryfont)
cb_2_Press_Units: Combobox = Combobox(root, values=press_umits, textvariable=eci_2_press_units, width=10)
cb_2_Press_Units.grid(row=23, column=2)   #, padx=4)
cb_2_Press_Units.config(font=entryfont)
cb_2_Press_Units.bind("<<ComboboxSelected>>", callback_set_press_units)
e_Press_Qty_2 = Entry(root, text="", textvariable=eci_press_2_qty, width=8)
e_Press_Qty_2.grid(row=23, column=3)   #, padx=4)
e_Press_Qty_2.config(font=entryfont)
cb_5_Temp_Units: Combobox = Combobox(root, values=temp_umits, textvariable=eci_5_temp_units, width=10)
cb_5_Temp_Units.grid(row=23, column=4)   #, padx=4)
cb_5_Temp_Units.config(font=entryfont)
cb_5_Temp_Units.bind("<<ComboboxSelected>>", callback_set_temp_units)
e_Temp_Qty_5 = Entry(root, text="", textvariable=eci_temp_2_qty, width=8)
e_Temp_Qty_5.grid(row=23, column=5, sticky=W)   #, padx=4)
e_Temp_Qty_5.config(font=entryfont)
cb_5_Press_Units: Combobox = Combobox(root, values=press_umits, textvariable=eci_5_press_units, width=10)
cb_5_Press_Units.grid(row=23, column=6)   #, padx=4)
cb_5_Press_Units.config(font=entryfont)
cb_5_Press_Units.bind("<<ComboboxSelected>>", callback_set_press_units)
e_Press_Qty_5 = Entry(root, text="", textvariable=eci_press_5_qty, width=8)
e_Press_Qty_5.grid(row=23, column=7)   #, padx=4)
e_Press_Qty_5.config(font=entryfont)

lbl_blank = Label(root, text="")
lbl_blank.grid(row=24, column=0)   #, columnspan=2)
lbl_blank.config(font=labelfont)

lbl_eci_3 = Label(root, text="   Select Element, Compound or Ion for ComboBox 3")
lbl_eci_3.grid(row=26, column=0, columnspan=3, sticky=W)
lbl_eci_3.config(font=labelfont)
cb_Select_CB3: Combobox = Combobox(root, values=eci_cb_values, width=10)
cb_Select_CB3.grid(row=26, column=3, sticky=W)   #, padx=4)
cb_Select_CB3.config(font=entryfont)
cb_Select_CB3.bind("<<ComboboxSelected>>", select_eci_3_type)
lbl_eci_6 = Label(root, text="Select Element, Compound or Ion for ComboBox 6 ")
lbl_eci_6.grid(row=26, column=4, columnspan=2, sticky=W)   #, columnspan=2)
lbl_eci_6.config(font=labelfont)
cb_Select_CB6: Combobox = Combobox(root, values=eci_cb_values, width=10)
cb_Select_CB6.grid(row=26, column=6, sticky=W)
cb_Select_CB6.config(font=entryfont)
cb_Select_CB6.bind("<<ComboboxSelected>>", select_eci_6_type)

lbl_eci_3_qty = Label(root, text="ECI Qty 3", width=8)
lbl_eci_3_qty.grid(row=27, column=0)    #, sticky=W
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
lbl_eci_6_qty.grid(row=27, column=4)   #, , sticky=W  padx=4)
lbl_eci_6_qty.config(font=labelfont)
lbl_eci_6_units = Label(root, text="Units 6", width=8)
lbl_eci_6_units.grid(row=27, column=5, sticky=W)   #, padx=4)
lbl_eci_6_units.config(font=labelfont)
lbl_eci_6 = Label(root, text="ECI 6", width=10)
lbl_eci_6.grid(row=27, column=6, sticky=W)   #, padx=4)
lbl_eci_6.config(font=labelfont)
lbl_eci_6_valence = Label(root, text="Valence 6", width=10)
lbl_eci_6_valence.grid(row=27, column=7, sticky=W)
lbl_eci_6_valence.config(font=labelfont)

e_eci_3_qty = Entry(root, text="", textvariable=eci_3_qty, width=8)
e_eci_3_qty.grid(row=28, column=0)   #, , sticky=W padx=4)
e_eci_3_qty.config(font=entryfont)
# cb_Elements1.bind("<<ComboboxSelected>>", callback_E1)
cb_eci_3_units: Combobox = Combobox(root, values=unit_values, textvariable=eci_3_units, width=8)
cb_eci_3_units.grid(row=28, column=1, sticky=W)   #, padx=4)
cb_eci_3_units.config(font=entryfont)
cb_eci_3_units.bind("<<ComboboxSelected>>", eci_units_selected)
cb_eci_3: Combobox = Combobox(root,  textvariable=eci_3, width=12)   #, width=30)
cb_eci_3.grid(row=28, column=2, sticky=W)   #, padx=4)
cb_eci_3.config(font=entryfont)
cb_eci_3['values'] = elements_symbols_list
cb_eci_3.bind("<<ComboboxSelected>>", setSelectedItemName)
cb_eci_3_valence: Combobox = Combobox(root, textvariable=eci_3_valence, width=8)
cb_eci_3_valence.grid(row=28, column=3)   #, padx=4)
cb_eci_3_valence.config(font=entryfont)
cb_eci_3_valence['values'] = valences
e_eci_6_qty = Entry(root, text="", textvariable=eci_6_qty, width=8)
e_eci_6_qty.grid(row=28, column=4)   #, padx=4)
e_eci_6_qty.config(font=entryfont)
cb_eci_6_units: Combobox = Combobox(root, values=unit_values, textvariable=eci_6_units, width=8)
cb_eci_6_units.grid(row=28, column=5)   #, padx=4)
cb_eci_6_units.config(font=entryfont)
cb_eci_6_units.bind("<<ComboboxSelected>>", eci_units_selected)
cb_eci_6: Combobox = Combobox(root, values=compound_symbols_list, textvariable=eci_6, width=12)   #, width=30)
cb_eci_6.grid(row=28, column=6)   #, padx=4)
cb_eci_6.config(font=entryfont)
cb_eci_6.bind("<<ComboboxSelected>>", setSelectedItemName)
cb_eci_6_valence: Combobox = Combobox(root, textvariable=eci_6_valence, width=5)
cb_eci_6_valence.grid(row=28, column=7)   #, padx=4)
cb_eci_6_valence.config(font=entryfont)
cb_eci_6_valence['values'] = valences

e_eci_3_M_qty = Entry(root, text=" ", width=8)
e_eci_3_M_qty.grid(row=29, column=0)   #, padx=4)
e_eci_3_M_qty.config(font=entryfont, textvariable=eci_3_M_qty)
lbl_eci_3_units_M = Label(root, text="Moles", width=8)
lbl_eci_3_units_M.grid(row=29, column=1)   #, padx=4)
lbl_eci_3_units_M.config(font=labelfont)
cb_eci_3_N: Combobox = Combobox(root, values=elements_name_list,  textvariable=eci_3_name, width=12)   #, width=30)
cb_eci_3_N.grid(row=29, column=2)   #, padx=4)
cb_eci_3_N.config(font=entryfont)
cb_eci_3_N.bind("<<ComboboxSelected>>", setSelectedItemFormula)
e_eci_6_M_qty = Entry(root, text="CompoundQty 6", textvariable=eci_6_M_qty, width=8)
e_eci_6_M_qty.grid(row=29, column=4)   #, padx=4)
e_eci_6_M_qty.config(font=entryfont)
lbl_eci_6_units_M = Label(root, text="Moles", width=8)
lbl_eci_6_units_M.grid(row=29, column=5)   #, padx=4)
lbl_eci_6_units_M.config(font=labelfont)
cb_eci_6_N: Combobox = Combobox(root, values=compound_names_list, textvariable=eci_6_name, width=12)   #, width=30)
cb_eci_6_N.grid(row=29, column=6)   #, padx=4)
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
lbl_Temp_Units_6 = Label(root, text="Temp Units", width=10) #, textvariable=eci_temp_5_units
lbl_Temp_Units_6.grid(row=30, column=4)
lbl_Temp_Units_6.config(font=labelfont)
lbl_Temp_Qty_6 = Label(root, text="Temp Qty", width=10) #, textvariable=eci_temp_5_qty
lbl_Temp_Qty_6.grid(row=30, column=5)
lbl_Temp_Qty_6.config(font=labelfont)
lbl_Press_Units_6 = Label(root, text="Press Units", width=10) #, textvariable=eci_press_5_units
lbl_Press_Units_6.grid(row=30, column=6)
lbl_Press_Units_6.config(font=labelfont)
lbl_Press_Qty_6 = Label(root, text="Press Qty", width=10) #, textvariable=eci_press_5_qty
lbl_Press_Qty_6.grid(row=30, column=7)
lbl_Press_Qty_6.config(font=labelfont)

cb_3_Temp_Units: Combobox = Combobox(root, values=temp_umits, textvariable=eci_3_temp_units, width=10)
cb_3_Temp_Units.grid(row=31, column=0)   #, padx=4)
cb_3_Temp_Units.config(font=entryfont)
cb_3_Temp_Units.bind("<<ComboboxSelected>>", callback_set_temp_units)
e_Temp_Qty_3 = Entry(root, text="", textvariable=eci_temp_3_qty, width=8)
e_Temp_Qty_3.grid(row=31, column=1)   #, padx=4)
e_Temp_Qty_3.config(font=entryfont)
cb_3_Press_Units: Combobox = Combobox(root, values=press_umits, textvariable=eci_3_press_units, width=10)
cb_3_Press_Units.grid(row=31, column=2)   #, padx=4)
cb_3_Press_Units.config(font=entryfont)
cb_3_Press_Units.bind("<<ComboboxSelected>>", callback_set_press_units)
e_Press_Qty_3 = Entry(root, text="", textvariable=eci_press_3_qty, width=8)
e_Press_Qty_3.grid(row=31, column=3)   #, padx=4)
e_Press_Qty_3.config(font=entryfont)
cb_6_Temp_Units: Combobox = Combobox(root, values=temp_umits, textvariable=eci_6_temp_units, width=10)
cb_6_Temp_Units.grid(row=31, column=4)   #, padx=4)
cb_6_Temp_Units.config(font=entryfont)
cb_6_Temp_Units.bind("<<ComboboxSelected>>", callback_set_temp_units)
e_Temp_Qty_6 = Entry(root, text="", textvariable=eci_temp_6_qty, width=8)
e_Temp_Qty_6.grid(row=31, column=5)   #, padx=4)
e_Temp_Qty_6.config(font=entryfont)
cb_6_Press_Units: Combobox = Combobox(root, values=press_umits, textvariable=eci_6_press_units, width=10)
cb_6_Press_Units.grid(row=31, column=6)   #, padx=4)
cb_6_Press_Units.config(font=entryfont)
cb_6_Press_Units.bind("<<ComboboxSelected>>", callback_set_press_units)
e_Press_Qty_6 = Entry(root, text="", textvariable=eci_press_6_qty, width=8)
e_Press_Qty_6.grid(row=31, column=7)   #, padx=4)
e_Press_Qty_6.config(font=entryfont)

lbl_blank = Label(root, text="")
lbl_blank.grid(row=32, column=0)   #, columnspan=2)
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
lbl_Side_effects = Label(root, text="Side effects", width=12) #, textvariable=eci_temp_5_units
lbl_Side_effects.grid(row=33, column=4)
lbl_Side_effects.config(font=labelfont)
lbl_By_products = Label(root, text="By-products", width=10) #, textvariable=eci_temp_5_qty
lbl_By_products.grid(row=33, column=5, sticky=W)
lbl_By_products.config(font=labelfont)
lbl_Variables = Label(root, text="Variables")
lbl_Variables.grid(row=33, column=6, sticky=W)
lbl_Variables.config(font=labelfont)
lbl_Variables = Label(root, text="Values", width=10)
lbl_Variables.grid(row=33, column=7, sticky=W)
lbl_Variables.config(font=labelfont)

cb_Equipment: Combobox = Combobox(root, values=equipment, textvariable=equipment_selected, width=12)
cb_Equipment.grid(row=34, column=0)   #, padx=4)
cb_Equipment.config(font=entryfont)
cb_Energy_type: Combobox = Combobox(root, values=energy_type, textvariable=energy_type_selected, width=12)
cb_Energy_type.grid(row=34, column=1, sticky=W)   #, padx=4)
cb_Energy_type.config(font=entryfont)
e_Energy_amount = Entry(root, text="", textvariable=energy_amount, width=12)
e_Energy_amount.grid(row=34, column=2)   #, padx=4)
e_Energy_amount.config(font=entryfont)
cb_Catalyst: Combobox = Combobox(root, values=catalyst, textvariable=catalyst_selected, width=12)
cb_Catalyst.grid(row=34, column=3, sticky=W)   #, padx=4)
cb_Catalyst.config(font=entryfont)
cb_Side_effects: Combobox = Combobox(root, values=side_effects, textvariable=side_effect_selected, width=12)
cb_Side_effects.grid(row=34, column=4)   #, padx=4)
cb_Side_effects.config(font=entryfont)
cb_By_products: Combobox = Combobox(root, values=by_products, textvariable=by_product_selected, width=12)
cb_By_products.grid(row=34, column=5, sticky=W)   #, padx=4)
cb_By_products.config(font=entryfont)
cb_Variables: Combobox = Combobox(root, values=variables, textvariable=variable_selected, width=12)
cb_Variables.grid(row=34, column=6, sticky=W)   #, padx=4)
cb_Variables.config(font=entryfont)
e_Variable_Value = Entry(root, text="", textvariable=variable_value, width=8)
e_Variable_Value.grid(row=34, column=7)   #, padx=4)
e_Variable_Value.config(font=entryfont)

lbl_Explanation = Label(root, text="Explanation", width=10)
lbl_Explanation.grid(row=35, column=0) #, padx=8
lbl_Explanation.config(font=labelfont)
lbl_Explanation = Label(root, text="Super subscript ", width=12)
lbl_Explanation.grid(row=35, column=1,) #, padx=8  columnspan=2
lbl_Explanation.config(font=labelfont)
lbl_LU_Process = Label(text='360\u2070 \u2070C H\u2082O') # C2H3O2-
lbl_LU_Process.grid(row=35, column=2)  #, columnspan=1)
lbl_LU_Process.config(font=labelfont)
'''
unicode numbers. degrees: \u2070 subscript 2: \u2082 subscript 3: \u2083 subscript e: \u2091
superscript 2:\u00B2 superscript 3:\u00B3 superscript 4: \u2074 superscript -: \u207B
'''
lbl_LU_Process = Label(text='X\u2074 + X\u00B2 = 0')
lbl_LU_Process.grid(row=35, column=3)  #, columnspan=1)
lbl_LU_Process.config(font=labelfont)
lbl_LU_Process = Label(text='C\u2082H\u2083O\u2082\u207B C\u2082H\u2083O\u00B2\u207B')
#lbl_LU_Process = Label(text='C\u00B2\u207A Fe\u00B3\u207A Cl\u207B e\u207B')
lbl_LU_Process.grid(row=35, column=4)  #, columnspan=1)
lbl_LU_Process.config(font=labelfont)
lbl_LU_Process = Label(text='Cl\u2091 Fe\u00B3\u207A ')
lbl_LU_Process.grid(row=35, column=5)  #, columnspan=1)
lbl_LU_Process.config(font=labelfont)
e_Explanation = Text(root, height=6, width=100)
e_Explanation.grid(row=36, column=0, columnspan=6, sticky=W)
e_Explanation.config(font=entryfont)
e_Explanation.rowconfigure(99)

#e_Explanation.insert(1, 'Fe\u00B2\u207A Fe\u00B3\u207A Cl\u207B e\u207B')
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
    #set_temp_and_press_settings()
    #make_element_dictionary()
    #make_compound_dictionary()
    #make_ion_dictionary()
    #make_compound_alpha_list()
    #make_ion_alpha_list()
    root.mainloop()
    #print(element)

''' *** e_eci_1_qty.bind('<FocusOut>', (lambda event: check_entry_changes())) ***'''
'''
sys.path is:
['C:\\Program Files\\JetBrains\\PyCharm Edu 2020.1\\plugins\\python-ce\\helpers\\pydev',
'C:\\Program Files\\JetBrains\\PyCharm Edu 2020.1\\plugins\\python-ce\\helpers\\third_party\\thriftpy',
'C:\\Program Files\\JetBrains\\PyCharm Edu 2020.1\\plugins\\python-ce\\helpers\\pydev', 
'C:\\Users\\Owner\\AppData\\Local\\Programs\\Python\\Python38\\python38.zip', 
'C:\\Users\\Owner\\AppData\\Local\\Programs\\Python\\Python38\\DLLs', 
'C:\\Users\\Owner\\AppData\\Local\\Programs\\Python\\Python38\\lib', 
'C:\\Users\\Owner\\AppData\\Local\\Programs\\Python\\Python38', 
'C:\\Users\\Owner\\Chemistry101A', 
'C:\\Users\\Owner\\Chemistry101A\\lib\\site-packages', 
'C:\\projects\\Chemistry101A', 
'C:/projects/Chemistry101A']

elif (compound[1].islower()) and len(compound) > 0:
# If the second character is an lowercase letter, 
#the first two characters are an element.
current_element = compound[0:2]
if compound[2].isupper() and len(compound) > 1:
# If the third character is an uppercase letter,  
current_element_multiplier = 1
current_compound.append(current_element)
current_compound.append(current_element_multiplier)
compound = compound[3:]
print('current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
print('current_compound is ', current_compound)
elif (compound[2].isdigit() and len(compound) > 1):
If the third character is a number, 
it is a subscript for the 2 character element. 

current_compound.append(current_element)
current_compound.append(current_element_multiplier)
current_element_multiplier = 1
compound = compound[3:]
#print('current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
#print('current_compound is ', current_compound)
elif (compound[1].isdigit()) and len(compound) > 0:
current_element_multiplier =  compound[1]
current_compound.append(current_element)
current_compound.append(current_element_multiplier)
current_element_multiplier = 1
compound = compound[2:]
print('current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
print('current_compound is ', current_compound)
else: compound = compound[2:]
print('current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
print('current_compound is ', current_compound)
#Following shouldnt happen
elif compound[0].isdigit():
current_element = compound[0]
current_element_multiplier =  compound[1]
current_compound.append(current_element)
#current_compound.append(":")
current_compound.append(current_element_multiplier)
compound = compound[2:]
print('current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
print('current_compound is ', current_compound)

#total_mass = 3 * db[eci_1]['mass']  #total_mass is  26.98153826.98153826.981538 prints mass 3 times

try:
    f = open(arg, 'r')
except OSError:
    print('cannot open', arg)
else:
    print(arg, 'has', len(f.readlines()), 'lines')
    f.close()
print("eci_db['eci_1']['display_press_units'] is ", eci_db['eci_1']['display_press_units'])
print("eci_db['eci_2']['display_press_units'] is ", eci_db['eci_2']['display_press_units'])
print("eci_db['eci_3']['display_press_units'] is ", eci_db['eci_3']['display_press_units'])
print("eci_db['eci_4']['display_press_units'] is ", eci_db['eci_4']['display_press_units'])
print("eci_db['eci_5']['display_press_units'] is ", eci_db['eci_5']['display_press_units'])
print("eci_db['eci_6']['display_press_units'] is ", eci_db['eci_6']['display_press_units'])        
#cb_eci_1_units.set('grams')
#cb_eci_1.select_clear()
#cb_eci_1.set(compounds_names_dict[cb_eci_1_N.get()])
#print('cb_eci_1 is ', compounds_names_dict[cb_eci_1_N.get()])
#print("In setItemFormula if not eci_1_N == ")
#print('cb_1_type is ', cb_1_type)
#index_N_1 = cb_eci_2_N.selection_get()
#print('index_N_1 is ', index_N_1)
#lbl_LU_Process = Label(text='H\u2082O')
#lbl_LU_Process.grid(row=36, column=4)  #, columnspan=1)
#lbl_LU_Process.config(font=labelfont)
lbl_blank = Label(root, text="", width=4)
lbl_blank.grid(row=35, column=8)   #, columnspan=2)
lbl_blank.config(font=labelfont)
    #H = dict(id= 1, symbol= 'H', name= 'Hydrogen', atomic_number= 1, mass= '1.008', period= 1, row= 1, column= 1, _group= '1A 7A',
    # protons= 1, neutrons= 0, electrons= 1, _1s= 1, _2s= 0, _2p= 0, _3s= 0, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0,
    # affinity= '-72', density= '0.00008988', electronegativity= '2.1', melt= '14.01', boil= '-252.76', e_fusion= 'ef', e_vapor= 'ev',
    # t_crit= '-240.17', p_crit= '12.77', valence= '1 -1', a_radius= '53')
    #CountElements()
    #eci_1 = cb_eci_1.get()
    #eci_1 = cb_eci_1.get()
    #eci_1 = compounds_names_dict[cb_eci_1_N.get()]
    #print('eci_1 is ', eci_1)
    
elif (compound[1].isdigit()):
    If the second character is an lowercase letter, 
    the first two characters are an element.
    print('In elif (compound[1].isdigit()):')
    #break
    current_element = compound[0:1]
    current_element_multiplier =  compound[1]
    current_compound.append(current_element)
    current_compound.append(current_element_multiplier)
    compound = compound[2:]
    print('current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
    print('current_compound is ', current_compound)
    if counter == 1:
        cb_4_type.set('elements')
        cb_eci_4.set(current_element)
        e_eci_4_M_qty.delete(0, END)
        e_eci_4_M_qty.insert(0, current_element_multiplier)
        counter += 1
        print('current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
        print('current_compound is ', current_compound)
    elif counter == 2:
        cb_5_type.set('elements')
        cb_eci_5.set(current_element)
        e_eci_5_M_qty.delete(0, END)
        e_eci_5_M_qty.insert(0, current_element_multiplier)
        counter += 1
        print('current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
        print('current_compound is ', current_compound)
    elif counter > 2:
        print('counter is greater than 2', counter) 
    if compound[2].isdigit():
        #If the third character is a number, 
        #it is a subscript for the 2 character element 
    #current_element_multiplier =  compound[2]
        current_compound.append(current_element)
        #current_compound.append(":")
        current_compound.append(current_element_multiplier)
        current_element_multiplier = 1
        compound = compound[3:]
        if counter == 1:
            cb_4_type.set('elements')
            cb_eci_4.set(current_element)
            e_eci_4_M_qty.delete(0, END)
            e_eci_4_M_qty.insert(0, current_element_multiplier)
            counter += 1
            print('current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
            print('current_compound is ', current_compound)
        elif counter == 2:
            cb_5_type.set('elements')
            cb_eci_5.set(current_element)
            e_eci_5_M_qty.delete(0, END)
            e_eci_5_M_qty.insert(0, current_element_multiplier)
            counter += 1
            print('current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
            print('current_compound is ', current_compound)
        elif counter > 2:
            print('counter is greater than 2', counter)
'''
