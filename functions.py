import glob
import os


class SqliteHelper:
    # setup software environment
    def __init__(self):
        # check if db exists
        self.dbname = get_dbname()


def get_dbname(directory="db"):
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
        dbname = input("Name of database: ")
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
