# Builds the Header of the library seen by the user.
def dashboard(): 
    print('_' * 40)
    print("📚 YOUR LIBRARY")
    print('_' * 40)

#number of pages divided by 40 pages per hour to give the total reading hours for the book entered by user
def estimate_reading_time(pages):
    hours = pages/40
    return round(hours,1)

#Information the user will enter
def add_book():
    title = input("Enter the book title: ").title()
    author = input("Enter the Author's name: ")
    pages = int(input("How many pages are in the book?  "))
    hours = estimate_reading_time(pages)
    print(f"'{title}' by {author} -- approx. {hours} hours to read")

def main():
    dashboard()
    add_book()

if __name__ == "__main__":
    main()




