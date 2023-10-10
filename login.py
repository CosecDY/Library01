import csv
Users = {}
status = ""

def account ():
    with open("account.csv","w",newline="") as f:
        fw = csv.writer(f)
        fw

def Users_login ():
    print(" wellcome ")
    print(" 1.login ")
    print(" 2.register ")
    print(" 3.forgot password ")
    print(" 4.Exit")
    status = input("Enter : ")
    if status == "1":
        login()
    elif status == "2":
        register()
    elif status == "3":
        forgotPass()       

def register():
    CreateID=input("Create Username : ")
    if CreateID in Users:
        print("ID online")
    else:
        createPass1 = input("Create passeord :")
        createPass2 = input("confirm password :")
        if createPass1 != createPass2:
            print("password not similar")
        elif createPass1 == createPass2:
            Users[CreateID]=createPass1
            print("Create succeed")

def login():
    login=input ("Username ID : ")
    password=input("password : ")

    if login in Users and Users[login]==password:
        print("login secceed")
    else:
        print("wrong ID or Password")

def forgotPass():
    OldUser=input("Enter Username :")
    if OldUser in Users :
        newPass1 = input("new password :")
        newPass2 = input("confirm password :")
        if newPass1 != newPass2:
            print("password not similar")
        elif newPass1 == newPass2:
            Users[OldUser]==newPass1
            print("complete change password")
        
    else :
        print("Do not have this User in dta ")

while status != "4":
    Users_login()