# Example of a custom module

print('Imported mymodule')

test = 'Test String'

def find_index(to_search, target):
    """
    Returns the index of target in to_search list.
    Returns -1 if not found.
    """
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1
