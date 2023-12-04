from connect import *

# create subroutine 
def read_films():

    # select all records from films
    dbCursor.execute("SELECT * FROM tblFilms")

    #fetch/get all records from the film table
    allRecords = dbCursor.fetchall()

    # loop through and display all records from the film table
    for eachRecord in allRecords:
        print(eachRecord)

if __name__ == "__main__":
    read_films()