from flask import Flask, jsonify, render_template
from Library import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('UiLoginPage.html')

@app.route('/login')
def login():
    return render_template('UiLoginPage.html')

@app.route('/forget_password')
def forgot():
    return render_template('UiForgotPassword.html')

@app.route('/register')
def register():
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

if __name__ == '__main__':
    app.run(debug=True)

