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

user_typeface='Raleway 18'

layout = [
        [sg.Text('Pleae enter a variable label, text, and punches', font='Raleway 20')],
        [sg.Text('Variable label', size=(10, 1), font=user_typeface), sg.InputText(font=user_typeface)],
        [sg.Text('Item text', size=(10, 1), font=user_typeface), sg.InputText(font=user_typeface)],
        [sg.Text('What type of\nquestion is it?', font=user_typeface), sg.Radio('Single', 'C1', font=user_typeface), sg.Radio('Multiple', 'C1', font=user_typeface), sg.Radio('Open', 'C3', font=user_typeface), sg.Radio('Open', 'Dyngrid', font=user_typeface)],
        [sg.Text('Randomizations', font=user_typeface), sg.Radio('None', 'C1', font=user_typeface), sg.Radio('One', 'C1', font=user_typeface), sg.Radio('Two', 'C3', font=user_typeface)],
        [sg.Submit('Submit'), sg.Cancel()]
        ]

window = sg.Window('Survey item entry window', layout, resizable=True, grab_anywhere=True, size = (600,300))

while True:
    event, values = window.read()
    if event in (None,'Exit'):
        break
    print(event, values)
    window.close()

