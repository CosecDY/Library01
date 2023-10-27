from flask import Flask, jsonify, render_template, request
from Library import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('UiMainPage.html')

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

if __name__ == '__main__':
    app.run(debug=True)

# book_data = [
#     {
#         "imgSrc": "static/image/book_1.jpg",
#         "writer": "John Deo",
#         "categories": "Thriller, Horror, Romance",
#         "price": "$25.50",
#         "learnMoreLink": "#"
#     },
#     {
#         "imgSrc": "image/book_2.jpg",
#         "writer": "John Deo",
#         "categories": "Thriller, Horror, Romance",
#         "price": "$25.50",
#         "learnMoreLink": "#"
#     },
#     {
#         "imgSrc": "image/book_3.jpg",
#         "writer": "John Deo",
#         "categories": "Thriller, Horror, Romance",
#         "price": "$25.50",
#         "learnMoreLink": "#"
#     },
#     {
#         "imgSrc": "image/book_4.jpg",
#         "writer": "John Deo",
#         "categories": "Thriller, Horror, Romance",
#         "price": "$25.50",
#         "learnMoreLink": "#"
#     },
#     {
#         "imgSrc": "image/book_5.jpg",
#         "writer": "John Deo",
#         "categories": "Thriller, Horror, Romance",
#         "price": "$25.50",
#         "learnMoreLink": "#"
#     }
# ]