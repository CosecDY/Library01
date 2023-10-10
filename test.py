import csv

def register():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    # ตรวจสอบว่า Username ซ้ำหรือไม่
    if is_username_duplicate(username):
        print("duplicate Username")
    else:
        with open('user_data.csv', 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([username, password])
        print("succeed register")

def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if is_valid_login(username, password):
        print("suceed login")
    else:
        print("wromg username or password")

def forgot_password():
    username = input("Enter Old Username: ")

    if is_username_duplicate(username):
        new_password = input("New password: ")

        # อ่านข้อมูลทั้งหมดจากไฟล์ CSV
        rows = []
        with open('user_data.csv', 'r', newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if row[0] == username:
                    row[1] = new_password
                rows.append(row)

        # เขียนข้อมูลที่แก้ไขลงในไฟล์ CSV
        with open('user_data.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(rows)

        print("succeed change password")
    else:
        print("Username invalid")

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
            forgot_password()
        elif choice == '4':
            break
        else:
            print("please choice")

if __name__ == "__main__":
    main()
