# simple Library Management System
books=[]
members=[]
borrowed_books={}
# Function to add a book
def add_book():
    title=input("enter book title: ")
    if title in books:
        print("book already exists.")
    else:
        books.append(title)
        print(f"book{title}added.")
#function to register a member
def register_member():
    name=input("enter member name:")
    if name in members: 
        print('member already registered.')
    else:
        members.append(name)
        borrowed_books[name]=[]
        print(f"member'{name}'registered.")
#function to borrow a book 
def borrow_book():
    name=input('enter member name:')
    title=input('enter book title to borrow: ')
    if name not in members:
        print("member not registered.")
    elif title not in books:
        print('book not available.')
    elif title in sum (borrowed_books.values(),[]):
        print('book is currently borrowed.')
    else:
        borrowed_books[name].append(title)
        print(f"book'{title}'borrowed by {name}.")
#function tp return a book
def return_book():
    name=input('enter member name:')
    title=input('enter book title to return:')
    if name in borrowed_books and title in borrowed_books[name]:
        borrowed_books[name].remove(title)
        print(f"book'{title}'returned by {name}.")
    else:
        print("invalid return.book not borrowed.") 
#function to view available books
def view_books():
    print("\nAvailable Books:")
    for book in books:
        if book not in sum(borrowed_books.values(),[]):
            print(f"-{book}")
            print()
#main menu
def menu():
    while True:
        print('\n---Library Menu---')
        print('1.Add Book')
        print('2.register member')
        print('3.borrow book')
        print('4.return book')
        print('5.view available books')
        print('6.exit')
        choice=input("enter choice: ")
        if choice=="1":
            add_book()
        elif choice=='2':
            register_member()
        elif choice=='3':
            borrow_book()
        elif choice=='4':
            return_book()
        elif choice=='5':
            view_books()
        elif choice=='6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.Try again.")
        
menu()

                      
                    