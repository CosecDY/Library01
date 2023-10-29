import random
from flask import Flask, jsonify, redirect, render_template, request,url_for,flash
from Library import *
import secrets
import string
import os
import json


app = Flask(__name__)
app.secret_key = secrets.token_hex(24)

@app.route('/')
def first_page():
    return render_template('UiLoginPage.html')

@app.route('/register')
def UiRegister():
    return render_template('UiRegisterPage.html')

libraryComic = Library()
libraryFiction = Library()
libraryHorror = Library()
libraryLearning = Library()
libraryRomance = Library()

book_data = []

book_data_Comic = []
book_data_Fiction = []
book_data_Horror = []
book_data_Learning = []
book_data_Romance = []

libraryComic.load_from_file("Comic", book_data_Comic)
libraryFiction.load_from_file("Fiction", book_data_Fiction)
libraryHorror.load_from_file("Horror", book_data_Horror)
libraryLearning.load_from_file("Learning", book_data_Learning)
libraryRomance.load_from_file("Romance", book_data_Romance)

book_data.append(book_data_Comic)
book_data.append(book_data_Fiction)
book_data.append(book_data_Horror)
book_data.append(book_data_Learning)
book_data.append(book_data_Romance)

def load_user_data():
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory,'static/UsernamePassword.txt')
    users = [] 
    try:
        with open(file_path, 'r', encoding='utf-8') as inputFile:
            for line in inputFile:
                if line.startswith("username:") and "password:" in line:
                    username = line.split("username:")[1].split(",")[0].strip()
                    password = line.split("password:")[1].strip()
                    users.append({"username": username, "password": password})
    except FileNotFoundError:
        print(f"ไฟล์ '{file_path}' ไม่พบ")
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการโหลดข้อมูล: {str(e)}")

    return users


def save_user_data(users):
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory,'static/UsernamePassword.txt')
    with open(file_path, 'w', encoding='utf-8') as outputFile:
        for user in users:
            line = f"username: {user['username']}, password: {user['password']}\n"
            outputFile.write(line)
        


def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Routes
@app.route('/register_page', methods=['GET', 'POST'])
def register():
      
    
    if request.method == 'POST':
        
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('Confirm_password')
        if password == confirm_password:
            users = load_user_data()
            users.append({'username': username, 'password': password})
            save_user_data(users)

            flash('Registration successful!')
            return redirect(url_for('login'))
        else:
            return render_template('UiRegisterPage.html')

    return render_template('UiRegisterPage.html')

@app.route('/login_page', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        users = load_user_data()
    
        user = next((u for u in users if u['username'] == username and u['password'] == password), None)
        
        if user is not None:
            return render_template('UiMainPage.html', username=username)
        
        else:
            return render_template('UiLoginPage.html')

    return render_template('UiLoginPage.html')


@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        username = request.form.get('username')
        users = load_user_data()
        
        user = next((u for u in users if u['username'] == username), None)

        if user:
            new_password = generate_random_password()
            user['password'] = new_password
            save_user_data(users)

            flash(f'Your new password is: {new_password}', 'success')
            return redirect(url_for('login'))
        else:
            flash('Username not found', 'error')

    return render_template('UiForgotPasswordPage.html')

# @app.route('/logout')
# def logout():
#     # ตรวจสอบว่าผู้ใช้ลงชื่อออกหรือยังตามความต้องการของคุณ
#     # ตัวอย่าง: ตรวจสอบสถานะการลงชื่อออกจากแอปพลิเคชัน
#     if 'username' in session:
#         # ทำการลงชื่อออกจากแอปพลิเคชันตามความต้องการของคุณ
#         # ตัวอย่าง: เคลียร์คุณสมบัติที่แสดงสถานะการลงชื่อเข้าใช้ของผู้ใช้ในแอปพลิเคชัน
#         flash('Logged out successfully', 'success')
#     return redirect(url_for('login'))














#######################################################################################


















@app.route('/api/book_data', methods=['GET'])
def get_book_data():
    return jsonify(data=book_data)

def calculate_top_books():
    all_books = []
    categories = ["Comic", "Fiction", "Horror", "Learning", "Romance"]
    
    for category in categories:
        category_books = eval(f'book_data_{category}')
        all_books.extend(category_books)
    
    all_books.sort(key=lambda book: book['totalLikes'], reverse=True)
    
    top_books = all_books[:5]
    
    return top_books

topBookdata = calculate_top_books()


















@app.route('/api/top_book_data', methods=['GET'])
def get_top_book_data():
    return jsonify(data=topBookdata)

@app.route('/search', methods=['POST','GET'])
def search_books():
    search_text = request.form.get('search_text')
    matched_books = []

    for category_data in book_data:
        for book in category_data:
            if search_text.lower() in book['nameBook'].lower():
                matched_books.append(book)

    group_items=[matched_books[i:i+5] for i in range(0,len(matched_books),5)]
    return render_template('SearchResults.html', data=group_items)

























@app.route('/send_data')
def send_data():
    param1 = request.args.get('param1')
    bookId = int(param1)
    if libraryComic.search(bookId):
        return render_template('UiBookPage.html',book = libraryComic.search(bookId).data.to_json())
    elif libraryFiction.search(bookId):
        return render_template('UiBookPage.html',book = libraryFiction.search(bookId).data.to_json())
    elif libraryHorror.search(bookId):
        return render_template('UiBookPage.html',book = libraryHorror.search(bookId).data.to_json())
    elif libraryLearning.search(bookId):
        return render_template('UiBookPage.html',book = libraryLearning.search(bookId).data.to_json())
    elif libraryRomance.search(bookId):
       return render_template('UiBookPage.html',book = libraryRomance.search(bookId).data.to_json())
    else:
        return "not found"

@app.route('/receive_data/<book>', methods=['GET'])
def receive_data(book):
    bookId = int(book)
    if libraryComic.search(bookId):
        return render_template('UiBookPage.html',book = libraryComic.search(bookId).data.to_json())
    elif libraryFiction.search(bookId):
        return render_template('UiBookPage.html',book = libraryFiction.search(bookId).data.to_json())
    elif libraryHorror.search(bookId):
        return render_template('UiBookPage.html',book = libraryHorror.search(bookId).data.to_json())
    elif libraryLearning.search(bookId):
        return render_template('UiBookPage.html',book = libraryLearning.search(bookId).data.to_json())
    elif libraryRomance.search(bookId):
       return render_template('UiBookPage.html',book = libraryRomance.search(bookId).data.to_json())
    else:
        return "not found"























if __name__ == '__main__':
    app.run(debug=True)

