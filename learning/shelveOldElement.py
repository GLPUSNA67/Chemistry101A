import shelve

class Element:
    def __init__(self, symbol, name, a_number, a_mass, group, period, column,
                 protons, neutrons, electrons, density, a_radius, affinity,  electronegativity,
                 melting, boiling, triple, e_fusion, e_vapor, temp_crit, press_crit, char,
                 _1s, _2s, _2p, _3s, _3p, _3d, _4s, _4p, _4d, _4f, _5s=0, _5p=0, _5d=0, _5f=0, _6s=0, _6p=0, _6d=0, _7s=0,
                 reserved=""):
        # 'symbol', 'name', 'a_number', 'a_mass', 'group', 'period', 'row', 'column', 'protons', 'neutrons', 'electrons',
        # 'affinity', 'density'", 'electronegativity' 'melting', 'boiling', 'triple', 'e_fusion', 'e_vapor',
        # 'temp_crit', 'press_crit', 'char', '1s', '2s', '2p', '3s', '3p', '3d', '4s', '4p', '4d', '4f'
        self.symbol = symbol
        self.name = name
        self.a_number  = a_number
        self.a_mass  = a_mass
        self.group  = group
        self.period = period
        self.column = column
        self.protons = protons
        self.neutrons = neutrons
        self.electrons = electrons
        self.density = density
        self.a_radius = a_radius
        self.affinity = affinity
        self.electronegativity = electronegativity
        self.melting = melting
        self.boiling = boiling
        self.triple = triple
        self.e_fusion = e_fusion
        self.e_vapor = e_vapor
        self.temp_crit = temp_crit
        self.press_crit = press_crit
        self.char = char
        self._1s = _1s
        self._2s = _2s
        self._2p = _2p
        self._3s = _3s
        self._3p = _3p
        self._3d = _3d
        self._4s = _4s
        self._4p = _4p
        self._4d = _4d
        self._4f = _4f
        self._5s = _5s
        self._5p = _5p
        self._5d = _5d
        self._5f = _5f
        self._6s = _6s
        self._6p = _6p
        self._6d = _6d
        self._7s = _7s
        self.reserved = reserved


    #def lastName(self):
    #    return self.name.split()[-1]
    #def giveRaise(self, percent):
    #    self.pay *= (1.0 + percent)

# symbol, name, a_number, a_mass, group, period, column,
# protons, neutrons, electrons, density, affinity,  electronegativity,
# melting, boiling, triple, e_fusion, e_vapor, temp_crit, press_crit,
# char, _1s, _2s, _2p, _3s, _3p, _3d, _4s, _4p, _4d, _4f, reserved):
if __name__ == '__main__':
    H = Element('H','Hydrogen', 1, 1.00794, '1A', 1, 1, 1, 0, 1, 'density', 'a_radius', 'affinity', 'electronegativity',
                'melting', 'boiling', 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
                'char', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'reserved')
    He = Element('He','Helium',  2,  4.002602,  '8A', 1, 1, 1, 0, 1, 'density', 'a_radius', 'affinity', 'electronegativity',
                'melting', 'boiling', 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
                'char', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'reserved')
    Li = Element('Li', 'Lithium',  3,  6.941,  '1A', 1, 1, 1, 0, 1, 'density', 'a_radius', 'affinity', 'electronegativity',
                'melting', 'boiling', 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
                'char', 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'reserved')
    '''
    H = Element('H','Hydrogen', 1, 1.00794, '1A', 1, 1, 1, 0, 1, 'density', 'a_radius', 'affinity', 'electronegativity',
                'melting', 'boiling', 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
                'char', '_1s', '_2s', '_2p', '_3s', '_3p', '_3d', '_4s', '_4p', '_4d', '_4f', 'reserved')

    array from VB elements
    Public arrElements2 = {'{"Index", "symbol", "name", "Atomic Number", "Atomic Mass", "Period", "Row", "Column", "Group", "Protons", "Neutrons", "Electrons", "1s", "2s", "2p", "3s", "3p", "3d", "4s", "4p", "4d", "4f", "Affinity", "Density", "Electronegativity", "Melting", "Boiling", "E Fusion", "E Vapor", "Temp Crit", "Press Crit", "Lewis"},
                           {"0", "H", "Hydrogen", "1", "1.008", "1", "1", "1", "1A, 7A", "1", "0", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "-72", "0.00008988", "2.1", "14.01", "-252.76", "E Fusion", "E Vapor", "-240.17", "12.77", "E1"},
                           {"1", "He", "Helium    ", "2", "4.003", "1", "1", "18", "8A", "2", "2", "2", "2", "0", "0", "0", "0", "0", "0", "0", "0", "0", "20", "Density", "0.0", "Melting", "-268.94", "E Fusion", "E Vapor", "-267.96", "2.261", "Lewis"},
                           {"2", "Li", "Lithiumn   ", "3", "6.941", "2", "2", "1", "1A", "3", "3", "3", "2", "1", "0", "0", "0", "0", "0", "0", "0", "0", "-60", "Density", "1.0", "Melting", "Boiling", "E Fusion", "E Vapor", "Temp Crit", "Press Crit", "Lewis"},
                           {"3", "Be", "Beryllium  ", "4", "9.012", "2", "2", "2", "2A", "4", "4", "4", "2", "2", "0", "0", "0", "0", "0", "0", "0", "0", "240", "Density", "1.5", "Melting", "Boiling", "E Fusion", "E Vapor", "Temp Crit", "Press Crit", "Lewis"},
                           {"4", "B", "Boron     ", "5", "10.011", "2", "2", "13", "3A", "5", "5", "5", "2", "2", "1", "0", "0", "0", "0", "0", "0", "0", "-23", "Density", "2.0", "Melting", "Boiling", "E Fusion", "E Vapor", "Temp Crit", "Press Crit", "Lewis"},
                           {"5", "C", "Carbon    ", "6", "12.011", "2", "2", "14", "4A", "6", "6", "6", "2", "2", "2", "0", "0", "0", "0", "0", "0", "0", "-123", "Density", "2.5", "Melting", "Boiling", "E Fusion", "E Vapor", "Temp Crit", "Press Crit", "Lewis"},
                           {"6", "N", "Nitrogen  ", "7", "14.007", "2", "2", "15", "5A", "7", "7", "7", "2", "2", "3", "0", "0", "0", "0", "0", "0", "0", "0", "Density", "3.0", "Melting", "-195.81", "E Fusion", "E Vapor", "-146.89", "33.54", "E1N2W1S1"},
                           {"7", "O", "Oxygen    ", "8", "15.999", "2", "2", "16", "6A", "8", "8", "8", "2", "2", "4", "0", "0", "0", "0", "0", "0", "0", "-141", "Density", "3.5", "Melting", "-182.96", "E Fusion", "E Vapor", "-118.38", "50.14", "Lewis"},
                           {"8", "F", "Flourine   ", "9", "18.998", "2", "2", "17", "7A", "9", "9", "9", "2", "2", "5", "0", "1", "0", "0", "0", "0", "0", "-322", "Density", "4.0", "Melting", "Boiling", "E Fusion", "E Vapor", "Temp Crit", "Press Crit", "Lewis"},
                           {"9", "Ne", "Neon ", "10", "20.180", "2", "2", "18", "8A", "10", "10", "10", "2", "2", "6", "0", "0", "0", "0", "0", "0", "0", "30", "Density", "0.0", "Melting", "-246.1", "E Fusion", "E Vapor", "-228.71", "26.86", "Lewis"},
                           {"10", "Na", "Sodium", "11", "22.990", "3", "3", "1", "1A", "11", "11", "11", "2", "2", "6", "1", "0", "0", "0", "0", "0", "0", "-53", "Density", "0.9", "Melting", "Boiling", "E Fusion", "E Vapor", "Temp Crit", "Press Crit", "E1"},
                           {"11", "Mg", "Manganese", "12", "24.305", "3", "3", "2", "2A", "12", "12", "12", "2", "2", "6", "2", "0", "0", "0", "0", "0", "0", "230", "Density", "1.2", "14.01", "Boiling", "E Fusion", "E Vapor", "Temp Crit", "Press Crit", "E2"},
                           {"12", "Al", "Aluminun", "13", "26.982", "3", "3", "13", "3A", "13", "13", "13", "2", "2", "6", "2", "1", "0", "0", "0", "0", "0", "-44", "Density", "1.5", "Melting", "Boiling", "E Fusion", "E Vapor", "Temp Crit", "Press Crit", "E2N1"},
                           {"13", "Si", "Silicon", "14", "28.086", "3", "3", "14", "4A", "14", "14", "14", "2", "2", "6", "2", "2", "0", "0", "0", "0", "0", "-120", "Density", "1.8", "Melting", "Boiling", "E Fusion", "E Vapor", "Temp Crit", "Press Crit", "E1N2W1"},
                           {"14", "P", "Phosphorus", "15", "30.974", "3", "3", "15", "5A, 7A", "15", "15", "15", "2", "2", "6", "2", "3", "0", "0", "0", "0", "0", "-74", "Density", "2.1", "Melting", "Boiling", "E Fusion", "E Vapor", "Temp Crit", "Press Crit", "E1N2W1S1"},
                           {"15", "S", "Sulfur", "16", "32.066", "3", "3", "16", "6A", "16", "16", "16", "2", "2", "6", "2", "4", "0", "0", "0", "0", "0", "-201", "Density", "2.5", "Melting", "Boiling", "E Fusion", "E Vapor", "Temp Crit", "Press Crit", "E1N2W2S1"},
                           {"16", "Cl", "Clorine", "17", "35.453", "3", "3", "17", "7A", "17", "17", "17", "2", "2", "6", "2", "5", "0", "0", "0", "0", "0", "-348", "Density", "3.0", "14.01", "-34.03", "E Fusion", "E Vapor", "144.0", "78.1", "E1N2W2S2"},
                           {"17", "Ar", "Argon", "18", "39.948", "3", "3", "18", "8A", "18", "18", "18", "2", "2", "6", "2", "6", "0", "0", "0", "0", "0", "35", "Density", "0.0", "Melting", "Boiling", "E Fusion", "E Vapor", "Temp Crit", "Press Crit", "E2N2W2S2"},
                           {"18", "K", "Potassium", "19", "39.0983", "4", "4", "1", "1A", "19", "19", "19", "2", "2", "6", "2", "6", "0", "1", "0", "0", "0", "-48", "Density", "0.8", "14.01", "20.28", "E Fusion", "E Vapor", "Temp Crit", "Press Crit", "Lewis"},
                           {"19", "Ca", "Calcium", "20", "40.078", "4", "4", "2", "2A", "20", "20", "20", "2", "2", "6", "2", "6", "0", "2", "0", "0", "0", "Affinity", "Density", "1.0", "14.01", "20.28", "E Fusion", "E Vapor", "Temp Crit", "Press Crit", "E2"},
                           {"20", "Se", "Selenium", "21", "44.956", "4", "4", "3", "3B", "21", "21", "21", "2", "2", "6", "2", "6", "1", "2", "0", "0", "0", "Affinity", "Density", "1.3", "Melting", "Boiling", "E Fusion", "E Vapor", "Temp Crit", "Press Crit", "Lewis"},
                           {"21", "Ti", "Titanium", "22", "47.88", "4", "4", "4", "4B", "22", "22", "22", "2", "2", "6", "2", "6", "2", "2", "0", "0", "0", "Affinity", "Density", "1.5", "14.01", "20.28", "E Fusion", "E Vapor", "Temp Crit", "Press Crit", "Lewis"},
                           {"22", "V", "Vanadium", "23", "50.9415", "4", "4", "5", "5B", "23", "23", "23", "2", "2", "6", "2", "6", "3", "2", "0", "0", "0", "Affinity", "Density", "1.6", "Melting", "Boiling", "E Fusion", "E Vapor", "Temp Crit", "Press Crit", "Lewis"},
                           {"23", "Cr", "Chromium", "24", "51.9961", "4", "4", "6", "6B", "24", "24", "24", "2", "2", "6", "2", "6", "5", "1", "0", "0", "0", "Affinity", "Density", "1.6", "14.01", "20.28", "E Fusion", "E Vapor", "Temp Crit", "Press Crit", "Lewis"},
                           {"24", "Mn", "Manganese", "25", "54.93805", "4", "4", "7", "7B", "25", "25", "25", "2", "2", "6", "2", "6", "5", "2", "0", "0", "0", "Affinity", "Density", "1.5", "Melting", "Boiling", "E Fusion", "E Vapor", "Temp Crit", "Press Crit", "Lewis"},
                           {"25", "Fe", "Iron", "26", "55.845", "4", "4", "8", "8B", "26", "26", "26", "2", "2", "6", "2", "6", "6", "2", "0", "0", "0", "Affinity", "Density", "1.8", "14.01", "20.28", "E Fusion", "E Vapor", "Temp Crit", "Press Crit", "Lewis"},
                           {"26", "Co", "Cobalt", "27", "58.99320", "4", "4", "9", "8B", "27", "27", "27", "2", "2", "6", "2", "6", "7", "2", "0", "0", "0", "Affinity", "Density", "1.9", "Melting", "Boiling", "E Fusion", "E Vapor", "Temp Crit", "Press Crit", "Lewis"},
                           {"27", "Ni", "Nickel", "28", "58.6934", "4", "4", "10", "8B", "28", "28", "28", "2", "2", "6", "2", "6", "8", "2", "0", "0", "0", "Affinity", "Density", "1.9", "14.01", "20.28", "E Fusion", "E Vapor", "Temp Crit", "Press Crit", "Lewis"},
                           {"28", "Cu", "Copper", "29", "63.546", "4", "4", "11", "1B", "29", "29", "29", "2", "2", "6", "2", "6", "10", "2", "0", "0", "0", "Affinity", "Density", "1.9", "Melting", "Boiling", "E Fusion", "E Vapor", "Temp Crit", "Press Crit", "Lewis"},
                           {"29", "Zn", "Zinc", "30", "65.39", "4", "4", "12", "2B", "30", "30", "30", "2", "2", "6", "2", "6", "0", "0", "0", "0", "0", "Affinity", "Density", "1.6", "14.01", "20.28", "E Fusion", "E Vapor", "Temp Crit", "Press Crit", "Lewis"}}
    '{"Index", "symbol", "name", "Atomic Number", "Atomic Mass", "Period", "Row", "Column", "Group", "Protons", "Neutrons", "Electrons", "1s", "2s", "2p", "3s", "3p", "3d", "4s", "4p", "4d", "4f", "Affinity", "Density", "Electronegativity", "Melting", "Boiling", "E Fusion", "E Vapor", "Temp Crit", "Press Crit", "Lewis"}}

Index", "symbol", "name", "Atomic Number", "Atomic Mass", "Period", "Row", "Column", "Group", "Protons", "Neutrons", "Electrons", "1s", "2s", "2p", "3s", "3p", "3d", "4s", "4p", "4d", "4f", "Affinity", "Density", "Electronegativity", "Melting", "Boiling", "E Fusion", "E Vapor", "Temp Crit", "Press Crit", "Lewis"},
{"0", "H", "Hydrogen", "1", "1.008", "1", "1", "1", "1A, 7A", "1", "0", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "-72", "0.00008988", "2.1", "14.01", "-252.76", "E Fusion", "E Vapor", "-240.17", "12.77", "E1", "Period", "Row", "Column", "Group", "Protons", "Neutrons", "Electrons", "1s", "2s", "2p", "3s", "3p", "3d", "4s", "4p", "4d", "4f", "Affinity",
    "Density", "Electronegativity", "Melting", "Boiling", "E Fusion", "E Vapor", "Temp Crit", "Press Crit", "Valence"}
H = {"symbol": "H", "name": "Hydrogen", "Atomic Number": 1, "Atomic Mass": 1.008, "Period": 1, "Row": 1,
 "Column": "1,7", "Group": "1A 7A", "Protons": 1, "Neutrons": 0, "Electrons": 1, "_1s": 1, "_2s": 0, "_2p": 0,
  "_3s": 0, "_3p": 0, "_3d": 0, "_4s": 0, "_4p": 0, "_4d": 0, "-4f": 0, "Affinity": -72,
 "Density": 0, "Electronegativity": 0, "Melting": 0, "Boiling": 0, "E Fusion": 0, "E Vapor": 0, "Temp Crit": 0, "Press Crit": 0, "Valence": "1 -1"}

    '''
    db = shelve.open('class-element-shelve')
    db['H'] = H
    db['He'] = He
    db['Li'] = Li
    db.close()
    print(H.name, H.group, He.name, He.group, Li.name, Li.group)
    #bob = Person('Bob Smith', 42, 30000, 'software')
    #print(bob.lastName())
    #sue.giveRaise(.10)
    #print(sue.pay)

