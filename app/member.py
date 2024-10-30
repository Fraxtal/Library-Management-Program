from datetime import date, datetime

#Checks the amount of days the member has already borrowed the book for
def overdue_checker(d : str) -> int:
	d = datetime.strptime(d, '%m-%d-%Y').date()
	diff = date.today() - d
	return diff.days

# Views the amount of loaned books that the member has
def view_loaned_books(username : str):
    bkr_users = []
    bkr_b_ids = []
    bkr_dates = []
    b_id = []
    b_title = []
    b_author = []

    print("---------------\nLoaned Books\n---------------")
    with open("database/bookrental_records.txt", "r") as bkr, open("database/books.txt", "r") as b:
        bkr_lines = bkr.readlines()
        b_lines = b.readlines()
        for line in bkr_lines:
            u, bookid, date = line.split(',')
            bkr_users.append(u.strip())
            bkr_b_ids.append(bookid.strip())
            bkr_dates.append(date.strip())
        
        for line in b_lines:
            id, title, author = line.split(',')
            b_id.append(id.strip())
            b_title.append(title.strip())
            b_author.append(author.strip())

        if username in bkr_users:
            for i in range(len(bkr_users)):
                if username == bkr_users[i]:
                    price = 0
                    x = overdue_checker(bkr_dates[i])
                    if x > 0:
                        if x > 5:
                            price = 10
                        else:
                            price = 1 + x
                    for index in range(len(b_id)):
                        if b_id[index] == bkr_b_ids[i]:
                            print(f"{username} has borrowed {b_title[index]} with ID of {b_id[index]} by {b_author[index]} for {x} days.")
                            if price > 0:
                                print(f"Thus, you must pay a return fee of {float(price):.2f} upon returning the book.\n")
        else:
            print("User does not have any loaned books")

# Function to allow the member to edit his personal
def editprofile(usrID : str):
    id = []
    pwd = []
    name = []
    email = []
    
    with open("database/members.txt", "r+") as users:
        lines = users.readlines()
        for line in lines:
            users_id, users_pwd, users_name, users_email = line.split(',')
            id.append(users_id.strip())
            pwd.append(users_pwd.strip())
            name.append(users_name.strip())
            email.append(users_email.strip())
        if usrID in id:
            x = id.index(usrID)
            print(f"{name[x]} with user id of {id[x]}")
            user_input = (input("What would you like to change?\n(Select options Name, Username, Password) ")).lower()
            if user_input == "name":
                name[x] = input("What would you like to change the name to? ")
            elif user_input == "username":
                id[x] = input("What would you like to change the username to? ")
            elif user_input == "password":
                pwd[x] = input("What would you like to change the password to? ")
            elif user_input == "email":
                email[x] == input("What would you like to change the email to? ")
            else:
                raise Exception("Invalid Input, please try again")
            users.seek(0)
            users.truncate(0)
            for i in range(len(id)):
                    users.write(f"{id[i]},{pwd[i]},{name[i]},{email[i]}\n")
        else:
            raise Exception("Invalid Username")

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
