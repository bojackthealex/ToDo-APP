import functions
import PySimpleGUI

label = PySimpleGUI.Text("Type in a ToDo")
input_box = PySimpleGUI.InputText(tooltip="Enter a ToDo", key="TASK")
add_button = PySimpleGUI.Button("ADD")

window = PySimpleGUI.Window("My ToDo-APP",
                            layout=[[label],
                                    [input_box, add_button],
                                    ],
                            font=('Helvetica', 14))

while True:
    event, values = window.read()

    match event:
        case "ADD":
            tasks = functions.get_todos()
            tasks.append(values["TASK"] + "\n")
            functions.write_todos(tasks)
        case sg.WIN_CLOSED:
            break

window.close()