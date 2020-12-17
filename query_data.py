import sqlite3
from sqlite3 import Error


def create_connection(chemistry_db_file):
    """ create a database connection to the SQLite database
        specified by the chemistry_db_file
    :param chemistry_db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(chemistry_db_file)
    except Error as e:
        print(e)

    return conn


def select_all_element(conn):
    """
    Query all rows in the element table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM element")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_element_by_symbol(conn, symbol):
    """
    Query elements by priority
    :param conn: the Connection object
    :param symbol:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM element WHERE symbol=?", (symbol,))

    rows = cur.fetchall()

    for row in rows:
        print(row)
rowdicts= []
def create_dictionaries(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM element") # WHERE symbol=?", (symbol,))
    colnames = [desc[0] for desc in cur.description]
    #rowdicts= []

    for row in cur.fetchall(): #    rowdicts.append(dict(zip(colnames, row)))
        # record = dict(zip(headers, row))
        # record
        # {'price': '32.20', 'name': 'AA', 'shares': '100'}
        ''' *** Use this instead of the code that follows  '''
        record = dict(zip(colnames, row))
        record
        print(record)
        # {'price': '32.20', 'name': 'AA', 'shares': '100'}
        ''' *** Use the code above instead of the code that follows  '''
        ''' *** The code that follows produces multiple lines for each row '''
        #newdict = {}
        #for symbol, val in zip(colnames, row):
        #    newdict[symbol] =val
        #    rowdicts.append(newdict)

    #print(rowdicts)
#for row in rowdicts: print(row)


def main():
    database = r"C:\sqlite\db\chemistrysqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        create_dictionaries(conn)
    for row in rowdicts: print(row)
        #print("1. Query task by priority:")
        #select_element_by_symbol(conn, 'H')

        #print("2. Query all tasks")
        #select_all_elements(conn)


if __name__ == '__main__':
    main()

'''
H = {'symbol': 'H', 'name': 'hydrogen', 'atomic_number': 1, 'mass': '1', 'period': 1, 'row': 1, 'column': 1, '_group': '1A', 'protons': 1, 'neutrons': 0, 'electrons': 1, '_1s': 1, '_2s': 0, '_2p': 0, '_3s': 0, '_3p': 0, '_3d': 0, '_4s': 0, '_4p': 0, '_4d': 0, '_4f': 0, 'affinity': '2', 'density': '2', 'electronegativity': '2', 'melt': '3', 'boil': '3', 'e_fusion': '121', 'e_vapor': '131', 't_crit': '25', 'p_crit': '35', 'lewis': 'none'},

'''
