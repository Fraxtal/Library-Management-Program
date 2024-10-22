from datetime import date, datetime

# Checks the eligibility of the member of whether he is able to borrow an extra book or not
def eligibility(username: str):
    with open("database/members.txt", "r") as members:
        temp_u = []
        lines = members.readlines()
        for line in lines:
            u, p, n, e = line.split(',')
            temp_u.append(u.strip())
        if username not in temp_u:
            return (False, "Invalid Username or Username not Found")
        if not check_member_loans(username):
            return (False, "User either has more than 5 books borrowed or has a book that has not been returned.")
        else:
            return (True, "")

# Checks the existence of the book and its availability
def checkbook(book: str):
    book_b = []
    book_bkr = []
    with open("database/books.txt", "r") as b, open("database/bookrental_records.txt", "r") as bkr:
        b_lines = b.readlines()
        for line in b_lines:
            bk, t, a = line.split(",")
            book_b.append(bk.strip())

        bkr_lines = bkr.readlines()
        for line in bkr_lines:
            user, bk, d = line.split(",")
            book_bkr.append(bk.strip())


        if book not in book_b:
            return (False, "Invalid BookId or Incorrect BookID")
        elif book in book_bkr:
            return (False, f"Book with id {book} is unavailable to be borrowed at the moment")
        else:
            return (True, "")
        
# Checks the due date of the book being lent to the member
def check_due_date(d: str) -> bool:
    d = datetime.strptime(d, '%m/%d/%Y').date()  # Ensure the format matches the stored format
    return (date.today() - d).days <= 7

# Checks if the member has borrowed more than 5 books from the library
def check_member_loans(username: str) -> bool:
    with open("database/bookrental_records.txt", "r") as bkr:
        lines = bkr.readlines()
        loans = [line.strip().split(',') for line in lines]
    
    loan_count = sum(1 for loan in loans if loan[0] == username)
    if loan_count > 5:
        return False
    for loan in loans:
        if loan[0] == username and not check_due_date(loan[2]):
            return False
    return True  # Return True if the member is eligible for more loans

# The main function for loaning a book to a member
def loan():
    member_username = input("Username of member: ")
    status, message = eligibility(member_username)
    if not status:
        raise Exception(message)
    
    book_input = input("What is the BookID of the book to be borrowed?: ")
    status, message = checkbook(book_input)
    if not status:
        raise Exception(message)
    
    # Get the current date and format it as mm/dd/yyyy
    d = date.today().strftime('%m/%d/%Y')
    
    with open("database/bookrental_records.txt", "a") as bkr:
        bkr.write(f"{member_username},{book_input},{d}\n")
        print(f"Book {book_input} has been successfully loaned to {member_username}.")
