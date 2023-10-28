import os

class Book:
    nextBookId = 0  

    def __init__(self, nameBook, availableQuantity, author, category, price, totalLikes, imgSrc):
        self.bookId = Book.nextBookId  
        Book.nextBookId += 1  
        self.nameBook = nameBook
        self.author = author
        self.availableQuantity = availableQuantity
        self.category = category
        self.price = price
        self.totalLikes = totalLikes
        self.imgSrc = imgSrc

    def to_json(self):
        return {
            'bookId': self.bookId,
            'nameBook': self.nameBook,
            'writer': self.author,
            'availableQuantity': self.availableQuantity,
            'categories': self.category,
            'price': self.price,
            'totalLikes': self.totalLikes,
            'imgSrc' : self.imgSrc
        }

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Library:
    def __init__(self):
        self.root = None

    def insert(self, book):
        self.root = self._insert_recursive(self.root, book)

    def _insert_recursive(self, node, book):
        if node is None:
            return TreeNode(book)
        if book.bookId < node.data.bookId:
            node.left = self._insert_recursive(node.left, book)
        else:
            node.right = self._insert_recursive(node.right, book)
        return node

    def search(self, book_id):
        return self._search_recursive(self.root, book_id)

    def _search_recursive(self, node, book_id):
        if node is None or node.data.bookId == book_id:
            return node
        if book_id < node.data.bookId:
            return self._search_recursive(node.left, book_id)
        return self._search_recursive(node.right, book_id)

    def delete(self, book_id):
        self.root = self._delete_recursive(self.root, book_id)

    def _delete_recursive(self, node, book_id):
        if node is None:
            return node
        if book_id < node.data.bookId:
            node.left = self._delete_recursive(node.left, book_id)
        elif book_id > node.data.bookId:
            node.right = self._delete_recursive(node.right, book_id)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_node = self._find_min(node.right)
            node.data = min_node.data
            node.right = self._delete_recursive(node.right, min_node.data.bookId)
        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
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
        except IOError as e:
            print(f"Unable to open the file: {e}")

    def load_from_file(self, category, book_data_list):
        current_directory = os.getcwd()
        try:
            file_path = os.path.join(current_directory, "ListBooks", category + ".txt")
            with open(file_path, "r", encoding="utf-8") as inputFile:
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

                        book_info = Book(nameBook, available, author, category, price, totalLikes, imgSrc)
                        book_info.bookId = bookId  
                    
                        self.insert(book_info)
                        book_data_list.append(book_info.to_json())
        except FileNotFoundError as e:
            print(f"Unable to open the file: {e}")




     # def _minValueNode(self, node):
    #     while node.left is not None:
    #         node = node.left
    #     return node.data

    # def borrow(self, bookId, category):
    #     book = self.search(bookId)
    #     if book and book.available:
    #         book.available = False
    #         self.save_to_file(category)
    #         return True
    #     return False

    # def return_book(self, bookId, category):
    #     book = self.search(bookId)
    #     if book and not book.available:
    #         book.available = True
    #         self.save_to_file(category)
    #         return True
    #     return False
    
    # def getbookIdsInCategory(self, category):
    #     bookIds = []
    #     self._getbookIdsInCategory(self.root, category, bookIds)
    #     return bookIds

    # def _getbookIdsInCategory(self, node, category, bookIds):
    #     if node is not None:
    #         self._getbookIdsInCategory(node.left, category, bookIds)
    #         if node.data.category == category:
    #             bookIds.append(node.data.bookId)
    #         self._getbookIdsInCategory(node.right, category, bookIds)

    # def getAllBookNames(self):
    #     bookNames = []
    #     self._inOrderBookNames(self.root, bookNames)
    #     return bookNames

    # def _inOrderBookNames(self, node, bookNames):
    #     if node is not None:
    #         self._inOrderBookNames(node.left, bookNames)
    #         bookNames.append(node.data.nameBook)
    #         self._inOrderBookNames(node.right, bookNames)

    # def getAllbookIds(self):
    #     bookIds = []
    #     self._inOrderbookIds(self.root, bookIds)
    #     return bookIds

    # def _inOrderbookIds(self, node, bookIds):
    #     if node is not None:
    #         self._inOrderbookIds(node.left, bookIds)
    #         bookIds.append(node.data.bookId)
    #         self._inOrderbookIds(node.right, bookIds)
