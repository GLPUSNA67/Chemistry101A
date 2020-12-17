from tkinter import *  # get widget classes
from tkinter.ttk import Combobox #,Textbox
from tkinter.messagebox import *  # get standard dialogs

root = Tk()

titlefont= ('Ariel', 15, 'bold')
labelfont= ('Ariel', 12) #, 'bold')
buttonfont= ('Ariel', 12) #, 'bold')
entryfont= ('Ariel', 12) #, 'bold')

unit_values = "Moles grams kilograms ounces pounds liters(l) liters(g) ml(l) ml(g)"
elements = "Ac Ag Al Am Ar As At Au B Ba Be Bi Bk Br C Ca Cd Ce Cf Cl Cm Co Cr "
elements = elements + "Cs Cu Dy Er Es Eu F Fe Fm Fr Ga Gd Ge H He Hf Hg Ho I In Ir K Kr "
elements = elements + "La Li Lu M Mn Mo N Na Nb Nd Ne Ni Np O Os P Pa Pb Pd Pm Po Pr "
elements = elements + "Pt Pu Ra Rb Re Rh Rn  Ru S Sb Sc Se Si Sm Sn Sr Ta Tb Tc Te Th Ti "
elements = elements + "Ti Tm U V W Xe Y Yb Zn Zr "

compound_values = "Al4C3 2HBr CaI Ca(OH)2 Ca3P2 CdS CH3CO2H CO CO2 CsF CuS FeCl2 FeCl3 GaBr3 "
compound_values = compound_values + "HgO Hg2O HNO2 HNO3 H2CO3 H2SO3 H2SO4 H3PO4 HC2H3O2 HCl HClO4"
compound_values = compound_values + "HF HI H2S LiCl K2SO4 Kbr KOH Mg3N2 NaCl NaOH Na2O NH3 "
compound_values = compound_values + "NO2 N2O4 N2O5 H2O ZnO ZnCO3"
process ="synthesis metathesis refine oxidize"
compound_symbols_list = "Al4C3 Ar2He2Kr2Ne2Xe2Rn2 BCl3 CH4 C2H6 C3H8 C4H10 C4H10_M C5H12 C6H14 C7H16 C8H18 " \
                        "C9H20 C10H22 C14H30 C18H38 CaH2PO4 CaI CaOH2 Ca3P2 CdS CsF C6H8O7 CH3CO2H C2H4COH " \
                        "CO CO2 HBr_g HBr_aq HC2H3O2 HCl HCl_g HCl_aq HClO4 HCN H2CO3 HF_g HF_aq HI_g HI_aq " \
                        "HNO2 HNO3 H3PO4 H2S_g H2S_aq H2SO3 H2SO4 IF7 KBr KOH LiCl Mg3N2 NaCl NaHCO3 Na2O NaOH " \
                        "NH3 N2H4 NO NO2 N2O4 N2O N2O5 PF5 SO2 SO3"
compound_names_list = "aluminum_carbide air boron_trichloride methane ethane propane butane 2-methylpropane" \
                      " pentane hexane heptane octane nonane decane tetradecane octadecane calcium_dihydrogen_phosphate" \
                      " calcium_iodide calcium_hydroxide calcium_phosphide cadmium_sulfide cesium_fluoride citric_acid" \
                      " acetic_acid acetic_acid carbon_monoxide carbon_dioxide hydrogen_bromide hydrobromic_acid" \
                      " acetic_acid hydrogen_chloride hydrogen_chloride hydrochloric_acid perchloric_acid hydrogen_cyanide" \
                      " carbonic_acid hydrogen_fluoride hydrofluoric_acid hydrogen_iodide hydroiodic_acid nitrous_acid" \
                      " nitric_acid phosphoric_acid hydrogen_suflide hydrosulfuric_acid sulfurous_acid sulfuric_acid" \
                      " iodine_heptafluoride potassium_bromide potassium_hydroxide lithium_chloride magnesium_nitride" \
                      " sodium_chloride bicarbonate_of_soda sodium_oxide sodium_hydroxide ammonia hydrazine nitric_oxide" \
                      " nitorgen_dioxide dinitrogen_tetroxide nitrous_oxide dinitrogen_pentoxide phosphorus_pentafluoride" \
                      " sulfur_dioxide sulfur_trioxide"

des_list = {"AlC": "[Al4C3]", "Ar2He2Kr2Ne2Xe2Rn2": "[Ar2He2Kr2Ne2Xe2Rn2]", "BCl": "[BCl3]",
                "CH": ["CH4", "C2H6", "C3H8", "C4H10", "C4H10_M", "C5H12", "C6H14", "C7H16", "C8H18",
                "C9H20", "C10H22", "C14H30", "C18H38"]}

process_list = "Synthesis Decompose Refine Metathesis Oxidization Reduction"
equipment = "refinery blah1 blah2"
energy_type = "heat electricity"
catalyst = "blah1 blah2 blah3 blah4"
side_effects = "air_polution water_polution land_polution"
by_products = "CO CO2 NO NO2"
equipment_selected = ""
energy_type_selected = ""
catalyst_selected = ""
side_effects_selected = ""
by_products_selected = ""

ECI_Types = "Element Compound Ion"
element1 = StringVar()
#el1 = element1.get()
eci_qty = StringVar()
#eci_qty.set(element1)

def set_element1():
    element1 = StringVar()
    el1 = element1.get()
    eci_qty = StringVar()
    eci_qty.set(element1)
    #eci_qty = StringVar()
    #eci1_qty = element1
    #pass       # The following does not get or set element1
    #e1 = element1.get()
    print('In process Set_Element. Element 1 is: ', el1)

def makeform(root):
    pass


if __name__ == '__main__':
    #make_Title_Frame('Chemistry')

    #root = Tk()
    root.title('Chemistry')
    makeform(root)
    root.bind('<Return>', lambda event: set_element1())
    mainloop()

'''
compound_values = "Al4C3 2HBr CaI Ca(OH)2 Ca3P2 CdS CH3CO2H CO CO2 CsF CuS FeCl2 FeCl3 GaBr3 "
compound_values = compound_values + "HgO Hg2O HNO2 HNO3 H2CO3 H2SO3 H2SO4 H3PO4 HC2H3O2 HCl HClO4"
compound_values = compound_values + "HF HI H2S LiCl K2SO4 Kbr KOH Mg3N2 NaCl NaOH Na2O NH3 "
compound_values = compound_values + "NO2 N2O4 N2O5 H2O ZnO ZnCO3"
'''
