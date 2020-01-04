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

single_window_active = False
multi_window_active = False
openend_window_active = False
dyngrid_window_active = False
ab_randomization_window_active = False
abc_randomization_window_active = False

layout = [
        [sg.Text('Pleae enter a variable label, text, and punches', font='Raleway 20')],
        [sg.Text('Variable label', size=(10, 1), font=user_typeface), sg.InputText(font=user_typeface)],
        [sg.Text('Item text', size=(10, 1), font=user_typeface), sg.InputText(font=user_typeface)],
        [sg.Text('What type of\nquestion is it?', font=user_typeface), sg.Radio('Single', 'C1', font=user_typeface), sg.Radio('Multiple', 'C1', font=user_typeface), sg.Radio('Open', 'C2', font=user_typeface), sg.Radio('Open', 'C3', font=user_typeface), sg.Radio('Message test with A/B split', 'C4', font=user_typeface), sg.Radio('Message test with A/B/C split', 'C5', font=user_typeface)],
        [sg.Submit('Submit'), sg.Cancel()]
        ]

window = sg.Window('Survey item entry window', layout, resizable=True, grab_anywhere=True, size = (600,300))

while True:
    event, values = window.read()
    if event in (None,'Exit'):
        break
    print(event, values)
    window.close()

