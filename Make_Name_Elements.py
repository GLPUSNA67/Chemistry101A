elements_symbols_list = ['Ac', 'Ag', 'Al', 'Am', 'Ar', 'As', 'At', 'Au', 'B', 'Ba', 'Be', 'Bi', 'Bk', 'Br', 'C', 'Ca', 'Cd', 'Ce', 'Cf', 'Cl', 'Cm', 'Co', 'Cr', 'Cs', 'Cu', 'Dy', 'Er', 'Es', 'Eu',
'F', 'Fe', 'Fm', 'Fr', 'Ga', 'Gd', 'Ge', 'H', 'He', 'Hf', 'Hg', 'Ho', 'I', 'In', 'Ir', 'K', 'Kr', 'La', 'Li', 'Lu', 'Md', 'Mn', 'Mo', 'N', 'Na', 'Nb', 'Nd', 'Ne', 'Ni', 'Np', 'O', 'Os',
'P', 'Pa', 'Pb', 'Pd', 'Pm', 'Po', 'Pr', 'Pt', 'Pu', 'Ra', 'Rb', 'Re', 'Rh', 'Rn', 'Ru', 'S', 'Sb', 'Sc', 'Se', 'Si', 'Sm', 'Sn', 'Sr', 'Ta', 'Tb', 'Tc', 'Te', 'Th', 'Ti', 'Tl', 'Tm',
'U', 'V', 'W', 'Xe', 'Y', 'Yb', 'Zn', 'Zr']

elements_name_list =['Actinium', 'Silver', 'Aluminum', 'Americium', 'Argon', 'Arsenic', 'Astatine', 'Gold', 'Boron',
                     'Barium', 'Beryllium', 'Bismuth', 'Berkelium', 'Bromine', 'Carbon', 'Calcium', 'Cadmium', 'Cerium',
                     'Californium', 'Chlorine', 'Curium', 'Cobalt', 'Chromium', 'Cesium', 'Copper', 'Dysprosium',
                     'Erbium', 'Einsteinium', 'Europium', 'Fluorine', 'Iron', 'Fermium', 'Francium', 'Gallium',
                     'Gadolinium', 'Germanium', 'Hydrogen', 'Helium', 'Hafnium', 'Mercury', 'Holmium', 'Iodine',
                     'Indium', 'Iridium', 'Potassium', 'Krypton', 'Lanthanum', 'Lithium', 'Lutetium', 'Mendelevium',
                     'Manganese', 'Molybdenum', 'Nitrogen', 'Na', 'Niobium', 'Neodymium', 'Neon', 'Nickel',
                     'Neptunium', 'Oxygen', 'Osmium', 'Phosphorus', 'Protactinium', 'Lead', 'Palladium', 'Promethium',
                     'Polonium', 'Praseodymium', 'Platnum', 'Plutonium', 'Radium', 'Rubidium', 'Rhenium', 'Rhodium',
                     'Radon', 'Rutherfordium', 'Sulfur', 'Antimony', 'Scandium', 'Selenium', 'Silicon', 'Samarium',
                     'Tin', 'Strontium', 'Tantalum', 'Terbium', 'Technetium', 'Tellurium', 'Thorium', 'Titanium',
                     'Thallium', 'Thulium', 'Uranium', 'Vanadium', 'Tungsten', 'Xenon', 'Yttrium', 'Ytterbium', 'Zinc',
                     'Zirconium']

element_names_Dict = {}
for (k,v) in zip(elements_name_list, elements_symbols_list):
    element_names_Dict[k] = v

print(element_names_Dict)

