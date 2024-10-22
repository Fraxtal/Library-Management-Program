# List the books down
def listbooks():
    print("---------------\nList of Books\n---------------")
    b = open("database/books.txt", "r+")
    for line in b:
        id, title, author = line.split(',')
        title = title.strip()
        author = author.strip()
        print(f"Book titled {title} with id {id} by {author}")
            
# Add a book into the library catalogue
def addbook():
    book = []
    title = []
    auth = []
    
    with open("database/books.txt", "r+") as b:
        lines = b.readlines()
        for line in lines:
            if line.strip() != "":
                b_id, b_title, b_auth = line.split(',')
                book.append(b_id.strip())
                title.append(b_title.strip())
                auth.append(b_auth.strip())

        book_id = input("BookID: ")
        title = input("Title: ")
        author = input("Author: ")

        if len(book_id) != 6:
            raise Exception("Please Key in a valid BookID. ")
        elif book_id in book:
            raise Exception("BookID already exists, please try another one. ")
        elif title in b:
            raise Exception("Title already exists, please try again. ")
        else:
            with open("database/books.txt", "w") as a:
                a.write(f"{book_id}, {title}, {author}\n")
                print(f"Book titled {title} with id {book_id} by {author} has been successfully added into the catalogue!")
        

# Deletes a book from the library catalogue
def delbook():
    book = []
    title = []
    auth = []
    
    with open("database/books.txt", "r+") as b:
        lines = b.readlines()
        for line in lines:
            if line.strip() != "":
                b_id, b_title, b_auth = line.split(',')
                book.append(b_id.strip())
                title.append(b_title.strip())
                auth.append(b_auth.strip())
            
        book_id = input("BookID: ")
        if book_id in book:
            x = book.index(book_id)
            
            del book[x]
            del title[x]
            del auth[x]
            b.seek(0)
            b.truncate(0)
            for i in range(len(book)):
                if book[i] and title[i] and auth[x] is not None:
                    b.write(f"{book[i]}, {title[i]}, {auth[i]}\n")
            print("The book title that you have requested has been successfully removed from the catalogue.")
        else:
            raise Exception("Invalid BookID or BookID does not exist, please try again")

# Searches for a book from the library catalogue
def searchbook():
    with open("database/books.txt", "r") as b:
        x = input("Search for: ")
        found = False
        
        # Loop through each line to search for the book
        for line in b:
            if x in line:
                print(line)
                found = True
            
        if not found:
            raise Exception("Nothing is Found")


# Edits information of a book in the library catalogue
def editbook():
    book_ids = []
    titles = []
    authors = []
    
    with open("database/books.txt", "r+") as b:
        lines = b.readlines()
        for line in lines:
            if line.strip() != "":
                b_id, b_title, b_auth = line.split(',')
                b_title = b_title.strip()
                b_auth = b_auth.strip()
                book_ids.append(b_id)
                titles.append(b_title)
                authors.append(b_auth)
        book_id = input("BookID of the book that you want to edit: ")
        
        if book_id in book_ids:
            index = book_ids.index(book_id)
            change = input(f"What data do you want to change for BookID {book_id}? (Title or Author): ").strip().lower()
            
            if change == "title":
                new_title = input("Enter the new title: ").strip()
                titles[index] = new_title
            elif change == "author":
                new_author = input("Enter the new author: ").strip()
                authors[index] = new_author
            else:
                print("Invalid choice. Please select either 'Title' or 'Author'.")
                return
            b.truncate(0)
            
            for i in range(len(book_ids)):
                b.write(f"{book_ids[i]}, {titles[i]}, {authors[i]}\n")
            
            print("The book details have been successfully updated.")
        else:
            raise Exception("Invalid BookID or BookID does not exist, please try again.")
