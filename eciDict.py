'''
The following is a guess at what an eci dictionary will contain.
It includes all the items needed for each frame of elements, compounds or ions.
It will hold variables essential to a process.
*** Everytime a new eci is selected, the dictionary for that frame will need to be reset
so incorrect values are not retained. ***
Also, when creating a database record of each step of the process, all of these items and
all the other process related items will be added to a process dictionary, and that dictionary
will be used to create a database record of each step of the process.
'''
eci_1 = dict(eci = 'eci_1', eci_type = "", name ="", column = "", electronegativity = "", _group = "",
             display_qty = "", qty = "", M_qty = "" , mass = "", Oxidation_State ="", display_units = "", units = "", valence = "",
             display_temp_units= "", display_temp_qty="", display_press_units= "", display_press_qty= "",
             temp_units= "", temp_qty="", press_units= "", press_qty= "")
eci_2 = dict(eci = 'eci_2', eci_type = "", name ="", column = "", electronegativity = "", _group = "",
             display_qty = "", qty = "", M_qty = "" , mass = "", Oxidation_State ="", display_units = "", units = "", valence = "",
             display_temp_units= "", display_temp_qty="", display_press_units= "", display_press_qty= "",
             temp_units= "", temp_qty="", press_units= "", press_qty= "")
eci_3 = dict(eci = 'eci_3', eci_type = "", name ="", column = "", electronegativity = "", _group = "",
             display_qty = "", qty = "", M_qty = "" , mass = "", Oxidation_State ="", display_units = "", units = "", valence = "",
             display_temp_units= "", display_temp_qty="", display_press_units= "", display_press_qty= "",
             temp_units= "", temp_qty="", press_units= "", press_qty= "")
eci_4 = dict(eci = 'eci_4', eci_type = "", name ="", column = "", electronegativity = "", _group = "",
             display_qty = "", qty = "", M_qty = "" , mass = "", Oxidation_State ="", display_units = "", units = "", valence = "",
             display_temp_units= "", display_temp_qty="", display_press_units= "", display_press_qty= "",
             temp_units= "", temp_qty="", press_units= "", press_qty= "")
eci_5 = dict(eci = 'eci_5', eci_type = "", name ="", column = "", electronegativity = "", _group = "",
             display_qty = "", qty = "", M_qty = "" , mass = "", Oxidation_State ="", display_units = "", units = "", valence = "",
             display_temp_units= "", display_temp_qty="", display_press_units= "", display_press_qty= "",
             temp_units= "", temp_qty="", press_units= "", press_qty= "")
eci_6 = dict(eci = 'eci_6', eci_type = "", name ="", column = "", electronegativity = "", _group = "",
             display_qty = "", qty = "", M_qty = "" , mass = "", Oxidation_State ="", display_units = "", units = "", valence = "",
             display_temp_units= "", display_temp_qty="", display_press_units= "", display_press_qty= "",
             temp_units= "", temp_qty="", press_units= "", press_qty= "")

eci_db = {}
eci_db['eci_1'] = eci_1
eci_db['eci_2'] = eci_2
eci_db['eci_3'] = eci_3
eci_db['eci_4'] = eci_4
eci_db['eci_5'] = eci_5
eci_db['eci_6'] = eci_6
