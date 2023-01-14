def write_todo(todo_arg, filepath='todo_list.txt'):
    """This function will write the list to text file"""
    with open(filepath, 'w') as file_write:
        file_write.writelines(todo_arg)

