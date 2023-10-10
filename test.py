import csv

def is_admin(username, password):
    # สมมติว่าคุณมีรายชื่อ Username และรหัสผ่านของแอดมิน
    admin_credentials = {"admin1": "11111111", "admin2": "22222222", "admin3": "33333333"}
    return username in admin_credentials and admin_credentials[username] == password

def register():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    # ตรวจสอบว่า Username ซ้ำหรือไม่
    if is_username_duplicate(username):
        print("duplicate Username")
        print("-------------------------------------------------")
    else:
        with open('user_data.csv', 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([username, password])
         
        print("succeed register")
        print("-------------------------------------------------")   
def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if is_valid_login(username, password):
        print("suceed login")
        print("-------------------------------------------------")
    else:
        print("wromg username or password")
        print("-------------------------------------------------")

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
        print("-------------------------------------------------")
    else:
        print("Username invalid")
        print("-------------------------------------------------")

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

def users_main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. forgot password")
        print("4. exit")
        choice = input("Enter : ")

        if choice == '1':
            print("-------------------------------------------------")
            register()
        elif choice == '2':
            print("-------------------------------------------------")
            login()
        elif choice == '3':
            print("-------------------------------------------------")
            forgot_password()
        elif choice == '4':
            print("out of user Interface")
            print("-------------------------------------------------")
            break
        else:
            print("please choice")
            print("-------------------------------------------------")

def admin_menu():
    while True:
        print("1. เพิ่มผู้ใช้")
        print("2. ลบผู้ใช้")
        print("3. ดูรายชื่อผู้ใช้")
        print("4. ออกจากโปรแกรมแอดมิน")
        admin_choice = input("โปรดเลือกรายการ: ")

        if admin_choice == '1':
            # เพิ่มโค้ดเพิ่มผู้ใช้ หรืออะไรที่คุณต้องการ
            pass
            
        elif admin_choice == '2':
            # เพิ่มโค้ดลบผู้ใช้ หรืออะไรที่คุณต้องการ
            pass
            
        elif admin_choice == '3':
            # เพิ่มโค้ดดูรายชื่อผู้ใช้ หรืออะไรที่คุณต้องการ
            pass
            
        
        elif admin_choice == '4':
            print("ออกจากโปรแกรมแอดมิน")
            break
        else:
            print("โปรดเลือกรายการที่ถูกต้อง")

if __name__ == "__main__":
    while True:
        print("1. Users Interface")
        print("2. admin Interface")
        print("3. Exit")
        user_type = input("Enter : ")
        

        if user_type == '1':
            print("-------------------------------------------------")
            users_main()
            
        elif user_type == '2':
            admin_username = input("Enter admin Username: ")
            admin_password = input("Enter admin password: ")
            print("-------------------------------------------------")
            if is_admin(admin_username, admin_password):
                
                admin_menu()
            else:
                print("worng password")

        elif user_type == '3':
            print("Exit")
            break
        else:
            print("please ")
