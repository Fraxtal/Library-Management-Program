from .authentication import is_valid_email

# Adds a user into the account book
def addusr(src : str):
    with open(src, "r+") as user:
        username = input("Username: ")
        name = input("Name: ")
        email = input("Email: ")
        pwd = input("Create your Password: ")
        cfm_pwd = input("Confirm your Password: ")
        
        users = user.read()
        
        if pwd != cfm_pwd:
            raise Exception("Passwords don't match, please try again")
        elif len(pwd) <= 6:
            raise Exception("Password is too short, please try again")
        elif username in users:
            raise Exception("Username exists, please try again")
        elif name in users:
            raise Exception("Name already exists, please try again")
        elif not is_valid_email(email):
            raise Exception("Invalid Email, please try again")
        elif email in users:
            raise Exception("Email already exists, please try again")
        else:
            user.write(f"{username},{pwd},{name},{email}\n")
            print(f"{name} with username {username} has been successfully added into the database. ")

# List users in a specific account book
def listusr(src : str, role : str):
    print(f"---------------\n List of {role.capitalize()}s\n---------------")
    
    with open(src, "r") as accs:
        for line in accs:
            username, pwd, name, email = line.split(',')
            print(f"{username}, {name}, {email.strip()}")

# Edits a user's account information from a specific account book
def editusr(src : str):
    id = []
    pwd = []
    name = []
    email = []
    usrID = input("Username of the user information that you want to edit: ")

    if usrID == "root":
        raise Exception("You cannot edit this account!")
    
    with open(src, "r+") as users:
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

# Searches for a user in a specific account book
def searchusr(src : str):
    x = input("Search for: ")
    with open(src, "r") as users:
        lines = users.readlines()
        found = False
        for line in lines:
            if x in line:
                print(line.strip())
                found = True
        if not found:
            raise Exception("User is not found")

# Deletes a user from a specific account book
def delusr(src : str):
    id = []
    pwd = []
    name = []
    email = []
    id_input = input("Username: ")
    if src == "database/admin.txt" and id_input == "root":
        raise Exception("You cannot delete this account!")
    
    with open(src, "r") as u:
        for line in u:
            u_id, u_pwd, u_name, u_email = line.split(',')
            id.append(u_id.strip())
            pwd.append(u_pwd.strip())
            name.append(u_name.strip())
            email.append(u_email.strip())
        
    
    if id_input in id:
        cfm = (input(f"Are you sure that you want to delete {id_input} (Yes or No)?: ")).lower()
        if cfm == "yes":
            x = id.index(id_input)
            del id[x]
            del pwd[x]
            del name[x]
            del email[x]
            with open(src, "w") as u:
                u.seek(0)
                u.truncate(0)
                for i in range(len(id)):
                    u.write(f"{id[i]},{pwd[i]},{name[i]},{email[i]}\n")
        else:
            print("Action Declined")
            return()
        
        print("The user that you have requested has been successfully removed from the database.")
    else:
        raise Exception("Invalid Username or Username does not exist, please try again.")
