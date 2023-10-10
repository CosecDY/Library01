import csv

def register():
    username = input("Username: ")
    password = input("Password: ")

    # ตรวจสอบว่า Username ซ้ำหรือไม่
    if is_username_duplicate(username):
        print("duplicate Username")
    else:
        with open('user_data.csv', 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([username, password])
        print("succeed register")

def login():
    username = input("Username: ")
    password = input("Password: ")
    if is_valid_admin(username, password):
        print("admin suceed login")
    elif is_valid_login(username, password):
        print("suceed login")
    else:
        print("wromg username or password")

def forgotPass():
    username = input("Username: ")
    if check_username(username):
        ss

def is_username_duplicate(username):
    with open('user_data.csv', 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row[0] == username:
                return True
    return False

def is_valid_login(username, password):
    with open('user_data.csv', 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row[0] == username and row[1] == password:
                return True
    return False

def is_valid_admin(username, password):
    with open('amid_dataa.csv', 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row[0] == username and row[1] == password:
                return True
    return False

def check_username(username):
    with open('user_data.csv', 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row[0] == username:
                return True
    return False

def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. forgot password")
        print("4. exit")
        choice = input("Enter : ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            forgotPass()
        elif choice == '4':
            break
        else:
            print("please choice")

if __name__ == "__main__":
    main()
