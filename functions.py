import os

FILEPATH = "todos.txt"

def get_todos():
    filepath = 'todos.txt'
    if not os.path.exists(filepath):
        with open(filepath, 'w') as file_local:
            pass  # Create the file if it doesn't exist

    """
    Read a text file and return the list of
    to do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


#print(help(get_todos))

def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the todos text file.
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


#print(__name__)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())


def count(phrase):
    return phrase.count('.')
