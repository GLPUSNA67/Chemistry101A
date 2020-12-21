import sqlite3
from sqlite3 import Error

def create_connection(chemistry_db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(chemistry_db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"C:\sqlite\db\chemistrysqlite.db"
#_1s,_2s,_2p,_3s,_3p,_4s,_3d,_4p,_4d,_5s,_5p,_6s,_5d,_6p,_7s,affinity,density,electronegativity
    # ,melt,boil,e_fusion,e_vapor,t_crit,p_crit,valence,a_radius)
    sql_create_element_table = """ CREATE TABLE IF NOT EXISTS element (
                                        id integer PRIMARY KEY,
                                        symbol text,
                                        name text,
                                        atomic_number integer,
                                        mass text,
                                        period integer,
                                        row integer,
                                        column integer,
                                        _group text,
                                        protons integer,
                                        neutrons integer,
                                        electrons integer,
                                        _1s integer,
                                        _2s integer,
                                        _2p integer,
                                        _3s integer,
                                        _3p integer,
                                        _4s integer,
                                        _3d integer,
                                        _4p integer,
                                        _4d integer,
                                        _5s integer,
                                        _5p integer,
                                        _6s integer,
                                        _5d integer,
                                        _6p integer,
                                        _7s integer,
                                        affinity text,
                                        density text,
                                        electronegativity text,
                                        melt text,
                                        boil text,
                                        e_fusion text,
                                        e_vapor text,
                                        t_crit text,
                                        p_crit text,
                                        valence text,
                                        a_radius text
                                    ); """

    sql_create_compounds_table = """ CREATE TABLE IF NOT EXISTS compounds (
                                        id integer PRIMARY KEY,
                                        formula text,
                                        name text,      
                                        alpha text
                                        m_mass text,
                                        bond text,
                                        electronegativity text,
                                        density text,
                                        melting text,
                                        boiling text,
                                        Vanderwaals_radius text,
                                        Ionic_radius text,
                                        Isotopes text,
                                        electronic_shell text,
                                        Energy_of_first_ionization text,
                                        energy_of_second_ionization text,
                                        standard_potential text,
                                        structure text
                                    ); """

    sql_create_ions_table = """ CREATE TABLE IF NOT EXISTS ions (
                                        id integer PRIMARY KEY,
                                        name text,
                                        formula text,
                                        alpha text,
                                        charge text
                                    ); """

    sql_create_processes_table = """CREATE TABLE IF NOT EXISTS processes (
                                    id integer PRIMARY KEY,
                                    name text,
                                    process text,
                                    environment text,
                                    eci_1_type text,
                                    eci_1 text
                                );"""
    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:

        #create_table(conn, sql_create_element_table)
        create_table(conn, sql_create_compounds_table)
        create_table(conn, sql_create_ions_table)
        #create_table(conn, sql_create_processes_table)

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()

'''


    sql_create_processes_table = """CREATE TABLE IF NOT EXISTS processes (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    process text NOT NULL,
                                    environment text NOT NULL,
                                    eci_1_type text NOT NULL,
                                    eci_1 text NOT NULL
                                );"""
        # create processes table
        create_table(conn, sql_create_processes_table)

                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
'''
