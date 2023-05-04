BOOKS = [
    {
        "id": 1,
        "title": "A Promised Land",
        "image": "https://images-na.ssl-images-amazon.com/images/I/91+NBrXG-PL.jpg",
        "price": "24.99",
        "sale": False,
        "description": ""
    },
    {
        "id": 2,
        "title": "Children of Blood and Bone",
        "image": "https://images-na.ssl-images-amazon.com/images/I/A1agLFsWkOL.jpg",
        "price": "12.99",
        "sale": True,
        "description": ""
    },
    {
        "id": 3,
        "title": "A People's History of the United States of America",
        "image": "https://images-na.ssl-images-amazon.com/images/I/51529Lfc2ML.jpg",
        "price": "30.00",
        "sale": False,
        "description": ""
    }
]


def get_all_books():
    """Get all the books"""
    return BOOKS

# Function with a single parameter
def get_single_book(id):
    """Get a single book"""
    # Variable to hold the found book, if it exists
    requested_book = None

    # Iterate the BOOKS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for book in BOOKS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if book["id"] == id:
            requested_book = book

    return requested_book

def create_book(book):
    """Creates new book"""
    # Get the id value of the last animal in the list
    max_id = BOOKS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    book["id"] = new_id

    # Add the animal dictionary to the list
    BOOKS.append(book)

    # Return the dictionary with `id` property added
    return book

def delete_book(id):
    """Deletes"""
    # Initial -1 value for animal index, in case one isn't found
    book_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, book in enumerate(BOOKS):
        if book["id"] == id:
            # Found the animal. Store the current index.
            book_index = index

    # If the animal was found, use pop(int) to remove it from list
    if book_index >= 0:
        BOOKS.pop(book_index)
