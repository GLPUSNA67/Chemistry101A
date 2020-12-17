from tkinter import *  # get widget classes
from tkinter.ttk import Combobox #,Textbox
from tkinter.messagebox import *  # get standard dialogs
import tkinter as tk
#import element *

root = Tk()
root.title('Chemistry')
titlefont= ('Ariel', 14, 'bold')
labelfont= ('Ariel', 12) #, 'bold')
buttonfont= ('Ariel', 12) #, 'bold')
entryfont= ('Ariel', 12) #, 'bold')

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

'''
def callback_print_vars():             #eventObject
    eci_1 = cb_eci_1.get()
    eci_1_units = cb_eci_1_units.get()
    eci_1_qty = e_eci_1_qty.get()
    eci_1_M_qty = e_eci_1_M_qty.get()
    eci_2 = cb_eci_2.get()
    eci_2_units = cb_eci_2_units.get()
    eci_2_qty = e_eci_2_qty.get()
    eci_2_M_qty = e_eci_2_M_qty.get()

    eci_4 = cb_eci_4.get()
    eci_4_units = cb_eci_4_units.get()
    eci_4_qty = e_eci_4_qty.get()
    eci_4_M_qty = e_eci_4_M_qty.get()
    eci_5 = cb_eci_5.get()
    eci_5_units = cb_eci_5_units.get()
    eci_5_qty = e_eci_5_qty.get()
    eci_5_M_qty = e_eci_5_M_qty.get()
    #eciRadio1 = radio1.get()   #eciRadio1.set(0)
    #print(radio1)
    #print('eciRadio1 = ', eciRadio1)

    for var in variables:
        print(var)

    print('eci_1 = ', eci_1)
    print('eci_1_units = ', eci_1_units)
    print('eci_1_qty = ',eci_1_qty)
    print('eci_1_M_qty = ', eci_1_M_qty)
    print('eci_2 = ', eci_2)
    print('eci_2_units = ', eci_2_units)
    print('eci_2_qty = ', eci_2_qty)
    print('eci_2_M_qty = ', eci_2_M_qty)
    print('eci_4 = ',eci_4)
    print('eci_4_units = ', eci_4_units)
    print('eci_4_qty = ', eci_4_qty)
    print('eci_4_M_qty = ', eci_4_M_qty)
    print('eci_5 = ', eci_5)
    print('eci_5_units = ', eci_5_units)
    print('eci_5_qty = ',eci_5_qty)
    print('eci_5_M_qty = ', eci_5_M_qty)
    print('5 times eci_1_qty = ', 5* float(eci_1_qty))


    #eci_temp_1_units = eci_temp_1_units.get()  eci_temp_1_qty
    print('eci_temp_1_units = ', eci_temp_1_units.get())
    print('eci_temp_1_qty = ', eci_temp_1_qty.get())
    print('eci_press_1_units = ', eci_press_1_units.get())
    print('eci_press_1_units = ', eci_press_1_qty.get())

def Decompose():
    pass
    #print(eci_1_qty)
    #print(eci_1_M_qty)
    #callback_eci_1_qty()
    #print("break")
    #callback_eci_1_M_qty()
    #callback_eci_2_qty()
    #callback_eci_4_qty()

'''
# cb_Elements1.bind("<<ComboboxSelected>>", callback_E1)
element1 = StringVar()
eci_1 = StringVar()
eci_2 = StringVar()
eci_3 = StringVar()
eci_4 = StringVar()
eci_5 = StringVar()
eci_6 = StringVar()
eci_1_M = StringVar()
eci_2_M = StringVar()
eci_3_M = StringVar()
eci_4_M = StringVar()
eci_5_M = StringVar()
eci_6_M = StringVar()

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

process = "Mine Refine Make Use Purify "
temp_umits = "K C F"
press_umits = "ATM torr psi hg"

lbl_Title = Label(root, text="Chemistry")
lbl_Title.pack(side=TOP)
lbl_Title.config(font=titlefont)

lbl_blank = Label(root, text="")
lbl_blank.pack(side=TOP)
lbl_blank.config(font=labelfont)

#class file_ops(Frame):
#    def __init__(self, parent=None):
#        self.grid(row=1, column=1, columnspan=5)
lbl_record_create = Label(text="Create a record name:")
lbl_record_create.pack(side=LEFT)
lbl_record_create.config(font=labelfont)
e_recordname = Entry(root, text="", width=30)
e_recordname.pack(side=LEFT)
e_recordname.config(font=labelfont)

btn_create_record = Button(root, text = 'Create New Record')
btn_create_record.pack(side=LEFT)    # , expand=YES, fill=BOTH
btn_create_record.config(font=buttonfont)
lbl_blank = Label(root, text="")
lbl_blank.pack(side=LEFT, expand=YES, fill=BOTH)
lbl_blank.config(font=labelfont)
lbl_blank = Label(root, text="")
lbl_blank.pack(side=RIGHT, expand=YES, fill=BOTH)
lbl_blank.config(font=labelfont)
lbl_blank = Label(root, text="")
lbl_blank.pack(side=TOP, expand=YES, fill=BOTH)
lbl_blank.config(font=labelfont)
lbl_recordname_instruction = Label(text="Record name form is: Formula_Process_Location_step_totalSteps: Such as: NaCl_Synthesis_Industry_1_2")
lbl_recordname_instruction.pack(side=LEFT)   #anchor=SW)
lbl_recordname_instruction.config(font=labelfont)
S = tk.Scrollbar(root)

lbl_blank = Label(root, text="")
lbl_blank.pack(side=TOP)
lbl_blank.config(font=labelfont)

'''
lbl_blank = Label(root, text="")
lbl_blank.grid(row=4, column=0, columnspan=1)
lbl_blank.config(font=labelfont)

lbl_record_ops = Label(text="Retrieve a record name:")
lbl_record_ops.grid(row=5, column=0, columnspan=2)
lbl_record_ops.config(font=labelfont)
cb_RecordName = Combobox(root, values=elements, width=30)
cb_RecordName.grid(row=5, column=2, columnspan=2)
cb_RecordName.config(font=entryfont)
#e_recordname = Entry(root, text="", width=30)
#e_recordname.grid(row=3, column=3)
#e_recordname.config(font=labelfont)
btn_create_record = Button(root, text = 'Get Existing Record')
btn_create_record.grid(row=5, column=4)
btn_create_record.config(font=buttonfont)
btn_update_record = Button(root, text = 'Update Record')
btn_update_record.grid(row=5, column=6)
btn_update_record.config(font=buttonfont)

lbl_blank = Label(root, text="")
lbl_blank.grid(row=6, column=0, columnspan=2)
lbl_blank.config(font=labelfont)

lbl_record_ops = Label(text="Look up compound:")
lbl_record_ops.grid(row=7, column=0, columnspan=1)
lbl_record_ops.config(font=labelfont)
cb_RecordName = Combobox(root, values=compound_values, width=20)
cb_RecordName.grid(row=7, column=1, columnspan=2)
cb_RecordName.config(font=entryfont)
lbl_record_ops = Label(text="Look up process:")
lbl_record_ops.grid(row=7, column=3, columnspan=1)
lbl_record_ops.config(font=labelfont)
cb_RecordName = Combobox(root, values=process, width=30)
cb_RecordName.grid(row=7, column=4, columnspan=2)
cb_RecordName.config(font=entryfont)

lbl_blank = Label(root, text="")
lbl_blank.grid(row=8, column=0, columnspan=2)
lbl_blank.config(font=labelfont)
lbl_record_ops = Label(text="*** Select process here ***")
lbl_record_ops.grid(row=8, column=3, columnspan=1)
lbl_record_ops.config(font=titlefont)
#  Create radio buttons which will determine contents of dropdown list boxes
variables = []
def radio1():
    #global eciRadio1
    eciRadio1 = IntVar()
    var = StringVar()
    #for i in range(10):
    radE = Radiobutton(root, text='Elements', variable='Elements', value='elements')
    radE.grid(row=10, column=0)
    radE.config(font=labelfont)
    radC = Radiobutton(root, text='Compounds', variable='Compounds', value='compounds')
    radC.grid(row=10, column=1)
    radC.config(font=labelfont)
    radI = Radiobutton(root, text='Ions', variable='Ions', value='ions')
    radI.grid(row=10, column=2)
    radI.config(font=labelfont)
    eciRadio1.set(0) # deselect all initially
    variables.append(var)
    #print("eciRadio1 is", eciRadio1)

def radio4():
    #global eciRadio1
    eciRadio4 = IntVar()
    var = StringVar()
    #for i in range(10):
    radE = Radiobutton(root, text='Elements', variable=var, value='elements')
    radE.grid(row=10, column=4)
    radE.config(font=labelfont)
    radC = Radiobutton(root, text='Compounds', variable=var, value='compounds')
    radC.grid(row=10, column=5)
    radC.config(font=labelfont)
    radI = Radiobutton(root, text='Ions', variable=var, value='ions')
    radI.grid(row=10, column=6)
    radI.config(font=labelfont)
    eciRadio4.set(1) # deselect all initially
    variables.append(var)
    #print("eciRadio4 is", eciRadio4)

def radio2():
    #global eciRadio1
    eciRadio2 = IntVar()
    var = StringVar()
    #for i in range(10):
    radE = Radiobutton(root, text='Elements', variable=var, value='elements')
    radE.grid(row=18, column=0)
    radE.config(font=labelfont)
    radC = Radiobutton(root, text='Compounds', variable=var, value='compounds')
    radC.grid(row=18, column=1)
    radC.config(font=labelfont)
    radI = Radiobutton(root, text='Ions', variable=var, value='ions')
    radI.grid(row=18, column=2)
    radI.config(font=labelfont)
    eciRadio2.set(2) # deselect all initially
    variables.append(var)
    #print("eciRadio2 is", eciRadio2)

def radio5():
    #global eciRadio1
    eciRadio5 = IntVar()
    var = StringVar()
    #for i in range(10):
    radE = Radiobutton(root, text='Elements', variable=var, value='elements')
    radE.grid(row=18, column=4)
    radE.config(font=labelfont)
    radC = Radiobutton(root, text='Compounds', variable=var, value='compounds')
    radC.grid(row=18, column=5)
    radC.config(font=labelfont)
    radI = Radiobutton(root, text='Ions', variable=var, value='ions')
    radI.grid(row=18, column=6)
    radI.config(font=labelfont)
    eciRadio5.set(1) # deselect all initially
    variables.append(var)
    #print("eciRadio5 is", eciRadio5)

def Synthesis(variables):
    #radio1() #eciRadio5.set(1)
    # print(element1)
#def fetch(variables):   #names, jobs, pay):    #variables,
    for variable in variables:
       print('Input => "%s"' % variable.get())

#radio1()
#radio2()
#radio4()
#radio5()

lbl_eci_1 = Label(root, text="Select Element, Compound or Ion items for ComboBox 1 ")
lbl_eci_1.grid(row=9, column=0, columnspan=2)
lbl_eci_1.config(font=labelfont)
btn_Select_CB1 = Button(root, command=Synthesis(variables), text = 'Elements')
btn_Select_CB1.grid(row=9, column=2)
btn_Select_CB1.config(font=buttonfont)
cb_Process = Combobox(root, values=process_list, width=20)
cb_Process.grid(row=9, column=3) # , columnspan=2
cb_Process.config(font=entryfont)
lbl_eci_4 = Label(root, text="Select Element, Compound or Ion items for ComboBox 4 ")   #Element, Compound or Ion number 4
lbl_eci_4.grid(row=9, column=4, columnspan=2)
lbl_eci_4.config(font=labelfont)
btn_Select_CB1 = Button(root, command=Synthesis(variables), text = 'Compounds')
btn_Select_CB1.grid(row=9, column=6)
btn_Select_CB1.config(font=buttonfont)


lbl_eci_1_qty = Label(root, text="Quantity 1", width=8)
lbl_eci_1_qty.grid(row=11, column=0)
lbl_eci_1_qty.config(font=labelfont)
lbl_eci_1_units = Label(root, text="Units 1", width=6)
lbl_eci_1_units.grid(row=11, column=1)
lbl_eci_1_units.config(font=labelfont)
lbl_eci_1 = Label(root, text="ECI 1")
lbl_eci_1.grid(row=11, column=2)
lbl_eci_1.config(font=labelfont)
btn_Continue = Button(root, text = 'Continue', command=callback_print_vars)
btn_Continue.grid(row=11, column=3)
btn_Continue.config(font=buttonfont)
lbl_eci_4_qty = Label(root, text="Quantity 4", width=8)
lbl_eci_4_qty.grid(row=11, column=4, padx=4)
lbl_eci_4_qty.config(font=labelfont)
lbl_eci_4_units = Label(root, text="Units 4", width=8)
lbl_eci_4_units.grid(row=11, column=5, padx=4)
lbl_eci_4_units.config(font=labelfont)
lbl_eci_4 = Label(root, text="ECI 4", width=10)
lbl_eci_4.grid(row=11, column=6, padx=4)
lbl_eci_4.config(font=labelfont)
# e_eci_1_qty
e_eci_1_qty = Entry(root, text="", textvariable=eci_1_qty, width=8)
e_eci_1_qty.grid(row=12, column=0, padx=4)
e_eci_1_qty.config(font=entryfont)
#e_eci_1_qty.bind(callback_eci_1_qty)            #root, textvariable=user_input
cb_eci_1_units = Combobox(root, values=unit_values, textvariable=eci_1_units, width=8)
cb_eci_1_units.grid(row=12, column=1, padx=4)
cb_eci_1_units.config(font=entryfont)
#cb_eci_1_units.bind("<<ComboboxSelected>>", callback_eci_1_units)
cb_eci_1 = Combobox(root, values=compound_symbols_list,  textvariable=eci_1, width=30)
cb_eci_1.grid(row=12, column=2, padx=4)
cb_eci_1.config(font=entryfont)
#cb_eci_1.bind("<<ComboboxSelected>>", callback_eci_1)

e_eci_4_qty = Entry(root, text="CompoundQty 4", textvariable=eci_4_qty, width=8)
e_eci_4_qty.grid(row=12, column=4, padx=4)
e_eci_4_qty.config(font=entryfont)
cb_eci_4_units = Combobox(root, values=unit_values, textvariable=eci_4_units, width=8)
cb_eci_4_units.grid(row=12, column=5, padx=4)
cb_eci_4_units.config(font=entryfont)
#cb_eci_4_units.bind("<<ComboboxSelected>>", callback_eci_4_units)
cb_eci_4 = Combobox(root, values=compound_values, textvariable=eci_4, width=30)
cb_eci_4.grid(row=12, column=6, padx=4)
cb_eci_4.config(font=entryfont)
#cb_eci_4.bind("<<ComboboxSelected>>", callback_eci_4)

e_eci_1_M_qty = Entry(root, text="", textvariable=eci_1_M_qty, width=8)
e_eci_1_M_qty.grid(row=13, column=0, padx=4)
e_eci_1_M_qty.config(font=entryfont)

lbl_eci_1_units_M = Label(root, text="Moles", width=8)
lbl_eci_1_units_M.grid(row=13, column=1, padx=4)
lbl_eci_1_units_M.config(font=labelfont)
# cb_Elements1 = Combobox(root, values=elements, width=30)
cb_eci_1_M = Combobox(root, values=compound_names_list,  textvariable=eci_1_M, width=30)
cb_eci_1_M.grid(row=13, column=2, padx=4)
cb_eci_1_M.config(font=entryfont)
#cb_eci_1_M.bind("<<ComboboxSelected>>", callback_eci_1_M)

e_eci_4_M_qty = Entry(root, text="CompoundQty 4", textvariable=eci_4_M_qty, width=8)
e_eci_4_M_qty.grid(row=13, column=4, padx=4)
e_eci_4_M_qty.config(font=entryfont)
lbl_eci_4_units_M = Label(root, text="Moles", width=8)
lbl_eci_4_units_M.grid(row=13, column=5, padx=4)
lbl_eci_4_units_M.config(font=labelfont)
cb_eci_4_M = Combobox(root, values=compound_values, textvariable=eci_4_M, width=30)
cb_eci_4_M.grid(row=13, column=6, padx=4)
cb_eci_4_M.config(font=entryfont)

lbl_TU1 = Label(root, text="Temp Units", width=10)
lbl_TU1.grid(row=14, column=0)
lbl_TU1.config(font=labelfont)
lbl_TQ1 = Label(root, text="Temp Qty", width=10)
lbl_TQ1.grid(row=14, column=1)
lbl_TQ1.config(font=labelfont)
lbl_PU1 = Label(root, text="Press Units", width=10)
lbl_PU1.grid(row=14, column=2)
lbl_PU1.config(font=labelfont)
lbl_PQ1 = Label(root, text="Press Qty", width=10)
lbl_PQ1.grid(row=14, column=3)
lbl_PQ1.config(font=labelfont)

lbl_CTU1 = Label(root, text="Temp Units", width=10)
lbl_CTU1.grid(row=14, column=4)
lbl_CTU1.config(font=labelfont)
lbl_CTQ1 = Label(root, text="Temp Qty", width=10)
lbl_CTQ1.grid(row=14, column=5)
lbl_CTQ1.config(font=labelfont)
lbl_CPU1 = Label(root, text="Press Units", width=10)
lbl_CPU1.grid(row=14, column=6)
lbl_CPU1.config(font=labelfont)
lbl_CPQ1 = Label(root, text="Press Qty", width=10)
lbl_CPQ1.grid(row=14, column=7)
lbl_CPQ1.config(font=labelfont)

cb_Temp_Units_1 = Combobox(root, values=temp_umits, textvariable=eci_temp_1_units, width=12) # eci_temp_1_units
cb_Temp_Units_1.grid(row=15, column=0, padx=4)
cb_Temp_Units_1.config(font=entryfont)
#cb_Temp_Units_1.bind("<<ComboboxSelected>>", callback_eci_1_units())
e_Temp_Qty_1 = Entry(root, text="", textvariable=eci_temp_1_qty, width=12)
e_Temp_Qty_1.grid(row=15, column=1, padx=4)
e_Temp_Qty_1.config(font=entryfont)
cb_Press_Units_1 = Combobox(root, values=press_umits, textvariable=eci_press_1_units, width=12)
cb_Press_Units_1.grid(row=15, column=2, padx=4)
cb_Press_Units_1.config(font=entryfont)
#cb_Temp_Units_1.bind("<<ComboboxSelected>>", callback_eci_1_units())
e_Press_Qty_1 = Entry(root, text="", textvariable=eci_press_1_qty, width=12)
e_Press_Qty_1.grid(row=15, column=3, padx=4)
e_Press_Qty_1.config(font=entryfont)

cb_TU1 = Combobox(root, values=temp_umits, textvariable=eci_temp_4_units, width=12)
cb_TU1.grid(row=15, column=4, padx=4)
cb_TU1.config(font=entryfont)
e_TQ4 = Entry(root, text="", textvariable=eci_temp_4_qty, width=12)
e_TQ4.grid(row=15, column=5, padx=4)
e_TQ4.config(font=entryfont)
cb_PU4 = Combobox(root, values=press_umits, textvariable=eci_press_4_units, width=12)
cb_PU4.grid(row=15, column=6, padx=4)
cb_PU4.config(font=entryfont)
e_PQ4 = Entry(root, text="", textvariable=eci_press_4_qty, width=12)
e_PQ4.grid(row=15, column=7, padx=4)
e_PQ4.config(font=entryfont)

lbl_blank = Label(root, text="")
lbl_blank.grid(row=16, column=0, columnspan=2)
lbl_blank.config(font=labelfont)
#btn_Reduction = Button(root, command=Synthesis(variables), text = 'Reduction')
#btn_Reduction.grid(row=12, column=3)
'''
'''
lbl_eci_2 = Label(root, text="Element, Compound or Ion number 2.")
#btn_Reduction.config(font=buttonfont)
lbl_eci_2.grid(row=17, column=0, columnspan=2)
lbl_eci_2.config(font=labelfont)
lbl_eci_5 = Label(root, text="Element, Compound or Ion number 5.")
lbl_eci_5.grid(row=17, column=4, columnspan=2)
lbl_eci_5.config(font=labelfont)
'''
'''
lbl_eci_2 = Label(root, text="Select Element, Compound or Ion items for ComboBox 2 ")
lbl_eci_2.grid(row=17, column=0, columnspan=2)
lbl_eci_2.config(font=labelfont)
btn_Select_CB2 = Button(root, command=Synthesis(variables), text = 'Elements')
btn_Select_CB2.grid(row=17, column=2)
btn_Select_CB2.config(font=buttonfont)
lbl_eci_5 = Label(root, text="Select Element, Compound or Ion items for ComboBox 5 ")
lbl_eci_5.grid(row=17, column=4, columnspan=2)
lbl_eci_5.config(font=labelfont)
btn_Select_CB5 = Button(root, command=Synthesis(variables), text = 'Compounds')
btn_Select_CB5.grid(row=17, column=6)
btn_Select_CB5.config(font=buttonfont)

lbl_eci_2_qty = Label(root, text="Quantity 2", width=8)
lbl_eci_2_qty.grid(row=19, column=0)
lbl_eci_2_qty.config(font=labelfont)
lbl_eci_2_units = Label(root, text="Units 2", width=6)
lbl_eci_2_units.grid(row=19, column=1)
lbl_eci_2_units.config(font=labelfont)
lbl_eci_2 = Label(root, text="ECI 2")
lbl_eci_2.grid(row=19, column=2)
lbl_eci_2.config(font=labelfont)
lbl_eci_5_qty = Label(root, text="Quantity 5", width=8)
lbl_eci_5_qty.grid(row=19, column=4, padx=4)
lbl_eci_5_qty.config(font=labelfont)
lbl_eci_5_units = Label(root, text="Units 5", width=8)
lbl_eci_5_units.grid(row=19, column=5, padx=4)
lbl_eci_5_units.config(font=labelfont)
lbl_eci_5 = Label(root, text="ECI 5", width=10)
lbl_eci_5.grid(row=19, column=6, padx=4)
lbl_eci_5.config(font=labelfont)

e_eci_2_qty = Entry(root, text="", textvariable=eci_2_qty, width=8)
e_eci_2_qty.grid(row=20, column=0, padx=4)
e_eci_2_qty.config(font=entryfont)
# cb_Elements1.bind("<<ComboboxSelected>>", callback_E1)
cb_eci_2_units = Combobox(root, values=unit_values, textvariable=eci_2_units, width=8)
cb_eci_2_units.grid(row=20, column=1, padx=4)
cb_eci_2_units.config(font=entryfont)
#cb_eci_2_units.bind("<<ComboboxSelected>>", callback_eci_2_units)
cb_eci_2 = Combobox(root, values=elements,  textvariable=eci_2, width=30)
cb_eci_2.grid(row=20, column=2, padx=4)
cb_eci_2.config(font=entryfont)
#cb_eci_2.bind("<<ComboboxSelected>>", callback_eci_2)

e_eci_5_qty = Entry(root, text="", textvariable=eci_5_qty, width=8)
e_eci_5_qty.grid(row=20, column=4, padx=4)
e_eci_5_qty.config(font=entryfont)
cb_eci_5_units = Combobox(root, values=unit_values, textvariable=eci_5_units, width=8)
cb_eci_5_units.grid(row=20, column=5, padx=4)
cb_eci_5_units.config(font=entryfont)
cb_eci_5 = Combobox(root, values=compound_values, textvariable=eci_5, width=30)
cb_eci_5.grid(row=20, column=6, padx=4)
cb_eci_5.config(font=entryfont)

e_eci_2_M_qty = Entry(root, text=" ", width=8)
e_eci_2_M_qty.grid(row=21, column=0, padx=4)
e_eci_2_M_qty.config(font=entryfont, textvariable=eci_2_M_qty)
lbl_eci_2_units_M = Label(root, text="Moles", width=8)
lbl_eci_2_units_M.grid(row=21, column=1, padx=4)
lbl_eci_2_units_M.config(font=labelfont)
cb_eci_2_M = Combobox(root, values=compound_values,  textvariable=eci_2_M, width=30)
cb_eci_2_M.grid(row=21, column=2, padx=4)
cb_eci_2_M.config(font=entryfont)
e_eci_5_M_qty = Entry(root, text="CompoundQty 5", textvariable=eci_5_M_qty, width=8)
e_eci_5_M_qty.grid(row=21, column=4, padx=4)
e_eci_5_M_qty.config(font=entryfont)
lbl_eci_5_units_M = Label(root, text="Moles", width=8)
lbl_eci_5_units_M.grid(row=21, column=5, padx=4)
lbl_eci_5_units_M.config(font=labelfont)
cb_eci_5_M = Combobox(root, values=compound_values, textvariable=eci_5_M, width=30)
cb_eci_5_M.grid(row=21, column=6, padx=4)
cb_eci_5_M.config(font=entryfont)

lbl_TU2 = Label(root, text="Temp Units", width=10)
lbl_TU2.grid(row=22, column=0)
lbl_TU2.config(font=labelfont)
lbl_TQ2 = Label(root, text="Temp Qty", width=10)
lbl_TQ2.grid(row=22, column=1)
lbl_TQ2.config(font=labelfont)
lbl_PU2 = Label(root, text="Press Units", width=10)
lbl_PU2.grid(row=22, column=2)
lbl_PU2.config(font=labelfont)
lbl_PQ2 = Label(root, text="Press Qty", width=10)
lbl_PQ2.grid(row=22, column=3)
lbl_PQ2.config(font=labelfont)
lbl_CTU5 = Label(root, text="Temp Units", width=10) #, textvariable=eci_temp_5_units
lbl_CTU5.grid(row=22, column=4)
lbl_CTU5.config(font=labelfont)
lbl_CTQ5 = Label(root, text="Temp Qty", width=10) #, textvariable=eci_temp_5_qty
lbl_CTQ5.grid(row=22, column=5)
lbl_CTQ5.config(font=labelfont)
lbl_CPU5 = Label(root, text="Press Units", width=10) #, textvariable=eci_press_5_units
lbl_CPU5.grid(row=22, column=6)
lbl_CPU5.config(font=labelfont)
lbl_CPQ5 = Label(root, text="Press Qty", width=10) #, textvariable=eci_press_5_qty
lbl_CPQ5.grid(row=22, column=7)
lbl_CPQ5.config(font=labelfont)

cb_TU2 = Combobox(root, values=temp_umits, textvariable=eci_temp_2_units, width=12) #, textvariable=eci_temp_2_units
cb_TU2.grid(row=23, column=0, padx=4)
cb_TU2.config(font=entryfont)
e_TQ2 = Entry(root, text="", width=12)
e_TQ2.grid(row=23, column=1, padx=4)
e_TQ2.config(font=entryfont)
cb_PU2 = Combobox(root, values=press_umits, textvariable=eci_press_2_units, width=12)
cb_PU2.grid(row=23, column=2, padx=4)
cb_PU2.config(font=entryfont)
e_PQ2 = Entry(root, text="", width=12)
e_PQ2.grid(row=23, column=3, padx=4)
e_PQ2.config(font=entryfont)
cb_TU5 = Combobox(root, values=temp_umits, width=12)
cb_TU5.grid(row=23, column=4, padx=4)
cb_TU5.config(font=entryfont)
e_TQ5 = Entry(root, text="", width=12)
e_TQ5.grid(row=23, column=5, padx=4)
e_TQ5.config(font=entryfont)
cb_PU5 = Combobox(root, values=press_umits, width=12)
cb_PU5.grid(row=23, column=6, padx=4)
cb_PU5.config(font=entryfont)
e_PQ5 = Entry(root, text="", width=12)
e_PQ5.grid(row=23, column=7, padx=4)
e_PQ5.config(font=entryfont)
# *************************
lbl_blank = Label(root, text="")
lbl_blank.grid(row=25, column=0, columnspan=2)
lbl_blank.config(font=labelfont)

lbl_eci_3 = Label(root, text="Select Element, Compound or Ion items for ComboBox 3 ")
lbl_eci_3.grid(row=26, column=0, columnspan=2)
lbl_eci_3.config(font=labelfont)
btn_Select_CB3 = Button(root, command=Synthesis(variables), text = 'Elements')
btn_Select_CB3.grid(row=26, column=2)
btn_Select_CB3.config(font=buttonfont)
lbl_eci_6 = Label(root, text="Select Element, Compound or Ion items for ComboBox 6 ")
lbl_eci_6.grid(row=26, column=4, columnspan=2)
lbl_eci_6.config(font=labelfont)
btn_Select_CB6 = Button(root, command=Synthesis(variables), text = 'Compounds')
btn_Select_CB6.grid(row=26, column=6)
btn_Select_CB6.config(font=buttonfont)

lbl_eci_3_qty = Label(root, text="Quantity 3", width=8)
lbl_eci_3_qty.grid(row=27, column=0)
lbl_eci_3_qty.config(font=labelfont)
lbl_eci_3_units = Label(root, text="Units 3", width=6)
lbl_eci_3_units.grid(row=27, column=1)
lbl_eci_3_units.config(font=labelfont)
lbl_eci_3 = Label(root, text="ECI 3")
lbl_eci_3.grid(row=27, column=2)
lbl_eci_3.config(font=labelfont)
lbl_eci_6_qty = Label(root, text="Quantity 6", width=8)
lbl_eci_6_qty.grid(row=27, column=4, padx=4)
lbl_eci_6_qty.config(font=labelfont)
lbl_eci_6_units = Label(root, text="Units 6", width=8)
lbl_eci_6_units.grid(row=27, column=5, padx=4)
lbl_eci_6_units.config(font=labelfont)
lbl_eci_6 = Label(root, text="ECI 6", width=10)
lbl_eci_6.grid(row=27, column=6, padx=4)
lbl_eci_6.config(font=labelfont)

e_eci_3_qty = Entry(root, text="", textvariable=eci_3_qty, width=8)
e_eci_3_qty.grid(row=28, column=0, padx=4)
e_eci_3_qty.config(font=entryfont)
# cb_Elements1.bind("<<ComboboxSelected>>", callback_E1)
cb_eci_3_units = Combobox(root, values=unit_values, textvariable=eci_3_units, width=8)
cb_eci_3_units.grid(row=28, column=1, padx=4)
cb_eci_3_units.config(font=entryfont)
#cb_eci_2_units.bind("<<ComboboxSelected>>", callback_eci_2_units)
cb_eci_3 = Combobox(root, values=elements,  textvariable=eci_3, width=30)
cb_eci_3.grid(row=28, column=2, padx=4)
cb_eci_3.config(font=entryfont)
#cb_eci_2.bind("<<ComboboxSelected>>", callback_eci_2)

e_eci_6_qty = Entry(root, text="", textvariable=eci_6_qty, width=8)
e_eci_6_qty.grid(row=28, column=4, padx=4)
e_eci_6_qty.config(font=entryfont)
cb_eci_6_units = Combobox(root, values=unit_values, textvariable=eci_6_units, width=8)
cb_eci_6_units.grid(row=28, column=5, padx=4)
cb_eci_6_units.config(font=entryfont)
cb_eci_6 = Combobox(root, values=compound_values, textvariable=eci_6, width=30)
cb_eci_6.grid(row=28, column=6, padx=4)
cb_eci_6.config(font=entryfont)

e_eci_3_M_qty = Entry(root, text=" ", width=8)
e_eci_3_M_qty.grid(row=29, column=0, padx=4)
e_eci_3_M_qty.config(font=entryfont, textvariable=eci_3_M_qty)
lbl_eci_3_units_M = Label(root, text="Moles", width=8)
lbl_eci_3_units_M.grid(row=29, column=1, padx=4)
lbl_eci_3_units_M.config(font=labelfont)
cb_eci_3_M = Combobox(root, values=compound_values,  textvariable=eci_3_M, width=30)
cb_eci_3_M.grid(row=29, column=2, padx=4)
cb_eci_3_M.config(font=entryfont)
e_eci_6_M_qty = Entry(root, text="CompoundQty 6", textvariable=eci_6_M_qty, width=8)
e_eci_6_M_qty.grid(row=29, column=4, padx=4)
e_eci_6_M_qty.config(font=entryfont)
lbl_eci_6_units_M = Label(root, text="Moles", width=8)
lbl_eci_6_units_M.grid(row=29, column=5, padx=4)
lbl_eci_6_units_M.config(font=labelfont)
cb_eci_6_M = Combobox(root, values=compound_values, textvariable=eci_6_M, width=30)
cb_eci_6_M.grid(row=29, column=6, padx=4)
cb_eci_6_M.config(font=entryfont)

lbl_TU3 = Label(root, text="Temp Units", width=10)
lbl_TU3.grid(row=30, column=0)
lbl_TU3.config(font=labelfont)
lbl_TQ3 = Label(root, text="Temp Qty", width=10)
lbl_TQ3.grid(row=30, column=1)
lbl_TQ3.config(font=labelfont)
lbl_PU3 = Label(root, text="Press Units", width=10)
lbl_PU3.grid(row=30, column=2)
lbl_PU3.config(font=labelfont)
lbl_PQ3 = Label(root, text="Press Qty", width=10)
lbl_PQ3.grid(row=30, column=3)
lbl_PQ3.config(font=labelfont)
lbl_CTU6 = Label(root, text="Temp Units", width=10) #, textvariable=eci_temp_5_units
lbl_CTU6.grid(row=30, column=4)
lbl_CTU6.config(font=labelfont)
lbl_CTQ6 = Label(root, text="Temp Qty", width=10) #, textvariable=eci_temp_5_qty
lbl_CTQ6.grid(row=30, column=5)
lbl_CTQ6.config(font=labelfont)
lbl_CPU6 = Label(root, text="Press Units", width=10) #, textvariable=eci_press_5_units
lbl_CPU6.grid(row=30, column=6)
lbl_CPU6.config(font=labelfont)
lbl_CPQ6 = Label(root, text="Press Qty", width=10) #, textvariable=eci_press_5_qty
lbl_CPQ6.grid(row=30, column=7)
lbl_CPQ6.config(font=labelfont)

cb_TU3 = Combobox(root, values=temp_umits, textvariable=eci_temp_2_units, width=12) #, textvariable=eci_temp_2_units
cb_TU3.grid(row=31, column=0, padx=4)
cb_TU3.config(font=entryfont)
e_TQ3 = Entry(root, text="", width=12)
e_TQ3.grid(row=31, column=1, padx=4)
e_TQ3.config(font=entryfont)
cb_PU3 = Combobox(root, values=press_umits, textvariable=eci_press_2_units, width=12)
cb_PU3.grid(row=31, column=2, padx=4)
cb_PU3.config(font=entryfont)
e_PQ3 = Entry(root, text="", width=12)
e_PQ3.grid(row=31, column=3, padx=4)
e_PQ3.config(font=entryfont)
cb_TU6 = Combobox(root, values=temp_umits, width=12)
cb_TU6.grid(row=31, column=4, padx=4)
cb_TU6.config(font=entryfont)
e_TQ6 = Entry(root, text="", width=12)
e_TQ6.grid(row=31, column=5, padx=4)
e_TQ6.config(font=entryfont)
cb_PU6 = Combobox(root, values=press_umits, width=12)
cb_PU6.grid(row=31, column=6, padx=4)
cb_PU6.config(font=entryfont)
e_PQ6 = Entry(root, text="", width=12)
e_PQ6.grid(row=31, column=7, padx=4)
e_PQ6.config(font=entryfont)

lbl_blank = Label(root, text="")
lbl_blank.grid(row=32, column=0, columnspan=2)
lbl_blank.config(font=labelfont)

lbl_Explanation = Label(root, text="Explanation", width=10)
lbl_Explanation.grid(row=33, column=0) #, padx=8
lbl_Explanation.config(font=labelfont)
e_Explanation = Entry(root, text="", width=20) # , width=12
e_Explanation.grid(row=34, column=0) #, columnspan=8
e_Explanation.config(font=entryfont)

lbl_blank = Label(root, text="")
lbl_blank.grid(row=35, column=0, columnspan=2)
lbl_blank.config(font=labelfont)
'''
if __name__ == '__main__':
    #make_Title_Frame('Chemistry')
    #file_ops()
    root.mainloop()
    #radio1()
    #radio2()
    #radio4()
    #radio5()
    #set_element1()
    #element1 = cb_Elements1.get()
    # print('Element1 value is ', el1)    #eci1_qty
    # print('Element1 quantity is ', eci1_qty)    #

'''
def callback_eci_1(eventObject):
    eci_1 = cb_eci_1.get()
    print(eci_1)

def callback_eci_1_qty():             #eventObject
    eci_1_qty = e_eci_1_qty.get()
    #eci_1_M_qty = e_eci_1_M_qty.get()
    print('eci_1_qty = ',eci_1_qty)
    #print('eci_1_M_qty = ', eci_1_M_qty)

def callback_eci_1_units(eventObject):
    eci_1_units = cb_eci_1_units.get()
    print(eci_1_units)

def callback_eci_1_M(eventObject):
    eci_1_M = cb_eci_1_M.get()
    print(eci_1_M)

def callback_eci_1_M_qty():
    eci_1_M_qty = e_eci_1_M_qty.get()
    print('eci_1_M_qty = ', eci_1_M_qty)

def callback_eci_2(eventObject):
    eci_2 = cb_eci_2.get()
    print(eci_2)

def callback_eci_2_qty():
    eci_2_qty = e_eci_2_qty.get()
    print(eci_2_qty)

def callback_eci_2_units(eventObject):
    eci_1_units = eci_2_units.get()
    print(eci_1_units)


def callback_eci_3(eventObject):
    element1 = cb_eci_3.get()
    print(element1)
    #print(cb_Elements1.get())
def callback_eci_3_units(eventObject):
    units_E1 = eci_3_units.get()
    print(units_E1)


def callback_eci_4(eventObject):
    eci_4 = cb_eci_4.get()     # = Combobox(root, values=compound_values, textvariable=eci_4, width=30)
    print(eci_4)

def callback_eci_4_qty():
    eci_4_qty = cb_eci_4.get()
    print(eci_4_qty)

def callback_eci_4_units(eventObject):
    eci_4_units = cb_eci_4_units.get()
    print(eci_4_units)
'''
