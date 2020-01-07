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
        [sg.Text('What type of question do you want to write?', font=user_typeface)],
        [sg.Radio('Single', key='Launch single window radio', font=user_typeface), sg.Radio('Multiple', key='Launch multi window', font=user_typeface), sg.Radio('Open', key='Launch openend window', font=user_typeface)],
        [sg.Radio('Dyngrid', key='Launch dyngrid window', font=user_typeface), sg.Radio('Message test with A/B split', key='Launch a/b split window', font=user_typeface), sg.Radio('Message test with A/B/C split', key='Launch a/b/c split window', font=user_typeface)],
        [sg.Submit('Single', key='Launch single window'), sg.Cancel()]
        ]

window = sg.Window('Survey item entry window', layout, resizable=True, grab_anywhere=True, size = (700,300))

i=0

while True:
    event, values = window.read()
    if event in (None,'Exit'):
        break
    i+=1
    if event == 'Launch single window' and not single_window_active:
        single_window_active = True
        single_window_layout = [
                [sg.Text('Single-response item')],
                [sg.Text('Variable label: ', font=user_typeface), sg.Input(font=user_typeface)],
                [sg.Text('Item text', font=user_typeface), sg.Input(font=user_typeface)]
                [sg.Text('What type of item is it?')],
                [sg.Radio('Support/oppose', font=user_typeface), sg.Radio('Approve/disapprove', font=user_typeface), sg.Radio('Agree/disagree', font=user_typeface)]
                ]
        single_window = sg.Window('Single-response item window', single_window_layout)
    if event == 'Launch multi window' and not single_window_active:
        single_window_active = True
        single_window_layout = [
                [sg.Text('Single-response item')],
                [sg.Text('Variable label: ', font=user_typeface), sg.Input(font=user_typeface)],
                [sg.Text('Item text', font=user_typeface), sg.Input(font=user_typeface)]
                [sg.Text('What type of item is it?')],
                [sg.Radio('Support/oppose', font=user_typeface), sg.Radio('Approve/disapprove', font=user_typeface), sg.Radio('Agree/disagree', font=user_typeface)]
                ]
        single_window = sg.Window('Single-response item window', single_window_layout)
    if single_window_active:
        event, values = single_window.read(timeout=100)
        if event != sg.TIMEOUT_KEY:
            print("single-reponse item window ", event)
        if event in (None, 'Exit'):
            single_window_active = False
            single_window.close()

window.close()

