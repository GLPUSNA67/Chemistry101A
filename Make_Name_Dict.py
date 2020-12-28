compound_names_list = ['aluminum_carbide', 'aluminum_chloride', 'air', 'boron_trichloride', 'methane', 'ethane', 'propane', 'butane', '2-methylpropane',
                    'pentane', 'hexane', 'heptane', 'octane', 'nonane', 'decane', 'tetradecane', 'octadecane', 'calcium_dihydrogen_phosphate',
                    'calcium_iodide', 'calcium_hydroxide', 'calcium_phosphide', 'cadmium_sulfide', 'cesium_fluoride', 'citric_acid',
                    'acetic_acid', 'acetic_acid', 'carbon_monoxide', 'carbon_dioxide', 'hydrogen_bromide', 'hydrobromic_acid',
                    'acetic_acid', 'hydrogen_chloride', 'hydrogen_chloride', 'hydrochloric_acid', 'perchloric_acid', 'hydrogen_cyanide',
                    'carbonic_acid', 'hydrogen_fluoride', 'hydrofluoric_acid', 'hydrogen_iodide', 'hydroiodic_acid', 'nitrous_acid',
                    'nitric_acid', 'phosphoric_acid', 'hydrogen_suflide', 'hydrosulfuric_acid', 'sulfurous_acid', 'sulfuric_acid',
                    'iodine_heptafluoride', 'potassium_bromide', 'potassium_hydroxide', 'lithium_chloride', 'magnesium_nitride',
                    'sodium_chloride', 'bicarbonate_of_soda', 'sodium_oxide', 'sodium_hydroxide', 'sodium_sulfate', 'ammonia', 'hydrazine', 'nitric_oxide',
                    'nitorgen_dioxide', 'dinitrogen_tetroxide', 'nitrous_oxide', 'dinitrogen_pentoxide', 'phosphorus_pentafluoride',
                    'sulfur_dioxide', 'sulfur_trioxide']

compound_symbols_list = ['Al4C3', 'AlCl3', 'Ar2He2Kr2Ne2Xe2Rn2', 'BCl3', 'CH4', 'C2H6', 'C3H8', 'C4H10', 'C4H10_M', 'C5H12', 'C6H14', 'C7H16', 'C8H18',
                         'C9H20', 'C10H22', 'C14H30', 'C18H38', 'CaH2PO4', 'CaI', 'CaOH2', 'Ca3P2', 'CdS', 'CsF', 'C6H8O7', 'CH3CO2H', 'C2H4COH',
                         'CO', 'CO2', 'HBr_g', 'HBr_aq', 'HC2H3O2', 'HCl', 'HCl_g', 'HCl_aq', 'HClO4', 'HCN', 'H2CO3', 'HF_g', 'HF_aq', 'HI_g', 'HI_aq',
                         'HNO2', 'HNO3', 'H3PO4', 'H2S_g', 'H2S_aq', 'H2SO3', 'H2SO4', 'IF7', 'KBr', 'KOH', 'LiCl', 'Mg3N2', 'NaCl', 'NaHCO3', 'Na2O', 'NaOH',
                         'Na2SO4', 'NH3', 'N2H4', 'NO', 'NO2', 'N2O4', 'N2O', 'N2O5', 'PF5', 'SO2', 'SO3']

compound_names_Dict = {}
for (k,v) in zip(compound_names_list, compound_symbols_list):
    compound_names_Dict[k] = v

print(compound_names_Dict)
