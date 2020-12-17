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


def delete_element(conn, id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the element
    :return:
    """
    sql = 'DELETE FROM elements WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()


def delete_all_elements(conn):
    """
    Delete all rows in the elements table
    :param conn: Connection to the SQLite database
    :return:
    """
    sql = 'DELETE FROM elements'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def main():
    database = r"C:\sqlite\db\chemistrysqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        delete_element(conn, 1);
        # delete_all_tasks(conn);


if __name__ == '__main__':
    main()
