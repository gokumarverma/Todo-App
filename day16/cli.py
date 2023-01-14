from get_todo import get_todo
from write_todo import write_todo
import time


now = time.strftime('%Y %b %d-%A %w %H:%H:%S %p')
print("Here are the details:")
print(f'Toady is {now}')

while True:
    user_action = input("Please enter add, edit, complete, show or exit: ").strip()
    if user_action.startswith("add"):

        item = user_action[4:]+'\n'
        todo = get_todo()

        todo.append(item)

        write_todo(todo)

    elif user_action.startswith('edit'):
        try:
            sr_no = int(user_action[5:])-1
            new_item = input("Enter new item to be updated: ")

            todo = get_todo()

            todo[sr_no] = new_item+'\n'

            write_todo(todo)

        except ValueError:
            print("Please enter a valid command")
            continue

    elif user_action.startswith('complete'):
        try:
            sr_c = int(user_action[9:])-1

            todo = get_todo()

            todo.pop(sr_c)

            write_todo(todo)

        except IndexError:
            print("please enter sr. in range")
            continue

    elif user_action.startswith('show'):
        todo = get_todo()

        new_todo = [i.strip("\n") for i in todo]

        for index, item in enumerate(new_todo):
            print(f'{index+1}. {item.capitalize()}')
        # for index, item in enumerate(todo):
        #     item = item.strip("\n")
            #     print(f'{index+1}. {item.capitalize()}')

    elif user_action.startswith('exit'):
        break
    else:
        print("wrong command")

print('Bye!!')
