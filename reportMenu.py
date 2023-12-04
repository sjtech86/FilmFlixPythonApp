import readFilm, reportFilm

# function to read the respective menu files 
def menu_file():
    with open('FilmFlixPythonApp/ReportMenu.txt') as filmFile:
        userMenu = filmFile.read()
    return userMenu

# create the film menu
def films_menu():
    option = 0
    optionsList = ["1","2","3","4","5","6"] 
    choiceMenu = menu_file()

    while option not in optionsList:
        print(choiceMenu)#  display the options from the menu file

        #re-assign the option variable with the input function
        option = input("Enter an option from the film main menu: ") 

        # check if the use input from the option variable is a match with any of the options in the optionsList
        if option not in optionsList:
            #do this/execute the code below
            print(f"{option} is not a valid choice! ")
    return option

# create a boolean variable 
mainProgram = True

while mainProgram: # while True
    #initialise the film_menu function with mainMenu variable
    mainMenu = films_menu()

      # if the user input is a string value 1
    #if user input is '1' == '1'
    if mainMenu == "1":
        # then go into readFilm file and call the read_film() function 
        readFilm.read_films()

    elif mainMenu == "2":
        # then go into readFilm file and call the read_film() function 
        value = input("Enter a genre ")
        reportFilm.films_reports(value, mainMenu)

    elif mainMenu == "3":
        # then go into readFilm file and call the read_film() function 
        value = input("Enter a year release ")
        reportFilm.films_reports(value, mainMenu)

    elif mainMenu == "4":
        # then go into readFilm file and call the read_film() function 
        value = input("Enter a rating ")
        reportFilm.films_reports(value, mainMenu)

    elif mainMenu == "5":
        # then go into readFilm file and call the read_film() function 
        value = input("Enter duration ")
        reportFilm.films_reports(value, mainMenu)

    else: # this exits the program
        # re-assign the boolean variable of 'mainProgram' to False
        mainProgram = False
input("Enter to quit the film App")