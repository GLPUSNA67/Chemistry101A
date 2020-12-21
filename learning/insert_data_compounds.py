import sqlite3
from sqlite3 import Error

def create_connection(chemistry_db_file):
    """ create a database connection to the SQLite database
        specified by chemistry_db_file
    :param chemistry_db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(chemistry_db_file)
    except Error as e:
        print(e)

    return conn

def create_compound(conn, compound):
    """
    Create a new compound into the compounds table
    :param conn:
    :param compounds:
    :return: compound id
    """
    sql = ''' INSERT INTO compounds(formula, alpha, name, melting, boiling)
         VALUES(?,?,?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql, compound)
    conn.commit()
    return cur.lastrowid

def insert_compound(conn, compound):
    """
    Create a new compound into the compound table
    :param conn:
    :param compound:
    :return: compound id
    """

    sql = ''' INSERT INTO compound(formula, alphas='',  '', charge="", m_mass='', bond='', electronegativity='', density='', ('', '',
                 Vanderwaals_radius='', Ionic_radius='', Isotopes='', electronic_shell='', Energy_of_first_ionization='',
                 energy_of_second_ionization='', standard_potential='', structure='')
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, compound)
    conn.commit()
    return cur.lastrowid

def main():
    database = r"C:\sqlite\db\chemistrysqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        '''
        #formula, alphas='',  '', charge=""
        #Al4C3 = ('Al4C3', 'AlC','aluminum_carbide')
        #Al4C3 = create_compound(conn, Al4C3)
        AlCl3 = ('AlC3', 'AlC','aluminum_chloride')
        AlCl3 = create_compound(conn, AlCl3)
        Ar2He2Kr2Ne2Xe2Rn2 = ('Ar2He2Kr2Ne2Xe2Rn2','ArHeKrNeXeRn','air')
        Ar2He2Kr2Ne2Xe2Rn2 = create_compound(conn, Ar2He2Kr2Ne2Xe2Rn2)
        BCl3 = ('BCl3','BCl','boron_trichloride')
        BCl3 = create_compound(conn, BCl3)
        CaH2PO4 =  ('Ca(H2PO4)2',   'CaHOP',  'calcium_dihydrogen_phosphate')
        CaH2PO4 = create_compound(conn, CaH2PO4)
        CaI =  ('CaI',   'CaI',  'calcium_iodide')
        CaI = create_compound(conn, CaI)
        CaOH2 =  ('Ca(OH)2',   'CaHO',   'calcium_hydroxide')
        CaOH2 = create_compound(conn, CaOH2)
        Ca3P2 =  ('Ca3P2',   'CaP',   'calcium_phosphide')
        Ca3P2 = create_compound(conn, Ca3P2)
        CdS =  ('CdS',   'CdS',   'cadmium_sulfide')
        CdS = create_compound(conn, CdS)
        CsF =  ('CsF',   'CsF',   'cesium_fluoride')
        CsF = create_compound(conn, CsF)
        C6H8O7 =  ('C6H8O7',   'CHO',   'citric_acid')
        C6H8O7 = create_compound(conn, C6H8O7)
        CH3CO2H =  ('CH3CO2H',   'CHO',   'acetic_acid')
        CH3CO2H = create_compound(conn, CH3CO2H)
        C2H4COH =  ('C2H4COH',   'CHO',   'acetic_acid')
        C2H4COH = create_compound(conn, C2H4COH)
        CO =  ('CO',   'CO',   'carbon_monoxide')
        CO = create_compound(conn, CO)
        CO2 =  ('CO2',   'CO',   'carbon_dioxide')
        CO2 = create_compound(conn, CO2)
        HBr_g =  ('HBr_g',   'BrH',   'hydrogen_bromide')
        HBr_g = create_compound(conn, HBr_g)
        HBr_aq =  ('HBr_aq',   'BrH',   'hydrobromic_acid')
        HBr_aq = create_compound(conn, HBr_aq)
        HC2H3O2 =  ('HC2H3O2',   'CHO',   'acetic_acid')
        HC2H3O2 = create_compound(conn, HC2H3O2)
        HCl =  ('HCl',   'ClH',   'hydrogen_chloride')
        HCl = create_compound(conn, HCl)
        HCl_g =  ('HCl_g',   'ClH',   'hydrogen_chloride_g')
        HCl_g = create_compound(conn, HCl_g)
        HCl_aq =  ('HCl_aq',   'ClH',   'hydrochloric_acid')
        HCl_aq = create_compound(conn, HCl_aq)
        HClO4 =  ('HClO4',   'ClHO',   'perchloric_acid')
        HClO4 = create_compound(conn, HClO4)
        HCN =  ('HCN',   'CHN',   'hydrogen_cyanide')
        HCN = create_compound(conn, HCN)
        H2CO3 =  ('H2CO3',   'CHO',   'carbonic_acid')
        H2CO3 = create_compound(conn, H2CO3)
        HF_g =  ('HF_g',  'FH',   'hydrogen_fluoride')
        HF_g = create_compound(conn, HF_g)
        HF_aq =  ('HF_aq',  'FH',   'hydrofluoric_acid')
        HF_aq = create_compound(conn, HF_aq)
        HI_g =  ('HI_g',  'HI',   'hydrogen_iodide')
        HI_g = create_compound(conn, HI_g)
        HI_aq =  ('HI_aq',  'HI',   'hydroiodic_acid')
        HI_aq = create_compound(conn, HI_aq)
        HNO2 =  ('HNO2',  'HNO',   'nitrous_acid')
        HNO2 = create_compound(conn, HNO2)
        HNO3 =  ('HNO3',  'HNO',   'nitric_acid')
        HNO3 = create_compound(conn, HNO3)
        H3PO4 =  ('H3PO4',  'HOS',   'phosphoric_acid')
        H3PO4 = create_compound(conn, H3PO4)
        H2S_g =  ('H2S_g',  'HS',   'hydrogen_suflide')
        H2S_g = create_compound(conn, H2S_g)
        H2S_aq =  ('H2S_aq',  'HS',   'hydrosulfuric_acid')
        H2S_aq = create_compound(conn, H2S_aq)
        H2SO3 =  ('H2SO3',  'HOS',   'sulfurous_acid')
        H2SO3 = create_compound(conn, H2SO3)
        H2SO4 =  ('H2SO4',  'HOS',   'sulfuric_acid')
        H2SO4 = create_compound(conn, H2SO4)
        IF7 =  ('IF7',  'FI',   'iodine_heptafluoride')
        IF7 = create_compound(conn, IF7)
        KBr =  ('KBr',  'BrK',   'potassium_bromide')
        KBr = create_compound(conn, KBr)
        KOH =  ('KOH',  'HKO',   'potassium_hydroxide')
        KOH = create_compound(conn, KOH)
        LiCl =  ('LiCl',  'ClLi',   'lithium_chloride')
        LiCl = create_compound(conn, LiCl)
        Mg3N2 =  ('Mg3N2',  'MgN',   'magnesium_nitride')
        Mg3N2 = create_compound(conn, Mg3N2)
        NaCl =  ('NaCl',  'ClNa',   'sodium_chloride')
        NaCl = create_compound(conn, NaCl)
        NaHCO3 =  ('NaHCO33',  'CHNaO)',   'bicarbonate_of_soda')
        NaHCO3 = create_compound(conn, NaHCO3)
        Na2O =  ('Na2O',  'NaO',   'sodium_oxide')
        Na2O = create_compound(conn, Na2O)
        NaOH =  ('NaOH',  'HNaO',   'sodium_hydroxide')
        NaOH = create_compound(conn, NaOH)
        NH3 =  ('NH3',  'HN',   'ammonia')
        NH3 = create_compound(conn, NH3)
        N2H4 =  ('N2H4',  'HN',   'hydrazine')
        N2H4 = create_compound(conn, N2H4)
        NO =  ('NO',  'NO',   'nitric_oxide')
        NO = create_compound(conn, NO)
        NO2 =  ('NO2',  'NO',   'nitorgen_dioxide')
        NO2 = create_compound(conn, NO2)
        N2O4 =  ('N2O4',  'NO',   'dinitrogen_tetroxide')
        N2O4 = create_compound(conn, N2O4)
        N2O =  ('N2O',  'NO',   'nitrous_oxide')
        N2O = create_compound(conn, N2O)
        N2O5 =  ('N2O5',  'NO',   'dinitrogen_pentoxide')
        N2O5 = create_compound(conn, N2O5)
        PF5 =  ('PF5',  'FP',   'phosphorus_pentafluoride')
        PF5 = create_compound(conn, PF5)
        SO2 =  ('SO2',  'OS',   'sulfur_dioxide')
        SO2 = create_compound(conn, SO2)
        SO3 =  ('SO3',  'OS',   'sulfur_trioxide')
        SO3 = create_compound(conn, SO3)
        '''
        CH4 = ( 'CH4',  'CH',  'methane', -182.5, -161.5)
        CH4 = create_compound(conn, CH4)
        C2H6 = ( 'C2H6',  'CH',  'ethane', -183.2, -88.6)
        C2H6 = create_compound(conn, C2H6)
        C3H8 = ( 'C3H8',  'CH',  'propane', -187.7, -42.1)
        C3H8 = create_compound(conn, C3H8)
        C4H10 = ( 'C4H10',  'CH',  'butane', -138.3, -0.5)
        C4H10 = create_compound(conn, C4H10)
        C4H10_M = ( 'C4H10_M',  'CH',  '2-methylpropane', '', '')
        C4H10_M = create_compound(conn, C4H10_M)
        C5H12 = ( 'C5H12',  'CH',  'pentane', -129.7, 36.1)
        C5H12 = create_compound(conn, C5H12)
        C6H14 = ( 'C6H14',  'CH',  'hexane', -95.3, 68.7)
        C6H14 = create_compound(conn, C6H14)
        C7H16 = ( 'C7H16',  'CH',  'heptane', -90.6, 98.4)
        C7H16 = create_compound(conn, C7H16)
        C8H18 = ( 'C8H18',  'CH',  'octane', -56.8, 125.7)
        C8H18 = create_compound(conn, C8H18)
        C9H20 = ( 'C9H20',  'CH',  'nonane', -53.6, 150.8)
        C9H20 = create_compound(conn, C9H20)
        C10H22 = ( 'C10H22',  'CH',  'decane', -29.7, 174.0)
        C10H22 = create_compound(conn, C10H22)
        C14H30 = ( 'C14H30',  'CH',  'tetradecane', 5.9, 253.5)
        C14H30 = create_compound(conn, C14H30)
        C18H38 = ( 'C18H38',  'CH',  'octadecane', 28.2, 316.1)
        C18H38 = create_compound(conn, C18H38)
 

if __name__ == '__main__':
    main()
    # H =  (symbol= 'H',   'Hydrogen', atomic_number= 1, mass= '1.008', period= 1)
