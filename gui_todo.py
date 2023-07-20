import functions
import PySimpleGUI

label = PySimpleGUI.Text("Type in a ToDo")
input_box = PySimpleGUI.InputText(tooltip="Enter a ToDo", key="TASK")
add_button = PySimpleGUI.Button("ADD")
edit_button = PySimpleGUI.Button("EDIT")
list_box = PySimpleGUI.Listbox(values=functions.get_todos(),
                               key="todos",
                               enable_events=True,
                               size=[45, 10])

window = PySimpleGUI.Window("My ToDo-APP",
                            layout=[[label],
                                    [input_box, add_button],
                                    [list_box, edit_button]],
                            font=('Arial', 14))

while True:
    event, values = window.read()

    match event:
        case "ADD":
            tasks = functions.get_todos()
            tasks.append(values["TASK"] + "\n")
            functions.write_todos(tasks)
            window["todos"].update(values=tasks)
        case "EDIT":
            todo_to_edit = values["todos"][0]
            new_todo = values["TASK"] + "\n"

            tasks = functions.get_todos()
            index = tasks.index(todo_to_edit)
            tasks[index] = new_todo
            functions.write_todos(tasks)
            window["todos"].update(values=tasks)
        case "todos":
            window["TASK"].update(value=values['todos'][0])


        case PySimpleGUI.WIN_CLOSED:
            break
    print(f"EVENT: {event}, VALUES: {values}")


window.close()
