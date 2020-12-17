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


def update_elements(conn, elements):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param element:
    :return: project id
    """
    sql = ''' UPDATE elements
              SET mass = ? ,
                  period = ? ,
                  row = ? ,
                  column = ? ,
                  _group = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, elements)
    conn.commit()


def main():
    database = r"C:\sqlite\db\chemistrysqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        update_elements(conn, (2, 1, 1, 2, "1A",1))


if __name__ == '__main__':
    main()
