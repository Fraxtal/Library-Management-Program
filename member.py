from datetime import date, datetime

#Checks the amount of days the member has already borrowed the book for
def overdue_checker(d : str) -> int:
	d = datetime.strptime(d, '%m-%d-%Y').date()
	diff = date.today() - d
	return diff.days

# Views the amount of loaned books that the member has
def view_loaned_books(username : str):
	users = []
	book_ids = []
	dates = []

	print("---------------\nLoaned Books\n---------------")
	with open("database/bookrental_records.txt", "r") as bkr, open("database/books.txt", "r") as b:
		bkr.seek(0)
		lines = bkr.readlines()
		for line in lines:
			bkr_username, bkr_bookid, bkr_date = line.split(',')
			users.append(bkr_username.strip())
			book_ids.append(bkr_bookid.strip())
			dates.append(bkr_date.strip())

		for i in range(len(users)):
			if username == users[i]:
				x = overdue_checker(dates[i]) - 7
				for line in b:
					if book_ids[i] in line:
						id, title, author = line.split(',')
				if x > 0:
					if x > 5:
						price = 10
					else:
						price = 1
						for t in range(x):
							price =+ 1
				print(f"{username} has borrowed {title.strip()} with ID of {id.strip()} by {author.strip()} and is overdued for {x} days.\n"
		   			f"Thus, you must pay a return fee of {float(price):.2f} upon returning the book.\n")

# Function to allow the member to edit his personal
def editprofile(usrID : str):
    id = []
    pwd = []
    name = []
    email = []
    
    with open("database/members.txt", "r+") as users:
        users.seek(0)
        lines = users.readlines()
        for line in lines:
            users_id, users_pwd, users_name, users_email = line.split(',')
            users_pwd = users_pwd.strip()
            users_name = users_name.strip()
            users_email = users_email.strip()
            id.append(users_id)
            pwd.append(users_pwd)
            name.append(users_name)
            email.append(users_email)
            
        try:
            x = id.index(usrID)
        except ValueError:
            raise Exception("User ID not found.")
        
        print(f"{name[x]} with user id of {id[x]}")
        user_input = (input("What would you like to change?\n(Select options Name, Username, Password) ")).lower
        if user_input == "name":
            name[x] = input("What would you like to change the name to? ")
        elif user_input == "username":
            id[x] = input("What would you like to change the username to? ")
        elif user_input == "password":
            pwd[x] = input("What would you like to change the password to? ")
        elif user_input == "email":
            email[x] = input("What would you like to change the email to? ")
        else:
            raise Exception("Invalid Input, please try again")
	print("Change has been done successfully")
		
#Allows member to search and check for the availablity of a specific book
def search_and_check_availability():
    search_query = input("Enter Book Title or BookID to search: ")
    
    # Search in the book catalogue
    with open("database/books.txt", "r") as db_books:
        books = db_books.readlines()
        
    found_books = []
    for line in books:
        b_id, title, author = line.split(',')
        title = title.strip()
        b_id = b_id.strip()
        
        if search_query in title or search_query == b_id:
            found_books.append((b_id, title, author.strip()))
    
    if not found_books:
        raise Exception("No books found matching your search.")

    print("Found Books:")
    for b_id, title, author in found_books:
        print(f"Book ID: {b_id}, Title: {title}, Author: {author}")

        # Check availability for each found book
        with open("database/bookrental_records.txt", "r") as db_rentals:
            rentals = db_rentals.readlines()
            is_available = True
            
            for rental in rentals:
                r_username, r_bookid, r_date = rental.split(',')
                if r_bookid.strip() == b_id:
                    is_available = False
                    break
            
            if is_available:
                print(f"The book '{title}' (ID: {b_id}) is available for borrowing.")
            else:
                print(f"The book '{title}' (ID: {b_id}) is currently borrowed and not available.")
