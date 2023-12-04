from connect import *

# create subroutine 
def films_reports(value, option):
    if option == '2':
        dbCursor.execute('SELECT * FROM tblFilms WHERE genre = ?',(value,))

    elif option == '3':
        dbCursor.execute('SELECT * FROM tblFilms WHERE yearReleased = ?',(value,))

    elif option == '4':
        dbCursor.execute('SELECT * FROM tblFilms WHERE rating = ?',(value,))

    elif option == '5':
        dbCursor.execute('SELECT * FROM tblFilms WHERE duration = ?',(value,))

    else:
        print(f"you have not selected an option") 
        
    #dbCursor.execute("SELECT * FROM tblFilms")

    #dbCursor.execute("SELECT * FROM tblFilms ORDER BY filmId DESC")
    #dbCursor.execute("SELECT yearReleased, title FROM tblFilms")
    #dbCursor.execute("SELECT * FROM tblFilms WHERE genre = 'Action' ")
    #dbCursor.execute("SELECT * FROM tblFilms WHERE rating = 'excellent' ")
    #dbCursor.execute("SELECT * FROM tblFilms WHERE title LIKE 'a%' ")
    #dbCursor.execute("SELECT * FROM tblFilms WHERE genre LIKE '%a%' ")
    #dbCursor.execute("SELECT genre FROM tblFilms WHERE genre LIKE '%a%' ")
    #dbCursor.execute("SELECT title, rating FROM tblFilms WHERE title LIKE '%p%' OR rating LIKE '%r%' ")
    #dbCursor.execute("SELECT * FROM tblFilms WHERE yearReleased = 2016")
   


    
    reports = dbCursor.fetchall()
    for aRecord in reports:
        print(aRecord)

if __name__ == "__main__":
    films_reports()

  
