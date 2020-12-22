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

def create_ions(conn, ions):
    """
    Create a new compound into the compounds table
    :param conn:
    :param ions:
    :return: ions id
    """
    sql = ''' INSERT INTO ions(formula, alpha, name, charge)
         VALUES(?,?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql, ions)
    conn.commit()
    return cur.lastrowid

def insert_ions(conn, ions):
    """
    Create a new compound into the compound table
    :param conn:
    :param ions:
    :return: ions id
    """

    sql = ''' INSERT INTO ions(formula, alphas='',  '', "", m_mass='', bond='', electronegativity='', density='', ('', '',
                 Vanderwaals_radius='', Ionic_radius='', Isotopes='', electronic_shell='', Energy_of_first_ionization='',
                 energy_of_second_ionization='', standard_potential='', structure='')
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, ions)
    conn.commit()
    return cur.lastrowid

def main():
    database = r"C:\sqlite\db\chemistrysqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:

        C2H3O2 = ('C2H3O2-', 'CHO', 'acetate', '-1')
        C2H3O2 = create_ions(conn, C2H3O2)
        ClO2 = ('ClO2-',  'ClO',  'chlorite',  '-1')
        ClO2 = create_ions(conn, ClO2)
        ClO3 = ('ClO3-',  'ClO',  'chlorate',  '-1')
        ClO3 = create_ions(conn, ClO3)
        ClO4 = ('ClO4-',  'ClO',  'perchlorate',  '-1')
        ClO4 = create_ions(conn, ClO4)
        CN = ('CN-',  'CN',  'cyanide',  '-1')
        CN = create_ions(conn, CN)
        CN = ('CO32-',  'CO',  'carbonate',  '-1')
        CN = create_ions(conn, CN)
        CuS = ('CuS+',  'CuS',  'copper_(II)_sulfide',  '1')
        CuS = create_ions(conn, CuS)
        FeCl2 = ('FeCl2+',  'ClFe',  'iron_(II)_chloride',  '1')
        FeCl2 = create_ions(conn, FeCl2)
        FeCl3 = ('FeCl3+',  'ClFe',  'iron_(III)_chloride',  '1')
        FeCl3 = create_ions(conn, FeCl3)
        H2PO4 = ('H2PO4-',  'HOP',  'dihydrogen_phosphate',  '-1')
        H2PO4 = create_ions(conn, H2PO4)
        HCO3 = ('HCO3-',  'CHO',  'hydrogen_carbonate',  '-1')
        HCO3 = create_ions(conn, HCO3)
        Hg2O = ('HgO+',  'HgO',  'mercury_(I)_oxide',  '1')
        Hg2O = create_ions(conn, Hg2O)
        HgO = ('HgO+',  'HgO',  'mercury_(II)_oxide',  '1')
        HgO = create_ions(conn, HgO)
        H3O = ('H3O+',  'HO',  'hydronium',  '1')
        H3O = create_ions(conn, H3O)
        HPO42 = ('HPO42-',  'HOP',  'hydrogen phosphate',  '-1')
        HPO42 = create_ions(conn, HPO42)
        HSO4 = ('HSO4-',  'HOS',  'hydrogen_sulfate',  '-1')
        HSO4 = create_ions(conn, HSO4)
        OH = ('OH-',  'HO',  'hydroxide',  '-1')
        OH = create_ions(conn, OH)
        NH4 = ('NH4+',  'HN',  'ammonium',  '1')
        NH4 = create_ions(conn, NH4)
        NO3 = ('NO3-',  'NO',  'nitrate',  '-1')
        NO3 = create_ions(conn, NO3)
        NO2 = ('NO2-',  'NO',  'nitrite',  '-1')
        NO2 = create_ions(conn, NO2)
        MNO4 = ('MNO4-',  'MNO',  'permanganate',  '-1')
        MNO4 = create_ions(conn, MNO4)
        O22 = ('O22-',  'O',  'peroxide',  '-1')
        O22 = create_ions(conn, O22)
        SO42 = ('SO42-',  'OS',  'sulfate',  '-1')
        SO42 = create_ions(conn, SO42)
        SO32 = ('SO32-',  'So',  'sulfite',  '-1')
        SO32 = create_ions(conn, SO32)
        PO43 = ('PO43-',  'PO',  'phosphate',  '-1')
        PO43 = create_ions(conn, PO43)

if __name__ == '__main__':
    main()
    # H =  (symbol= 'H',   'Hydrogen', atomic_number= 1, mass= '1.008', period= 1)
