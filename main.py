# Library Management System

library = []

def add_book():
    book = input("Enter Book Name: ")
    library.append(book)
    print("Book added successfully!")

def show_books():
    if len(library) == 0:
        print("Library is empty.")
    else:
        print("\nBooks in Library:")
        for i, book in enumerate(library, start=1):
            print(i, ".", book)

def search_book():
    name = input("Enter book name to search: ")
    if name in library:
        print("Book found!")
    else:
        print("Book not found.")

def delete_book():
    name = input("Enter book name to delete: ")
    if name in library:
        library.remove(name)
        print("Book deleted.")
    else:
        print("Book not found.")

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        show_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        delete_book()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice")