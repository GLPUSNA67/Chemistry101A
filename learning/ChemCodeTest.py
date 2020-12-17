from tkinter import *  # get widget classes
from tkinter.ttk import Combobox #,Textbox
from tkinter.messagebox import *  # get standard dialogs
import sqlite3
from sqlite3 import Error

root = Tk()
root.title('Chemistry')

entryfont= ('Ariel', 12) #, 'bold')

elements = "Ac Ag Al Am Ar As At Au B Ba Be Bi Bk Br C Ca Cd Ce Cf Cl Cm Co Cr Cs Cu Dy Er Es Eu " \
 "F Fe Fm Fr Ga Gd Ge H He Hf Hg Ho I In Ir K Kr La Li Lu Md Mn Mo N Na Nb Nd Ne Ni Np O Os " \
 "P Pa Pb Pd Pm Po Pr Pt Pu Ra Rb Re Rh Rn  Ru S Sb Sc Se Si Sm Sn Sr Ta Tb Tc Te Th Ti Tl Tm " \
 "U V W Xe Y Yb Zn Zr "

eci_1 = StringVar()
eci_1_mass = DoubleVar()

H = {'symbol': 'H', 'name': 'Hydrogen', 'atomic_number': 1, 'mass': '1.008', 'period': 1, 'row': 1, 'column': 1, '_group': '1A 7A', 'protons': 1, 'neutrons': 0, 'electrons': 1, '_1s': 1, '_2s': 0, '_2p': 0, '_3s': 0, '_3p': 0, '_4s': 0, '_3d': 0, '_4p': 0, '_4d': 0, '_5s': 0, '_5p': 0, '_6s': 0, '_5d': 0, '_6p': 0, '_7s': 0, 'affinity': '-72', 'density': '0.00008988', 'electronegativity': '2.1', 'melt': '14.01', 'boil': '-252.76', 'e_fusion': 'ef', 'e_vapor': 'ev', 't_crit': '-240.17', 'p_crit': '12.77', 'valence': '1 -1', 'a_radius': '53'}
He = {'symbol': 'He', 'name': 'Helium', 'atomic_number': 2, 'mass': '4.002602', 'period': 1, 'row': 1, 'column': 18, '_group': '8A', 'protons': 2, 'neutrons': 2, 'electrons': 2, '_1s': 2, '_2s': 0, '_2p': 0, '_3s': 0, '_3p': 0, '_4s': 0, '_3d': 0, '_4p': 0, '_4d': 0, '_5s': 0, '_5p': 0, '_6s': 0, '_5d': 0, '_6p': 0, '_7s': 0, 'affinity': '20', 'density': '0.0001785', 'electronegativity': '0.0', 'melt': 'NULL', 'boil': '-268.94', 'e_fusion': 'E Fusion', 'e_vapor': 'E Vapor', 't_crit': '-267.9550', 'p_crit': '2.261', 'valence': '0', 'a_radius': '31'}

#car = {
#    "brand": "Ford",
#    "model": "Mustang",
#    "year": 1964
#    }

class Element:
    def __init__(self, symbol,name,a_number,mass,period,row,column,_group,protons,neutrons,electrons,
                 _1s=0,_2s=0,_2p=0,_3s=0,_3p=0,_4s=0,_3d=0,_4p=0,_4d=0,_5s=0,_5p=0,_6s=0,_5d=0,_6p=0,_7s=0,
                 affinity=0,density=0,electronegativity=0,melt=0,boil=0,e_fusion=0,e_vapor=0,t_crit='NULL',p_crit='NULL'
                 ,valence=0,a_radius=0):
        self.symbol = symbol
        self.name  = name
        self.a_number  = a_number
        self.mass  = mass
        self.period = period
        self.row  = row
        self.column  = column
        self._group = _group
        self.protons  = protons
        self.neutrons  = neutrons
        self.electrons = electrons
        self._1s  = _1s
        self._2s  = _2s
        self._2p  = _2p
        self._3s  = _3s
        self._3p  = _3p
        self._4s  = _4s
        self._3d  = _3d
        self._4p  = _4p
        self._4d  = _4d
        self._5s  = _5s
        self._5p  = _5p
        self._6s  = _6s
        self._5d  = _5d
        self._6p  = _6p
        self._7s  = _7s
        self.affinity  = affinity
        self.density  = density
        self.electronegativity  = electronegativity
        self.melt  = melt
        self.boil  = boil
        self.e_fusion  = e_fusion
        self.e_vapor  = e_vapor
        self.t_crit  = t_crit
        self.p_crit  = p_crit
        self.valence  = valence
        self.a_radius  = a_radius


def setClassItem(eventObject):
    print("setClassItem process entered")
    #Print works. Now, if the selected item is of type 'element' set the ECI to the class instance.

    eci_1 = cb_eci_1.get()          # This works
    eci_1_mass = H.get("mass")      # This works
    #eci_1_mass = eci_1.get("mass")  # AttributeError: 'str' object has no attribute 'get'

    #eci_1_mass =  H.mass           # This works
    #print('H.mass is ', eci_temp_1_qty)
    #eci_temp_1_qty =  eci_1.mass    # AttributeError: 'str' object has no attribute 'mass'
    #eci_temp_1_qty =  H(3)

    print('eci_1 = ', eci_1)
    print('eci_1_mass = ', eci_1_mass)
    #print('eci_1_mass = ', eci_1.get("mass"))   # This assignment does not works

    #print('H.mass is ', eci_temp_1_qty) # TypeError: 'Element' object is not callable
    #eci_temp_1_qty =  H[3]
    #print('H.mass is ', eci_temp_1_qty) # TypeError: 'Element' object is not subscriptable

lbl_eci_1 = Label(root, text="   Select Element, Compound or Ion number 1")
cb_eci_1 = Combobox(root, textvariable=eci_1, width=12) #, command=setClassItem
cb_eci_1.grid(row=12, column=2)   #, padx=4)
cb_eci_1.config(font=entryfont)
cb_eci_1['values'] = elements
cb_eci_1.bind("<<ComboboxSelected>>", setClassItem)

if __name__ == '__main__':
    #H = Element('H','Hydrogen','1','1.008','1','1','1','1A 7A','1','0','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','-72','0.00008988','2.1','14.01','-252.76','ef','ev','-240.17','12.77','1 -1','53')
    #He = Element('He', 'Helium', '2', '4.002602', '1', '1', '18', '8A', '2', '2', '2', '2', '0','0','0','0','0','0','0','0', '0', '0', '0', '0', '0', '0', '20', '0.0001785', '0.0', 'NULL', '-268.94', 'E Fusion', 'E Vapor', '-267.9550', '2.261', '0','31')
    #H = {'H','Hydrogen','1','1.008','1','1','1','1A 7A','1','0','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','-72','0.00008988','2.1','14.01','-252.76','ef','ev','-240.17','12.77','1 -1','53'}
    #He = {'He', 'Helium', '2', '4.002602', '1', '1', '18', '8A', '2', '2', '2', '2', '0','0','0','0','0','0','0','0', '0', '0', '0', '0', '0', '0', '20', '0.0001785', '0.0', 'NULL', '-268.94', 'E Fusion', 'E Vapor', '-267.9550', '2.261', '0','31'}

    #x = H.Keys()
    #print(x)
    root.mainloop()

    x = H.get("mass")
    print(x)


