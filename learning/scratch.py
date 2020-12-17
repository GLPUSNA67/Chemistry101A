
from tkinter import *  # get widget classes
from tkinter.ttk import Combobox #,Textbox
from tkinter.messagebox import *  # get standard dialogs

root = Tk()
root.title('Chemistry')
titlefont= ('Ariel', 15, 'bold')
labelfont= ('Ariel', 13) #, 'bold')
buttonfont= ('Ariel', 13) #, 'bold')
entryfont= ('Ariel', 13) #, 'bold')
'''
def callback_E1(eventObject):
    element1 = cb_Elements1.get()
    print(element1)
    #print(cb_Elements1.get())

def callback_U1(eventObject):
    units_E1 = cb_Units1.get()
    print(units_E1)
    #print(cb_Elements1.get())
'''
# cb_Elements1.bind("<<ComboboxSelected>>", callback_E1)
element1 = StringVar()
units_E1 = StringVar()
el1 = element1.get()
eci_qty = StringVar()
eci1_qty = element1

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

lbl_Title = Label(root, text="Chemistry")
lbl_Title.pack(side=TOP)
lbl_Title.config(font=labelfont)

#class file_ops(Frame):
#    def __init__(self, parent=None):
#        self.grid(row=1, column=1, columnspan=5)
lbl_record_create = Label(text="Create a record name:")
lbl_record_create.pack(side=LEFT)
# lbl_record_create.grid(row=1, column=0, columnspan=2)
lbl_record_create.config(font=labelfont)

e_recordname = Entry(root, text="", width=30)
e_recordname.pack(side=TOP)
# e_recordname.grid(row=1, column=2, columnspan=2)
e_recordname.config(font=labelfont)

btn_create_record = Button(root, text = 'Create New Record')
btn_create_record.pack(side=RIGHT)
# btn_create_record.grid(row=1, column=4)
btn_create_record.config(font=buttonfont)

lbl_recordname_instruction = Label(text="Record name form is Formula_Process_Location_step_totalSteps: Such as: NaCl_Synthesis_Industry_1_2")
lbl_recordname_instruction.pack(side=TOP)
#lbl_recordname_instruction.grid(row=2, column=0, columnspan=6)
lbl_recordname_instruction.config(font=labelfont)
'''
'''
if __name__ == '__main__':
    root.mainloop()
