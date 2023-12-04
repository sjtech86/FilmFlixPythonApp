from connect import *

# create subroutine 
def update_film():

    idField = input("Enter the filmID of the record to be updated: ")

    #ask user the field to update
    fieldName = input("Enter Title or yearReleased as field name: ").title()

    # ask the user to provide the value/data for the field they want to update 
    fieldValue = input(f"Enter the value for {fieldName} field: ")

 
    dbCursor.execute(f"UPDATE tblFilms SET {fieldName} = {fieldValue} WHERE filmID = {idField}")
    dbConnetion.commit()

    print(f"Record {idField} update from tblFilms table ")

if __name__ == "__main__":
    update_film()