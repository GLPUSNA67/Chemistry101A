''' Constants Variables Functions Lists etc '''
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
from collections import defaultdict
import re

#root = tk.Tk()
#root.title('Constants Variables Functions Lists Etc')

titlefont = ('Ariel', 14, 'bold')
labelfont = ('Ariel', 14)  # , 'bold')
buttonfont = ('Ariel', 12)  # , 'bold')
entryfont = ('Ariel', 12)  # , 'bold')

elements = "Ac Ag Al Am Ar As At Au B Ba Be Bi Bk Br C Ca Cd Ce Cf Cl Cm Co Cr Cs Cu Dy Er Es Eu " \
           "F Fe Fm Fr Ga Gd Ge H He Hf Hg Ho I In Ir K Kr La Li Lu Md Mn Mo N Na Nb Nd Ne Ni Np O Os " \
           "P Pa Pb Pd Pm Po Pr Pt Pu Ra Rb Re Rh Rn  Ru S Sb Sc Se Si Sm Sn Sr Ta Tb Tc Te Th Ti Tl Tm" \
           "U V W Xe Y Yb Zn Zr "
'''Not all the elements and their attributes have been added to the database. H\u2082 works for H2 subscript'''
''' The following are not lists, but have list in the title because the string lists the items.'''
elements_symbols_list = "Ac Ag Al Am Ar As At Au B Ba Be Bi Bk Br C Ca Cd Ce Cf Cl Cm Co Cr Cs Cu Dy Er Es Eu " \
                        "F Fe Fm Fr Ga Gd Ge H He Hf Hg Ho I In Ir K Kr La Li Lu Md Mn Mo N Na Nb Nd Ne Ni Np O Os " \
                        "P Pa Pb Pd Pm Po Pr Pt Pu Ra Rb Re Rh Rn  Ru S Sb Sc Se Si Sm Sn Sr Ta Tb Tc Te Th Ti Tl Tm" \
                        "U V W Xe Y Yb Zn Zr "
elements_name_list = "Actinium Silver Aluminum Americium Argon Arsenic Astatine Gold Boron Barium Beryllium " \
                     "Bismuth Berkelium Bromine Carbon Calcium Cadmium Cerium Californium Chlorine Curium Cobalt Chromium " \
                     "Cesium Copper Dysprosium Erbium Einsteinium Europium Fluorine Iron Fermium Francium Gallium Gadolinium " \
                     "Germanium Hydrogen Helium Hafnium Mercury Holmium Iodine Indium Iridium Potassium Krypton " \
                     "Lanthanum Lithium Lutetium Mendelevium Manganese Molybdenum Nitrogen Na Niobium Neodymium Neon Nickel " \
                     "Neptunium Oxygen Osmium Phosphorus Protactinium Lead Palladium Promethium Polonium Praseodymium " \
                     "Platnum Plutonium Radium Rubidium Rhenium Rhodium Radon Rutherfordium Sulfur Antimony Scandium Selenium Silicon " \
                     "Samarium Tin Strontium Tantalum Terbium Technetium Tellurium Thorium Titanium " \
                     "Thallium Thulium Uranium Vanadium Tungsten Xenon Yttrium Ytterbium Zinc Zirconium "
''' This list of elements and names will help retrieve names from symbols. '''
# element = zip(elements_symbols_list, elements_name_list)
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
''' An initial list of ions and names to fill the combo boxes until a proper list can be made. '''
ion_symbols_list = "C2H3O2 ClO2 ClO3 ClO4 CN CO32 CuS FeCl2 FeCl3 H2PO4 HCO3 Hg2O HgO H3O HPO42 HSO4 OH NH4 NO3 NO2 MnO4 O22 SO42 SO32 PO43"
ion_names_list = "acetate chlorite chlorate perchlorate cyanide carbonate copper_(II)_sulfide " \
                 "iron_(II)_chloride iron_(III)_chloride dihydrogen_phosphate hydrogen_carbonate " \
                 "mercury_(I)_oxide mercury_(II)_oxide hydronium hydrogen_phosphate hydrogen_sulfate " \
                 "hydroxide ammonium nitrate nitrite permanganate peroxide sulfate sulfite phosphate "

ion_names_dict = {'acetate': 'C2H3O2', 'chlorite': 'ClO2', 'chlorate': 'ClO3', 'perchlorate': 'ClO4',
                  'cyanide': 'CN', 'carbonate': 'CO32', 'copper_(II)_sulfide': 'CuS', 'iron_(II)_chloride': 'FeCl2',
                  'iron_(III)_chloride': 'FeCl3', 'dihydrogen_phosphate': 'H2PO4', 'hydrogen_carbonate': 'HCO3',
                  'mercury_(I)_oxide': 'Hg2O', 'mercury_(II)_oxide': 'HgO', 'hydronium': 'H3O',
                  'hydrogen_phosphate': 'HPO42', 'hydrogen_sulfate': 'HSO4', 'hydroxide': 'OH',
                  'ammonium': 'NH4', 'nitrate': 'NO3', 'nitrite': 'NO2',
                  'permanganate': 'MnO4', 'peroxide': 'H2O22', 'sulfate': 'SO42',
                  'sulfite': 'SO32', 'phosphate': 'PO43'}

''' Other variables used by Chemistry and other programs '''
unit_values = "Moles grams kilograms ounces pounds liters(l) liters(g) ml(l) ml(g)"
eci_cb_values = "elements compounds ions"
environment = "Laboratory Industry Nature"
temp_units = "K F C"
press_units = "ATM torr psi hg"

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
variable_value = "" #DoubleVar()
Init_default_T_and_P = FALSE
Av = "" #DoubleVar()
Bv = "" #DoubleVar()
Cv = "" #DoubleVar()
Kv = "" #DoubleVar()

''' Miscellaneous variables to use until proper variables are created. '''
valences = "7 6 5 4 3 2 1 0 -1 -2 -3 -4"

#mainloop()
