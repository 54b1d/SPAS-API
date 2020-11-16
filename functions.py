import glob
import os
import sqlite3


class SqliteHelper:
    # all database functions here
    # creates sqlite cursor here

    def __init__(self):
        self.dbname = get_dbname()
        self.conn = None
        self.cursor = None

        # start cursor
        self.open()

    def open(self):
        print("running open")
        try:
            self.conn = sqlite3.connect(self.dbname)
            self.cursor = self.conn.cursor()
            print('Sqlite version ' + sqlite3.version)
        except sqlite3.Error as err:
            print("Failed connecting to database..", err)


def get_dbname(directory="db"):
    # todo ask for directory if not found
    # check for existing *.db
    # list db to give selection choice
    # look for db in files with db ext
    # input new name if not available
    # returns database name as str
    databases = {}
    i = 1
    # list databases inside a directory
    os.chdir(directory)

    for dbname in glob.glob("*.db"):
        databases[i] = str(dbname)
        i += 1

    if len(databases) == 0:
        print("No database found.\nEnter a new DB name.")
        dbname = input("Name of database: ")+".db"
    else:
        print(databases)
        dbNumber = int(input("Choose a database number: "))
        while dbNumber > len(databases):
            dbNumber = int(input("Choose a valid database number: "))

    print(dbname, type(dbname))  # removeThis
    return dbname


def greetings():
    print("Welcome")
    print("You are using v0.1")


##############
# test codes #
##############
SqliteHelper()
