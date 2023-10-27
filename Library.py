import os

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

    
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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
                            "learnMoreLink":bookId
                        }

                        book_data_list.append(book_info)
        except FileNotFoundError:
            print("Unable to open the file.")

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
