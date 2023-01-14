# import get_todo
# import write_todo
# import PySimpleGUI as sg
#
# label = sg.Text("Add text")
# text_input = sg.InputText(tooltip='add text only')
# button = sg.Button("Add")
#
#
# das = sg.Window('WellBeing', layout=[[label], [text_input,button]])
# das.read()
# das.close()

import PySimpleGUI as sg

label1 = sg.Text('Enter feet:')
box1 = sg.InputText(tooltip='Enter feets to convert')

label2 = sg.Text('Enter Inches:')
box2 = sg.InputText(tooltip='Enter inches to convert')

button = sg.Button('Convert')

gui = sg.Window('Convertor', layout=[[label1,box1],
                                     [label2,box2],
                                     [button]])
gui.read()
gui.close()
