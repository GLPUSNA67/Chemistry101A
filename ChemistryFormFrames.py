from tkinter import *  # get widget classes
from tkinter.ttk import Combobox #,Textbox
from tkinter.messagebox import *  # get standard dialogs
import tkinter as tk
import sqlite3
from sqlite3 import Error
#from ElementsDict import *
#from ElementClass import Element
root = tk.Tk()
#root = Tk()
root.title('Chemistry')
titlefont= ('Ariel', 14, 'bold')
labelfont= ('Ariel', 12) #, 'bold')
buttonfont= ('Ariel', 12) #, 'bold')
entryfont= ('Ariel', 12) #, 'bold')

# *** Start descriptions and list of constants and variables
elements = "Ac Ag Al Am Ar As At Au B Ba Be Bi Bk Br C Ca Cd Ce Cf Cl Cm Co Cr Cs Cu Dy Er Es Eu" \
 "F Fe Fm Fr Ga Gd Ge H He Hf Hg Ho I In Ir K Kr La Li Lu Md Mn Mo N Na Nb Nd Ne Ni Np O Os " \
 "P Pa Pb Pd Pm Po Pr Pt Pu Ra Rb Re Rh Rn  Ru S Sb Sc Se Si Sm Sn Sr Ta Tb Tc Te Th Ti Tl Tm" \
 "U V W Xe Y Yb Zn Zr "
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

compound_symbols_list = "Al4C3 Ar2He2Kr2Ne2Xe2Rn2 BCl3 CH4 C2H6 C3H8 C4H10 C4H10_M C5H12 C6H14 C7H16 C8H18 " \
                        "C9H20 C10H22 C14H30 C18H38 CaH2PO4 CaI CaOH2 Ca3P2 CdS CsF C6H8O7 CH3CO2H C2H4COH " \
                        "CO CO2 HBr_g HBr_aq HC2H3O2 HCl HCl_g HCl_aq HClO4 HCN H2CO3 HF_g HF_aq HI_g HI_aq " \
                        "HNO2 HNO3 H3PO4 H2S_g H2S_aq H2SO3 H2SO4 IF7 KBr KOH LiCl Mg3N2 NaCl NaHCO3 Na2O NaOH " \
                        "Na2SO4 NH3 N2H4 NO NO2 N2O4 N2O N2O5 PF5 SO2 SO3"
compound_names_list = "aluminum_carbide air boron_trichloride methane ethane propane butane 2-methylpropane" \
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

H = dict(id= 1, symbol= 'H', name= 'Hydrogen', atomic_number= 1, mass= '1.008', period= 1, row= 1, column= 1, _group= '1A 7A', protons= 1, neutrons= 0, electrons= 1, _1s= 1, _2s= 0, _2p= 0, _3s= 0, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-72', density= '0.00008988', electronegativity= '2.1', melt= '14.01', boil= '-252.76', e_fusion= 'ef', e_vapor= 'ev', t_crit= '-240.17', p_crit= '12.77', valence= '1 -1', a_radius= '53')
He = dict(id= 2, symbol= 'He', name= 'Helium', atomic_number= 2, mass= '4.002602', period= 1, row= 1, column= 18, _group= '8A', protons= 2, neutrons= 2, electrons= 2, _1s= 2, _2s= 0, _2p= 0, _3s= 0, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '20', density= '0.0001785', electronegativity= '0.0', melt= 'NULL', boil= '-268.94', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '-267.9550', p_crit= '2.261', valence= '0', a_radius= '31')
Li = dict(id= 3, symbol= 'Li', name= 'Lithium', atomic_number= 3, mass= '6.941', period= 2, row= 2, column= 1, _group= '1A', protons= 3, neutrons= 3, electrons= 3, _1s= 2, _2s= 1, _2p= 0, _3s= 0, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-60', density= '0.535', electronegativity= '1.0', melt= '180.50', boil= '1342', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '2950', p_crit= '67', valence= '1', a_radius= '167')
Be = dict(id= 4, symbol= 'Be', name= 'Beryllium', atomic_number= 4, mass= '9.012182', period= 2, row= 2, column= 2, _group= '2A', protons= 4, neutrons= 4, electrons= 4, _1s= 2, _2s= 2, _2p= 0, _3s= 0, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '240', density= '1.848', electronegativity= '1.5', melt= '1287', boil= '2468', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '4932', p_crit= 'NULL', valence= '2', a_radius= '112')
B = dict(id= 5, symbol= 'B', name= 'Boron', atomic_number= 5, mass= '10.8111', period= 2, row= 2, column= 13, _group= '3A', protons= 5, neutrons= 5, electrons= 5, _1s= 2, _2s= 2, _2p= 1, _3s= 0, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-23', density= '2.460', electronegativity= '2.0', melt= '2077', boil= '4000', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= '3', a_radius= '87')
C = dict(id= 6, symbol= 'C', name= 'Carbon', atomic_number= 6, mass= '12.0107', period= 2, row= 2, column= 14, _group= '4A', protons= 6, neutrons= 6, electrons= 6, _1s= 2, _2s= 2, _2p= 2, _3s= 0, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-123', density= '2.260', electronegativity= '2.5', melt= '4489', boil= '3825', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= '4 3 2 1 0 -1 -2 -3 -4', a_radius= '67')
N = dict(id= 7, symbol= 'N', name= 'Nitrogen', atomic_number= 7, mass= '14.0087', period= 2, row= 2, column= 15, _group= '5A', protons= 7, neutrons= 7, electrons= 7, _1s= 2, _2s= 2, _2p= 3, _3s= 0, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '0', density= '0.001251', electronegativity= '3.0', melt= '-210.0', boil= '-195.795', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '-146.89', p_crit= '33.54', valence= '5 4 3 2 1 -1 -2 -3', a_radius= '56')
O = dict(id= 8, symbol= 'O', name= 'Oxygen', atomic_number= 8, mass= '15.9994', period= 2, row= 2, column= 16, _group= '6A', protons= 8, neutrons= 8, electrons= 8, _1s= 2, _2s= 2, _2p= 4, _3s= 0, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-141', density= '0.001429', electronegativity= '3.5', melt= '-218.79', boil= '-182.962', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '-118.38', p_crit= '50.14', valence= '-1 -2', a_radius= '48')
F = dict(id= 9, symbol= 'F', name= 'Fluorine', atomic_number= 9, mass= '18.9984032', period= 2, row= 2, column= 17, _group= '7A', protons= 9, neutrons= 9, electrons= 9, _1s= 2, _2s= 2, _2p= 5, _3s= 0, _3p= 1, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-322', density= '0.001696', electronegativity= '4.0', melt= '-219.67', boil= '-188.11', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '-128.74', p_crit= '5.1724', valence= '-1', a_radius= '42')
Ne = dict(id= 10, symbol= 'Ne', name= 'Neon', atomic_number= 10, mass= '20.1797', period= 2, row= 2, column= 18, _group= '8A', protons= 10, neutrons= 10, electrons= 10, _1s= 2, _2s= 2, _2p= 6, _3s= 0, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '30', density= '0.000900', electronegativity= '0.0', melt= '-248.59', boil= '-246.046', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '-228.6580', p_crit= '26.86', valence= '0', a_radius= '38')
Na = dict(id= 11, symbol= 'Na', name= 'Sodium', atomic_number= 11, mass= '22.989770', period= 3, row= 3, column= 1, _group= '1A', protons= 11, neutrons= 11, electrons= 11, _1s= 2, _2s= 2, _2p= 6, _3s= 1, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-53', density= '0.968', electronegativity= '0.9', melt= '97.794', boil= '882.940', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '2300', p_crit= '35', valence= '1', a_radius= '190')
Mg = dict(id= 12, symbol= 'Mg', name= 'Magnesium', atomic_number= 12, mass= '24.3050', period= 3, row= 3, column= 2, _group= '2A', protons= 12, neutrons= 12, electrons= 12, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '230', density= '1.738', electronegativity= '1.2', melt= '650', boil= '1090', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= '2', a_radius= '145')
Al = dict(id= 13, symbol= 'Al', name= 'Aluminum', atomic_number= 13, mass= '26.981538', period= 3, row= 3, column= 13, _group= '3A', protons= 13, neutrons= 13, electrons= 13, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 1, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-44', density= '2.7', electronegativity= '1.5', melt= '660.323', boil= '2519', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '6427', p_crit= 'NULL', valence= '3', a_radius= '118')
Si = dict(id= 14, symbol= 'Si', name= 'Silicon', atomic_number= 14, mass= '28.0855', period= 3, row= 3, column= 14, _group= '4A', protons= 14, neutrons= 14, electrons= 14, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 2, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-120', density= '2.330', electronegativity= '1.8', melt= '1414', boil= '3265', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= '4', a_radius= '111')
P = dict(id= 15, symbol= 'P', name= 'Phosphorus', atomic_number= 15, mass= '30.973761', period= 3, row= 3, column= 15, _group= '5A, 7A', protons= 15, neutrons= 15, electrons= 15, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 3, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-74', density= '1.823', electronegativity= '2.1', melt= '44.15 579.2', boil= '280.5 431', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '721', p_crit= 'NULL', valence= '5 3 -3', a_radius= '98')
S = dict(id= 16, symbol= 'S', name= 'Sulfur', atomic_number= 16, mass= '32.065', period= 3, row= 3, column= 16, _group= '6A', protons= 16, neutrons= 16, electrons= 16, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 4, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-201', density= '1.960', electronegativity= '2.5', melt= '95.2 115.21', boil= '4461', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '1041', p_crit= 'NULL', valence= '6 4 -2', a_radius= '88')
Cl = dict(id= 17, symbol= 'Cl', name= 'Chlorine', atomic_number= 17, mass= '35.453', period= 3, row= 3, column= 17, _group= '7A', protons= 17, neutrons= 17, electrons= 17, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 5, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-348', density= '0.003214', electronegativity= '3.0', melt= '-101.5', boil= '-34.03', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '143.9', p_crit= '78.1', valence= '7 5 3 1 -1', a_radius= '79')
Ar = dict(id= 18, symbol= 'Ar', name= 'Argon', atomic_number= 18, mass= '39.948', period= 3, row= 3, column= 18, _group= '8A', protons= 18, neutrons= 18, electrons= 18, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '35', density= '0.001784', electronegativity= '0.0', melt= '-189.34', boil= '-185.854', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '-122.463', p_crit= '4.863', valence= '0', a_radius= '71')
K = dict(id= 19, symbol= 'K', name= 'Potassium', atomic_number= 19, mass= '39.0983', period= 4, row= 4, column= 1, _group= '1A', protons= 19, neutrons= 19, electrons= 19, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 1, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-48', density= '0.856', electronegativity= '0.8', melt= '63.5', boil= '759', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '1950', p_crit= '16', valence= '1', a_radius= '243')
Ca = dict(id= 20, symbol= 'Ca', name= 'Calcium', atomic_number= 20, mass= '40.078', period= 4, row= 4, column= 2, _group= '2A', protons= 20, neutrons= 20, electrons= 20, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 0, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '150', density= '1.550', electronegativity= '1.0', melt= '842', boil= '1484', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= '2', a_radius= '194')
Sc = dict(id= 21, symbol= 'Sc', name= 'Scandium', atomic_number= 21, mass= '44.955910', period= 4, row= 4, column= 3, _group= '3B', protons= 21, neutrons= 21, electrons= 21, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 1, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '2.985', electronegativity= '1.3', melt= '1541', boil= '2836', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= 'NULL', a_radius= '184')
Ti = dict(id= 22, symbol= 'Ti', name= 'Titanium', atomic_number= 22, mass= '47.867', period= 4, row= 4, column= 4, _group= '4B', protons= 22, neutrons= 22, electrons= 22, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 2, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '4.507', electronegativity= '1.5', melt= '1670', boil= '3287', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= 'NULL', a_radius= '176')
V = dict(id= 23, symbol= 'V', name= 'Vanadium', atomic_number= 23, mass= '50.9415', period= 4, row= 4, column= 5, _group= '5B', protons= 23, neutrons= 23, electrons= 23, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 3, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '6.110', electronegativity= '1.6', melt= '1910', boil= '3407', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= 'NULL', a_radius= '171')
Cr = dict(id= 24, symbol= 'Cr', name= 'Chromium', atomic_number= 24, mass= '51.9961', period= 4, row= 4, column= 6, _group= '6B', protons= 24, neutrons= 24, electrons= 24, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 1, _3d= 5, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '7.140', electronegativity= '1.6', melt= '1907', boil= '2671', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= 'NULL', a_radius= '166')
Mn = dict(id= 25, symbol= 'Mn', name= 'Manganese', atomic_number= 25, mass= '54.938049', period= 4, row= 4, column= 7, _group= '7B', protons= 25, neutrons= 25, electrons= 25, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 5, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '7.470', electronegativity= '1.5', melt= '1246', boil= '2061', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '4052', p_crit= 'NULL', valence= 'NULL', a_radius= '161')
Fe = dict(id= 26, symbol= 'Fe', name= 'Iron', atomic_number= 26, mass= '55.845', period= 4, row= 4, column= 8, _group= '8B', protons= 26, neutrons= 26, electrons= 26, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 6, _4p= 2, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '7.874', electronegativity= '1.8', melt= '1538', boil= '2861', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '9067', p_crit= 'NULL', valence= 'NULL', a_radius= '156')
Co = dict(id= 27, symbol= 'Co', name= 'Cobalt', atomic_number= 27, mass= '58.9932', period= 4, row= 4, column= 9, _group= '8B', protons= 27, neutrons= 27, electrons= 27, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 7, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '8.9', electronegativity= '1.9', melt= '1495', boil= '2927', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= 'NULL', a_radius= '152')
Ni = dict(id= 28, symbol= 'Ni', name= 'Nickel', atomic_number= 28, mass= '58.6934', period= 4, row= 4, column= 10, _group= '8B', protons= 28, neutrons= 28, electrons= 28, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 8, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '8.908', electronegativity= '1.9', melt= '1455', boil= '2913', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= 'NULL', a_radius= '149')
Cu = dict(id= 29, symbol= 'Cu', name= 'Copper', atomic_number= 29, mass= '63.546', period= 4, row= 4, column= 11, _group= '1B', protons= 29, neutrons= 29, electrons= 29, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 1, _3d= 10, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '8.920', electronegativity= '1.9', melt= '1084.62', boil= '2560', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= 'NULL', a_radius= '145')
Zn = dict(id= 30, symbol= 'Zn', name= 'Zinc', atomic_number= 30, mass= '65.409', period= 4, row= 4, column= 12, _group= '2B', protons= 30, neutrons= 30, electrons= 30, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 0, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '7.140', electronegativity= '1.6', melt= '419.527', boil= '907', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= '2', a_radius= '142')
Ga = dict(id= 31, symbol= 'Ga', name= 'Gallium', atomic_number= 31, mass= '69.723', period= 4, row= 4, column= 13, _group= '3A', protons= 31, neutrons= 31, electrons= 31, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 1, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-40', density= '5.904', electronegativity= '1.6', melt= '29.7646', boil= '2229', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'NULL', p_crit= 'NULL', valence= '3', a_radius= '136')
Ge = dict(id= 32, symbol= 'Ge', name= 'Germanium', atomic_number= 32, mass= '72.64', period= 4, row= 4, column= 14, _group= '4A', protons= 32, neutrons= 32, electrons= 32, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 2, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-116', density= '5.323', electronegativity= '1.8', melt= '938.25', boil= '2833', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '4', a_radius= '125')
As = dict(id= 33, symbol= 'As', name= 'Arsenic', atomic_number= 33, mass= '74.92160', period= 4, row= 4, column= 15, _group= '5A', protons= 33, neutrons= 33, electrons= 33, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 3, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-77', density= '5.727', electronegativity= '2.0', melt= '817', boil= '616', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '5 3 -3', a_radius= '114')
Se = dict(id= 34, symbol= 'Se', name= 'Selenium', atomic_number= 34, mass= '778.96', period= 4, row= 4, column= 16, _group= '6A', protons= 34, neutrons= 34, electrons= 34, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 4, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-195', density= '4.819', electronegativity= '2.4', melt= '220.8', boil= '685', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '6 4 -2', a_radius= '103')
Br = dict(id= 35, symbol= 'Br', name= 'Bromine', atomic_number= 35, mass= '79.904', period= 4, row= 4, column= 17, _group= '7A', protons= 35, neutrons= 35, electrons= 35, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 5, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-324', density= '3.120', electronegativity= '2.8', melt= '-7.2', boil= '58.8', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '7 5 3 1 -1', a_radius= '94')
Kr = dict(id= 36, symbol= 'Kr', name= 'Krypton', atomic_number= 36, mass= '83.798', period= 4, row= 4, column= 18, _group= '8A', protons= 36, neutrons= 36, electrons= 36, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 0, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '40', density= '0.00375', electronegativity= '0', melt= '-157.37', boil= '-153.415', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '4 2', a_radius= '88')
Rb = dict(id= 37, symbol= 'Rb', name= 'Rubidium', atomic_number= 37, mass= '85.4678', period= 5, row= 5, column= 1, _group= '1A', protons= 37, neutrons= 37, electrons= 37, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 0, _5s= 1, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-46', density= '1.532', electronegativity= '0.8', melt= '39.30', boil= '688', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '1', a_radius= '265')
Sr = dict(id= 38, symbol= 'Sr', name= 'Strontium', atomic_number= 38, mass= '87.62', period= 5, row= 5, column= 2, _group= '2A', protons= 38, neutrons= 38, electrons= 38, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 0, _5s= 2, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '160', density= '2.630', electronegativity= '1.0', melt= '777', boil= '1377', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '2', a_radius= '219')
Y = dict(id= 39, symbol= 'Y', name= 'Yttrium', atomic_number= 39, mass= '88.90585', period= 5, row= 5, column= 3, _group= '3B', protons= 39, neutrons= 39, electrons= 30, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 1, _5s= 2, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '4.472', electronegativity= '1.2', melt= '1522', boil= '3345', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= 'NULL', a_radius= '212')
Zr = dict(id= 40, symbol= 'Zr', name= 'Zirconium', atomic_number= 40, mass= '91.224', period= 5, row= 5, column= 4, _group= '4B', protons= 40, neutrons= 40, electrons= 40, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 2, _5s= 2, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '6.511', electronegativity= '1.4', melt= '1854', boil= '4406', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= 'NULL', a_radius= '206')
Nb = dict(id= 41, symbol= 'Nb', name= 'Niobium', atomic_number= 41, mass= '92.90638', period= 5, row= 5, column= 5, _group= '5B', protons= 41, neutrons= 41, electrons= 41, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 4, _5s= 1, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '8.570', electronegativity= '1.6', melt= '2477', boil= '4741', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= 'NULL', a_radius= '198')
Mo = dict(id= 42, symbol= 'Mo', name= 'Molybdenum', atomic_number= 42, mass= '95.94', period= 5, row= 5, column= 6, _group= '6B', protons= 42, neutrons= 42, electrons= 42, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 5, _5s= 1, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '10.280', electronegativity= '1.8', melt= '2622', boil= '4639', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= 'NULL', a_radius= '190')
Tc = dict(id= 43, symbol= 'Tc', name= 'Technetium', atomic_number= 43, mass= '98', period= 5, row= 5, column= 7, _group= '7B', protons= 43, neutrons= 43, electrons= 43, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 6, _5s= 1, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '11.5', electronegativity= '1.9', melt= '2157', boil= '4262', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= 'NULL', a_radius= '183')
Ru = dict(id= 44, symbol= 'Ru', name= 'Ruthenium', atomic_number= 44, mass= '101.07', period= 5, row= 5, column= 8, _group= '8B', protons= 44, neutrons= 44, electrons= 44, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 7, _5s= 1, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '12.370', electronegativity= '2.2', melt= '2333', boil= '4147', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= 'NULL', a_radius= '178')
Rh = dict(id= 45, symbol= 'Rh', name= 'Rhodium', atomic_number= 45, mass= '102.90550', period= 5, row= 5, column= 9, _group= '8B', protons= 45, neutrons= 45, electrons= 45, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 8, _5s= 1, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '12.450', electronegativity= '2.2', melt= '1963', boil= '3695', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= 'NULL', a_radius= '173')
Pd = dict(id= 46, symbol= 'Pd', name= 'Palladium', atomic_number= 46, mass= '106.42', period= 5, row= 5, column= 10, _group= '8B', protons= 46, neutrons= 46, electrons= 46, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 0, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '12.023', electronegativity= '2.2', melt= '1554.8', boil= '2963', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= 'NULL', a_radius= '169')
Ag = dict(id= 47, symbol= 'Ag', name= 'Silver', atomic_number= 47, mass= '107.8682', period= 5, row= 5, column= 11, _group= '1B', protons= 47, neutrons= 47, electrons= 47, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 1, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '10.490', electronegativity= '1.9', melt= '961.78', boil= '2162', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= '6137', p_crit= 'Press Crit', valence= 'NULL', a_radius= '165')
Cd = dict(id= 48, symbol= 'Cd', name= 'Cadmium', atomic_number= 48, mass= '112.411', period= 5, row= 5, column= 12, _group= '2B', protons= 48, neutrons= 48, electrons= 48, _1s= 2, _2s= 2, _2p= 6, _3s= 2, _3p= 6, _4s= 2, _3d= 10, _4p= 6, _4d= 10, _5s= 2, _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= 'NULL', density= '8.650', electronegativity= '1.7', melt= '321.069', boil= '767', e_fusion= 'E Fusion', e_vapor= 'E Vapor', t_crit= 'Temp Crit', p_crit= 'Press Crit', valence= '2', a_radius= '161')

db = {}
db['H'] = H
db['He'] = He
db['Li'] = Li
db['Be'] = Be
db['B'] = B
db['C'] = C
db['N'] = N
db['O'] = O
db['F'] = F
db['Ne'] = Ne
db['Na'] = Na
db['Mg'] = Mg
db['Al'] = Al
db['Si'] = Si
db['P'] = P
db['S'] = S
db['Cl'] = Cl
db['Ar'] = Ar
db['K'] = K
db['Ca'] = Ca
db['Sc'] = Sc
db['Ti'] = Ti
db['V'] = V
db['Cr'] = Cr
db['Mn'] = Mn
db['Fe'] = Fe
db['Co'] = Co
db['Ni'] = Ni
db['Cu'] = Cu
db['Zn'] = Zn
db['Ga'] = Ga
db['Ge'] = Ge
db['As'] = As
db['Se'] = Se
db['Br'] = Br
db['Kr'] = Kr
db['Rb'] = Rb
db['Sr'] = Sr
db['Y'] = Y
db['Zr'] = Zr
db['Nb'] = Nb
db['Mo'] = Mo
db['Tc'] = Tc
db['Ru'] = Ru
db['Rh'] = Rh
db['Pd'] = Pd
db['Ag'] = Ag
db['Cd'] = Cd

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

'''
The following is a first guess at what an eci dictiionary will contain. It includes all the items for the first eci.
Similar dictionaries will be needed for each other eci.
Also, all the other process items will be added to all these dictionaries to create a database record of the step
of the process.
eci_db = {}
d_eci_1 = dict(id= 1, eci_1_type= '', eci_1= '', eci_1_name= '', eci_1_mass= '', eci_1_column= '', eci_1_valence= '',
               eci_1_units= '', eci_1_qty= '', eci_1_moles= '', eci_1_temp_units= '', eci_1_temp_qty= '',
               eci_1_press_units= '', eci_1_press_qty= '')
eci_db['d_eci_1'] = d_eci_1
'''
c_db = {}
Na2SO4 = dict(formula= 'Na2SO4', name= 'sodium sulfate', elements= 'NaSO')
c_db['Na2SO4'] = Na2SO4
 # *** End constants and variables


# *** Start function descriptions
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
            print('eci_1_valence is:', eci_1_valence[0])

        elif eci_1_group == '7A':
            if cb_2_type == 'elements':
                eci_2 = cb_eci_2.get()
                eci_2_electronegativity = db[eci_2]['electronegativity']
                if eci_2_electronegativity > eci_1_electronegativity:
                    eci_2_valence= -1
                    print('eci_2_valence is:', eci_2_valence[0])
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
                                print('eci_2_valence is ', eci_2_valence)
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

# Make new dictionaries of elements, compounds and ions to ensure they are current.
# Also, if the data is changed in a dictionary, it needs to be changed in the database.
# Current, data will be changed in a dictionary and then changed in the database.
# Make new alpha lists of compounds and ions to ensure they are current.
# An alpha dictionary/list is a list of compound (or ion) elements in alphabetic order and a list of the compounds or ions 
# that have the same list of elements. After a set of elements have been chosen and alphabetized, these lists will be used
#  to determine which compounds have these elements, and that list will be used to fill the appropriate combo box
def make_element_dictionary():
    pass
def make_compound_dictionary():
    pass
def make_ion_dictionary():
    pass
def make_compound_alpha_dictionary():
    pass
def make_ion_alpha_dictionary():
    pass
    #a_list = [eci_1, eci_2, eci_3]
    #alpha = (sorted(a_list)) #Does not concatenate
    #beta = alpha(0) + alpha(1) + alpha(2)
    #print('In AlphabetizeElements', alpha)
    #print('In AlphabetizeElements', sorted(alpha))
'''
    #rtb_Explanation.Text = rtb_Explanation.Text & strAlphaElement
'''
# *** End function descriptions

# *** Start GUI layout
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
lbl_Select_Process.grid(row=7, column=0)   #, columnspan=2)
lbl_Select_Process.config(font=titlefont)
cb_Select_Process = Combobox(root, values=process_list, textvariable=process_selected, width=12)   #, width=30)
cb_Select_Process.grid(row=7, column=1)   #, columnspan=2)
cb_Select_Process.config(font=entryfont)
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
# *** End GUI layout

if __name__ == '__main__':
    make_element_dictionary()
    make_compound_dictionary()
    make_ion_dictionary()
    make_compound_alpha_dictionary()
    make_ion_alpha_dictionary()
    root.mainloop()


'''
        eci_1_name = c_db[eci_1]['name']
        eci_1_col = db[eci_1]['column']
        eci_1_mass = db[eci_1]['mass']
        eci_1_valence = db[eci_1]['valence']
        print("db[eci_1]['name'] is ", eci_1_name)
        print("db[eci_1]['column'] is ", eci_1_col)
        print("db[eci_1]['mass'] is ", eci_1_mass)
        print("db[eci_1]['valence'] is ", eci_1_valence)
        #print(eci_1_valence)   # Prints out the variable #str(eci_1).affinity
        #elif cb_1_type == 'compounds':
        #eci_1 = cb_eci_1.get()
        #print('eci_1 = ', eci_1)
        #    print("Error in Oxidization_Reduction eci_1 can't process compounds yet")
        #if eci_1 == 'H':
        #eci_temp_1_qty =  H['mass']
        #eci_temp_1_qty = db['H']['mass']   # db[H]['mass']
'''
