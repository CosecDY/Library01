#คำณวนbig o จากโค้ด
class Book:
    nextBookId = 0  

    def __init__(self, nameBook, availableQuantity, author, category, price, totalLikes):
        self.bookId = Book.nextBookId  
        Book.nextBookId += 1  
        self.nameBook = nameBook
        self.author = author
        self.availableQuantity = availableQuantity
        self.category = category
        self.price = price
        self.totalLikes = totalLikes

    def to_json(self):
        return {
            'bookId': self.bookId,
            'nameBook': self.nameBook,
            'writer': self.author,
            'availableQuantity': self.availableQuantity,
            'categories': self.category,
            'price': self.price,
            'totalLikes': self.totalLikes
        }
        
#มีส่วนสำคัญคือคอนสตรัคเตอร์ (constructor) และเมทอด to_json ซึ่งเป็นส่วนที่คำนวณ Big O notation ของโค้ดนี้:
#ในคอนสตรัคเตอร์ __init__, คุณมีการกำหนดค่าให้กับคุณสมบัติต่าง ๆ ของอ็อบเจ็กต์ Book โดยมีบรรทัดที่ใช้ self.bookId = Book.nextBookId และ Book.nextBookId += 1 ซึ่งทำให้ค่า nextBookId เพิ่มขึ้นทุกครั้งที่สร้างอ็อบเจ็กต์ใหม่. การนี้จะมีความซับซ้อน O(1) หรือคงที่เท่านั้น เนื่องจากจำนวนขั้นตอนที่ทำงานไม่ขึ้นอยู่กับขนาดข้อมูลขาเข้า.
#เมทอด to_json ทำงานโดยสร้างอ็อบเจ็กต์ JSON และกำหนดค่าให้กับคุณสมบัติต่าง ๆ ของอ็อบเจ็กต์ Book. การทำงานนี้จะมีความซับซ้อน O(1) เช่นกัน เนื่องจากจำนวนขั้นตอนไม่ขึ้นอยู่กับขนาดข้อมูลขาเข้า.
#ดังนั้ โค้ดของคุณมี Big O notation ทั้งหมดเท่ากับ O(1) หรือ O(คงที่) เนื่องจากจำนวนขั้นตอนไม่ขึ้นอยู่กับขนาดข้อมูลขาเข้าในทั้งคอนสตรัคเตอร์และเมทอด to_json.





#คำณวนbig o จากโค้ด
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
#มีคอนสตรัคเตอร์ __init__ สำหรับคลาส TreeNode ที่มีการกำหนดค่าให้กับคุณสมบัติ data, left, และ right ของอ็อบเจ็กต์ TreeNode.
#การกำหนดค่าให้กับคุณสมบัติทั้งสามไม่ขึ้นอยู่กับขนาดข้อมูลขาเข้าแต่เพียงแค่กำหนดค่าให้กับตัวแปร 3 ตัวนี้ ดังนั้น Big O notation ของโค้ดนี้คือ O(1) หรือ O(คงที่) เนื่องจากจำนวนขั้นตอนไม่ขึ้นอยู่กับขนาดข้อมูลขาเข้าและเสมอ.





#คำณวนbig o จากโค้ด  
class Library:
    def __init__(self):
        self.root = None
    
    def contains(self, book):
        return self._contains(self.root, book)

    def _contains(self, node, book):
        if node is None:
            return False
        if node.data == book:
            return True
        if book.bookId < node.data.bookId:
            return self._contains(node.left, book)
        return self._contains(node.right, book)

    def insert(self, newNode, category):
        self.root = self._insert(self.root, newNode, category)

    def _insert(self, node, newNode, category):
        if node is None:
            return newNode
        if newNode.data.bookId == node.data.bookId:
            node.data.author = newNode.data.author
            node.data.category = newNode.data.category
            node.data.available = newNode.data.available
        elif newNode.data.bookId < node.data.bookId:
            node.left = self._insert(node.left, newNode, category)
        else:
            node.right = self._insert(node.right, newNode, category)
        return node

    def search(self, bookId):
        return self._search(self.root, bookId)

    def _search(self, node, bookId):
        if node is None:
            return None
        if node.data.bookId == bookId:
            return node.data
        if bookId < node.data.bookId:
            return self._search(node.left, bookId)
        return self._search(node.right, bookId)

    def delete(self, bookId, category):
        self.root = self._delete(self.root, bookId, category)

    def _delete(self, node, bookId, category):
        if node is None:
            return node

        if bookId < node.data.bookId:
            node.left = self._delete(node.left, bookId, category)
        elif bookId > node.data.bookId:
            node.right = self._delete(node.right, bookId, category)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.data = self._minValueNode(node.right)
            node.right = self._delete(node.right, node.data.bookId, category)

        return node
    def _inOrderTraversal(self, node, category, outputFile):
        if node is not None:
            self._inOrderTraversal(node.left, category, outputFile)
            if node.data.category == category:
                outputFile.write(
                    f"{node.data.bookId},{node.data.nameBook},{node.data.availableQuantity},{node.data.author},{node.data.price},{node.data.totalLikes}\n"
                )
            self._inOrderTraversal(node.right, category, outputFile)

    def save_to_file(self, category):
        current_directory = os.getcwd()
        try:
            file_path = os.path.join(current_directory, "ListBooks", category + ".txt")
            with open(file_path, "w") as outputFile:
                self._inOrderTraversal(self.root, category, outputFile)
        except IOError:
            print("Unable to open the file.")

    def load_from_file(self, category, book_data_list):
        current_directory = os.getcwd()
        try:
            file_path = os.path.join(current_directory, "ListBooks", category + ".txt")
            with open(file_path, "r") as inputFile:
                for line in inputFile:
                    data = line.strip().split(",")
                    if len(data) >= 6:
                        bookId = int(data[0])
                        nameBook = data[1]
                        available = int(data[2])
                        author = data[3]
                        price = float(data[4])
                        totalLikes = int(data[5])
                        imgSrc = f"static/image/book_{bookId}.jpg"
                    
                        book_info = {
                            "nameBook": nameBook,
                            "availableQuantity": available,
                            "author": author,
                            "price": price,
                            "totalLikes": totalLikes,
                            "category": category,
                            "imgSrc": imgSrc,
                            "learnMoreLink": bookId
                        }

                        book_data_list.append(book_info)
        except FileNotFoundError:
            print("Unable to open the file.")


#contains เรียก _contains โดยเริ่มที่ root node และทำการเปรียบเทียบค่าของหนังสือเรื่องนั้น ๆ กับ node ในต้นไม้. ถ้าไม่พบ node ใด ๆ ที่มีค่าตรงกับหนังสือนี้ ก็จะเดิมพันคืน False. ถ้าพบ node ที่มีค่าตรงกัน ก็จะเดิมพันคืน True. การนี้มีความซับซ้อน O(h) โดยที่ h คือความสูงของต้นไม้ (ในกรณีสุดซ้ายหรือสุดขวา, h จะเท่ากับจำนวน node ทั้งหมดในต้นไม้) แต่ในกรณีสุดรวม (balanced tree) h จะมีความซับซ้อน O(log n) โดยที่ n คือจำนวน node ทั้งหมดในต้นไม้.

#insert เรียก _insert เพื่อแทรกหนังสือใหม่ลงในต้นไม้. การแทรกนี้มีความซับซ้อน O(h) หรือ O(log n) ตามความสูงของต้นไม้เช่นเดียวกับ contains.

#search เรียก _search โดยเริ่มที่ root node และค้นหาหนังสือโดยใช้ค่าของ bookId. การค้นหานี้มีความซับซ้อนเช่นเดียวกับ contains ซึ่งเป็น O(h) หรือ O(log n).

#delete เรียก _delete เพื่อลบหนังสือโดยใช้ค่า bookId. การลบนี้มีความซับซ้อนเช่นเดียวกับ contains และ search ซึ่งเป็น O(h) หรือ O(log n).

#save_to_file เป็นการแสดงข้อมูลหนังสือตามหมวดหมู่ลงในไฟล์ข้อความ แต่ไม่เกี่ยวกับขนาดข้อมูลขาเข้า ดังนั้นมีความซับซ้อน O(1).

#load_from_file อ่านข้อมูลหนังสือจากไฟล์ข้อความ แต่ไม่เกี่ยวกับขนาดข้อมูลขาเข้า ดังนั้นมีความซับซ้อน O(1).

#เนื่องจากความซับซ้อนที่เหนือถูกเรียกใช้โดยตรงจาก _contains, _insert, _search, และ _delete, คำนวณ Big O notation ของคลาส Library จะขึ้นอยู่กับความสูงของต้นไม้ที่ใช้ในการจัดเก็บข้อมูลหนังสือ:

#ในกรณีสุดขวาหรือสุดซ้าย, Big O notation คือ O(n) โดยที่ n คือจำนวน node ทั้งหมดในต้นไม้.
#ในกรณีสุดรวม (balanced tree) Big O notation คือ O(log n) โดยที่ n คือจำนวน node ทั้งหมดในต้นไม้.
#ดังนั้น, Big O notation ของคลาส Library จะขึ้นอยู่กับความสูงของต้นไม้ที่ใช้ในการจัดเก็บข้อมูลหนังสือและจำนวน node ทั้งหมดในต้นไม้.