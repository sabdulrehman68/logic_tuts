class Book:
    def __init__(self,book_id,book_name,author_name):
        self.book_id = book_id
        self.book_name = book_name
        self.author_name = author_name

class Library:
    def __init__(self,address_lib,book_list):
        self.book_list = book_list
        self.address_lib = address_lib

    def count_books(self,bookCount):
        for book in self.book_list:
            if book.author_name in bookCount.keys():
                bookCount[book.author_name] += 1
            else:
                bookCount[book.author_name] = 1
        for key in bookCount.keys():
            key = key.upper()
        
        return bookCount
    def __str__(self):
        return book_list

def get_city(city_name,books,lists):
    for book in books:    
        if book.address_lib["city"] == city_name:
            for book1 in book.book_list:
                lists.append(book1.book_name)
    return lists

if __name__ == "__main__":
    no_lib_obj = int(input())
    all_books = []
    for i in range(0,no_lib_obj):
        count_of_book = int(input())
        book_list  = []
        address = {}
        for j in range(0,count_of_book):
            book_id = int(input())
            book_name = str(input())
            author_name = str(input())
            author_name1 = author_name.lower()
            book_list.append(Book(book_id,book_name,author_name1))
        street = str(input())
        area = str(input())
        city = str(input())
        state = str(input())
        zip_code = int(input())
        address["street"] = street
        address["area"] = area
        address["city"] = city
        address["state"] = state
        address["zip"] = zip_code
        lib = Library(address,book_list)
        all_books.append(lib)
    count_of_books = {}
    books_count = lib.count_books(count_of_books)
    city_name = str(input())
    for k in books_count:
        print(k, books_count[k])
    lists = []
    list1 = get_city(city_name,all_books,lists)
    print(list1)