import re

# Determines which account book the program will find the account of the user from
def role(r):
    if r == "admin":
        src = "database/admins.txt"
        return(src)
    elif r == "librarian":
        src = "database/librarians.txt"
        return(src)
    else:
        src = "database/members.txt"
        return(src)

# Ensures the validation of an email
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Register function for new members
def register():
    with open("database/members.txt", "r+") as user:
        username = input("Create your Username: ")
        name = input("Real Name: ")
        email = input("Email: ")
        pwd = input("Create your Password: ")
        cfm_pwd = input("Confirm your Password: ")
        
        user.seek(0)
        users = user.read()
        
        if pwd != cfm_pwd:
            print("Passwords don't match, please try again")
        elif len(pwd) <= 6:
            print("Password is too short, please try again")
        elif username in users:
            print("Username exists, please try again")
        elif name in users:
            print("Name already exists, please try again")
        elif not is_valid_email(email):
            print("Invalid Email, please try again")
        elif email in users:
            print("Email already exists, please try again")
        else:
            user.write(f"{username},{pwd},{name},{email}\n")
            print("Registration Successful!!")
            print(f"Welcome {username}!")
            return()

# Login function
def login(src):
    users = []
    pwds = []
    names = []

    inputted_user = input("Enter your Username: ")
    inputted_pwd = input("Enter your Password: ")

    with open(src, "r") as users_db:
        for line in users_db:
            user, pwd, name, email = line.split(',')
            pwd = pwd.strip()
            name = name.strip()
            users.append(user)
            pwds.append(pwd)
            names.append(name)
            
        if inputted_user in users:
            x = users.index(inputted_user)
            if inputted_pwd == pwds[x]:
                print("Login Successful!")
                print(f"Welcome {names[x]}!")
                return(inputted_user)
            else:
                raise Exception("Incorrect Password, please try again. ")
        else:
            raise Exception("Username not found, please try again. ")