FILEPATH = "todos.txt"



def get_todos(filepath=FILEPATH):
    """Read a TXT-File and returns a list of items"""
    with open("todos.txt", "r") as file_local:
        target_local = file_local.readlines()
    return target_local

def write_todos(todos_arg, filepath=FILEPATH):
    """Write items of a list in a text file."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)





