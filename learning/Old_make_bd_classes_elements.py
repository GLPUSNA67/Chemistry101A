import shelve
from element import Element

#bob = Person('Bob Smith', 42, 30000, 'software')
#sue = Person('Sue Jones', 45, 40000, 'hardware')
#tom = Manager('Tom Doe',  50, 50000)

#H = Element('H','Hydrogen', 1, 1.00794, '1A')
#He = Element('He','Helium',  2,  4.002602,  '8A')
#Li = Element('Li', 'Lithium',  3,  6.941,  '1A')
H = Element('H','Hydrogen', 1, 1.00794, '1A', 1, 1, 1, 0, 1, 0.0000899, 53, -72, 2.1,
            -259.14, -252.87, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'reserved')
He = Element('He','Helium',  2,  4.002602,  '8A', 1, 18, 2, 2, 2, 0.0001785, 31, 20, 0,
            -272.20, 268.934, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'reserved')
Li = Element('Li', 'Lithium',  3,  6.941,  '1A', 2, 1, 3, 3, 3, 0.535, 167, -60, 1.0,
            180.54, 1347, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'reserved')
Be = Element('Be', 'Beryllium',  4,  9.012182,  '2A', 2, 2, 4, 4, 4, 1.8477, 112, 240, 1.5,
            1278, 2970, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 'reserved')
B = Element('B', 'Boron',  5,  10.8111,  '3A', 2, 13, 5, 5, 5, 2.460, 87, -23, 2.0,
            2300, 3658, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 'reserved')
C = Element('C', 'Carbon',  6,  12.0107,  '4A', 2, 14, 6, 6, 6, 2.260, 67, -123, 2.5,
            3527, 4827, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 'reserved')
N = Element('N', 'Nitrogen',  7,  14.0067,  '5A', 2, 15, 7, 7, 7, 0.001251, 56, 0, 3.0,
            -209.86, -195.8, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 3, 0, 0, 0, 0, 0, 0, 0, 'reserved')
O = Element('O', 'Oxygen',  8,  15.9994,  '6A', 2, 16, 8, 8, 8, 0.001429, 48, -141, 3.5,
            -218.4, -182.96, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 4, 0, 0, 0, 0, 0, 0, 0, 'reserved')
F = Element('F', 'Flourine',  9,  18.9984032,  '7A', 2, 17, 9, 9, 9, 0.001696, 42, -322, 4.0,
            -219.62, -188.14, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 5, 0, 0, 0, 0, 0, 0, 0, 'reserved')
Ne = Element('Ne', 'Neon',  10,  20.1797,  '8A', 2, 18, 10, 10, 10, 0.000900, 38, 30, 0,
            -248.67, -246.05, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 'reserved')
Na = Element('Na', 'Sodium',  11,  22.989770,  '1A', 3, 1, 11, 11, 11, 0.968, 190, 53, 0.9,
            97.81, 882.9, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 1, 0, 0, 0, 0, 0, 0, 'reserved')
Mg = Element('Mg', 'Magnesium',  12,  24.3050,  '2A', 3, 2, 12, 12, 12, 1.738, 145, 230, 1.2,
            648.8, 1090, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 0, 0, 0, 0, 0, 0, 'reserved')
Al = Element('Al', 'Aluminum',  13,  26.981538,  '3A', 3, 13, 13, 13, 13, 2.7, 118, -44, 1.5,
            660.37, 2467, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 1, 0, 0, 0, 0, 0, 'reserved')
Si = Element('Si', 'Silicon',  14,  28.0855,  '4A', 3, 14, 14, 14, 14, 2.330, 111, -120, 1.8,
            1410, 2355, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 2, 0, 0, 0, 0, 0, 'reserved')
P = Element('P', 'Phosphorus',  15,  30.973761,  '5A', 3, 15, 15, 15, 15, 01.823, 98, -74, 2.1,
            44.1, 280, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 3, 0, 0, 0, 0, 0, 'reserved')
S = Element('S', 'Sulfur',  16,  32.065,  '6A', 3, 17, 16, 16, 16, 1.960, 88, -201, 2.5,
            113, 444.67, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 4, 0, 0, 0, 0, 0, 'reserved')
Cl = Element('Cl', 'Chlorine',  17,  35.453,  '7A', 3, 17, 17, 17, 17, 0.003214, 79, -348, 3.0,
            -100.98, -33.97, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 5, 0, 0, 0, 0, 0, 'reserved')
Ar = Element('Ar', 'Argon',  18,  39.948,  '8A', 3, 18, 18, 18, 18, 0.001784, 71, 35, 0,
            -189.37, -185.86, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 6, 0, 0, 0, 0, 0, 'reserved')
K = Element('K', 'Potassium',  19,  39.0983,  '1A', 4, 1, 19, 19, 19, 0.856, 243, -48, 0.8,
            63.65, -774, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 6, 0, 1, 0, 0, 0, 'reserved')
Ca = Element('Ca', 'Calcium',  20,  40.078,  '2A', 4, 2, 20, 20, 20, 1.550, 194, 150, 1.0,
            839, 1484, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 6, 0, 2, 0, 0, 0, 'reserved')
Sc = Element('Sc', 'Scandium',  21,  44.956,  '3B', 4, 3, 21, 21, 21, 2.985, 184, 'affinity', 1.3,
            1541, 2831, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 6, 1, 2, 0, 0, 0, 'reserved')
Ti = Element('Ti', 'Titanium',  22,  47.867,  '4B', 4, 4, 22, 22, 22, 4.507, 176, 'affinity', 1.5,
            1660, 3287, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 6, 2, 2, 0, 0, 0, 'reserved')
V = Element('V', 'Vanadium',  23,  50.9415,  '5B', 4, 5, 23, 23, 23, 6.110, 171, 'affinity',  1.6,
            1887, 3377, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 6, 3, 2, 0, 0, 0, 'reserved')
Cr = Element('Cr', 'Chromium',  24,  51.9961,  '6B', 4, 6, 24, 24, 24, 7.140, 166, 'affinity',  1.6,
            1857, 2672, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 6, 5, 1, 0, 0, 0, 'reserved')
Mn = Element('Mn', 'Manganese',  25,  54.938049,  '7B', 4, 7, 25, 25, 25, 7.470, 161, 'affinity',  1.5,
            1244, 1962, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 6, 5, 2, 0, 0, 0, 'reserved')
Fe = Element('Fe', 'Iron',  26,  55.845,  '8B', 4, 8, 26, 26, 26, 7.874, 156, 'affinity',  1.8,
            1535, 2750, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 6, 6, 2, 0, 0, 0, 'reserved')
Co = Element('Co', 'Cobalt',  27, 58.9332,  '8B', 4, 9, 27, 27, 27, 8.9, 152, 'affinity',  1.9,
            1495, 2870, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 6, 7, 2, 0, 0, 0, 'reserved')
Ni = Element('Ni', 'Nickel',  28, 58.6934,  '8B', 4, 10, 28, 28, 28, 8.908, 149, 'affinity',  1.9,
            1453, 2732, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 6, 8, 2, 0, 0, 0, 'reserved')
Cu = Element('Cu', 'Copper',  29, 63.546,  '1B', 4, 11, 29, 29, 29, 8.920, 145, 'affinity',  1.9,
            1083.4, 2567, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 6, 10, 1, 0, 0, 0, 'reserved')
Zn = Element('Zn', 'Zinc',  30, 65.409,  '2B', 4, 12, 30, 30, 30, 7.140, 142, 'affinity', 1.6,
            419.58, 907, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 6, 10, 2, 0, 0, 0, 'reserved')
Ga = Element('Ga', 'Gallium',  31, 69.723,  '3A', 4, 13, 31, 31, 31, 5.904, 136, -40, 1.6,
            29.78, 2403, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 6, 10, 2, 1, 0, 0, 'reserved')
Ge = Element('Ge', 'Germanium',  32, 72.61,  '4A', 4, 14, 32, 32, 32, 5.323, 125, -116, 1.8,
            937.4, 2830, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 6, 10, 2, 2, 0, 0, 'reserved')
As = Element('As', 'Arsenic',  33, 74.922,  '5A', 4, 15, 33, 33, 33,5.727, 114, -77, 2.0,
            817, 616, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 6, 10, 2, 3, 0, 0, 'reserved')
Se = Element('Se', 'Selenium',  34, 78.96,  '6A', 4, 16, 34, 34, 34, 4.819, 103, -195, 2.4,
            217, 684.9, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 6, 10, 2, 4, 0, 0, 'reserved')
Br = Element('BR', 'Bromine',  35, 79.904,  '7A', 4, 17, 35, 35, 35, 3.120, 94, -324, 2.8,
            -7.3, 58.78, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 6, 10, 2, 5, 0, 0, 'reserved')
Kr = Element('Kr', 'Krypton',  36, 83.798,  '8A', 4, 18, 36, 36, 36, 0.00375, 88, 40, 0,
            -156.6, -152.30, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 6, 10, 2, 6, 0, 0, 'reserved')
Rb = Element('Rb', 'Rubidium', 37, 85.4678,  '1A', 5, 1, 37, 37, 37, 1.532, 265, -46, 0.8,
            39.0, 688, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 6, 10, 2, 6, 0, 0, 1,'reserved')
Sr = Element('Sr', 'Strontium',  38,  87.62,  '2A', 5, 2, 38, 38, 38, 2.630, 219, 160, 1.0,
            769, 1384, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 6, 10, 2, 6, 0, 0, 2, 'reserved')
Y = Element('Y', 'Yttrium', 39, 88.90585,  '3B', 5, 3, 39, 39, 39, 4.472, 212, 'affinity', 1.2,
            39.0, 688, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 6, 10, 2, 6, 1, 0, 2, 'reserved')
Zr = Element('Zr', 'Zirconium',  40,  91.224,  '4B', 5, 4, 40, 40, 40, 6.511, 286, 'affinity', 1.4,
            769, 1384, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 6, 10, 2, 6, 2, 0, 2, 'reserved')
Nb = Element('Nb', 'Nioium', 41, 92.90638,  '5B', 5, 5, 41, 41, 41, 8.570, 198, 'affinity', 1.6,
            39.0, 688, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 6, 10, 2, 6, 4, 0, 1, 'reserved')
Mo = Element('Mo', 'Molybdenum',  42,  95.94,  '6B', 5, 6, 42, 42, 42, 10.280, 190, 'affinity', 1.8,
            769, 1384, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 6, 10, 2, 6, 5, 0, 1, 'reserved')
Tc = Element('Tc', 'Technetium', 43, '98',  '7B', 5, 7, 43, 43, 43, 11.5, 183, -46, 'affinity', 1.9,
            39.0, 688, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 6, 10, 2, 6, 6, 0, 1, 'reserved')
Ru = Element('Ru', 'Ruthenium',  44,  101.07,  '8B', 5, 8, 44, 44, 44, 12.370, 178, 'affinity', 2.2,
            769, 1384, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 6, 10, 2, 6, 7, 0, 1, 'reserved')
Rh = Element('Rh', 'Rhodium',  45,  102.90550,  '8B', 5, 9, 45, 45, 45, 12.450, 173, 'affinity', 2.0,
            769, 1384, 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
            'char', 2, 2, 6, 2, 6, 10, 2, 6, 8, 0, 1, 'reserved')
'''
            symbol, name, a_number, a_mass, group, period, column, protons, neutrons, electrons
H = Element('H','Hydrogen', 1, 1.00794, '1A', 1, 1, 1, 0, 1, 'density', 'a_radius', 'affinity', 'electronegativity',
            'melting', 'boiling', 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit','char',
            '_1s', '_2s', '_2p', '_3s', '_3p', '_3d', '_4s', '_4p', '_4d', '_4f', '_5s', '_5p', '_5d', '_5f',
            '_6s', '_6p', '_6d', '_7s','reserved')
'''
db = shelve.open('class-element-shelve')
'''
db['H'] = H
db['He'] = He
db['Li'] = Li
'''
db.close()
