import csv

def register():
    username = input("Username: ")
    password = input("Password: ")

    # ตรวจสอบว่า Username ซ้ำหรือไม่
    if is_username_duplicate(username):
        print("ขออภัย Username นี้มีอยู่แล้ว")
    else:
        with open('user_data.csv', 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([username, password])
        print("ลงทะเบียนเรียบร้อยแล้ว")

def login():
    username = input("กรุณาป้อน Username: ")
    password = input("กรุณาป้อน Password: ")

    if is_valid_login(username, password):
        print("เข้าสู่ระบบสำเร็จ")
    else:
        print("เข้าสู่ระบบล้มเหลว")

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
        print("3. ออกจากโปรแกรม")
        choice = input("โปรดเลือกรายการ: ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("ออกจากโปรแกรม")
            break
        else:
            print("โปรดเลือกรายการที่ถูกต้อง")

if __name__ == "__main__":
    main()
