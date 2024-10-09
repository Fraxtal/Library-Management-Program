def listbooks():
    print("---------------\nList of Books\n---------------")
    b = open("database/books.txt", "r+")
    for line in b:
        id, title, author = line.split(',')
        title = title.strip()
        author = author.strip()
        print(f"Book titled {title} with id {id} by {author}")
            
            
def addbook():
    b = open("database/books.txt", "r+")
    book_id = input("BookID: ")
    title = input("Title: ")
    author = input("Author: ")

    if len(book_id) != 6:
        raise Exception("Please Key in a valid BookID. ")
    elif book_id in b:
        raise Exception("BookID already exists, please try another one. ")
    elif title in b:
        raise Exception("Title already exists, please try again. ")
    else:
        b.write(f"{book_id}, {title}, {author}\n")
        print(f"Book titled {title} with id {book_id} by {author} has been successfully added into the catalogue!")
    b.close
            
def delbook():
    book = []
    title = []
    auth = []
    
    b = open("database/books.txt", "r+")
    for line in b:
        b_id, b_title, b_auth = line.split(',')
        b_title = b_title.strip()
        b_auth = b_auth.strip()
        book.append(b_id)
        title.append(b_title)
        auth.append(b_auth)
        
    book_id = input("BookID: ")
    if book_id in book:
        x = book.index(book_id)
        
        del book[x], title[x], auth[x]
        b.seek(0)
        b.truncate()
        for i in range(len(book)):
            b.write(f"{book[i]}, {title[i]}, {auth[i]}\n")
        print("The book title that you have requested has been successfully removed from the catalogue.")
    else:
        raise Exception("Invalid BookID or BookID does not exist, please try again")

def searchbook():
    b = open("database/books.txt", "r+")
    x = input("Search for: ")
    if x in b:
        for line in b:
            if x in line:
                print(line)
    else:
        raise Exception("Nothing is Found")

def editbook():
    book_ids = []
    titles = []
    authors = []
    
    with open("database/books.txt", "r+") as b:
        # Read the content of the file
        lines = b.readlines()
        
        # Process each line in the file
        for line in lines:
            b_id, b_title, b_auth = line.split(',')
            b_title = b_title.strip()
            b_auth = b_auth.strip()
            book_ids.append(b_id)
            titles.append(b_title)
            authors.append(b_auth)
        
        # Get the book ID that the user wants to edit
        book_id = input("BookID of the book that you want to edit: ")
        
        if book_id in book_ids:
            index = book_ids.index(book_id)
            
            # Ask what data the user wants to change
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
            
            # Rewind the file pointer and truncate the file to clear its content
            b.seek(0)
            b.truncate()
            
            # Write the updated data back to the file
            for i in range(len(book_ids)):
                b.write(f"{book_ids[i]}, {titles[i]}, {authors[i]}\n")
            
            print("The book details have been successfully updated.")
        else:
            raise Exception("Invalid BookID or BookID does not exist, please try again.")
