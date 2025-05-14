#Library management
#A small library needs to register their books in a easy system

"""
Tasks: 
Create: 
-Add new books to the dictionary
-Each book will have: ID, Title, Autor, Publication year

Read: 
-Show all stored books
-Allow to search a book by his ID or title 

Update: 
-Modify the information of a book given his ID 
Example: Change the autor or the publication year

Delete: 
-Delete a book using his ID 

"""
 
library = {
    '001': {'title': '100 años de soledad', 'author': 'Gabriel García Márquez', 'year': 1967},
    '002': {'title': '1984', 'author': 'George Orwell', 'year': 1949}
}

def add_book(id, title, author, year):
    if id in library:
        print("❌ A book with that ID already exists.")
        return
    library[id] = {'title': title, 'author': author, 'year': year}
    print("✅ Book added successfully.")

def show_books():
    if not library:
        print("There are no books registered.")
        return
    print("📚 Books in the library:")
    for id, data in library.items():
        print(f"ID: {id}, Title: {data['title']}, Author: {data['author']}, Year: {data['year']}")

def search_by_id(id):
    if id in library:
        book = library[id]
        print(f"✅ Book found: {book}")
    else:
        print("❌ No book found with that ID.")

def search_by_title(title):
    results = [f"ID: {id}, {info}" for id, info in library.items() if title.lower() in info['title'].lower()]
    if results:
        print("✅ Results found:")
        for r in results:
            print(r)
    else:
        print("❌ No book found with that title.")

def update_book(id, new_author=None, new_year=None):
    if id not in library:
        print("❌ Book not found.")
        return
    if new_author:
        library[id]['author'] = new_author
    if new_year:
        library[id]['year'] = new_year
    print("✅ Book updated successfully.")

def delete_book(id):
    if id in library:
        del library[id]
        print("✅ Book deleted successfully.")
    else:
        print("❌ Book not found.")

def menu():
    while True:
        print("\n📘 LIBRARY MENU 📘")
        print("1. Add book")
        print("2. Show all books")
        print("3. Search book by ID")
        print("4. Search book by title")
        print("5. Update book")
        print("6. Delete book")
        print("7. Exit")

        option = input("Choose an option (1-7): ")

        if option == "1":
            id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            try:
                year = int(input("Publication year: "))
                add_book(id, title, author, year)
            except ValueError:
                print("❌ Invalid year.")

        elif option == "2":
            show_books()

        elif option == "3":
            id = input("Book ID: ")
            search_by_id(id)

        elif option == "4":
            title = input("Title to search (partial): ")
            search_by_title(title)

        elif option == "5":
            id = input("ID of the book to update: ")
            new_author = input("New author (leave blank if no change): ") or None
            new_year = input("New year (leave blank if no change): ")
            new_year = int(new_year) if new_year else None
            update_book(id, new_author, new_year)

        elif option == "6":
            id = input("ID of the book to delete: ")
            delete_book(id)

        elif option == "7":
            print("👋 Closing library system.")
            break

        else:
            print("❌ Invalid option.")

menu()