import shelve
'''Learning process'''
class Compound:
    def __init__(self, formula, alphas='', name='', m_mass='', bond='', electronegativity='', density='', melting='', boiling='',
                 Vanderwaals_radius='', Ionic_radius='', Isotopes='', electronic_shell='', Energy_of_first_ionization='',
                 energy_of_second_ionization='', standard_potential='', structure=''):
        self.formula = formula
        self.alphas = alphas
        self.name = name
        self.m_mass  = m_mass
        self.bond  = bond
        self.electronegativity  = electronegativity
        self.density = density
        self.melting = melting
        self.boiling = boiling
        self.Vanderwaals_radius  = Vanderwaals_radius
        self.Ionic_radius = Ionic_radius
        self.Isotopes = Isotopes
        self.electronic_shell = electronic_shell
        self.Energy_of_first_ionization  = Energy_of_first_ionization
        self.energy_of_second_ionization  = energy_of_second_ionization
        self.standard_potential = standard_potential
        self.structure = structure

class Ion:
    def __init__(self, formula, alphas='', name='', charge="", m_mass='', bond='', electronegativity='', density='', melting='', boiling='',
                 Vanderwaals_radius='', Ionic_radius='', Isotopes='', electronic_shell='', Energy_of_first_ionization='',
                 energy_of_second_ionization='', standard_potential='', structure=''):
        self.formula = formula
        self.alphas = alphas
        self.name = name
        self.charge = charge
'''
    P"Al4C3BCl3BeH22HBrCaICa(OH)2CdSCH3CO2HCOCO2CsFCuSFeCl2FeCl3GaBr3HgOHg2OHNO2HNO3H2CO3H2SO3H2SO4H3PO4HC2H3O2HClHClO4HFHIH2SLiClK2SO4KBrKOHMg3N2NaClNaOHNa2ONH3NONO2N2O4N2O5H2OZZnCO3"
    "Al4C3 BCl3 BeH2 2HBr CaICa(OH)2CdSCH3CO2HCOCO2CsFCuSFeCl2FeCl3GaBr3HgOHg2OHNO2HNO3H2CO3H2SO3H2SO4H3PO4HC2H3O2HClHClO4HFHIH2SLiClK2SO4KBrKOHMg3N2NaClNaOHNa2ONH3NONO2N2O4N2O5H2OZZnCO3"
    "AlC BCl BeH HBr CaI Ca(OH) CaP CdS CHCOH CO CO CsF CuS FeCl FeCl GaBr HgO HgO HNO HNO HCO HSO HSO HPO HCHO
                                    HCl HClO HF HI HS LiCl KSO Kbr KOH MgN NaCl NaOH NaO NH NO NO NO NO HO ZnO ZnCO3"
    "CuS FeCl2 FeCl3 GaBr3 HgO Hg2O HNO2 HNO3 H2CO3 H2SO3 H2SO4 H3PO4 HC2H3O2 Hcl HclO4 HF HI H2S LiCl K2SO4
                                    Kbr KOH Mg3N2 NaCl NaOH Na2O NH3 NO NO2 N2O4 N2O5 H2O ZnO ZnCO3"
    "AcAgAlAmArAsAtAuBBaBeBiBkBrCCaCdCeCfClCmCoCrCsCuDyErEsEuFFeFmFrGaGdGeHHeHfHgHoIInIrKKrLaLiLuMgMnMoNNaNbNdNeNiNpOOsPPaPbPdPmPoPrPtPuRaRbReRhRnRuSSbScSeSiSmSnSrTaTbTcTeThTiTlTmUVWXeYYbZnZr"

'''


if __name__ == '__main__':

    #Na2SO4 = dict(formula= 'Na2SO4', elements= 'NaSO', name= 'sodium sulfate')
    Al4C3 = dict(formula= 'Al4C3', elements= 'AlC',name= 'aluminum_carbide')
    AlC3 = dict(formula= 'AlC3', elements= 'AlC',name= 'aluminum_chloride')
    Ar2He2Kr2Ne2Xe2Rn2 = dict(formula= 'Ar2He2Kr2Ne2Xe2Rn2', elements=  'ArHeKrNeXeRn', name= 'air')
    BCl3 = dict(formula= 'BCl3', elements= 'BCl',name= 'boron_trichloride')
    CH4 = dict(formula= 'CH4', elements= 'CH', name= 'methane', melting=-182.5, boiling=-161.5)
    C2H6 = dict(formula= 'C2H6', elements= 'CH', name= 'ethane', melting=-183.2, boiling=-88.6)
    C3H8 = dict(formula= 'C3H8', elements= 'CH', name= 'propane', melting=-187.7, boiling=-42.1)
    C4H10 = dict(formula= 'C4H10', elements= 'CH', name= 'butane', melting=-138.3, boiling=-0.5)
    C4H10_M = dict(formula= 'C4H10_M', elements= 'CH', name= '2-methylpropane', melting='', boiling='')
    C5H12 = dict(formula= 'C5H12', elements= 'CH', name= 'pentane', melting=-129.7, boiling=36.1)
    C6H14 = dict(formula= 'C6H14', elements= 'CH', name= 'hexane', melting=-95.3, boiling=68.7)
    C7H16 = dict(formula= 'C7H16', elements= 'CH', name= 'heptane', melting=-90.6, boiling=98.4)
    C8H18 = dict(formula= 'C8H18', elements= 'CH', name= 'octane', melting=-56.8, boiling=125.7)
    C9H20 = dict(formula= 'C9H20', elements= 'CH', name= 'nonane', melting=-53.6, boiling=150.8)
    C10H22 = dict(formula= 'C10H22', elements= 'CH', name= 'decane', melting=-29.7, boiling=174.0)
    C14H30 = dict(formula= 'C14H30', elements= 'CH', name= 'tetradecane', melting=5.9, boiling=253.5)
    C18H38 = dict(formula= 'C18H38', elements= 'CH', name= 'octadecane', melting=28.2, boiling=316.1)

    CaH2PO4 = dict(formula= 'Ca(H2PO4)2', elements= 'CaHOP',name= 'calcium_dihydrogen_phosphate')
    CaI = dict(formula= 'CaI', elements= 'CaI',name= 'calcium_iodide')
    CaOH2 = dict(formula= 'Ca(OH)2', elements= 'CaHO', name= 'calcium_hydroxide')
    Ca3P2 = dict(formula= 'Ca3P2', elements= 'CaP', name= 'calcium_phosphide')
    CdS = dict(formula= 'CdS', elements= 'CdS', name= 'cadmium_sulfide')
    CsF = dict(formula= 'CsF', elements= 'CsF', name= 'cesium_fluoride')
    C6H8O7 = dict(formula= 'C6H8O7', elements= 'CHO', name= 'citric_acid')
    CH3CO2H = dict(formula= 'CH3CO2H', elements= 'CHO', name= 'acetic_acid')
    C2H4COH = dict(formula= 'C2H4COH', elements= 'CHO', name= 'acetic_acid')
    CO = dict(formula= 'CO', elements= 'CO', name= 'carbon_monoxide')
    CO2 = dict(formula= 'CO2', elements= 'CO', name= 'carbon_dioxide')
    HBr_g = dict(formula= 'HBr_g', elements= 'BrH', name= 'hydrogen_bromide')
    HBr_aq = dict(formula= 'HBr_aq', elements= 'BrH', name= 'hydrobromic_acid')
    HC2H3O2 = dict(formula= 'HC2H3O2', elements= 'CHO', name= 'acetic_acid')
    HCl = dict(formula= 'HCl', elements= 'ClH', name= 'hydrogen_chloride')
    HCl_g = dict(formula= 'HCl_g', elements= 'ClH', name= 'hydrogen_chloride_g')
    HCl_aq = dict(formula= 'HCl_aq', elements= 'ClH', name= 'hydrochloric_acid')
    HClO4 = dict(formula= 'HClO4', elements= 'ClHO', name= 'perchloric_acid')
    HCN = dict(formula= 'HCN', elements= 'CHN', name= 'hydrogen_cyanide')
    H2CO3 = dict(formula= 'H2CO3', elements= 'CHO', name= 'carbonic_acid')

    HF_g = dict(formula= 'HF_g', elements= 'FH', name= 'hydrogen_fluoride')
    HF_aq = dict(formula= 'HF_aq', elements= 'FH', name= 'hydrofluoric_acid')
    HI_g = dict(formula= 'HI_g', elements= 'HI', name= 'hydrogen_iodide')
    HI_aq = dict(formula= 'HI_aq', elements= 'HI', name= 'hydroiodic_acid')
    HNO2 = dict(formula= 'HNO2', elements= 'HNO', name= 'nitrous_acid')
    HNO3 = dict(formula= 'HNO3', elements= 'HNO', name= 'nitric_acid')
    H3PO4 = dict(formula= 'H3PO4', elements= 'HOS', name= 'phosphoric_acid')
    H2S_g = dict(formula= 'H2S_g', elements= 'HS', name= 'hydrogen_suflide')
    H2S_aq = dict(formula= 'H2S_aq', elements= 'HS', name= 'hydrosulfuric_acid')
    H2SO3 = dict(formula= 'H2SO3', elements= 'HOS', name= 'sulfurous_acid')
    H2SO4 = dict(formula= 'H2SO4', elements= 'HOS', name= 'sulfuric_acid')
    IF7 = dict(formula= 'IF7', elements= 'FI', name= 'iodine_heptafluoride')
    KBr = dict(formula= 'KBr', elements= 'BrK', name= 'potassium_bromide')
    KOH = dict(formula= 'KOH', elements= 'HKO', name= 'potassium_hydroxide')
    LiCl = dict(formula= 'LiCl', elements= 'ClLi', name= 'lithium_chloride')
    Mg3N2 = dict(formula= 'Mg3N2', elements= 'MgN', name= 'magnesium_nitride')
    NaCl = dict(formula= 'NaCl', elements= 'ClNa', name= 'sodium_chloride')
    NaHCO3 = dict(formula= 'NaHCO33', elements= 'CHNaO)', name= 'bicarbonate_of_soda')
    Na2O = dict(formula= 'Na2O', elements= 'NaO', name= 'sodium_oxide')
    NaOH = dict(formula= 'NaOH', elements= 'HNaO', name= 'sodium_hydroxide')
    NH3 = dict(formula= 'NH3', elements= 'HN', name= 'ammonia')
    N2H4 = dict(formula= 'N2H4', elements= 'HN', name= 'hydrazine')
    NO = dict(formula= 'NO', elements= 'NO', name= 'nitric_oxide')
    NO2 = dict(formula= 'NO2', elements= 'NO', name= 'nitorgen_dioxide')
    N2O4 = dict(formula= 'N2O4', elements= 'NO', name= 'dinitrogen_tetroxide')
    N2O = dict(formula= 'N2O', elements= 'NO', name= 'nitrous_oxide')
    N2O5 = dict(formula= 'N2O5', elements= 'NO', name= 'dinitrogen_pentoxide')
    PF5 = dict(formula= 'PF5', elements= 'FP', name= 'phosphorus_pentafluoride')
    SO2 = dict(formula= 'SO2', elements= 'OS', name= 'sulfur_dioxide')
    SO3 = dict(formula= 'SO3', elements= 'OS', name= 'sulfur_trioxide')

    # Ions follow
    C2H3O2 = dict(formula= 'C2H3O2-', elements= 'CHO', name= 'acetate', charge= '-')
    ClO2 = dict(formula= 'ClO2-', elements= 'ClO', name= 'chlorite', charge= '-')
    ClO3 = dict(formula= 'ClO3-', elements= 'ClO', name= 'chlorate', charge= '-')
    ClO4 = dict(formula= 'ClO4-', elements= 'ClO', name= 'perchlorate', charge= '-')
    CN = dict(formula= 'CN-', elements= 'CN', name= 'cyanide', charge= '-')
    CO32 = dict(formula= 'CO32-', elements= 'CO', name= 'carbonate', charge= '-')
    CuS = dict(formula= 'CuS+', elements= 'CuS', name= 'copper_(II)_sulfide', charge= '+')
    FeCl2 = dict(formula= 'FeCl2+', elements= 'ClFe', name= 'iron_(II)_chloride', charge= '+')
    FeCl3 = dict(formula= 'FeCl3+', elements= 'ClFe', name= 'iron_(III)_chloride', charge= '+')
    H2PO4 = dict(formula= 'H2PO4-', elements= 'HOP', name= 'dihydrogen_phosphate', charge= '-')
    HCO3 = dict(formula= 'HCO3-', elements= 'CHO', name= 'hydrogen_carbonate', charge= '-')
    Hg2O = dict(formula= 'HgO+', elements= 'HgO', name= 'mercury_(I)_oxide', charge= '+')
    HgO = dict(formula= 'HgO+', elements= 'HgO', name= 'mercury_(II)_oxide', charge= '+')
    H3O = dict(formula= 'H3O+', elements= 'HO', name= 'hydronium', charge= '+')
    HPO42 = dict(formula= 'HPO42-', elements= 'HOP', name= 'hydrogen phosphate', charge= '-')
    HSO4 = dict(formula= 'HSO4-', elements= 'HOS', name= 'hydrogen_sulfate', charge= '-')
    OH = dict(formula= 'OH-', elements= 'HO', name= 'hydroxide', charge= '-')
    NH4 = dict(formula= 'NH4+', elements= 'HN', name= 'ammonium', charge= '+')
    NO3 = dict(formula= 'NO3-', elements= 'NO', name= 'nitrate', charge= '-')
    NO2 = dict(formula= 'NO2-', elements= 'NO', name= 'nitrite', charge= '-')
    MNO4 = dict(formula= 'MNO4-', elements= 'MNO', name= 'permanganate', charge= '-')
    O22 = dict(formula= 'O22-', elements= 'O', name= 'peroxide', charge= '-')
    SO42 = dict(formula= 'SO42-', elements= 'OS', name= 'sulfate', charge= '-')
    SO32 = dict(formula= 'SO32-', elements= 'So', name= 'sulfite', charge= '-')
    PO43 = dict(formula= 'PO43-', elements= 'PO', name= 'phosphate', charge= '-')
    # ***
'''
    #Na2SO4 = dict(formula= 'Na2SO4', elements= 'NaSO', name= 'sodium sulfate')
    Al4C3 = Compound(formula= 'Al4C3', elements= 'AlC',name= 'aluminum_carbide')
    Ar2He2Kr2Ne2Xe2Rn2 = Compound(formula= 'Ar2He2Kr2Ne2Xe2Rn2', elements=  'ArHeKrNeXeRn', name= 'air')
    BCl3 = Compound('formula= BCl3', elements= 'BCl',name= 'boron_trichloride')
    CH4 = Compound(formula= 'CH4', elements= 'CH', name= 'methane', melting=-182.5, boiling=-161.5)
    C2H6 = Compound(formula= 'C2H6', elements= 'CH', name= 'ethane', melting=-183.2, boiling=-88.6)
    C3H8 = Compound(formula= 'C3H8', elements= 'CH', name= 'propane', melting=-187.7, boiling=-42.1)
    C4H10 = Compound(formula= 'C4H10', elements= 'CH', name= 'butane', melting=-138.3, boiling=-0.5)
    C4H10_M = Compound(formula= 'C4H10_M', elements= 'CH', name= '2-methylpropane', melting='', boiling='')
    C5H12 = Compound(formula= 'C5H12', elements= 'CH', name= 'pentane', melting=-129.7, boiling=36.1)
    C6H14 = Compound(formula= 'C6H14', elements= 'CH', name= 'hexane', melting=-95.3, boiling=68.7)
    C7H16 = Compound(formula= 'C7H16', elements= 'CH', name= 'heptane', melting=-90.6, boiling=98.4)
    C8H18 = Compound(formula= 'C8H18', elements= 'CH', name= 'octane', melting=-56.8, boiling=125.7)
    C9H20 = Compound(formula= 'C9H20', elements= 'CH', name= 'nonane', melting=-53.6, boiling=150.8)
    C10H22 = Compound(formula= 'C10H22', elements= 'CH', name= 'decane', melting=-29.7, boiling=174.0)
    C14H30 = Compound(formula= 'C14H30', elements= 'CH', name= 'tetradecane', melting=5.9, boiling=253.5)
    C18H38 = Compound(formula= 'C18H38', elements= 'CH', name= 'octadecane', melting=28.2, boiling=316.1)

    CaH2PO4 = Compound(formula= 'Ca(H2PO4)2', elements= 'CaHOP',name= 'calcium_dihydrogen_phosphate')
    CaI = Compound(formula= 'CaI', elements= 'CaI',name= 'calcium_iodide')
    CaOH2 = Compound(formula= 'Ca(OH)2', elements= 'CaHO', name= 'calcium_hydroxide')
    Ca3P2 = Compound(formula= 'Ca3P2', elements= 'CaP', name= 'calcium_phosphide')
    CdS = Compound(formula= 'CdS', elements= 'CdS', name= 'cadmium_sulfide')
    CsF = Compound(formula= 'CsF', elements= 'CsF', name= 'cesium_fluoride')
    C6H8O7 = Compound(formula= 'C6H8O7', elements= 'CHO', name= 'citric_acid')
    CH3CO2H = Compound(formula= 'CH3CO2H', elements= 'CHO', name= 'acetic_acid')
    C2H4COH = Compound(formula= 'C2H4COH', elements= 'CHO', name= 'acetic_acid')
    CO = Compound(formula= 'CO', elements= 'CO', name= 'carbon_monoxide')
    CO2 = Compound(formula= 'CO2', elements= 'CO', name= 'carbon_dioxide')
    HBr_g = Compound(formula= 'HBr_g', elements= 'BrH', name= 'hydrogen_bromide')
    HBr_aq = Compound(formula= 'HBr_aq', elements= 'BrH', name= 'hydrobromic_acid')
    HC2H3O2 = Compound(formula= 'HC2H3O2', elements= 'CHO', name= 'acetic_acid')
    HCl = Compound(formula= 'HCl', elements= 'ClH', name= 'hydrogen_chloride')
    HCl_g = Compound(formula= 'HCl_g', elements= 'ClH', name= 'hydrogen_chloride_g')
    HCl_aq = Compound(formula= 'HCl_aq', elements= 'ClH', name= 'hydrochloric_acid')
    HClO4 = Compound(formula= 'HClO4', elements= 'ClHO', name= 'perchloric_acid')
    HCN = Compound(formula= 'HCN', elements= 'CHN', name= 'hydrogen_cyanide')
    H2CO3 = Compound(formula= 'H2CO3', elements= 'CHO', name= 'carbonic_acid')

    HF_g = Compound(formula= 'HF_g', elements= 'FH', name= 'hydrogen_fluoride')
    HF_aq = Compound(formula= 'HF_aq', elements= 'FH', name= 'hydrofluoric_acid')
    HI_g = Compound(formula= 'HI_g', elements= 'HI', name= 'hydrogen_iodide')
    HI_aq = Compound(formula= 'HI_aq', elements= 'HI', name= 'hydroiodic_acid')
    HNO2 = Compound(formula= 'HNO2', elements= 'HNO', name= 'nitrous_acid')
    HNO3 = Compound(formula= 'HNO3', elements= 'HNO', name= 'nitric_acid')
    H3PO4 = Compound(formula= 'H3PO4', elements= 'HOS', name= 'phosphoric_acid')
    H2S_g = Compound(formula= 'H2S_g', elements= 'HS', name= 'hydrogen_suflide')
    H2S_aq = Compound(formula= 'H2S_aq', elements= 'HS', name= 'hydrosulfuric_acid')
    H2SO3 = Compound(formula= 'H2SO3', elements= 'HOS', name= 'sulfurous_acid')
    H2SO4 = Compound(formula= 'H2SO4', elements= 'HOS', name= 'sulfuric_acid')
    IF7 = Compound(formula= 'IF7', elements= 'FI', name= 'iodine_heptafluoride')
    KBr = Compound(formula= 'KBr', elements= 'BrK', name= 'potassium_bromide')
    KOH = Compound(formula= 'KOH', elements= 'HKO', name= 'potassium_hydroxide')
    LiCl = Compound(formula= 'LiCl', elements= 'ClLi', name= 'lithium_chloride')
    Mg3N2 = Compound(formula= 'Mg3N2', elements= 'MgN', name= 'magnesium_nitride')
    NaCl = Compound(formula= 'NaCl', elements= 'ClNa', name= 'sodium_chloride')
    NaHCO3 = Compound(formula= 'NaHCO33', elements= 'CHNaO)', name= 'bicarbonate_of_soda')
    Na2O = Compound(formula= 'Na2O', elements= 'NaO', name= 'sodium_oxide')
    NaOH = Compound(formula= 'NaOH', elements= 'HNaO', name= 'sodium_hydroxide')
    NH3 = Compound(formula= 'NH3', elements= 'HN', name= 'ammonia')
    N2H4 = Compound(formula= 'N2H4', elements= 'HN', name= 'hydrazine')
    NO = Compound(formula= 'NO', elements= 'NO', name= 'nitric_oxide')
    NO2 = Compound(formula= 'NO2', elements= 'NO', name= 'nitorgen_dioxide')
    N2O4 = Compound(formula= 'N2O4', elements= 'NO', name= 'dinitrogen_tetroxide')
    N2O = Compound(formula= 'N2O', elements= 'NO', name= 'nitrous_oxide')
    N2O5 = Compound(formula= 'N2O5', elements= 'NO', name= 'dinitrogen_pentoxide')
    PF5 = Compound(formula= 'PF5', elements= 'FP', name= 'phosphorus_pentafluoride')
    SO2 = Compound(formula= 'SO2', elements= 'OS', name= 'sulfur_dioxide')
    SO3 = Compound(formula= 'SO3', elements= 'OS', name= 'sulfur_trioxide')

    db = shelve.open('chem-compounds')
    db['air'] = Ar2He2Kr2Ne2Xe2Rn2
    db['Al4C3'] = Al4C3
    db['BCl3'] = BCl3
    db['CH4'] = CH4
    db['C2H6'] = C2H6
    db['C3H8'] = C3H8
    db['C4H10'] = C4H10
    db['C4H10_M'] = C4H10_M
    db['C5H12'] = C5H12
    db['C6H14'] = C6H14
    db['C7H16'] = C7H16
    db['C8H18'] = C8H18
    db['C9H20'] = C9H20
    db['C10H22'] = C10H22
    db['C14H30'] = C14H30
    db['C18H38'] = C18H38

    db['CaH2PO4'] = CaH2PO4
    db['CaI'] = CaI
    db['CaOH2'] = CaOH2
    db['Ca3P2'] = Ca3P2
    db['CdS'] = CdS
    db['C6H8O7'] = C6H8O7
    db['CH3CO2H'] = CH3CO2H
    db['C2H4COH'] = C2H4COH
    db['CO'] = CO
    db['CO2'] = CO2
    db['HBr_g'] = HBr_g
    db['HBr_aq'] = HBr_aq
    db['HC2H3O2'] = HC2H3O2
    db['HCl'] = HCl
    db['HCl_g'] = HCl_g
    db['HCl_aq'] = HCl_aq
    db['HClO4'] = HClO4
    db['H2CO3'] = H2CO3

    #db.close()
    # formula, alphas='', name
    print(Al4C3.formula, Al4C3.alphas, Al4C3.name, BCl3.formula, BCl3.alphas, BCl3.name, CaH2PO4.formula, CaH2PO4.alphas, CaH2PO4.name)
    C2H3O2 = Ion(formula= 'C2H3O2-', elements= 'CHO', name= 'acetate', charge= '-')
    ClO2 = Ion(formula= 'ClO2-', elements= 'ClO', name= 'chlorite', charge= '-')
    ClO3 = Ion(formula= 'ClO3-', elements= 'ClO', name= 'chlorate', charge= '-')
    ClO4 = Ion(formula= 'ClO4-', elements= 'ClO', name= 'perchlorate', charge= '-')
    CN = Ion(formula= 'CN-', elements= 'CN', name= 'cyanide', charge= '-')
    CO32 = Ion(formula= 'CO32-', elements= 'CO', name= 'carbonate', charge= '-')
    CuS = Ion(formula= 'CuS+', elements= 'CuS', name= 'copper_(II)_sulfide', charge= '+')
    FeCl2 = Ion(formula= 'FeCl2+', elements= 'ClFe', name= 'iron_(II)_chloride', charge= '+')
    FeCl3 = Ion(formula= 'FeCl3+', elements= 'ClFe', name= 'iron_(III)_chloride', charge= '+')
    H2PO4 = Ion(formula= 'H2PO4-', elements= 'HOP', name= 'dihydrogen_phosphate', charge= '-')
    HCO3 = Ion(formula= 'HCO3-', elements= 'CHO', name= 'hydrogen_carbonate', charge= '-')
    Hg2O = Ion(formula= 'HgO+', elements= 'HgO', name= 'mercury_(I)_oxide', charge= '+')
    HgO = Ion(formula= 'HgO+', elements= 'HgO', name= 'mercury_(II)_oxide', charge= '+')
    H3O = Ion(formula= 'H3O+', elements= 'HO', name= 'hydronium', charge= '+')
    HPO42 = Ion(formula= 'HPO42-', elements= 'HOP', name= 'hydrogen phosphate', charge= '-')
    HSO4 = Ion(formula= 'HSO4-', elements= 'HOS', name= 'hydrogen_sulfate', charge= '-')
    OH = Ion(formula= 'OH-', elements= 'HO', name= 'hydroxide', charge= '-')
    NH4 = Compound(formula= 'NH4+', elements= 'HN', name= 'ammonium', charge= '+')
    NO3 = Ion(formula= 'NO3-', elements= 'NO', name= 'nitrate', charge= '-')
    NO2 = Ion(formula= 'NO2-', elements= 'NO', name= 'nitrite', charge= '-')
    MNO4 = Ion(formula= 'MNO4-', elements= 'MNO', name= 'permanganate', charge= '-')
    O22 = Ion(formula= 'O22-', elements= 'O', name= 'peroxide', charge= '-')
    SO42 = Ion(formula= 'SO42-', elements= 'OS', name= 'sulfate', charge= '-')
    SO32 = Ion(formula= 'SO32-', elements= 'So', name= 'sulfite', charge= '-')
    PO43 = Ion(formula= 'PO43-', elements= 'PO', name= 'phosphate', charge= '-')
    db = shelve.open('chem-ions')
    db['C2H3O2'] = C2H3O2
    db['ClO2'] = ClO2
    db['ClO3'] = ClO3
    db['CN'] = CN
    db['CuS'] = CuS
    db['FeCl2'] = FeCl2
    db['FeCl3'] = FeCl3
    db['Hg2O'] = Hg2O
    db['HgO'] = HgO
    db['H3O'] = H3O
    db['H3O'] = H3O
    db['HSO4'] = HSO4

    db['H2PO4'] = H2PO4
    db['HCO3'] = HCO3
    db['NO2'] = NO2
    db['NO2'] = NO2
    db['NO3'] = NO3
    db['OH'] = OH
'''

print(CuS.formula, CuS.alphas, CuS.name, CuS.charge)
print(FeCl2.formula, FeCl2.alphas, FeCl2.name, FeCl2.charge)
print(FeCl3.formula, FeCl3.alphas, FeCl3.name, FeCl3.charge)
''' A dictionary of compounds and their names '''
desn = {"AlCl3": "aluminum_carbide", "Ar2He2Kr2Ne2Xe2Rn2": "air", "BCl3": "boron_trichloride",
        "CH4":  "methane", "C2H6": "ethane", "C3H8": "propane", "C4H10": "butane",
        "C4H10_M": "2-methylpropane", "C5H12": "pentane", "C6H14": "hexane", "C7H16": "heptane",
        "C8H18": "octane", "C9H20": "nonane", "C10H22": "decane", "C14H30": "tetradecane",
        "C18H38": "octadecane", "CaH2PO4": "calcium_dihydrogen_phosphate", "CaI": "calcium_iodide",
        "CaOH2": "calcium_hydroxide", "Ca3P2": "calcium_phosphide", "CdS": "cadmium_sulfide",
        "CsF": "cesium_fluoride", "C6H8O7": "citric_acid", "CH3CO2H": "acetic_acid",
        "C2H4COH": "acetic_acid", "CO": "carbon_monoxide", "CO2": "carbon_dioxide",
        "HBr_g": "hydrogen_bromide", "HBr_aq": "hydrobromic_acid", "HC2H3O2": "acetic_acid",
        "HCl": "hydrogen_chloride", "HCl_g": "hydrogen_chloride", "HCl_aq": "hydrochloric_acid",
        "HClO4": "perchloric_acid", "HCN": "hydrogen_cyanide", "H2CO3": "carbonic_acid",
        "HF_g": "hydrogen_fluoride", "HF_aq": "hydrofluoric_acid", "HI_g": "hydrogen_iodide",
        "HI_aq": "hydroiodic_acid", "HNO2": "nitrous_acid", "HNO3": "nitric_acid",
        "H3PO4": "phosphoric_acid", "H2S_g": "hydrogen_suflide", "H2S_aq": "hydrosulfuric_acid",
        "H2SO3": "sulfurous_acid", "H2SO4": "sulfuric_acid", "IF7": "iodine_heptafluoride",
        "KBr": "potassium_bromide", "KOH": "potassium_hydroxide", "LiCl": "lithium_chloride",
        "Mg3N2": "magnesium_nitride", "NaCl": "sodium_chloride", "NaHCO3": "bicarbonate_of_soda",
        "Na2O": "sodium_oxide", "NaOH": "sodium_hydroxide", "NH3": "ammonia", "N2H4": "hydrazine",
        "NO": "nitric_oxide", "NO2": "nitorgen_dioxide", "N2O4": "dinitrogen_tetroxide",
        "N2O": "nitrous_oxide", "N2O5": "dinitrogen_pentoxide", "PF5": "phosphorus_pentafluoride",
        "SO2": "sulfur_dioxide", "SO3": "sulfur_trioxide"}
''' Following is an alphabetical list of elements and the compounds that are made of  those elements '''
des_list = {"AlC": "[Al4C3]", "Ar2He2Kr2Ne2Xe2Rn2": "[Ar2He2Kr2Ne2Xe2Rn2]", "BCl": "[BCl3]",
            "CH": ["CH4", "C2H6", "C3H8", "C4H10", "C4H10_M", "C5H12", "C6H14", "C7H16", "C8H18",
            "C9H20", "C10H22", "C14H30", "C18H38"]}

compound_symbols_list= ""      #Al4C3 Ar2He2Kr2Ne2Xe2Rn2 BCl3 CH4 C2H6 C3H8 C4H10 C4H10_M C5H12 C6H14 C7H16 C8H18 C9H20 C10H22 C14H30 C18H38 CaH2PO4 CaI CaOH2 Ca3P2 CdS CsF C6H8O7 CH3CO2H C2H4COH CO CO2 HBr_g HBr_aq HC2H3O2 HCl HCl_g HCl_aq HClO4 HCN H2CO3 HF_g HF_aq HI_g HI_aq HNO2 HNO3 H3PO4 H2S_g H2S_aq H2SO3 H2SO4 IF7 KBr KOH LiCl Mg3N2 NaCl NaHCO3 Na2O NaOH NH3 N2H4 NO NO2 N2O4 N2O N2O5 PF5 SO2 SO3"


for key in desn.keys():
    compound_symbols_list = compound_symbols_list  + "'"+ key + "' "

    #compound_names_list = "aluminum carbide air boron trichloride methane ethane propane butane 2-methylpropane pentane hexane heptane octane nonane decane tetradecane octadecane calcium dihydrogen phosphate calcium iodide calcium hydroxide calcium phosphide cadmium sulfide cesium fluoride citric acid acetic acid acetic acid carbon monoxide carbon dioxide hydrogen bromide hydrobromic acid acetic acid hydrogen chloride hydrogen chloride hydrochloric acid Perchloric acid hydrogen cyanide Carbonic acid hydrogen fluoride hydrofluoric acid hydrogen iodide hydroiodic acid nitrous acid nitric acid phosphoric acid hydrogen suflide hydrosulfuric acid sulfurous acid sulfuric acid iodine heptafluoride potassium bromide potassium hydroxide lithium chloride magnesium nitride sodium chloride bicarbonate of soda sodium oxide sodium hydroxide ammonia hydrazine nitric oxide nitorgen dioxide dinitrogen tetroxide nitrous oxide dinitrogen pentoxide phosphorus pentafluoride sulfur dioxide sulfur trioxide"
    compound_names_list = ""

    for value in desn.values():
        compound_names_list = compound_names_list + value + " "

    print (compound_symbols_list)
    print(compound_names_list)
    print(des_list)

    '''
    #alphabetic list of compounds that have similar alphabetic element lists
    "AlC": "[Al4C3]",
    "Ar2He2Kr2Ne2Xe2Rn2": "[Ar2He2Kr2Ne2Xe2Rn2]",
    "BCl": "[BCl3]",
    "CH": "["CH4", "C2H6", "C3H8", "C4H10", "C4H10_M", "C5H12", "C6H14", "C7H16", "C8H18",
        "C9H20", "C10H22", "C14H30", "C18H38"]"









    H = Element('H','Hydrogen', 1, 1.00794, '1A', 1, 1, 1, 0, 1, 'density', 'a_radius', 'affinity', 'electronegativity',
                'melting', 'boiling', 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
                'char', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'reserved')
    He = Element('He','Helium',  2,  4.002602,  '8A', 1, 1, 1, 0, 1, 'density', 'a_radius', 'affinity', 'electronegativity',
                'melting', 'boiling', 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
                'char', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'reserved')
    Li = Element('Li', 'Lithium',  3,  6.941,  '1A', 1, 1, 1, 0, 1, 'density', 'a_radius', 'affinity', 'electronegativity',
                'melting', 'boiling', 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
                'char', 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'reserved')

    H = Element('H','Hydrogen', 1, 1.00794, '1A', 1, 1, 1, 0, 1, 'density', 'a_radius', 'affinity', 'electronegativity',
                'melting', 'boiling', 'triple', 'e_fusion', 'e_vapor', 'temp_crit', 'press_crit',
                'char', '_1s', '_2s', '_2p', '_3s', '_3p', '_3d', '_4s', '_4p', '_4d', '_4f', 'reserved')

    db = shelve.open('class-element-shelve')
    db['H'] = H
    db['He'] = He
    db['Li'] = Li
    db.close()
    print(H.name, H.group, He.name, He.group, Li.name, Li.group)
    '''
