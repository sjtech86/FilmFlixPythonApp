from connect import *

# create subroutine 
def delete_film():

    # use primary key to delete a record 
    idField = input("Enter the filmID of the record to be deleted: ")


    # DELETE FROM songs WHERE filmID = 1/2/3/4/5/.....
    dbCursor.execute(f"DELETE FROM tblFilms WHERE filmID = {idField}")
    dbConnetion.commit()

    print(f"Record {idField} deleted from tblFilms table ")

if __name__ == "__main__":
    delete_film()