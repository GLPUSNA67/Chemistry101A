

''' The following does not work AttributeError: 'str' object has no attribute 'values
names_compounds = list(zip(compound_names_list.values(),compound_symbols_list.keys()))
print(names_compounds)

columns = ['name', 'shares', 'price']
values = ['GOOG', 100, 490.1 ]
pairs = zip(columns, values)
d = dict(zip(columns, values))   # use this to creat a (binary) dictionary
# ('name','GOOG'), ('shares',100), ('price',490.1)
compounds = zip(compound_symbols_list, compound_names_list)

H = dict(symbol= 'H', name= 'Hydrogen', atomic_number= 1, mass= '1.008', period= 1,

          row= 1, column= 1, _group= '1A 7A', protons= 1, neutrons= 0, electrons= 1,
         _1s= 1, _2s= 0, _2p= 0, _3s= 0, _3p= 0, _4s= 0, _3d= 0, _4p= 0, _4d= 0, _5s= 0,
         _5p= 0, _6s= 0, _5d= 0, _6p= 0, _7s= 0, affinity= '-72', density= '0.00008988',
         electronegativity= '2.1', melt= '14.01', boil= '-252.76', e_fusion= 'ef', e_vapor= 'ev',
         t_crit= '-240.17', p_crit= '12.77', valence= '1 -1', a_radius= '53')
#H = {'symbol': 'H', 'name': 'Hydrogen', "Atomic Number": 1, 'mass': 1.008}
H = {'symbol': 'H', 'name': 'Hydrogen', 'atomic_number': 1, 'mass': '1.008', 'period': 1, 'row': 1, 'column': 1, '_group': '1A 7A', 'protons': 1, 'neutrons': 0, 'electrons': 1, '_1s': 1, '_2s': 0, '_2p': 0, '_3s': 0, '_3p': 0, '_4s': 0, '_3d': 0, '_4p': 0, '_4d': 0, '_5s': 0, '_5p': 0, '_6s': 0, '_5d': 0, '_6p': 0, '_7s': 0, 'affinity': '-72', 'density': '0.00008988', 'electronegativity': '2.1', 'melt': '14.01', 'boil': '-252.76', 'e_fusion': 'ef', 'e_vapor': 'ev', 't_crit': '-240.17', 'p_crit': '12.77', 'valence': '1 -1', 'a_radius': '53'}
He = {'symbol': 'He', 'name': 'Helium', 'atomic_number': 2, 'mass': '4.002602', 'period': 1, 'row': 1, 'column': 18, '_group': '8A', 'protons': 2, 'neutrons': 2, 'electrons': 2, '_1s': 2, '_2s': 0, '_2p': 0, '_3s': 0, '_3p': 0, '_4s': 0, '_3d': 0, '_4p': 0, '_4d': 0, '_5s': 0, '_5p': 0, '_6s': 0, '_5d': 0, '_6p': 0, '_7s': 0, 'affinity': '20', 'density': '0.0001785', 'electronegativity': '0.0', 'melt': 'NULL', 'boil': '-268.94', 'e_fusion': 'E Fusion', 'e_vapor': 'E Vapor', 't_crit': '-267.9550', 'p_crit': '2.261', 'valence': '0', 'a_radius': '31'}
Li = {'symbol': 'Li', 'name': 'Lithium', 'atomic_number': 3, 'mass': '6.941', 'period': 2, 'row': 2, 'column': 1, '_group': '1A', 'protons': 3, 'neutrons': 3, 'electrons': 3, '_1s': 2, '_2s': 1, '_2p': 0, '_3s': 0, '_3p': 0, '_4s': 0, '_3d': 0, '_4p': 0, '_4d': 0, '_5s': 0, '_5p': 0, '_6s': 0, '_5d': 0, '_6p': 0, '_7s': 0, 'affinity': '-60', 'density': '0.535', 'electronegativity': '1.0', 'melt': '180.50', 'boil': '1342', 'e_fusion': 'E Fusion', 'e_vapor': 'E Vapor', 't_crit': '2950', 'p_crit': '67', 'valence': '1', 'a_radius': '167'}
Be = {'symbol': 'Be', 'name': 'Beryllium', 'atomic_number': 4, 'mass': '9.012182', 'period': 2, 'row': 2, 'column': 2, '_group': '2A', 'protons': 4, 'neutrons': 4, 'electrons': 4, '_1s': 2, '_2s': 2, '_2p': 0, '_3s': 0, '_3p': 0, '_4s': 0, '_3d': 0, '_4p': 0, '_4d': 0, '_5s': 0, '_5p': 0, '_6s': 0, '_5d': 0, '_6p': 0, '_7s': 0, 'affinity': '240', 'density': '1.848', 'electronegativity': '1.5', 'melt': '1287', 'boil': '2468', 'e_fusion': 'E Fusion', 'e_vapor': 'E Vapor', 't_crit': '4932', 'p_crit': 'NULL', 'valence': '2', 'a_radius': '112'}
B = {'symbol': 'B', 'name': 'Boron', 'atomic_number': 5, 'mass': '10.8111', 'period': 2, 'row': 2, 'column': 13, '_group': '3A', 'protons': 5, 'neutrons': 5, 'electrons': 5, '_1s': 2, '_2s': 2, '_2p': 1, '_3s': 0, '_3p': 0, '_4s': 0, '_3d': 0, '_4p': 0, '_4d': 0, '_5s': 0, '_5p': 0, '_6s': 0, '_5d': 0, '_6p': 0, '_7s': 0, 'affinity': '-23', 'density': '2.460', 'electronegativity': '2.0', 'melt': '2077', 'boil': '4000', 'e_fusion': 'E Fusion', 'e_vapor': 'E Vapor', 't_crit': 'NULL', 'p_crit': 'NULL', 'valence': '3', 'a_radius': '87'}
C = {'symbol': 'C', 'name': 'Carbon', 'atomic_number': 6, 'mass': '12.0107', 'period': 2, 'row': 2, 'column': 14, '_group': '4A', 'protons': 6, 'neutrons': 6, 'electrons': 6, '_1s': 2, '_2s': 2, '_2p': 2, '_3s': 0, '_3p': 0, '_4s': 0, '_3d': 0, '_4p': 0, '_4d': 0, '_5s': 0, '_5p': 0, '_6s': 0, '_5d': 0, '_6p': 0, '_7s': 0, 'affinity': '-123', 'density': '2.260', 'electronegativity': '2.5', 'melt': '4489', 'boil': '3825', 'e_fusion': 'E Fusion', 'e_vapor': 'E Vapor', 't_crit': 'NULL', 'p_crit': 'NULL', 'valence': '4 3 2 1 0 -1 -2 -3 -4', 'a_radius': '67'}
N = {'symbol': 'N', 'name': 'Nitrogen', 'atomic_number': 7, 'mass': '14.0087', 'period': 2, 'row': 2, 'column': 15, '_group': '5A', 'protons': 7, 'neutrons': 7, 'electrons': 7, '_1s': 2, '_2s': 2, '_2p': 3, '_3s': 0, '_3p': 0, '_4s': 0, '_3d': 0, '_4p': 0, '_4d': 0, '_5s': 0, '_5p': 0, '_6s': 0, '_5d': 0, '_6p': 0, '_7s': 0, 'affinity': '0', 'density': '0.001251', 'electronegativity': '3.0', 'melt': '-210.0', 'boil': '-195.795', 'e_fusion': 'E Fusion', 'e_vapor': 'E Vapor', 't_crit': '-146.89', 'p_crit': '33.54', 'valence': '5 4 3 2 1 -1 -2 -3', 'a_radius': '56'}
O = {'symbol': 'O', 'name': 'Oxygen', 'atomic_number': 8, 'mass': '15.9994', 'period': 2, 'row': 2, 'column': 16, '_group': '6A', 'protons': 8, 'neutrons': 8, 'electrons': 8, '_1s': 2, '_2s': 2, '_2p': 4, '_3s': 0, '_3p': 0, '_4s': 0, '_3d': 0, '_4p': 0, '_4d': 0, '_5s': 0, '_5p': 0, '_6s': 0, '_5d': 0, '_6p': 0, '_7s': 0, 'affinity': '-141', 'density': '0.001429', 'electronegativity': '3.5', 'melt': '-218.79', 'boil': '-182.962', 'e_fusion': 'E Fusion', 'e_vapor': 'E Vapor', 't_crit': '-118.38', 'p_crit': '50.14', 'valence': '-1 -2', 'a_radius': '48'}
F = {'symbol': 'F', 'name': 'Fluorine', 'atomic_number': 9, 'mass': '18.9984032', 'period': 2, 'row': 2, 'column': 17, '_group': '7A', 'protons': 9, 'neutrons': 9, 'electrons': 9, '_1s': 2, '_2s': 2, '_2p': 5, '_3s': 0, '_3p': 1, '_4s': 0, '_3d': 0, '_4p': 0, '_4d': 0, '_5s': 0, '_5p': 0, '_6s': 0, '_5d': 0, '_6p': 0, '_7s': 0, 'affinity': '-322', 'density': '0.001696', 'electronegativity': '4.0', 'melt': '-219.67', 'boil': '-188.11', 'e_fusion': 'E Fusion', 'e_vapor': 'E Vapor', 't_crit': '-128.74', 'p_crit': '5.1724', 'valence': '-1', 'a_radius': '42'}
Ne = {'symbol': 'Ne', 'name': 'Neon', 'atomic_number': 10, 'mass': '20.1797', 'period': 2, 'row': 2, 'column': 18, '_group': '8A', 'protons': 10, 'neutrons': 10, 'electrons': 10, '_1s': 2, '_2s': 2, '_2p': 6, '_3s': 0, '_3p': 0, '_4s': 0, '_3d': 0, '_4p': 0, '_4d': 0, '_5s': 0, '_5p': 0, '_6s': 0, '_5d': 0, '_6p': 0, '_7s': 0, 'affinity': '30', 'density': '0.000900', 'electronegativity': '0.0', 'melt': '-248.59', 'boil': '-246.046', 'e_fusion': 'E Fusion', 'e_vapor': 'E Vapor', 't_crit': '-228.6580', 'p_crit': '26.86', 'valence': '0', 'a_radius': '38'}
Na = {'symbol': 'Na', 'name': 'Sodium', 'atomic_number': 11, 'mass': '22.989770', 'period': 3, 'row': 3, 'column': 1, '_group': '1A', 'protons': 11, 'neutrons': 11, 'electrons': 11, '_1s': 2, '_2s': 2, '_2p': 6, '_3s': 1, '_3p': 0, '_4s': 0, '_3d': 0, '_4p': 0, '_4d': 0, '_5s': 0, '_5p': 0, '_6s': 0, '_5d': 0, '_6p': 0, '_7s': 0, 'affinity': '-53', 'density': '0.968', 'electronegativity': '0.9', 'melt': '97.794', 'boil': '882.940', 'e_fusion': 'E Fusion', 'e_vapor': 'E Vapor', 't_crit': '2300', 'p_crit': '35', 'valence': '1', 'a_radius': '190'}
Mg = {'symbol': 'Mg', 'name': 'Magnesium', 'atomic_number': 12, 'mass': '24.3050', 'period': 3, 'row': 3, 'column': 2, '_group': '2A', 'protons': 12, 'neutrons': 12, 'electrons': 12, '_1s': 2, '_2s': 2, '_2p': 6, '_3s': 2, '_3p': 0, '_4s': 0, '_3d': 0, '_4p': 0, '_4d': 0, '_5s': 0, '_5p': 0, '_6s': 0, '_5d': 0, '_6p': 0, '_7s': 0, 'affinity': '230', 'density': '1.738', 'electronegativity': '1.2', 'melt': '650', 'boil': '1090', 'e_fusion': 'E Fusion', 'e_vapor': 'E Vapor', 't_crit': 'NULL', 'p_crit': 'NULL', 'valence': '2', 'a_radius': '145'}
Al = {'symbol': 'Al', 'name': 'Aluminum', 'atomic_number': 13, 'mass': '26.981538', 'period': 3, 'row': 3, 'column': 13, '_group': '3A', 'protons': 13, 'neutrons': 13, 'electrons': 13, '_1s': 2, '_2s': 2, '_2p': 6, '_3s': 2, '_3p': 1, '_4s': 0, '_3d': 0, '_4p': 0, '_4d': 0, '_5s': 0, '_5p': 0, '_6s': 0, '_5d': 0, '_6p': 0, '_7s': 0, 'affinity': '-44', 'density': '2.7', 'electronegativity': '1.5', 'melt': '660.323', 'boil': '2519', 'e_fusion': 'E Fusion', 'e_vapor': 'E Vapor', 't_crit': '6427', 'p_crit': 'NULL', 'valence': '3', 'a_radius': '118'}
Si = {'symbol': 'Si', 'name': 'Silicon', 'atomic_number': 14, 'mass': '28.0855', 'period': 3, 'row': 3, 'column': 14, '_group': '4A', 'protons': 14, 'neutrons': 14, 'electrons': 14, '_1s': 2, '_2s': 2, '_2p': 6, '_3s': 2, '_3p': 2, '_4s': 0, '_3d': 0, '_4p': 0, '_4d': 0, '_5s': 0, '_5p': 0, '_6s': 0, '_5d': 0, '_6p': 0, '_7s': 0, 'affinity': '-120', 'density': '2.330', 'electronegativity': '1.8', 'melt': '1414', 'boil': '3265', 'e_fusion': 'E Fusion', 'e_vapor': 'E Vapor', 't_crit': 'NULL', 'p_crit': 'NULL', 'valence': '4', 'a_radius': '111'}
P = {'symbol': 'P', 'name': 'Phosphorus', 'atomic_number': 15, 'mass': '30.973761', 'period': 3, 'row': 3, 'column': 15, '_group': '5A, 7A', 'protons': 15, 'neutrons': 15, 'electrons': 15, '_1s': 2, '_2s': 2, '_2p': 6, '_3s': 2, '_3p': 3, '_4s': 0, '_3d': 0, '_4p': 0, '_4d': 0, '_5s': 0, '_5p': 0, '_6s': 0, '_5d': 0, '_6p': 0, '_7s': 0, 'affinity': '-74', 'density': '1.823', 'electronegativity': '2.1', 'melt': '44.15 579.2', 'boil': '280.5 431', 'e_fusion': 'E Fusion', 'e_vapor': 'E Vapor', 't_crit': '721', 'p_crit': 'NULL', 'valence': '5 3 -3', 'a_radius': '98'}
S = {'symbol': 'S', 'name': 'Sulfur', 'atomic_number': 16, 'mass': '32.065', 'period': 3, 'row': 3, 'column': 16, '_group': '6A', 'protons': 16, 'neutrons': 16, 'electrons': 16, '_1s': 2, '_2s': 2, '_2p': 6, '_3s': 2, '_3p': 4, '_4s': 0, '_3d': 0, '_4p': 0, '_4d': 0, '_5s': 0, '_5p': 0, '_6s': 0, '_5d': 0, '_6p': 0, '_7s': 0, 'affinity': '-201', 'density': '1.960', 'electronegativity': '2.5', 'melt': '95.2 115.21', 'boil': '4461', 'e_fusion': 'E Fusion', 'e_vapor': 'E Vapor', 't_crit': '1041', 'p_crit': 'NULL', 'valence': '6 4 -2', 'a_radius': '88'}
Cl = {'symbol': 'Cl', 'name': 'Chlorine', 'atomic_number': 17, 'mass': '35.453', 'period': 3, 'row': 3, 'column': 17, '_group': '7A', 'protons': 17, 'neutrons': 17, 'electrons': 17, '_1s': 2, '_2s': 2, '_2p': 6, '_3s': 2, '_3p': 5, '_4s': 0, '_3d': 0, '_4p': 0, '_4d': 0, '_5s': 0, '_5p': 0, '_6s': 0, '_5d': 0, '_6p': 0, '_7s': 0, 'affinity': '-348', 'density': '0.003214', 'electronegativity': '3.0', 'melt': '-101.5', 'boil': '-34.03', 'e_fusion': 'E Fusion', 'e_vapor': 'E Vapor', 't_crit': '143.9', 'p_crit': '78.1', 'valence': '7 5 3 1 -1', 'a_radius': '79'}

H = {"symbol": "H", "name": "Hydrogen", "Atomic Number": 1, "Atomic Mass": 1.008, "Period": 1, "Row": 1,
     "Column": "1,7", "Group": "1A 7A", "Protons": 1, "Neutrons": 0, "Electrons": 1, "_1s": 1, "_2s": 0,
     "_2p": 0, "_3s": 0, "_3p": 0, "_3d": 0, "_4s": 0, "_4p": 0, "_4d": 0, "-4f": 0, "Affinity": -72,
     "Density": 0, "Electronegativity": 0, "Melting": -259.15, "Boiling": -252.879, "E Fusion": 0, "E Vapor": 0,
     "Temp Crit": -259.3467, "Press Crit": 7.041, "Valence": "1 -1"}
H = {'symbol': 'H', 'name': 'hydrogen', 'atomic_number': 1, 'mass': '1', 'period': 1, 'row': 1, 'column': 1,
     '_group': '1A', 'protons': 1, 'neutrons': 0, 'electrons': 1, '_1s': 1, '_2s': 0, '_2p': 0, '_3s': 0,
     '_3p': 0, '_3d': 0, '_4s': 0, '_4p': 0, '_4d': 0, '_4f': 0, 'affinity': '2', 'density': '2',
     'electronegativity': '2', 'melt': '-259.15', 'boil': '-252.879', 'e_fusion': '121', 'e_vapor': '131', 't_crit': '25',
     'p_crit': '35', 'valance': '1 -1'}
    H = Element('H','Hydrogen','1','1.008','1','1','1','1A 7A','1','0','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','-72','0.00008988','2.1','14.01','-252.76','ef','ev','-240.17','12.77','1 -1','53')
    He = Element('He', 'Helium', '2', '4.002602', '1', '1', '18', '8A', '2', '2', '2', '2', '0','0','0','0','0','0','0','0', '0', '0', '0', '0', '0', '0', '20', '0.0001785', '0.0', 'NULL', '-268.94', 'E Fusion', 'E Vapor', '-267.9550', '2.261', '0','31')
    Li = Element('Li', 'Lithium', '3', '6.941', '2', '2', '1', '1A', '3', '3', '3', '2', '1', '0','0','0','0','0','0', '0', '0', '0', '0', '0', '0', '0', '-60', '0.535', '1.0', '180.50', '1342', 'E Fusion', 'E Vapor', '2950', '67', '1','167')
    Be = Element('Be', 'Beryllium', '4', '9.012182', '2', '2', '2', '2A', '4', '4', '4', '2', '2', '0', '0','0','0','0','0','0','0', '0', '0', '0', '0',  '0', '240', '1.848', '1.5', '1287', '2468', 'E Fusion', 'E Vapor', '4932', 'NULL', '2',112)
    B = Element('B', 'Boron', '5', '10.8111', '2', '2', '13', '3A', '5', '5', '5', '2', '2', '1', '0', '0', '0','0','0','0','0','0','0', '0', '0', '0',  '-23', '2.460', '2.0', '2077', '4000', 'E Fusion', 'E Vapor', 'NULL', 'NULL', '3',87)
    C = Element('C', 'Carbon', '6', '12.0107', '2', '2', '14', '4A', '6', '6', '6', '2', '2', '2', '0', '0', '0','0','0','0','0','0','0', '0', '0', '0', '-123', '2.260', '2.5', '4489', '3825', 'E Fusion', 'E Vapor', 'NULL', 'NULL', '4 3 2 1 0 -1 -2 -3 -4',67)
    N = Element('N', 'Nitrogen', '7', '14.0087', '2', '2', '15', '5A', '7', '7', '7', '2', '2', '3', '0', '0', '0','0','0','0','0','0','0', '0', '0', '0', '0', '0.001251', '3.0', '-210.0', '-195.795', 'E Fusion', 'E Vapor', '-146.89', '33.54', '5 4 3 2 1 -1 -2 -3',56)
    O = Element('O', 'Oxygen', '8', '15.9994', '2', '2', '16', '6A', '8', '8', '8', '2', '2', '4', '0', '0', '0', '0','0','0','0','0','0','0', '0', '0', '-141', '0.001429', '3.5', '-218.79', '-182.962', 'E Fusion', 'E Vapor', '-118.38', '50.14', '-1 -2',48)
    F = Element('F', 'Fluorine', '9', '18.9984032', '2', '2', '17', '7A', '9', '9', '9', '2', '2', '5', '0', '1', '0','0','0','0','0','0','0', '0', '0', '0', '-322', '0.001696', '4.0', '-219.67', '-188.11', 'E Fusion', 'E Vapor', '-128.74', '5.1724', '-1',42)
    Ne = Element('Ne', 'Neon', '10', '20.1797', '2', '2', '18', '8A', '10', '10', '10', '2', '2', '6', '0', '0', '0','0','0','0','0','0','0', '0', '0', '0', '30', '0.000900', '0.0', '-248.59', '-246.046', 'E Fusion', 'E Vapor', '-228.6580', '26.86', '0',38)
    Na = Element('Na', 'Sodium', '11', '22.989770', '3', '3', '1', '1A', '11', '11', '11', '2', '2', '6', '1', '0', '0','0','0','0','0','0','0', '0', '0', '0', '-53', '0.968', '0.9', '97.794', '882.940', 'E Fusion', 'E Vapor', '2300', '35', '1',190)
    Mg = Element('Mg', 'Magnesium', '12', '24.3050', '3', '3', '2', '2A', '12', '12', '12', '2', '2', '6', '2', '0','0','0','0','0','0', '0','0', '0', '0', '0', '230', '1.738', '1.2', '650', '1090', 'E Fusion', 'E Vapor', 'NULL', 'NULL', '2',145)
    Al = Element('Al', 'Aluminum', '13', '26.981538', '3', '3', '13', '3A', '13', '13', '13', '2', '2', '6', '2', '1', '0', '0', '0','0','0','0','0','0', '0', '0', '-44', '2.7', '1.5', '660.323', '2519', 'E Fusion', 'E Vapor', '6427', 'NULL', '3',118)
    Si = Element('Si', 'Silicon', '14', '28.0855', '3', '3', '14', '4A', '14', '14', '14', '2', '2', '6', '2', '2', '0', '0', '0', '0','0','0','0','0','0', '0', '-120', '2.330', '1.8', '1414', '3265', 'E Fusion', 'E Vapor', 'NULL', 'NULL', '4',111)
    P = Element('P', 'Phosphorus', '15', '30.973761', '3', '3', '15', '5A, 7A', '15', '15', '15', '2', '2', '6', '2', '3', '0', '0', '0','0','0','0','0','0','0', '0', '-74', '1.823', '2.1', '44.15 579.2', '280.5 431', 'E Fusion', 'E Vapor', '721', 'NULL', '5 3 -3',98)
    S = Element('S', 'Sulfur', '16', '32.065', '3', '3', '16', '6A', '16', '16', '16', '2', '2', '6', '2', '4', '0','0','0','0','0','0', '0', '0','0', '0', '-201', '1.960', '2.5', '95.2 115.21', '4461', 'E Fusion', 'E Vapor', '1041', 'NULL', '6 4 -2',88)
    Cl = Element('Cl', 'Chlorine', '17', '35.453', '3', '3', '17', '7A', '17', '17', '17', '2', '2', '6', '2', '5', '0', '0', '0', '0','0','0','0','0','0', '0', '-348', '0.003214', '3.0', '-101.5', '-34.03', 'E Fusion', 'E Vapor', '143.9', '78.1', '7 5 3 1 -1',79)
    Ar = Element('Ar', 'Argon', '18', '39.948', '3', '3', '18', '8A', '18', '18', '18', '2', '2', '6', '2', '6', '0', '0', '0', '0','0','0','0','0','0', '0', '35', '0.001784', '0.0', '-189.34', '-185.854', 'E Fusion', 'E Vapor', '-122.463', '4.863', '0',71)
    K = Element('K', 'Potassium', '19', '39.0983', '4', '4', '1', '1A', '19', '19', '19', '2', '2', '6', '2', '6', '0', '1', '0', '0','0','0','0','0','0', '0', '-48', '0.856', '0.8', '63.5', '759', 'E Fusion', 'E Vapor', '1950', '16', '1',243)
    Ca = Element('Ca', 'Calcium', '20', '40.078', '4', '4', '2', '2A', '20', '20', '20', '2', '2', '6', '2', '6', '0', '2', '0', '0', '0','0','0','0','0','0', '150', '1.550', '1.0', '842', '1484', 'E Fusion', 'E Vapor', 'NULL', 'NULL', '2',194)
    Sc = Element('Sc', 'Scandium', '21', '44.955910', '4', '4', '3', '3B', '21', '21', '21', '2', '2', '6', '2', '6', '1', '2', '0', '0','0','0','0','0','0', '0', 'NULL', '2.985', '1.3', '1541', '2836', 'E Fusion', 'E Vapor', 'NULL', 'NULL', 'NULL',184)
    Ti = Element('Ti', 'Titanium', '22', '47.867', '4', '4', '4', '4B', '22', '22', '22', '2', '2', '6', '2', '6', '2', '2', '2', '0','0','0','0','0','0', '0', 'NULL', '4.507', '1.5', '1670', '3287', 'E Fusion', 'E Vapor', 'NULL', 'NULL', 'NULL',176)
    V = Element('V', 'Vanadium', '23', '50.9415', '4', '4', '5', '5B', '23', '23', '23', '2', '2', '6', '2', '6', '3', '2', '0', '0','0','0','0','0','0', '0', 'NULL', '6.110', '1.6', '1910', '3407', 'E Fusion', 'E Vapor', 'NULL', 'NULL', 'NULL',171)
    Cr = Element('Cr', 'Chromium', '24', '51.9961', '4', '4', '6', '6B', '24', '24', '24', '2', '2', '6', '2', '6', '5', '1', '0', '0','0','0','0','0','0', '0', 'NULL', '7.140', '1.6', '1907', '2671', 'E Fusion', 'E Vapor', 'NULL', 'NULL', 'NULL',166)
    Mn = Element('Mn', 'Manganese', '25', '54.938049', '4', '4', '7', '7B', '25', '25', '25', '2', '2', '6', '2', '6', '5', '2', '0', '0','0','0','0','0','0', '0', 'NULL', '7.470', '1.5', '1246', '2061', 'E Fusion', 'E Vapor', '4052', 'NULL', 'NULL',161)
    Fe = Element('Fe', 'Iron', '26', '55.845', '4', '4', '8', '8B', '26', '26', '26', '2', '2', '6', '2', '6', '6', '6', '2', '0','0','0','0','0','0', '0', 'NULL', '7.874', '1.8', '1538', '2861', 'E Fusion', 'E Vapor', '9067', 'NULL', 'NULL',156)
    Co = Element('Co', 'Cobalt', '27', '58.9932', '4', '4', '9', '8B', '27', '27', '27', '2', '2', '6', '2', '6', '7', '2', '0', '0','0','0','0','0','0', '0', 'NULL', '8.9', '1.9', '1495', '2927', 'E Fusion', 'E Vapor', 'NULL', 'NULL', 'NULL',152)
    Ni = Element('Ni', 'Nickel', '28', '58.6934', '4', '4', '10', '8B', '28', '28', '28', '2', '2', '6', '2', '6', '8', '2', '0', '0','0','0','0','0','0', '0', 'NULL', '8.908', '1.9', '1455', '2913', 'E Fusion', 'E Vapor', 'NULL', 'NULL', 'NULL',149)
    Cu = Element('Cu', 'Copper', '29', '63.546', '4', '4', '11', '1B', '29', '29', '29', '2', '2', '6', '2', '6', '10', '1', '0', '0','0','0','0','0','0', '0', 'NULL', '8.920', '1.9', '1084.62', '2560', 'E Fusion', 'E Vapor', 'NULL', 'NULL', 'NULL',145)
    Zn = Element('Zn', 'Zinc', '30', '65.409', '4', '4', '12', '2B', '30', '30', '30', '2', '2', '6', '2', '6', '10', '2', '0', '0','0','0','0','0','0', '0', 'NULL', '7.140', '1.6', '419.527', '907', 'E Fusion', 'E Vapor', 'NULL', 'NULL', 2,142)
    Ga = Element('Ga', 'Gallium', '31', '69.723', '4', '4', '13', '3A', '31', '31', '31', '2', '2', '6', '2', '6', '2', '10', '1', '0','0','0','0','0','0', '0', '-40', '5.904', '1.6', '29.7646', '2229', 'E Fusion', 'E Vapor', 'NULL', 'NULL', 3,136)
    Ge = Element('Ge', 'Germanium', '32', '72.64', '4', '4', '14', '4A', '32', '32', '32', '2', '2', '6', '2', '6', '10', '2', '2', '0','0','0','0','0','0', '0', '-116', '5.323', '1.8', '938.25', '2833', 'E Fusion', 'E Vapor', 'Temp Crit', 'Press Crit', 4,125)
    As = Element('As', 'Arsenic', '33', '74.92160', '4', '4', '15', '5A', '33', '33', '33', '2', '2', '6', '2', '6', '10', '2', '3', '0','0','0','0','0','0', '0', '-77', '5.727', '2.0', '817', '616', 'E Fusion', 'E Vapor', 'Temp Crit', 'Press Crit', '5 3 -3',114)
    Se = Element('Se', 'Selenium', '34', '778.96', '4', '4', '16', '6A', '34', '34', '34', '2', '2', '6', '2', '6', '10', '2', '4', '0','0','0','0','0','0', '0', '-195', '4.819', '2.4', '220.8', '685', 'E Fusion', 'E Vapor', 'Temp Crit', 'Press Crit', '6 4 -2',103)
    Br = Element('Br', 'Bromine', '35', '79.904', '4', '4', '17', '7A', '35', '35', '35', '2', '2', '6', '2', '6', '10', '2', '5', '0','0','0','0','0','0', '0', '-324', '3.120', '2.8', '-7.2', '58.8', 'E Fusion', 'E Vapor', 'Temp Crit', 'Press Crit', '7 5 3 1 -1',94)
    Kr = Element('Kr', 'Krypton', '36', '83.798', '4', '4', '18', '8A', '36', '36', '36', '2', '2', '6', '2', '6', '10', '2', '6', '0','0','0','0','0','0', '0', '40', '0.00375', '0', '-157.37', '-153.415', 'E Fusion', 'E Vapor', 'Temp Crit', 'Press Crit', '4 2',88)
    Rb = Element('Rb', 'Rubidium', '37', '85.4678', '5', '5', '1', '1A', '37', '37', '37', '2', '2', '6', '2', '6', '10', '2', '6', '1','0','0','0','0','0', '0', '-46', '1.532', '0.8', '39.30', '688', 'E Fusion', 'E Vapor', 'Temp Crit', 'Press Crit', '1',265)
    Sr = Element('Sr', 'Strontium', '38', '87.62', '5', '5', '2', '2A', '38', '38', '38', '2', '2', '6', '2', '6', '10', '2', '6', '2', '0','0','0','0','0','0', '160', '2.630', '1.0', '777', '1377', 'E Fusion', 'E Vapor', 'Temp Crit', 'Press Crit', '2',219)
    Y = Element('Y', 'Yttrium', '39', '88.90585', '5', '5', '3', '3B', '39', '39', '30', '2', '2', '6', '2', '6', '10', '10', '6', '2', '1','0','0','0','0','0', 'NULL', '4.472', '1.2', '1522', '3345', 'E Fusion', 'E Vapor', 'Temp Crit', 'Press Crit', 'NULL',212)
    Zr = Element('Zr', 'Zirconium', '40', '91.224', '5', '5', '4', '4B', '40', '40', '40', '2', '2', '6', '2', '6', '10', '2', '6', '2', '2','0','0','0','0','0', 'NULL', '6.511', '1.4', '1854', '4406', 'E Fusion', 'E Vapor', 'Temp Crit', 'Press Crit', 'NULL',206)
    Nb = Element('Nb', 'Niobium', '41', '92.90638', '5', '5', '5', '5B', '41', '41', '41', '2', '2', '6', '2', '6', '10', '2', '6', '4', '1','0','0','0','0','0', 'NULL', '8.570', '1.6', '2477', '4741', 'E Fusion', 'E Vapor', 'Temp Crit', 'Press Crit', 'NULL',198)
    Mo = Element('Mo', 'Molybdenum', '42', '95.94', '5', '5', '6', '6B', '42', '42', '42', '2', '2', '6', '2', '6', '10', '2', '6', '5', '1','0','0','0','0','0', 'NULL', '10.280', '1.8', '2622', '4639', 'E Fusion', 'E Vapor', 'Temp Crit', 'Press Crit', 'NULL',190)
    Tc = Element('Tc', 'Technetium', '43', '98', '5', '5', '7', '7B', '43', '43', '43', '2', '2', '6', '2', '6', '10', '2', '6', '6', '1','0','0','0','0','0', 'NULL', '11.5', '1.9', '2157', '4262', 'E Fusion', 'E Vapor', 'Temp Crit', 'Press Crit', 'NULL',183)
    Ru = Element('Ru', 'Ruthenium', '44', '101.07', '5', '5', '8', '8B', '44', '44', '44', '2', '2', '6', '2', '6', '2', '10', '6', '7', '1','0','0','0','0','0', 'NULL', '12.370', '2.2', '2333', '4147', 'E Fusion', 'E Vapor', 'Temp Crit', 'Press Crit', 'NULL',178)
    Rh = Element('Rh', 'Rhodium', '45', '102.90550', '5', '5', '9', '8B', '45', '45', '45', '2', '2', '6', '2', '6', '2', '10', '6', '8', '1','0','0','0','0','0', 'NULL', '12.450', '2.2', '1963', '3695', 'E Fusion', 'E Vapor', 'Temp Crit', 'Press Crit', 'NULL',173)
    Pd = Element('Pd', 'Palladium', '46', '106.42', '5', '5', '10', '8B', '46', '46', '46', '2', '2', '6', '2', '6', '2', '10', '6', '10', '0','0','0','0','0','0', 'NULL', '12.023', '2.2', '1554.8', '2963', 'E Fusion', 'E Vapor', 'Temp Crit', 'Press Crit', 'NULL',169)
    Ag = Element('Ag', 'Silver', '47', '107.8682', '5', '5', '11', '1B', '47', '47', '47', '2', '2', '6', '2', '6', '2', '10', '6', '10', '1','0','0','0','0','0', 'NULL', '10.490', '1.9', '961.78', '2162', 'E Fusion', 'E Vapor', '6137', 'Press Crit', 'NULL',165)
    Cd = Element('Cd', 'Cadmium', '48', '112.411', '5', '5', '12', '2B', '48', '48', '48', '2', '2', '6', '2', '6', '2', '10', '6', '10', '2','0','0','0','0','0', 'NULL', '8.650', '1.7', '321.069', '767', 'E Fusion', 'E Vapor', 'Temp Crit', 'Press Crit', '2',161)

    #conn = create_connection('chemistry_db_file')
    #select_all_elements(conn)
    #select_elements_by_symbol(conn, 'symbol')

#eci_1_mass = getattr(H, 'mass') # This works
#eci_1_mass = getattr(eci_1, 'mass') # This assignment does not work
#eci_1_mass = H.mass # This works
#eci_1_mass = eci_1.mass # This assignment does not work
#print('eci_1_mass is', eci_1_mass)

#eci_1_mass = H.get("mass")      # This works
#eci_1_mass = eci_1.get("mass")  # This assignment does not work
#Print works. Now, if the selected item is of type 'element' set the ECI to the class instance.

#cb_eci_1 = Combobox(root, textvariable=eci_1, width=30)
#cb_eci_1.grid(row=12, column=2, padx=4)
#cb_eci_1.config(font=entryfont)

#cb_eci_1_M.bind("<<ComboboxSelected>>", callback_eci_1_M)
#cb_Select_CB3['values'] = elements
#btn_Select_CB3 = Button(root, command=Synthesis(variables), text = 'Elements')
#btn_Select_CB3.grid(row=26, column=2)
#btn_Select_CB3.config(font=buttonfont)
def Synthesis(variables):
    #for items in eci_cb_values:
    #    print(items)
    #radio1() #eciRadio5.set(1)
    # print(element1)
#def fetch(variables):   #names, jobs, pay):    #variables,
    for variable in variables:
       print('Input => "%s"' % variable.get())
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
    #print('eci_temp_1_units = ', eci_temp_1_units.get())
    #print('eci_temp_1_qty = ', eci_temp_1_qty.get())
    #print('eci_press_1_units = ', eci_press_1_units.get())
    #print('eci_press_1_units = ', eci_press_1_qty.get())

def Decompose():
    pass
#make_Title_Frame('Chemistry')
#file_ops()
#set_element1()
#element1 = cb_Elements1.get()
# print('Element1 value is ', el1)    #eci1_qty
# print('Element1 quantity is ', eci1_qty)    #

#lbl_recordname_instruction = Label(text="Record name form is: Formula_Process_Location_step_totalSteps: Such as: NaCl_Synthesis_Industry_1_2")
#lbl_recordname_instruction.grid(row=3, column=0, columnspan=8)
#lbl_recordname_instruction.config(font=labelfont)

#lbl_blank = Label(root, text="", width=14)
#lbl_blank.grid(row=3, column=0)
#lbl_blank.config(font=labelfont)

#btn_Reduction = Button(root, command=Synthesis(variables), text = 'Reduction')
#btn_Reduction.grid(row=12, column=3)

#lbl_eci_2 = Label(root, text="Element, Compound or Ion number 2.")
#btn_Reduction.config(font=buttonfont)
#lbl_eci_2.grid(row=17, column=0, columnspan=2)
#lbl_eci_2.config(font=labelfont)
#lbl_eci_5 = Label(root, text="Element, Compound or Ion number 5.")
#lbl_eci_5.grid(row=17, column=4, columnspan=2)
#lbl_eci_5.config(font=labelfont)

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
#radio1()
#radio2()
#radio4()
#radio5()

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

        #eci_1_electronegativity = db[eci_1]['electronegativity']
        #eci_1_valence= db[eci_1]['valence']
        #e_Explanation.insert(eci_1)
        #print('eci_1 = ', eci_1)
        #e_Explanation.insert(tk.END, "Just a text Widget\nin two lines\n")
        #e_Explanation.insert(tk.END, str(eci_1))
        #print("db[eci_1]['mass'] is ", eci_temp_1_qty)
        #print("db[eci_1]['name'] is ", eci_1_name)
        #print("db[eci_1]['electronegativity'] is ", eci_1_electronegativity)
        #print("db[eci_1]['valence'] is ", eci_1_valence)
        #elif cb_1_type == 'compounds':

#cb_eci_1['values'] = (' January',
#monthchoosen = ttk.Combobox(window, width = 27, textvariable = n)

# Adding combobox drop down list

#cb_eci_1.bind("<<ComboboxSelected>>", callback_eci_1)
# Adding combobox drop down list
monthchoosen['values'] = (' January',
                          ' February',
                          ' March',
                          ' April',
                          ' May',
                          ' June',
                          ' July',
                          ' August',
                          ' September',
                          ' October',
                          ' November',
                          ' December')

monthchoosen.grid(column = 1, row = 5)
monthchoosen.current()
# cb_Elements1.bind("<<ComboboxSelected>>", callback_E1)

'''
