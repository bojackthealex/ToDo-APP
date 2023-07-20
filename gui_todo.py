import functions
import PySimpleGUI

label = PySimpleGUI.Text("Type in a ToDo")
input_box = PySimpleGUI.InputText(tooltip="Enter a ToDo")
add_button = PySimpleGUI.Button("ADD")

window = PySimpleGUI.Window("My ToDo-APP", layout=[[label], [input_box, add_button]])
window.read()
window.close()