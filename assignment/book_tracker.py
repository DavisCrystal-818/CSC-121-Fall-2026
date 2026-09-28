# Builds the Header of the library seen by the user
def dashboard(): 
    print('_' * 40)
    print("📚 YOUR LIBRARY")
    print('_' * 40)

#number of pages divided by 40 pages per hour to give the total reading hours for the book entered by user
def estimate_reading_time(pages):
    hours = pages/40
    return round(hours,1)


#Show Menu
def show_menu():
    print()
    print("What would you like to do?")
    print("1) View Books")
    print("2) Add a book")
    print()
    print("q) Quit")

    user_choice = input(">  ").strip().lower()
    return user_choice



#Information the user will enter
def add_book(library):
    title = input("Enter the book title: ").title()
    author = input("Enter the Author's name: ")
    pages = int(input("How many pages are in the book?  "))
    hours = estimate_reading_time(pages)
    book = {"title": title, 
            "author": author,
            "pages": pages,
            "hours": hours}
    library.append(book)
    print("Book added:")
    print(f"'{title}' by {author} -- approx. {hours} hours to read")

#Library of books 
# shows all books currently in the user's library.
def view_books(library):
    if len(library) == 0:  # If no books have been added let the user know the library is empty
        print("Your library is empty. Add a book first!")

    else:# go through each position in the library list.
        for book_index in range(len(library)):
            book = library[book_index] # Get the book dictionary stored at the current position

            print( f"{book_index + 1}. '{book['title']}' - {book['author']} "
                   f"({book['pages']} pages - approx. {book['hours']} hours to read)")  # Added 1 because Python indexes from 0, but the displayed list should start at 1
def main():
    library = [] #Creates an emply list
    dashboard() #shows the library header before menu starts

    #need to add what happens when user chooses a menu option. Look at built QuiziMe in prior project for help.
    while True:
        user_choice = show_menu()
        if user_choice == "1":
            view_books(library) #Will show the books in the library
        elif user_choice == "2":
            add_book(library) #Will add book to the library
        elif user_choice == "q" or user_choice == "quit" or user_choice == "exit":
            print("Goodbye!") #When the user inputs q, quit, or exit the program will stop the loop and end the program.
            break
        else:
            print("Sorry, that option isn't available.")

if __name__ == "__main__":
    main()




