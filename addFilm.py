
from connect import*
#create subroutine
def insert_film():
    #filmId field is auto_increment(no data input required)
    #ask for user input for title,yearReleased,genre,rating,duration and genre
    filmTitle=input("Enter film title")
    yearReleased=input("Enter film yearRelease")
    filmRating=input("Enter filmRating")
    filmDuration=input("Enter filmDuration")
    filmGenre=input("Enter filmGenre")
    
    # add data in the respective field in the film table

    sql = "insert into tblFilms (title, yearReleased, rating, duration, genre) values(?,?,?,?,?)"
    val = (filmTitle,yearReleased,filmRating,filmDuration,filmGenre)

    dbCursor.execute(sql, val)
    dbConnetion.commit()
    print(f"{filmTitle} inserted in the film table")

if __name__ == "__main__":
    insert_film()  # call/invoke the function