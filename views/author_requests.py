AUTHORS = [
    {
        "id": 1,
        "first_name": "Barack",
        "last_name": "Obama",
        "image": "https://upload.wikimedia.org/wikipedia/commons/8/8d/President_Barack_Obama.jpg",
        "email": "ba@obama.com",
        "favorite": True
    },
    {
        "id": 2,
        "first_name": "Tomi",
        "last_name": "Adeyemi",
        "image": "https://upload.wikimedia.org/wikipedia/commons/1/17/Tomi_Adeyemi_2020.JPG",
        "email": "ta@ta.com.com",
        "favorite": True
    },
    {
        "id": 3,
        "first_name": "Howard",
        "last_name": "Zinn",
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/ef/Howard_Zinn%2C_2009_%28cropped%29.jpg",
        "email": "hz@zinn.com",
        "favorite": False
    }
]


def get_all_authors():
    """Get all the authors"""
    return AUTHORS

def get_single_author(id):
    """Get a single author"""
    # Variable to hold the found author, if it exists
    requested_author = None

    # Iterate the AUTHORS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for author in AUTHORS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if author["id"] == id:
            requested_author = author

    return requested_author

def create_author(author):
    """Creates new author"""
    # Get the id value of the last animal in the list
    max_id = AUTHORS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    author["id"] = new_id

    # Add the animal dictionary to the list
    AUTHORS.append(author)

    # Return the dictionary with `id` property added
    return author

def delete_author(id):
    """Deletes"""
    # Initial -1 value for animal index, in case one isn't found
    author_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, author in enumerate(AUTHORS):
        if author["id"] == id:
            # Found the animal. Store the current index.
            author_index = index

    # If the animal was found, use pop(int) to remove it from list
    if author_index >= 0:
        AUTHORS.pop(author_index)
