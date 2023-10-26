import csv

def main():
    while True:
        print("1 : User")
        print("2 : Admin")
        print("3 : Exit")
        choice = input("Choose : ")

        if(choice == '1'):
            print("---------------------------------")

        elif(choice == '2'):
            print("---------------------------------")
     
        elif(choice == '3'):
            break


def main_user():
    while True:
        print("1 : Login ")
        print("2 : Register ")
        print("3 : Forgot password ")
        print("4 : Exit ")
        choice = input("Choose : ")


        


   
def main_admin():
    username = input("Username : ")    
    password = input("password : ")        