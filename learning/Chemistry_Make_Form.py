from tkinter import *  # get widget classes
from tkinter.ttk import Combobox #,Textbox
from tkinter.messagebox import *  # get standard dialogs
import tkinter as tk
import sqlite3
from sqlite3 import Error
from ElementsDict import *
#from ElementClass import Element
root = tk.Tk()
#root = Tk()
root.title('Chemistry')
titlefont= ('Ariel', 14, 'bold')
labelfont= ('Ariel', 12) #, 'bold')
buttonfont= ('Ariel', 12) #, 'bold')
entryfont= ('Ariel', 12) #, 'bold')

elements_symbols_list = "Ac Ag Al Am Ar As At Au B Ba Be Bi Bk Br C Ca Cd Ce Cf Cl Cm Co Cr Cs Cu Dy Er Es Eu" \
 "F Fe Fm Fr Ga Gd Ge H He Hf Hg Ho I In Ir K Kr La Li Lu Md Mn Mo N Na Nb Nd Ne Ni Np O Os " \
 "P Pa Pb Pd Pm Po Pr Pt Pu Ra Rb Re Rh Rn  Ru S Sb Sc Se Si Sm Sn Sr Ta Tb Tc Te Th Ti Tl Tm" \
 "U V W Xe Y Yb Zn Zr "
elements_name_list = "Actinium Silver Aluminum Americium Argon Arsenic Astatine Gold Boron Barium Beryllium " \
    "Bismuth Berkelium Bromine Carbon Calcium Cadmium Cerium Californium Chlorine Curium Cobalt Chromium " \
    "Cesium Copper Dysprosium Erbium Einsteinium Europium Fluorine Iron Fermium Francium Gallium Gadolinium "\
    "Germanium Hydrogen Helium Hafnium Mercury Holmium Iodine Indium Iridium Potassium Krypton " \
    "Lanthanum Lithium Lutetium Mendelevium Manganese Molybdenum Nitrogen Na Niobium Neodymium Neon Nickel " \
    "Neptunium Oxygen Osmium Phosphorus Protactinium Lead Palladium Promethium Polonium Praseodymium " \
    "Platnum Plutonium Radium Rubidium Rhenium Rhodium Radon Rutherfordium Sulfur Antimony Scandium Selenium Silicon " \
    "Samarium Tin Strontium Tantalum Terbium Technetium Tellurium Thorium Titanium " \
    "Thallium Thulium Uranium Vanadium Tungsten Xenon Yttrium Ytterbium Zinc Zirconium "
element = zip(elements_symbols_list, elements_name_list)

compound_symbols_list = "Al4C3 Al4C3 Ar2He2Kr2Ne2Xe2Rn2 BCl3 CH4 C2H6 C3H8 C4H10 C4H10_M C5H12 C6H14 C7H16 C8H18 " \
                        "C9H20 C10H22 C14H30 C18H38 CaH2PO4 CaI CaOH2 Ca3P2 CdS CsF C6H8O7 CH3CO2H C2H4COH " \
                        "CO CO2 HBr_g HBr_aq HC2H3O2 HCl HCl_g HCl_aq HClO4 HCN H2CO3 HF_g HF_aq HI_g HI_aq " \
                        "HNO2 HNO3 H3PO4 H2S_g H2S_aq H2SO3 H2SO4 IF7 KBr KOH LiCl Mg3N2 NaCl NaHCO3 Na2O NaOH " \
                        "Na2SO4 NH3 N2H4 NO NO2 N2O4 N2O N2O5 PF5 SO2 SO3"
compound_names_list = "aluminum_carbide aluminum_chloride air boron_trichloride methane ethane propane butane 2-methylpropane" \
                      " pentane hexane heptane octane nonane decane tetradecane octadecane calcium_dihydrogen_phosphate" \
                      " calcium_iodide calcium_hydroxide calcium_phosphide cadmium_sulfide cesium_fluoride citric_acid" \
                      " acetic_acid acetic_acid carbon_monoxide carbon_dioxide hydrogen_bromide hydrobromic_acid" \
                      " acetic_acid hydrogen_chloride hydrogen_chloride hydrochloric_acid perchloric_acid hydrogen_cyanide" \
                      " carbonic_acid hydrogen_fluoride hydrofluoric_acid hydrogen_iodide hydroiodic_acid nitrous_acid" \
                      " nitric_acid phosphoric_acid hydrogen_suflide hydrosulfuric_acid sulfurous_acid sulfuric_acid" \
                      " iodine_heptafluoride potassium_bromide potassium_hydroxide lithium_chloride magnesium_nitride" \
                      " sodium_chloride bicarbonate_of_soda sodium_oxide sodium_hydroxide sodium_sulfate ammonia hydrazine nitric_oxide" \
                      " nitorgen_dioxide dinitrogen_tetroxide nitrous_oxide dinitrogen_pentoxide phosphorus_pentafluoride" \
                      " sulfur_dioxide sulfur_trioxide"
compounds = zip(compound_symbols_list, compound_names_list)

des_list = {"AlC": "[Al4C3]", "Ar2He2Kr2Ne2Xe2Rn2": "[Ar2He2Kr2Ne2Xe2Rn2]", "BCl": "[BCl3]",
                "CH": ["CH4", "C2H6", "C3H8", "C4H10", "C4H10_M", "C5H12", "C6H14", "C7H16", "C8H18",
                "C9H20", "C10H22", "C14H30", "C18H38"]}
ion_symbols_list = "OH- SO3-"
ion_names_list = "hydroxide sulfate"

record_name = ""
process_list = "Acid_Base Oxidization_Reduction Oxidation_Rate Precipitation Synthesis Decompose Refine Metathesis "
equipment = "refinery blah1 blah2"
energy_type = "heat electricity"
catalyst = "blah1 blah2 blah3 blah4"
side_effects = "air_polution water_polution land_polution"
by_products = "CO CO2 NO NO2"
variables ="Av Bv Cv Kv"     # Variable names cannot conflict with element symbols like B C H K etc
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
valences = "7 6 5 4 3 2 1 0 -1 -2 -3 -4"
element1 = StringVar()
eci_1 = StringVar()
eci_2 = StringVar()
eci_3 = StringVar()
eci_4 = StringVar()
eci_5 = StringVar()
eci_6 = StringVar()
eci_1_name = ""
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
eci_1_mass = DoubleVar()
eci_2_mass = DoubleVar()
eci_3_mass = DoubleVar()
eci_4_mass = DoubleVar()
eci_5_mass = DoubleVar()
eci_6_mass = DoubleVar()
eci_1_N = StringVar()
eci_2_N = StringVar()
eci_3_N = StringVar()
eci_4_N = StringVar()
eci_5_N = StringVar()
eci_6_N = StringVar()
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

eci_1_qty = DoubleVar()
eci_2_qty = DoubleVar()
eci_3_qty = DoubleVar()
eci_4_qty = DoubleVar()
eci_5_qty = DoubleVar()
eci_6_qty = DoubleVar()

eci_1_M_qty = DoubleVar()
eci_2_M_qty = DoubleVar()
eci_3_M_qty = DoubleVar()
eci_4_M_qty = DoubleVar()
eci_5_M_qty = DoubleVar()
eci_6_M_qty = DoubleVar()

eci_temp_1_units = StringVar()
eci_temp_2_units = StringVar()
eci_temp_3_units = StringVar()
eci_temp_4_units = StringVar()
eci_temp_5_units = StringVar()
eci_temp_6_units = StringVar()
eci_temp_1_qty = DoubleVar()
eci_temp_2_qty = DoubleVar()
eci_temp_3_qty = DoubleVar()
eci_temp_4_qty = DoubleVar()
eci_temp_5_qty = DoubleVar()
eci_temp_6_qty = DoubleVar()

eci_press_1_units = StringVar()
eci_press_2_units = StringVar()
eci_press_3_units = StringVar()
eci_press_4_units = StringVar()
eci_press_5_units = StringVar()
eci_press_6_units = StringVar()
eci_press_1_qty = DoubleVar()
eci_press_2_qty = DoubleVar()
eci_press_3_qty = DoubleVar()
eci_press_4_qty = DoubleVar()
eci_press_5_qty = DoubleVar()
eci_press_6_qty = DoubleVar()
eci_1_valence = StringVar()
eci_2_valence = StringVar()
eci_3_valence = StringVar()
eci_4_valence = StringVar()
eci_5_valence = StringVar()
eci_6_valence = StringVar()
energy_amount = DoubleVar()

unit_values = "Moles grams kilograms ounces pounds liters(l) liters(g) ml(l) ml(g)"
eci_cb_values = "elements compounds ions"

ions = "OH- SO3-"
cb_1_type = ""  # elements compounds ions
cb_2_type = ""
cb_3_type = ""
cb_4_type = ""
cb_5_type = ""
cb_6_type = ""

#process = "Mine Refine Make Use Purify "
environment = "Laboratory Industry Nature"
temp_umits = "K C F"
press_umits = "ATM torr psi hg"

def select_eci_1_type(eventObject):
    cb_1_type = cb_Select_CB1.get()
    if cb_1_type == 'elements':
        cb_eci_1['values'] = elements_symbols_list
        cb_eci_1_N['values'] = elements_name_list
    elif cb_1_type == 'compounds':
        cb_eci_1['values'] = compound_symbols_list   #compound_values
        cb_eci_1_N['values'] = compound_names_list
    elif cb_1_type == 'ions':
        cb_eci_1['values'] = ion_symbols_list
        cb_eci_1_N['values'] = ion_names_list
    else:
        print("Error is select_eci_1_type")
def select_eci_2_type(eventObject):
    cb_2_type = cb_Select_CB2.get()
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
def create_record():
    pass
def get_record():
    print("Pressed Get Record button")
def retrieve_record():
    print("Pressed Retrieve Record button")
def update_record():
    print("Pressed Update Record button")
def Continue():
    process_selected = cb_Select_Process.get()
    print("Process selected is " , process_selected)
    if process_selected == "Acid_Base":
        #print("Synthesis process entered")
        Acid_Base()
    elif process_selected == "Decompose":
        #print("Decompose process entered")
        Decompose()
    elif process_selected == "Oxidization_Reduction":
        #print("Decompose process entered")
        Oxidization_Reduction()
    elif process_selected == "Metathesis":  #Oxidation_Rate
        Metathesis()
        #print("Decompose process entered")
    elif process_selected == "Oxidation_Rate": #
        Oxidization_Rate()
    elif process_selected == "Precipitation":
        Precipitation()
    elif process_selected == "Reduction":
        Reduction()
    elif process_selected == "Refine":
        Refine()
    elif process_selected == "Synthesis":
        Synthesis()
    else: print("Error in Continue selection of process")
    #CountElements()
    #AlphabetizeElements()
    #eci_1 = cb_eci_1.get()
    #print("Process selected is " , process_selected)
    #print('eci_1 = ', eci_1)
    #print("Pressed Continue button")

def Oxidization_Reduction():
    ''' This function has been entered after elements have been selected and the COntinue button pressed'''
    e_Explanation.insert(tk.END, "Oxidization_Reduction process entered\n")
    #print("Oxidization_Reduction process entered")
    cb_1_type = cb_Select_CB1.get()   # Get the selected type of: element, compound, or ion
    print('eci_1_type = ', cb_1_type)
    eci_1 = cb_eci_1.get()
    print('eci_1 = ', eci_1)
    if cb_1_type == 'elements':
        '''  *** The following works! '''
        eci_1_name = db[eci_1]['name']
        eci_1_col = db[eci_1]['column']
        eci_1_mass = db[eci_1]['mass']
        eci_1_valence = db[eci_1]['valence']
        print("db[eci_1]['name'] is ", eci_1_name)
        print("db[eci_1]['column'] is ", eci_1_col)
        print("db[eci_1]['mass'] is ", eci_1_mass)
        print("db[eci_1]['valence'] is ", eci_1_valence)
        #print(eci_1_valence)   # Prints out the variable #str(eci_1).affinity
    elif cb_1_type == 'compounds':
        #eci_1 = cb_eci_1.get()
        #print('eci_1 = ', eci_1)
        e_Explanation.insert(tk.END, "Oxidization_Reduction process entered\n")
        print("Error in Oxidization_Reduction eci_1 can't process compounds yet")
    elif cb_1_type == 'ions':
        #eci_1 = cb_eci_1.get()
        #print('eci_1 = ', eci_1)
        e_Explanation.insert(tk.END, "Error in Oxidization_Reduction eci_1 can't process compounds yet")
    else: print("Error in Oxidization_Reduction process eci_1 else clause")
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
        print("Error in Oxidization_Reduction eci_2 can't process compounds yet")
    elif cb_2_type == 'ions':
        #eci_2 = cb_eci_2.get()
        #print('eci_2 = ', eci_2)
        print("Error in Oxidization_Reduction eci_2 can't process ions yet")
    else: print("Error in Oxidization_Reduction process eci_2 else clause")
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
        print("Error in Oxidization_Reduction eci_3 can't process compounds yet")
    elif cb_3_type == 'ions':
        #eci_3 = cb_eci_3.get()
        #print('eci_3 = ', eci_3)
        print("Error in Oxidization_Reduction eci_3 can't process ions yet")
    elif cb_3_type == "":
        pass
    else: e_Explanation.insert(tk.END, "Error in Oxidization_Reduction process eci_3 else clause\n")

    #if cb_eci_1.get() == 'elements':
    #    eci_1 = cb_eci_1.get()
    #    print('eci_1 = ', eci_1)
    #    print('eci_1_type = ', cb_eci_1.get())
def Precipitation():
    e_Explanation.insert(tk.END, "Precipitation process entered\n")
    #print("Precipitation process entered")

def Oxidization_Rate():
    ''' This function has been entered after elements have been selected and the COntinue button pressed'''
    e_Explanation.insert(tk.END, "Oxidization_Rate process entered\n")
    #print("Oxidization_Rate process entered")
    cb_1_type = cb_Select_CB1.get()   # Get the selected type of: element, compound, or ion
    print('eci_1_type = ', cb_1_type)
    eci_1 = cb_eci_1.get()
    print('eci_1 = ', eci_1)
    if cb_1_type == 'compounds':
        eci_1_name = c_db[eci_1]['name']
        eci_1_elements = c_db[eci_1]['elements']
        print("c_db[eci_1]['name'] is ", eci_1_name)
        print("c_db[eci_1]['elements'] is ", eci_1_elements)
        Parse_Compounds(eci_1_elements)
        #Na2SO4 = dict(formula= 'Na2SO4', name= 'sodium sulfate', elements= 'Na 2 S O 4')
        #  *** Need to process each element of the compound separately
        #Acquire the electronegativity of each element and calculate the affinities
        #    ***


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
    AlphabetizeElements()

    #H = dict(id= 1, symbol= 'H', name= 'Hydrogen', atomic_number= 1, mass= '1.008', period= 1, row= 1, column= 1, _group= '1A 7A',
    # protons= 1, neutrons= 0, electrons= 1, _1s= 1, _2s= 0, _2p= 0, _3s= 0, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0,
    # affinity= '-72', density= '0.00008988', electronegativity= '2.1', melt= '14.01', boil= '-252.76', e_fusion= 'ef', e_vapor= 'ev',
    # t_crit= '-240.17', p_crit= '12.77', valence= '1 -1', a_radius= '53')
    #CountElements()
    e_Explanation.insert(tk.END, "Synthesis process entered\n")
    print("Synthesis process entered")
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

    eci_1_valence = db[eci_1]['valence']
    eci_2_valence = db[eci_2]['valence']
    print("eci_1 is", eci_1, "eci_2 is", eci_2)
    #eci_3 = cb_eci_3.get()
     # and eci_1 != ''
    eci_1_valence = db[eci_1]['valence']
    #eci_3_group = db[eci_3]['_group']
    if cb_1_type == 'elements':
        eci_1_group = db[eci_1]['_group']
        print("eci_1_group is", eci_1_group)
        eci_1_electronegativity = db[eci_1]['electronegativity']
        print('eci_1_electronegativity is:', eci_1_electronegativity)
        if eci_1_group == '1A':
            eci_1_valence= 1
            print('eci_1_valence is:', eci_1_valence)
        elif eci_1_group == '2A':
            eci_1_valence= 2
            print('eci_1_valence is:', eci_1_valence)

        elif eci_1_group == '7A':
            if cb_2_type == 'elements':
                eci_2 = cb_eci_2.get()
                eci_2_electronegativity = db[eci_2]['electronegativity']
                if eci_2_electronegativity > eci_1_electronegativity:
                    eci_2_valence= -1
                    print('eci_2_valence is:', eci_2_valence)
                elif eci_2_electronegativity < eci_1_electronegativity:
                    print('eci_2_valence is not yet determined.')
                elif cb_2_type == 'compounds':
                    e_Explanation.insert(tk.END, "In Synthesis. Can't yet process compounds.\n")
                elif cb_2_type == 'ions':
                    e_Explanation.insert(tk.END, "In Synthesis. Can't yet process ions.\n")
        if cb_2_type == 'elements':
            eci_2_group = db[eci_2]['_group']
            eci_2_electronegativity = db[eci_2]['electronegativity']
            print('eci_2_electronegativity is:', eci_2_electronegativity)
            if eci_2_group == '1A':
                eci_2_valence= 1
                print('eci_2_valence is:', eci_2_valence)
            elif eci_2_group == '2A':
                eci_2_valence= 2
                print('eci_2_valence is:', eci_2_valence)
            elif eci_2_group == '7A':
                print('In elif eci_2_group == 7A')
                if eci_1_electronegativity > eci_2_electronegativity:
                    print('if eci_1_electronegativity > eci_2_electronegativity:')
                    eci_2_valence= -2
                    print('eci_2_valence is:', eci_2_valence[0])
                    print('eci_2_electronegativity > eci_1_electronegativity.')
                elif eci_2_electronegativity > eci_1_electronegativity:
                    print('elif eci_2_electronegativity > eci_1_electronegativity:')
                    if str(eci_2_valence):
                        print('eci_2_valence is a string')
                        if int(eci_1_valence) > 0:
                            print('eci_1_valence is a positive number')
                            if '-1' in eci_2_valence:
                                print('-1 is in the string eci_2_valence')
                                eci_2_valence = 1
                                print('eci_2_valence is ', eci_2_valence[0])
                        else: eci_2_valence = 6
                        #print('eci_2_valence is a string')
                    #eci_2_valence= -1
                    #print('eci_2_valence is:', eci_2_valence)
                    #print('eci_2_electronegativity < eci_1_electronegativity.')
        elif cb_2_type == 'compounds':
            e_Explanation.insert(tk.END, "In Synthesis. Can't yet process compounds.\n")
        elif cb_2_type == 'ions':
            e_Explanation.insert(tk.END, "In Synthesis. Can't yet process ions.\n")




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
        #eci_1 = cb_eci_1.get()
        #print('eci_1 = ', eci_1)
        print("In setClassItem at elif compounds")
def Parse_Compounds(compound):
    e_Explanation.insert(tk.END, "Parse_Compounds process entered\n")
    if compound == "":
        pass
    else: print("Parse_Compounds process entered", compound)

    ''' I need to parse for number, upper, lower. First number always applies to element or formula,
    later numbers may apply to preceeding or following element.
    '''
    compound_formula_qty = 1
    element_1 = ''
    current_element = ""
    current_element_multiplier = 1
    #e_Explanation.
    print('Parse_Compounds compound is ', compound)
    ''' Start with a normal compound which does not start with an integer.'''
     #compound = 'Na2SO4'
    if compound == "":
        pass
    elif compound[0].isdigit():
        compound_formula_qty =  compound[0]
        compound = compound[1:]
        print('Parse_Compounds compound first character is integer ', compound[0] )
        if len(compound) != 0:
            Parse_Compounds(compound)
    elif (compound[0].isupper()):
        if (compound[1].isupper()):
            current_element = compound[0]
            compound = compound[1:]
            print('current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
            if len(compound) != 0:
                Parse_Compounds(compound)
        elif (compound[1].islower()):
            current_element = compound[0:2]
            #print(current_element)
            if compound[2].isdigit():
                current_element_multiplier =  compound[2]
                compound = compound[3:]
                print('current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
                Parse_Compounds(compound)
            else: compound = compound[2:]
            print('current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
            if len(compound) != 0:
                Parse_Compounds(compound)
        elif compound[1].isdigit():
            current_element = compound[0]
            current_element_multiplier =  compound[1]
            compound = compound[2:]
            print('current_element is ', current_element, ' current_element_multiplier is ', current_element_multiplier)
            if len(compound) != 0:
                Parse_Compounds(compound)
        # print('Get the valence number for the element')

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


def make_form():
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
    cb_RecordName = Combobox(root, values="", width=12)
    cb_RecordName.grid(row=3, column=1)  #, columnspan=2)
    cb_RecordName.config(font=entryfont)
    cb_RecordName.bind("<<ComboboxSelected>>", retrieve_record)
    #e_recordname = Entry(root, text="")   #, width=30)
    #e_recordname.grid(row=3, column=3)
    #e_recordname.config(font=labelfont)
    btn_create_record = Button(root, text = 'Get Record', command=get_record)
    btn_create_record.grid(row=3, column=3)
    btn_create_record.config(font=buttonfont)
    btn_create_record.bind("<<ComboboxSelected>>", create_record)


    #lbl_blank = Label(root, text="")
    #lbl_blank.grid(row=6, column=0, columnspan=2)
    #lbl_blank.config(font=labelfont)


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
    cb_Select_Process = Combobox(root, values=process_list, textvariable=process_selected, width=12)   #, width=30)
    cb_Select_Process.grid(row=7, column=3)   #, columnspan=2)
    cb_Select_Process.config(font=entryfont)
    lbl_Select_Environment = Label(text="   Select environment:", width=22)
    lbl_Select_Environment.grid(row=7, column=4)
    lbl_Select_Environment.config(font=labelfont)
    cb_Select_Environment = Combobox(root, values=environment, width=12)   #, width=30)
    cb_Select_Environment.grid(row=7, column=5)   #, columnspan=2)
    cb_Select_Environment.config(font=entryfont)

    cb_Select_Process.bind("<<ComboboxSelected>>", process_selected)
    lbl_blank = Label(root, text="")
    lbl_blank.grid(row=8, column=0) #, columnspan=2)
    lbl_blank.config(font=labelfont)

    lbl_eci_1 = Label(root, text="   Select Element, Compound or Ion for ComboBox 1")
    lbl_eci_1.grid(row=9, column=0, columnspan=3, sticky=W)
    lbl_eci_1.config(font=labelfont)
    cb_Select_CB1 = Combobox(root, values=eci_cb_values, width=10)
    cb_Select_CB1.grid(row=9, column=3, sticky=W)
    cb_Select_CB1.config(font=entryfont)
    cb_Select_CB1.bind("<<ComboboxSelected>>", select_eci_1_type)
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
    e_eci_1_qty.grid(row=12, column=0)   #, padx=4)
    e_eci_1_qty.config(font=entryfont)
    #e_eci_1_qty.bind(callback_eci_1_qty)            #root, textvariable=user_input
    cb_eci_1_units = Combobox(root, values=unit_values, textvariable=eci_1_units, width=10)
    cb_eci_1_units.grid(row=12, column=1)   #, padx=4)
    cb_eci_1_units.config(font=entryfont)
    #cb_eci_1_units.bind("<<ComboboxSelected>>", callback_eci_1_units)
    cb_eci_1 = Combobox(root, textvariable=eci_1, width=12) #, command=setClassItem
    cb_eci_1.grid(row=12, column=2)   #, padx=4)
    cb_eci_1.config(font=entryfont)
    cb_eci_1['values'] = elements_symbols_list
    cb_eci_1.bind("<<ComboboxSelected>>", setClassItem)

    cb_eci_1_valence = Combobox(root, textvariable=eci_1_valence, width=8)
    cb_eci_1_valence.grid(row=12, column=3)   #, padx=4)
    cb_eci_1_valence.config(font=entryfont)
    cb_eci_1_valence['values'] = valences

    e_eci_4_qty = Entry(root, text="", textvariable=eci_4_qty, width=8)
    e_eci_4_qty.grid(row=12, column=4)   #, padx=4)
    e_eci_4_qty.config(font=entryfont)
    cb_eci_4_units = Combobox(root, values=unit_values, textvariable=eci_4_units, width=10)
    cb_eci_4_units.grid(row=12, column=5)   #, padx=4)
    cb_eci_4_units.config(font=entryfont)
    #cb_eci_4_units.bind("<<ComboboxSelected>>", callback_eci_4_units)
    cb_eci_4 = Combobox(root, textvariable=eci_4, width=12)   # , values=compound_values
    cb_eci_4.grid(row=12, column=6)   #, padx=4)
    cb_eci_4.config(font=entryfont)
    cb_eci_4['values'] = compound_symbols_list
    #cb_eci_4.bind("<<ComboboxSelected>>", callback_eci_4)
    cb_eci_4_valence = Combobox(root, textvariable=eci_4_valence, width=5)
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
    cb_eci_1_N = Combobox(root,  textvariable=eci_1_N, width=12)
    cb_eci_1_N.grid(row=13, column=2)   #, padx=4)
    cb_eci_1_N.config(font=entryfont)
    cb_eci_1_N['values'] = compound_names_list

    e_eci_4_M_qty = Entry(root, text="", textvariable=eci_4_M_qty, width=8)
    e_eci_4_M_qty.grid(row=13, column=4)   #, padx=4)
    e_eci_4_M_qty.config(font=entryfont)
    lbl_eci_4_units_M = Label(root, text="Moles", width=10)
    lbl_eci_4_units_M.grid(row=13, column=5)   #, padx=4)
    lbl_eci_4_units_M.config(font=labelfont)
    cb_eci_4_N = Combobox(root, values=compound_symbols_list, textvariable=eci_4_N, width=12)
    cb_eci_4_N.grid(row=13, column=6)   #, padx=4)
    cb_eci_4_N.config(font=entryfont)

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

    cb_Temp_Units_1 = Combobox(root, values=temp_umits, textvariable=eci_temp_1_units, width=10) # eci_temp_1_units
    cb_Temp_Units_1.grid(row=15, column=0)   #, padx=4)
    cb_Temp_Units_1.config(font=entryfont)
    #cb_Temp_Units_1.bind("<<ComboboxSelected>>", callback_eci_1_units())
    e_Temp_Qty_1 = Entry(root, text="", textvariable=eci_temp_1_qty, width=8)   #, width=12)
    e_Temp_Qty_1.grid(row=15, column=1)   #, padx=4)
    e_Temp_Qty_1.config(font=entryfont)
    cb_Press_Units_1 = Combobox(root, values=press_umits, textvariable=eci_press_1_units, width=10)   #, width=12)
    cb_Press_Units_1.grid(row=15, column=2)  #, padx=4)
    cb_Press_Units_1.config(font=entryfont)
    #cb_Temp_Units_1.bind("<<ComboboxSelected>>", callback_eci_1_units())
    e_Press_Qty_1 = Entry(root, text="", textvariable=eci_press_1_qty, width=8)   #, width=12)
    e_Press_Qty_1.grid(row=15, column=3)   #, padx=4)
    e_Press_Qty_1.config(font=entryfont)

    cb_Temp_Units_4 = Combobox(root, values=temp_umits, textvariable=eci_temp_4_units, width=10)   #, width=12)
    cb_Temp_Units_4.grid(row=15, column=4)   #, padx=4)
    cb_Temp_Units_4.config(font=entryfont)
    e_Temp_Qty_4 = Entry(root, text="", textvariable=eci_temp_4_qty, width=8)   #, width=12)
    e_Temp_Qty_4.grid(row=15, column=5, sticky=W)  #, padx=4)
    e_Temp_Qty_4.config(font=entryfont)
    cb_Press_Units_4 = Combobox(root, values=press_umits, textvariable=eci_press_4_units, width=10)   #, width=12)
    cb_Press_Units_4.grid(row=15, column=6)   #, padx=4)
    cb_Press_Units_4.config(font=entryfont)
    e_Press_Qty_4 = Entry(root, text="", textvariable=eci_press_4_qty, width=8)   #, width=12)
    e_Press_Qty_4.grid(row=15, column=7)   #, padx=4)
    e_Press_Qty_4.config(font=entryfont)

    lbl_blank = Label(root, text="")
    lbl_blank.grid(row=16, column=0)   #, columnspan=2)
    lbl_blank.config(font=labelfont)

    lbl_eci_2 = Label(root, text="   Select Element, Compound or Ion for ComboBox 2")
    lbl_eci_2.grid(row=17, column=0, columnspan=3, sticky=W)
    lbl_eci_2.config(font=labelfont)
    cb_Select_CB2 = Combobox(root, values=eci_cb_values, width=10)
    cb_Select_CB2.grid(row=17, column=3, sticky=W) # , columnspan=2
    cb_Select_CB2.config(font=entryfont)
    cb_Select_CB2.bind("<<ComboboxSelected>>", select_eci_2_type)

    #btn_Select_CB2 = Button(root, command=Synthesis(variables), text = 'Elements')
    #btn_Select_CB2.grid(row=17, column=2)
    #btn_Select_CB2.config(font=buttonfont)
    lbl_eci_5 = Label(root, text="Select Element, Compound or Ion for ComboBox 5")
    lbl_eci_5.grid(row=17, column=4, columnspan=2, sticky=W)
    lbl_eci_5.config(font=labelfont)
    cb_Select_CB5 = Combobox(root, values=eci_cb_values, width=10)   #, width=20)
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
    cb_eci_2_units = Combobox(root, values=unit_values, textvariable=eci_2_units, width=10)   #, width=8)
    cb_eci_2_units.grid(row=20, column=1)   #, padx=4)
    cb_eci_2_units.config(font=entryfont)
    #cb_eci_2_units.bind("<<ComboboxSelected>>", callback_eci_2_units)
    cb_eci_2 = Combobox(root,  textvariable=eci_2, width=12)    #, values=elements, width=30)
    cb_eci_2.grid(row=20, column=2)   #, padx=4)
    cb_eci_2.config(font=entryfont)
    cb_eci_2['values'] = elements_symbols_list
    #cb_eci_2.bind("<<ComboboxSelected>>", callback_eci_2)
    cb_eci_2_valence = Combobox(root, textvariable=eci_2_valence, width=8)
    cb_eci_2_valence.grid(row=20, column=3)   #, padx=4)
    cb_eci_2_valence.config(font=entryfont)
    cb_eci_2_valence['values'] = valences

    e_eci_5_qty = Entry(root, text="", textvariable=eci_5_qty, width=8)
    e_eci_5_qty.grid(row=20, column=4)    #, padx=4)
    e_eci_5_qty.config(font=entryfont)
    cb_eci_5_units = Combobox(root, values=unit_values, textvariable=eci_5_units, width=10)
    cb_eci_5_units.grid(row=20, column=5)   #, padx=4)
    cb_eci_5_units.config(font=entryfont)
    cb_eci_5 = Combobox(root, values=compound_symbols_list, textvariable=eci_5, width=12)   #, width=30)
    cb_eci_5.grid(row=20, column=6)   #, padx=4)
    cb_eci_5.config(font=entryfont)
    cb_eci_5_valence = Combobox(root, textvariable=eci_5_valence, width=5)
    cb_eci_5_valence.grid(row=20, column=7)   #, padx=4)
    cb_eci_5_valence.config(font=entryfont)
    cb_eci_5_valence['values'] = valences

    e_eci_2_M_qty = Entry(root, text=" ", width=8)
    e_eci_2_M_qty.grid(row=21, column=0)   #, padx=4)
    e_eci_2_M_qty.config(font=entryfont, textvariable=eci_2_M_qty)
    lbl_eci_2_units_M = Label(root, text="Moles", width=10)
    lbl_eci_2_units_M.grid(row=21, column=1)   #, padx=4)
    lbl_eci_2_units_M.config(font=labelfont)
    cb_eci_2_N = Combobox(root, values=elements_name_list,  textvariable=eci_2_N, width=12)   #, width=30)
    cb_eci_2_N.grid(row=21, column=2)   #, padx=4)
    cb_eci_2_N.config(font=entryfont)
    e_eci_5_M_qty = Entry(root, text="CompoundQty 5", textvariable=eci_5_M_qty, width=8)   #, width=8)
    e_eci_5_M_qty.grid(row=21, column=4)   #, padx=4)
    e_eci_5_M_qty.config(font=entryfont)
    lbl_eci_5_units_M = Label(root, text="Moles", width=10)
    lbl_eci_5_units_M.grid(row=21, column=5)   #, padx=4)
    lbl_eci_5_units_M.config(font=labelfont)
    cb_eci_5_N = Combobox(root, values=compound_names_list, textvariable=eci_5_N, width=12)   #, width=30)
    cb_eci_5_N.grid(row=21, column=6)   #, padx=4)
    cb_eci_5_N.config(font=entryfont)

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

    cb_Temp_Units_2 = Combobox(root, values=temp_umits, textvariable=eci_temp_2_units, width=10) #, textvariable=eci_temp_2_units
    cb_Temp_Units_2.grid(row=23, column=0)   #, padx=4)
    cb_Temp_Units_2.config(font=entryfont)
    e_Temp_Qty_2 = Entry(root, text="", textvariable=eci_temp_2_qty, width=8)  #eci_temp_2_qty
    e_Temp_Qty_2.grid(row=23, column=1)   #, padx=4)
    e_Temp_Qty_2.config(font=entryfont)
    cb_Press_Units_2 = Combobox(root, values=press_umits, textvariable=eci_press_2_units, width=10)
    cb_Press_Units_2.grid(row=23, column=2)   #, padx=4)
    cb_Press_Units_2.config(font=entryfont)
    e_Press_Qty_2 = Entry(root, text="", textvariable=eci_press_2_qty, width=8)
    e_Press_Qty_2.grid(row=23, column=3)   #, padx=4)
    e_Press_Qty_2.config(font=entryfont)
    cb_Temp_Units_5 = Combobox(root, values=temp_umits, width=10)
    cb_Temp_Units_5.grid(row=23, column=4)   #, padx=4)
    cb_Temp_Units_5.config(font=entryfont)
    e_Temp_Qty_5 = Entry(root, text="", textvariable=eci_temp_2_qty, width=8)
    e_Temp_Qty_5.grid(row=23, column=5, sticky=W)   #, padx=4)
    e_Temp_Qty_5.config(font=entryfont)
    cb_Press_Units_5 = Combobox(root, values=press_umits, width=10)
    cb_Press_Units_5.grid(row=23, column=6)   #, padx=4)
    cb_Press_Units_5.config(font=entryfont)
    e_Press_Qty_5 = Entry(root, text="", textvariable=eci_press_5_qty, width=8)
    e_Press_Qty_5.grid(row=23, column=7)   #, padx=4)
    e_Press_Qty_5.config(font=entryfont)

    lbl_blank = Label(root, text="")
    lbl_blank.grid(row=24, column=0)   #, columnspan=2)
    lbl_blank.config(font=labelfont)

    lbl_eci_3 = Label(root, text="   Select Element, Compound or Ion for ComboBox 3")
    lbl_eci_3.grid(row=26, column=0, columnspan=3, sticky=W)
    lbl_eci_3.config(font=labelfont)
    cb_Select_CB3 = Combobox(root, values=eci_cb_values, width=10)
    cb_Select_CB3.grid(row=26, column=3, sticky=W)   #, padx=4)
    cb_Select_CB3.config(font=entryfont)
    cb_Select_CB3.bind("<<ComboboxSelected>>", select_eci_3_type)

    lbl_eci_6 = Label(root, text="Select Element, Compound or Ion for ComboBox 6 ")
    lbl_eci_6.grid(row=26, column=4, columnspan=2, sticky=W)   #, columnspan=2)
    lbl_eci_6.config(font=labelfont)
    cb_Select_CB6 = Combobox(root, values=eci_cb_values, width=10)
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
    cb_eci_3_units = Combobox(root, values=unit_values, textvariable=eci_3_units, width=8)
    cb_eci_3_units.grid(row=28, column=1, sticky=W)   #, padx=4)
    cb_eci_3_units.config(font=entryfont)
    #cb_eci_2_units.bind("<<ComboboxSelected>>", callback_eci_2_units)
    cb_eci_3 = Combobox(root,  textvariable=eci_3, width=12)   #, width=30)
    cb_eci_3.grid(row=28, column=2, sticky=W)   #, padx=4)
    cb_eci_3.config(font=entryfont)
    cb_eci_3['values'] = elements_symbols_list
    #cb_eci_3.bind("<<ComboboxSelected>>", callback_eci_3)
    cb_eci_3_valence = Combobox(root, textvariable=eci_3_valence, width=8)
    cb_eci_3_valence.grid(row=28, column=3)   #, padx=4)
    cb_eci_3_valence.config(font=entryfont)
    cb_eci_3_valence['values'] = valences

    e_eci_6_qty = Entry(root, text="", textvariable=eci_6_qty, width=8)
    e_eci_6_qty.grid(row=28, column=4)   #, padx=4)
    e_eci_6_qty.config(font=entryfont)
    cb_eci_6_units = Combobox(root, values=unit_values, textvariable=eci_6_units, width=8)
    cb_eci_6_units.grid(row=28, column=5)   #, padx=4)
    cb_eci_6_units.config(font=entryfont)
    cb_eci_6 = Combobox(root, values=compound_symbols_list, textvariable=eci_6, width=12)   #, width=30)
    cb_eci_6.grid(row=28, column=6)   #, padx=4)
    cb_eci_6.config(font=entryfont)
    cb_eci_6_valence = Combobox(root, textvariable=eci_6_valence, width=5)
    cb_eci_6_valence.grid(row=28, column=7)   #, padx=4)
    cb_eci_6_valence.config(font=entryfont)
    cb_eci_6_valence['values'] = valences

    e_eci_3_M_qty = Entry(root, text=" ", width=8)
    e_eci_3_M_qty.grid(row=29, column=0)   #, padx=4)
    e_eci_3_M_qty.config(font=entryfont, textvariable=eci_3_M_qty)
    lbl_eci_3_units_M = Label(root, text="Moles", width=8)
    lbl_eci_3_units_M.grid(row=29, column=1)   #, padx=4)
    lbl_eci_3_units_M.config(font=labelfont)
    cb_eci_3_N = Combobox(root, values=elements_name_list,  textvariable=eci_3_N, width=12)   #, width=30)
    cb_eci_3_N.grid(row=29, column=2)   #, padx=4)
    cb_eci_3_N.config(font=entryfont)
    e_eci_6_M_qty = Entry(root, text="CompoundQty 6", textvariable=eci_6_M_qty, width=8)
    e_eci_6_M_qty.grid(row=29, column=4)   #, padx=4)
    e_eci_6_M_qty.config(font=entryfont)
    lbl_eci_6_units_M = Label(root, text="Moles", width=8)
    lbl_eci_6_units_M.grid(row=29, column=5)   #, padx=4)
    lbl_eci_6_units_M.config(font=labelfont)
    cb_eci_6_N = Combobox(root, values=compound_names_list, textvariable=eci_6_N, width=12)   #, width=30)
    cb_eci_6_N.grid(row=29, column=6)   #, padx=4)
    cb_eci_6_N.config(font=entryfont)

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

    cb_Temp_Units_3 = Combobox(root, values=temp_umits, textvariable=eci_temp_2_units, width=10) #, textvariable=eci_temp_2_units
    cb_Temp_Units_3.grid(row=31, column=0)   #, padx=4)
    cb_Temp_Units_3.config(font=entryfont)
    e_Temp_Qty_3 = Entry(root, text="", textvariable=eci_temp_3_qty, width=8)
    e_Temp_Qty_3.grid(row=31, column=1)   #, padx=4)
    e_Temp_Qty_3.config(font=entryfont)
    cb_Press_Units_3 = Combobox(root, values=press_umits, textvariable=eci_press_2_units, width=10)
    cb_Press_Units_3.grid(row=31, column=2)   #, padx=4)
    cb_Press_Units_3.config(font=entryfont)
    e_Press_Qty_3 = Entry(root, text="", textvariable=eci_press_3_qty, width=8)
    e_Press_Qty_3.grid(row=31, column=3)   #, padx=4)
    e_Press_Qty_3.config(font=entryfont)
    cb_Temp_Units_6 = Combobox(root, values=temp_umits, width=10)
    cb_Temp_Units_6.grid(row=31, column=4)   #, padx=4)
    cb_Temp_Units_6.config(font=entryfont)
    e_Temp_Qty_6 = Entry(root, text="", textvariable=eci_temp_6_qty, width=8)
    e_Temp_Qty_6.grid(row=31, column=5)   #, padx=4)
    e_Temp_Qty_6.config(font=entryfont)
    cb_Press_Units_6 = Combobox(root, values=press_umits, width=10)
    cb_Press_Units_6.grid(row=31, column=6)   #, padx=4)
    cb_Press_Units_6.config(font=entryfont)
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

    cb_Equipment = Combobox(root, values=equipment, textvariable=equipment_selected, width=12)
    cb_Equipment.grid(row=34, column=0)   #, padx=4)
    cb_Equipment.config(font=entryfont)
    cb_Energy_type = Combobox(root, values=energy_type, textvariable=energy_type_selected, width=12)
    cb_Energy_type.grid(row=34, column=1, sticky=W)   #, padx=4)
    cb_Energy_type.config(font=entryfont)
    e_Energy_amount = Entry(root, text="", textvariable=energy_amount, width=12)
    e_Energy_amount.grid(row=34, column=2)   #, padx=4)
    e_Energy_amount.config(font=entryfont)
    cb_Catalyst = Combobox(root, values=catalyst, textvariable=catalyst_selected, width=12)
    cb_Catalyst.grid(row=34, column=3, sticky=W)   #, padx=4)
    cb_Catalyst.config(font=entryfont)
    cb_Side_effects = Combobox(root, values=side_effects, textvariable=side_effect_selected, width=12)
    cb_Side_effects.grid(row=34, column=4)   #, padx=4)
    cb_Side_effects.config(font=entryfont)
    cb_By_products = Combobox(root, values=by_products, textvariable=by_product_selected, width=12)
    cb_By_products.grid(row=34, column=5, sticky=W)   #, padx=4)
    cb_By_products.config(font=entryfont)
    cb_Variables = Combobox(root, values=variables, textvariable=variable_selected, width=12)
    cb_Variables.grid(row=34, column=6, sticky=W)   #, padx=4)
    cb_Variables.config(font=entryfont)
    e_Variable_Value = Entry(root, text="", textvariable=variable_value, width=8)
    e_Variable_Value.grid(row=34, column=7)   #, padx=4)
    e_Variable_Value.config(font=entryfont)

    lbl_blank = Label(root, text="", width=4)
    lbl_blank.grid(row=35, column=8)   #, columnspan=2)
    lbl_blank.config(font=labelfont)

    lbl_Explanation = Label(root, text="Explanation", width=10)
    lbl_Explanation.grid(row=36, column=0) #, padx=8
    lbl_Explanation.config(font=labelfont)
    e_Explanation = tk.Text(root, height=6, width=100)
    e_Explanation.grid(row=37, column=0, columnspan=6, sticky=W)
    e_Explanation.config(font=entryfont)
    e_Explanation.rowconfigure(99)
    S = tk.Scrollbar(root)
    S.grid(row=37, column=7, sticky=E)
    S.config(command=e_Explanation.yview)
    #e_Explanation = tk.Text(root, text="", height=6, width=100) # , width=12
    #e_Explanation.grid(row=37, column=0, columnspan=6)
    #e_Explanation.config(font=entryfont)
    #e_Explanation.rowconfigure(99)

    lbl_blank = Label(root, text="")
    lbl_blank.grid(row=40, column=0, columnspan=2)
    lbl_blank.config(font=labelfont)
    lbl_blank = Label(root, text="")
    lbl_blank.grid(row=41, column=0, columnspan=2)
    lbl_blank.config(font=labelfont)
    lbl_blank = Label(root, text="")
    lbl_blank.grid(row=42, column=0, columnspan=2)
    lbl_blank.config(font=labelfont)

if __name__ == '__main__':
    make_form()
    root.mainloop()
