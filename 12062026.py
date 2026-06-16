

# Generate a set of unique numbers from a given list
numbers = [1, 2, 3, 4, 5, 3, 2, 6, 7, 8]
unique_numbers = set(numbers)
print("Unique numbers:", unique_numbers)

# Add new elements to the set
unique_numbers.add(9)
unique_numbers.update([10, 11])
print("After adding elements:", unique_numbers)

# Remove existing elements from the set
unique_numbers.remove(2)   # removes element 2
unique_numbers.discard(5)  # removes element 5 if present
print("After removing elements:", unique_numbers)

# Perform union, intersection, and difference with another set
other_set = {5, 6, 7, 12, 13}
print("Union:", unique_numbers.union(other_set))
print("Intersection:", unique_numbers.intersection(other_set))
print("Difference:", unique_numbers.difference(other_set))




# Dictionary to store books
library = {}

# Function to add a new book
def add_book(title, author, year, genre):
    library[title] = {
        "Author": author,
        "Year": year,
        "Genre": genre
    }

# Function to remove a book
def remove_book(title):
    if title in library:
        del library[title]
        print(f"Removed book: {title}")
    else:
        print(f"Book '{title}' not found.")

# Function to search for books by title, author, or genre
def search_books(keyword):
    results = []
    for title, info in library.items():
        if (keyword.lower() in title.lower() or
            keyword.lower() in info["Author"].lower() or
            keyword.lower() in info["Genre"].lower()):
            results.append((title, info))
    return results

# Function to display all books sorted by title or author
def display_books(sort_by="title"):
    if sort_by == "title":
        sorted_books = sorted(library.items(), key=lambda x: x[0])
    elif sort_by == "author":
        sorted_books = sorted(library.items(), key=lambda x: x[1]["Author"])
    else:
        sorted_books = library.items()
    
    for title, info in sorted_books:
        print(f"{title} - {info['Author']} ({info['Year']}) [{info['Genre']}]")


# Add sample books
add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Novel")
add_book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction")
add_book("1984", "George Orwell", 1949, "Dystopian")
add_book("Pride and Prejudice", "Jane Austen", 1813, "Romance")

print("\nAll books sorted by title:")
display_books("title")

print("\nAll books sorted by author:")
display_books("author")

print("\nSearch results for 'George':")
for book in search_books("George"):
    print(book)

# Remove a book
remove_book("1984")

print("\nLibrary after removal:")
display_books("title")




output:
    
    Unique numbers: {1, 2, 3, 4, 5, 6, 7, 8}
After adding elements: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
After removing elements: {1, 3, 4, 6, 7, 8, 9, 10, 11}
Union: {1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
Intersection: {6, 7}
Difference: {1, 3, 4, 8, 9, 10, 11}

All books sorted by title:
1984 - George Orwell (1949) [Dystopian]
Pride and Prejudice - Jane Austen (1813) [Romance]
The Great Gatsby - F. Scott Fitzgerald (1925) [Novel]
To Kill a Mockingbird - Harper Lee (1960) [Fiction]

All books sorted by author:
The Great Gatsby - F. Scott Fitzgerald (1925) [Novel]
1984 - George Orwell (1949) [Dystopian]
To Kill a Mockingbird - Harper Lee (1960) [Fiction]
Pride and Prejudice - Jane Austen (1813) [Romance]

Search results for 'George':
('1984', {'Author': 'George Orwell', 'Year': 1949, 'Genre': 'Dystopian'})
Removed book: 1984

Library after removal:
Pride and Prejudice - Jane Austen (1813) [Romance]
The Great Gatsby - F. Scott Fitzgerald (1925) [Novel]
To Kill a Mockingbird - Harper Lee (1960) [Fiction]
PS C:\Users\prave\Desktop\PJ> 
    
    