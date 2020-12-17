import tkinter as tk
from tkinter.ttk import *

master = tk.Tk()
master.title("Gas Calculator")
v = tk.IntVar()
combo = Combobox(master)

compound_values = "Al4C3 2HBr CaI Ca(OH)2 Ca3P2 CdS CH3CO2H CO CO2 CsF CuS FeCl2 FeCl3 GaBr3 "
compound_values = compound_values + "HgO Hg2O HNO2 HNO3 H2CO3 H2SO3 H2SO4 H3PO4 HC2H3O2 HCl HClO4"
compound_values = compound_values + "HF HI H2S LiCl K2SO4 Kbr KOH Mg3N2 NaCl NaOH Na2O NH3 "
compound_values = compound_values + "NO2 N2O4 N2O5 H2O ZnO ZnCO3"

def callback1(eventObject):
    print(comboARU.get())
    #comboARU.bind("<<ComboboxSelected>>", callback1)
comboARU = Combobox(master)
comboARU['values']= compound_values    #("Acres", "Ft^2")
#comboARU.current(0) #set the selected item
comboARU.grid(row=3, column=2)
comboARU.bind("<<ComboboxSelected>>", callback1)

master.mainloop()
