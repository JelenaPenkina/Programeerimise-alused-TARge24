from Book import Book
import Store

if __name__ == '__main__':
    b1 = Book("Sipsik", "Eno Raud", 5.5, 5)
    b2 = Book("Sipsik 2", "Eno Raud", 15.5, 3)
    b3 = Book("Sipsik 3", "Eno Raud", 1.5, 4)

    shop = Store('Black Books', 5)
    print(shop.add_book(b1))
    print(shop.add_book(b2))
    print(shop.add_book(b3))

    print(shop.books.append(b1))

    print(shop.can_remove_book(b2))
    print(shop.remove_book(b2))
    print(shop.can_remove_book(b2))
    print(shop.books)

    print(shop.get_all_books())
    print(shop.get_books_by_price())
    print(shop.get_books_popular_book())

