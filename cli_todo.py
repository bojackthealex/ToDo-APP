import functions
import time


while True:
    #----------------- MAIN MENU -------------------------------
    now = time.strftime("%b %d, %Y %H:%M:%S")
    print(f"It is: {now}")
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()
    #----------------- ACTIONS ----------------------------------

        #-------- ADDING TODOS ----------
    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()
        todos.append(todo + "\n")

        functions.write_todos(todos)

    # --------- SHOWING TODOS -----------
    elif user_action.startswith("show"):

        todos = functions.get_todos()

        new_todos = [item.strip('\n') for item in todos]

        #--- ENUMERATE THE ITEMS ---
        for index, item in enumerate(new_todos):
            row = f"{index + 1}-{item}"
            print(row)


    #---------- EDITING TODOS ------------
    elif user_action.startswith("edit"):


        number = int(user_action[5:])
        number -= 1
        new_todo = input("Enter new todo: ")

        todos = functions.get_todos()

        todos[number] = new_todo + "\n"

        functions.write_todos(todos)
    #------------ COMPLETING A TASK -----------------
    elif user_action.startswith("complete"):
        number = int(user_action[8:])

        todos = functions.get_todos()
        todos.pop(number - 1)

        functions.write_todos(todos)
    #----------- CLOSING THE PROGRAM ----------------
    elif user_action == "exit":
        break
    else:
        print("Command is invalid!")
print("Good bye!")
