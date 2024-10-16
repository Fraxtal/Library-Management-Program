from imports import *

def main():
	while True:
		#Asking User about what role would they like to sign in as (If they would like to register, we would refer them to choose Member, if they would like to quit the program, they can just write "quit" to quit)
		# Utilization of try..except is also involved in this part for efficient error handling
		try:
            	# Ask the user for their role
	            r = input("What are you logging in as? (Member, Admin, or Librarian)\n**PS: Member if you want to register instead.// Type 'quit' to quit the program\n").lower()
	            
	            if r in ["admin", "librarian"]:
	                src = role(r)
	                username = login(src)  # Call login function
	                if not username:
	                    # If login fails, continue asking for login
	                    print("Login failed. Try again.")
	                    continue  # Go back to login prompt
	                else:
	                    break  # Break out of the loop after successful login
	            
	            elif r == "member":
	                temp = input("Would you like to register or login? ").lower()
	                if temp == "register":
	                    register()
	                elif temp == "login":
	                    src = role(r)
	                    username = login(src)  # Call login function
	                    if not username:
	                        print("Login failed. Try again.")
	                        continue  # Go back to login prompt
	                    else:
	                        break  # Break out of loop after successful login
	                else:
	                    print("Invalid option for member, please choose 'register' or 'login'.")
	            elif r == "quit":
	                print("Quitting the program.")
	                return() # Graceful exit
	            else:
	                print("Invalid role, please try again.")
	                
	        except Exception as e:
	            print(f"Error: {e}")
			
# After successful login, proceed to the user's respective menu
	while True:
		# the variable r defines the role of the user and matches it to the case provided.
		# After that, the user is then procided to their own respective menus.
		# The menus for the user utilizes the method of match case as well to have a cleaner view of the code.
		# Utilization of try..except is also involved in these match cases for efficient error handling
		try:
			match r:
				case "admin":
					print(f"What would you like to do?")
					print(f"1) Add User\n2) List Users\n3) Edit User Information\n4) Search User\n5) Delete User\n6) Logout")
					match int(input("Choose one (1 - 6)")):
						case 1:
							target = input("Which user role would you like to add? (Admin, Member, Librarian)\n").lower()
							addusr(role(target))
						case 2:
							target = input("Which user list would you like me to list down? (Admin, Member, Librarian)\n").lower()
							listusr(role(target))
						case 3:
							target = input("Which user role would you like to edit from? (Admin, Member, Librarian)\n").lower()
							editusr(role(target))
						case 4:
							target = input("Which user role would you like to search from? (Admin, Member, Librarian)\n").lower()
							searchusr(role(target), role)
						case 5:
							target = input("Which user role would you like to delete from? (Admin, Member, Librarian)\n").lower()
							delusr(role(target))
						case 6:
							print("You have been logged out!")
							break
						case _:
							raise Exception("Invalid Input, Please Try Again")

				case "librarian":
					print(f"What would you like to do?")
					print(f"1) Add Book\n2) List Books\n3) Edit Book Information\n4) Search Book\n5) Delete Book\n6) Loan Book\n7) Logout")
					match int(input("Choose one (1 - 7)")):
						case 1:
							addbook()
						case 2:
							listbooks()
						case 3:
							editbook()
						case 4:
							searchbook()
						case 5:
							delbook()
						case 6:
							loan()
						case 7:
							print("You have been logged out!")
							break
						case _:
							raise Exception("Invalid Input, Please Try Again")
				
				case "member":
					print(f"What would you like to do?")
					print(f"1) View Current Loaned Books\n2) Update Personal Information\n3) Search Book Catalogue\n4) Logout")
					match int(input("Choose one (1 - 4)\n")):
						case 1:
							view_loaned_books(username)
						case 2:
							editprofile(username)
						case 3:
							search_and_check_availability()
						case 4:
							print("You have been logged out!")
							break
						case _:
							raise Exception("Invalid Input, Please Try Again")

		except Exception as e:
	            print(f"Error: {e}")


#Runs this when the main file is being initialised
if __name__ == '__main__':
	# Scanning to see if the directory "database" is present in order to store data and if not it will create the directory
	dir = "database"
	exist = os.path.exists(dir)
	if not exist:
		os.mkdir(dir)
		print(f"The main directory {dir} has been created!")
	
	#Print Startup Header for the Application
	print("\t -----------------------------------------------\n"
		"\t    Brickfields Kuala Lumpur Community Library \n"
		"\t ------------------------------------------------")

	#Runs the main function to start the code
	main()
