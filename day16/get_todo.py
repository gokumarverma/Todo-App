def get_todo(filepath='todo_list.txt'):
    """This function will read the text file and return a list"""
    with open(filepath, 'r') as file_local:
        todo_local = file_local.readlines()
    return todo_local



