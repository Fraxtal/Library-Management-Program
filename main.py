from app import main
import os

#Runs this when the main file is being initialised
if __name__ == '__main__':
    # Scanning to see if the directory "database" is present in order to store data and if not it will create the directory
    dir = "database"
    if not os.path.exists(dir):
        os.mkdir(dir)
        print(f"The main directory {dir} has been created!")
	
    if not os.path.exists("database/admins.txt"):
        with open("database/admins.txt", "x") as file:
            file.write("root,123123123,admin,brickfieldskl@gmail.com\n")
    if not os.path.exists("database/bookrental_records.txt"):
        with open("database/bookrental_records.txt", "x") as file:
            pass
    if not os.path.exists("database/books.txt"):
        with open("database/books.txt", "x") as file:
            pass
    if not os.path.exists("database/librarians.txt"):
        with open("database/librarians.txt", "x") as file:
            pass
    if not os.path.exists("database/members.txt"):
        with open("database/members.txt", "x") as file:
            pass

    #Print Startup Header for the Application
    print("\t -----------------------------------------------\n"
          "\t    Brickfields Kuala Lumpur Community Library \n"
          "\t ------------------------------------------------")

	#Runs the main function to start the code
    main()