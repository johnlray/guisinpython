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
        [sg.Button('Single', key='SINGLE1'), sg.Cancel()]
        ]

window = sg.Window('Survey item entry window', layout, resizable=True, grab_anywhere=True, size = (700,300))

i=0

while True:
    event, values = window.read(timeout=100)
    #if event != sg.TIMEOUT_KEY:
    #    print(i, event, values)
    if event in (None,'Exit'):
        break
    #elif event == 'SINGLE1':
    #    sg.popup('This is a BLOCKING popup','all windows remain inactive while popup active')
    i+=1
    if event == 'SINGLE1' and not single_window_active:
        single_window_active = True
        single_window_layout = [
                [sg.Text('Single-response item')],
                [sg.Text('Variable label: ', font=user_typeface), sg.Input(font=user_typeface, key='-IN-')],
                [sg.Text('Item text', font=user_typeface), sg.Input(font=user_typeface)],
                [sg.Text('What type of item is it?', font=user_typeface)],
                [sg.Radio('Support-oppose', 'RADIO1', font=user_typeface)],
                [sg.Submit('Done')]
                ]
        single_window = sg.Window('Single-response item window', single_window_layout)
    if single_window_active:
        event, values = single_window.read(timeout=100)
        if event != sg.TIMEOUT_KEY:
            print("single-reponse item window ", event)
        if event in (None, 'Exit'):
            single_window_active = False
            single_window.close()
        if event == 'Show':
            sg.popup('You entered', values['-IN-'])

window.close()

