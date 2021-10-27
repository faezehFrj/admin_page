import sqlite3
from sqlite3 import Error
import os,sys
from datetime import datetime

dataBase_path = 'ArtaCompany.db'
database = r"ArtaCompany.db"

# def connectionToDatabase():



def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
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


def create_employee(conn, employeeTable):
    """
    Create a new employee into the employeeTable table
    :param conn:
    :param employeeTable:
    :return: employeeTable idCard
    """
    sql = ''' INSERT INTO employeeTable(idCard,firsName,lastName,finger1,finger2,statis_finger,status)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, employeeTable)
    conn.commit()
    return cur.lastrowid


def create_log(conn, logTable):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO logTable(date,timeInput,timeOutput,idCard)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, logTable)
    conn.commit()
    return cur.lastrowid


def select_all_employee(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM employeeTable")

    rows = cur.fetchall()
    #
    # for row in rows:
    #     print(row)

    return rows

#----change it to give all employee who are status 1
def select_task_by_priority(conn, idCard):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param idCard:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM employeeTable WHERE idCard=? and status = '1'", (idCard,))

    rows = cur.fetchall()
    return rows

#******select employee by idcart and return id***********#

def select_return_id(idCard):
    sqliteConnection = sqlite3.connect(dataBase_path)
    cursor = sqliteConnection.cursor()
    sqlite_select_query = """SELECT userID  from employeeTable Where idCard = ?"""
    cursor.execute(sqlite_select_query,(idCard,))
    records = cursor.fetchall()
    return records[0][0]
# *****select employee by fingerprint id ******

def select_employee_by_fingerprint(idFingerprint):
    try:
        sqliteConnection = sqlite3.connect(dataBase_path)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_select_query = """SELECT * FROM employeeTable WHERE  finger1= ? OR finger2= ?"""
        cursor.execute(sql_select_query, (idFingerprint, idFingerprint,))
        records = cursor.fetchall()
        print("Printing ID ", idFingerprint)
        return records

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)


# *******delete task ********
def delete_task(conn, userID):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = 'DELETE FROM employeeTable WHERE userID=?'
    cur = conn.cursor()
    cur.execute(sql, (userID,))
    conn.commit()



# *******update********

def updateLogTable(timeOutput, idCard):
    try:
        sqliteConnection = sqlite3.connect(dataBase_path)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sql_update_query = """Update logTable set timeOutput = ?  WHERE  idCard = ?   and (id=(SELECT MAX(id) FROM logTable))"""
        data = (timeOutput, idCard)
        cursor.execute(sql_update_query, data)
        # cursor.execute(sql_update_query)
        sqliteConnection.commit()
        print("Record Updated successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    # finally:
    #     if sqliteConnection:
    #         sqliteConnection.close()
    #         print("The SQLite connection is closed")


# *******create table in db*******

def mainCreateTable():
    # database = dataBase_path

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS employeeTable (
                                        userID integer PRIMARY KEY AUTOINCREMENT ,
                                        idCard text NOT NULL UNIQUE,
                                        firsName TEXT NOT NULL,
                                        lastName TEXT NOT NULL,
                                        finger1 TEXT ,
                                        finger2 TEXT ,
                                        statis_finger TEXT,
                                        status TEXT NOT NULL
                                    ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS logTable (
                                    id integer PRIMARY KEY AUTOINCREMENT ,
                                    date  text,
                                    timeInput   text,
                                    timeOutput  text,
                                    idCard  text ,
                                    FOREIGN KEY(idCard) REFERENCES employee(idCard) 
                                );"""

    sql_create_save_end_fingerprint = """CREATE TABLE IF NOT EXISTS fingerprintID (
                                    finalFingerprintID integer 
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)

        # create tasks table
        create_table(conn, sql_create_tasks_table)

        # create fingerprint
        create_table(conn, sql_create_save_end_fingerprint)
    else:
        print("Error! cannot create the database connection.")


# ******main create data in table ********


def maincreatedata(RFIDcode, FirstName, LastName, finger1, finger2, Status):
    # database = dataBase_path

    # create a database connection
    conn = create_connection(database)
    with conn:
        try:
            # create a new project'
            employee = (RFIDcode, FirstName, LastName, finger1, finger2, 0, Status)
            # employee = ('C6BFFDAEl', 'arashh', 'golsaz', '1')
            employee_id = create_employee(conn, employee)
            return True

        except sqlite3.IntegrityError:
            print('UNIQUE constraint failed: employeeTable.idCard')
            return False
        except Error as e:
            print(e)

        except UnboundLocalError:
            print('local variable employee_id referenced before assignment')
        except:
            print('some thing is wrong')


def mainCreateLog(date, timeEnter, timeOut, employee_id):
    # database = dataBase_path

    # create a database connection
    conn = create_connection(database)
    with conn:
        try:
            log_1 = (date, timeEnter, timeOut, employee_id)
            # create tasks
            create_log(conn, log_1)
            return 'successfull'
            print("successfull")
        except sqlite3.Error as error:
            print('some thing is wrong')
            print(error)


def mainCreatefingerprintID():
    try:
        sqliteConnection = sqlite3.connect(dataBase_path)
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")

        sqlite_insert_query = """INSERT INTO fingerprintID
                                  (finalFingerprintID) 
                                   VALUES 
                                  (1)"""

        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


# *******main select data from table **************
def mainSelectData():
    # database = dataBase_path

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Query task by priority:")
        select_task_by_priority(conn, 'ff')

        print("2. Query all tasks")
        select_all_employee(conn)


def searchIdCard(idCard):
    # database = r"D:\V2.0.0\Programme\qt\DB\ArtaDoor.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Query task by priority:")
        return select_task_by_priority(conn, idCard)


def searchIdFingerprint(idFingerprint):
    # database = r"D:\V2.0.0\Programme\qt\DB\ArtaDoor.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Query task by priority:")
        return select_task_by_priority(conn, idFingerprint)


def main_select_all_employee():
    # database = r"D:\V2.0.0\Programme\qt\DB\ArtaDoor.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("2. Query all tasks")
        return select_all_employee(conn)


def mainDeleteTask(idCard):
    # database = r"D:\V2.0.0\Programme\qt\DB\ArtaDoor.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        delete_task(conn, idCard)
        # delete_all_tasks(conn);


def selectEmployeeAndTimeIN(idCard1):
    sqliteConnection = sqlite3.connect(dataBase_path)
    cursor = sqliteConnection.cursor()
    # sqlite_select_query = """SELECT timeInput,timeOutput from employeeTable INNER JOIN logTable
    # ON employeeTable.idCard=logTable.idCard where userID =? and (id=(SELECT MAX(id) FROM logTable))"""

    sqlite_select_query = """SELECT timeInput,timeOutput from employeeTable INNER JOIN logTable 
       ON employeeTable.idCard=logTable.idCard where  (id=(SELECT MAX(id) FROM logTable where idCard = ?))"""

    cursor.execute(sqlite_select_query, (idCard1,))
    records = cursor.fetchall()
    print("Total rows are:  ", len(records))
    return records
    # for row in records:
    #     print(row)
    # cursor.close()

##for export ib excel

def create_export(userID,month):

    sqliteConnection = sqlite3.connect(dataBase_path)
    cursor = sqliteConnection.cursor()
    nMonth=month+"%"
    sqlite_select_query = """SELECT firsName,lastName,date,timeInput,timeOutput from employeeTable INNER JOIN logTable 
    ON employeeTable.idCard=logTable.idCard where userID =? and date like ? """
    cursor.execute(sqlite_select_query, (userID,nMonth,))
    records = cursor.fetchall()
    print("Total rows are:  ", len(records))
    for row in records:
        print(row)

    cursor.close()
    return records
def getAllEmployeeAndTime():
    sqliteConnection = sqlite3.connect(dataBase_path)
    cursor = sqliteConnection.cursor()
    sqlite_select_query = """SELECT userID,firsName,idCard from employeeTable"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    return records


def update_fingerprint_id(number):
    try:
        sqliteConnection = sqlite3.connect(dataBase_path)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_select_query = """Update fingerprintID set finalFingerprintID = ?"""
        cursor.execute(sql_select_query, (number,))
        sqliteConnection.commit()
        print("Record Updated successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

def select_number_fingerprint_id():
    try:
        sqliteConnection = sqlite3.connect(dataBase_path)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from fingerprintID"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        cursor.close()
        return records[0][0]

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def update_employee_select(Fname,Lname,rfidCode,idEmployee):
        try:
            sqliteConnection = sqlite3.connect(dataBase_path)
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
            sql_update_query = """Update employeeTable set firsName = ?,lastName=?,RFIDcode=?  WHERE  userID = ?)"""
            edit = (Fname, Lname,rfidCode,idEmployee)
            cursor.execute(sql_update_query, edit)
            # cursor.execute(sql_update_query)
            sqliteConnection.commit()
            print("Record Updated successfully ")
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)
        # finally:
        #     if sqliteConnection:
        #         sqliteConnection.close()
        #         print("The SQLite connection is closed")


#update number statis_finger

def update_number_status_finger(userID,number):
    try:
        sqliteConnection = sqlite3.connect(dataBase_path)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sql_update_query = """Update employeeTable set statis_finger=?  WHERE  userID = ?"""
        edit = (number,userID)
        cursor.execute(sql_update_query, edit)
        # cursor.execute(sql_update_query)
        sqliteConnection.commit()
        print("Record Updated successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    # finally:
    #     if sqliteConnection:
    #         sqliteConnection.close()
    #         print("The SQLite connection is closed")

def update_status_employee(status,userID):
    try:
        sqliteConnection = sqlite3.connect(dataBase_path)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sql_update_query = """Update employeeTable set status=?  WHERE  userID = ?"""
        cursor.execute(sql_update_query, (status,userID,))
        # cursor.execute(sql_update_query)
        sqliteConnection.commit()
        print("Record Updated successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)


if __name__ == '__main__':
    update_status_employee("0",1)
#     select_return_id("aaa")
#     r=selectEmployeeAndTimeIN(2)
#     print(r[0][0])

#     # maincreatedata("39402094","farnaz","farajzadeha","5","6","1")
#     # print(select_employee_by_fingerprint(3))
#     # getAllEmployeeAndTime()
#     # main_select_all_employee()
     #mainCreateTable()
    #mainCreatefingerprintID()
#     #print(select_number_fingerprint_id())
#     # update_fingerprint_id(4)
#     create_export(2)
#     #selectEmployeeAndTimeIN("2")
#         mainCreateLog("2021-10-18", "12:8", "12:8", "9409488")
#         mainCreateLog("2021-10-12", "12:8", "12:8", "9409488")
#         mainCreateLog("2021-10-13", "12:8", "12:8", "940948")
#         mainCreateLog("2021-09-18", "12:8", "12:8", "9409488")
#         create_export(2,"2021-10-10","2021-10-19")
