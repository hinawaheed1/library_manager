
import streamlit as st

class Book:
    def __init__(self, title, author, publication_year, genre, read_status):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre
        self.read_status = read_status

class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = st.text_input("Enter book title: ")
        author = st.text_input("Enter book author: ")
        publication_year = st.number_input("Enter book publication year: ")
        genre = st.text_input("Enter book genre: ")
        read_status = st.selectbox("Have you read this book?", ["Yes", "No"])
        if st.button("Add Book"):
            book = Book(title, author, publication_year, genre, read_status == "Yes")
            self.books.append(book)
            st.success("Book added successfully!")

    def remove_book(self):
        title = st.text_input("Enter title of book to remove: ")
        if st.button("Remove Book"):
            for book in self.books:
                if book.title.lower() == title.lower():
                    self.books.remove(book)
                    st.success("Book removed successfully!")
                    return
            st.error("Book not found!")

    def search_book(self):
        st.write("Search by:")
        choice = st.selectbox("", ["Title", "Author"])
        if choice == "Title":
            title = st.text_input("Enter title: ")
            if st.button("Search"):
                for book in self.books:
                    if book.title.lower() == title.lower():
                        st.write(f"Title: {book.title}")
                        st.write(f"Author: {book.author}")
                        st.write(f"Publication Year: {book.publication_year}")
                        st.write(f"Genre: {book.genre}")
                        st.write(f"Read Status: {book.read_status}")
                        return
                st.error("Book not found!")
        elif choice == "Author":
            author = st.text_input("Enter author: ")
            if st.button("Search"):
                for book in self.books:
                    if book.author.lower() == author.lower():
                        st.write(f"Title: {book.title}")
                        st.write(f"Author: {book.author}")
                        st.write(f"Publication Year: {book.publication_year}")
                        st.write(f"Genre: {book.genre}")
                        st.write(f"Read Status: {book.read_status}")
                        return
                st.error("Book not found!")

    def display_all_books(self):
        st.write("Your Library:")
        for i, book in enumerate(self.books, start=1):
            st.write(f"{i}. {book.title} by {book.author} ({book.publication_year}) - {book.genre} - {'Read' if book.read_status else 'Unread'}")

    def display_statistics(self):
        total_books = len(self.books)
        read_books = sum(1 for book in self.books if book.read_status)
        unread_books = total_books - read_books
        st.write(f"Total books: {total_books}")
        st.write(f"Read books: {read_books}")
        st.write(f"Unread books: {unread_books}")
        st.write(f"Percentage read: {(read_books / total_books) * 100:.2f}%")

def main():
    library = Library()
    st.title("Personal Library Manager")
    st.write("Welcome to your personal library manager!")
    st.write("Please select an option from the menu below:")
    choice = st.selectbox("", ["Add a book", "Remove a book", "Search for a book", "Display all books", "Display statistics", "Exit"])
    if choice == "Add a book":
        library.add_book()
    elif choice == "Remove a book":
        library.remove_book()
    elif choice == "Search for a book":
        library.search_book()
    elif choice == "Display all books":
        library.display_all_books()
    elif choice == "Display statistics":
        library.display_statistics()
    elif choice == "Exit":
        st.write("Goodbye!")

if __name__ == "__main__":
    main()

