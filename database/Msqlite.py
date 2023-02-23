 #todo: setting up a sqlite database 
##########################
#auther: soumyajit maity
#purpose of the module: personal diy module to handle simple sqlite functionalities

##########################



def createDatabase(databaseName: str)->str:
    import os
    os.system("touch " + databaseName + ".db")
    return __path__ + " " +databaseName + ".db"

def getConnection(databaseName:str):
    import sqlite3
    con = sqlite3.connect(databaseName + '.db')
    return con.cursor()

def createTable(databaseName,tableName,tableStructure):
    database_cursor = getConnection(databaseName + '.db')
    database_cursor.execute('CREATE TABLE ' + tableName + '(' + tableStructure + ')')

def tableStructure(dataModelJSONobj) -> str:
    s = ""
    for key in dataModelJSONobj:
        s += key + " " + dataModelJSONobj[key] + notnull(True) + ","
    
    return s[:len(s)-1]
 
def notnull(b:bool)->str:
    if b: return ' NOT NULL '
    else: return 

def stringfield(size)->str:
    return "varchar({size})".format(size = size)

def IntegerField(): return "Integer"

def randomIDgenerator(s) -> int:
    ID = 0

    return  ID
