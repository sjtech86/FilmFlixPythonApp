import sqlite3 as sql

dbConnetion = sql.connect("FilmFlixPythonApp/filmflix.db")

dbCursor = dbConnetion.cursor()

