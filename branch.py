def search_book():
    keyword=input('enter book title keyword:').lower()
    found=[book for book in books if keyword in book.lower()]
    if found:
        print("book found: ")
        for b in found:
            print(f"-{b}")
        else:
            print("no books found with that keyword.")