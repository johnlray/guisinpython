import PySimpleGUI as sg

sg.LOOK_AND_FEEL_TABLE['theme_percy'] = {'BACKGROUND': '#DAD0CE',
               'TEXT': 'black',
               'INPUT': '#DBCBAC',
               'SCROLL': '#CF6F55',
               'TEXT_INPUT': 'black',
               'BUTTON': ('white', '#6D9F85'),
               'PROGRESS': '#B48D70',
               'BORDER': 1,
               'SLIDER_DEPTH': 0,
               'PROGRESS_DEPTH': 0}

sg.change_look_and_feel('theme_percy')

layout = [
        [sg.Text('Pleae enter a variable label, text, and punches')],
        [sg.Text('Variable label', size=(30, 1)), sg.InputText()],
        [sg.Text('Item text', size=(30, 1)), sg.InputText()],
        [sg.Text('What type of\nquestion is it?', size=(30,1)), sg.InputText()]
        ]

window = sg.Window('Survey item entry window', layout, resizable=True)
event, values = window.read()
window.close()
print(event, values[0], values[1], values[2])