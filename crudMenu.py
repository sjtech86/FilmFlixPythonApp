import readFilm, addFilm, updateFilm, deleteFilm

# function to read the respective menu files 
def menu_file():
    with open('FilmFlixPythonApp/FilmsMenu.txt') as filmFile:
        userMenu = filmFile.read()
    return userMenu

# create the flimMenu
def films_menu():
    option = 0 #initialise the option with an integer data type
    optionsList = ["1","2","3","4","5"] # list data structure with string data type
    #initialise the menu_file function with choiceMenu variable
    choiceMenu = menu_file()

    #create a while
    while option not in optionsList:
        # call/invoke the menu_file function through the choiceMenu variable
        print(choiceMenu)#  display the options from the menu file

        #re-assign the option variable with the input function
        option = input("Enter an option from the film main menu: ") 

        # check if the use input from the option variable is a match with any of the options in the optionsList
        if option not in optionsList:
            #do this/execute the code below
            print(f"{option} is not a valid choice! ")# 0/7/8/9
    return option

# create a boolean variable 
mainProgram = True

while mainProgram: # while True
    #initialise the flim_menu function with mainMenu variable
    mainMenu = films_menu()

    # if the user input is a string value 1
    #if user input is '1' == '1'
    if mainMenu == "1":
        # then go into read films file and call the read_flims() function 
        readFilm.read_films()
    
    elif mainMenu == "2":
        addFilm.insert_film()

    elif mainMenu == "3":
        updateFilm.update_film()
    
    elif mainMenu == "4":
        deleteFilm.delete_film()

    else: # this exits the program
        # re-assign the boolean variable of 'mainProgram' to False
        mainProgram = False
input("Enter to quit the film App")