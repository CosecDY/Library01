from flask import Flask, jsonify, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('UiMainPage.html')

# รายการข้อมูลหนังสือในรูปแบบของออบเจกต์ Python
book_data = [
    {
        "imgSrc": "image/book_1.jpg",
        "writer": "John Deo",
        "categories": "Thriller, Horror, Romance",
        "price": "$25.50",
        "learnMoreLink": "#"
    },
    {
        "imgSrc": "image/book_2.jpg",
        "writer": "John Deo",
        "categories": "Thriller, Horror, Romance",
        "price": "$25.50",
        "learnMoreLink": "#"
    },
    {
        "imgSrc": "image/book_3.jpg",
        "writer": "John Deo",
        "categories": "Thriller, Horror, Romance",
        "price": "$25.50",
        "learnMoreLink": "#"
    },
    {
        "imgSrc": "image/book_4.jpg",
        "writer": "John Deo",
        "categories": "Thriller, Horror, Romance",
        "price": "$25.50",
        "learnMoreLink": "#"
    },
    {
        "imgSrc": "image/book_5.jpg",
        "writer": "John Deo",
        "categories": "Thriller, Horror, Romance",
        "price": "$25.50",
        "learnMoreLink": "#"
    }
]


@app.route('/api/book_data', methods=['GET'])
def get_book_data():
    return jsonify(data=book_data)

if __name__ == '__main__':
    app.run(debug=True)
