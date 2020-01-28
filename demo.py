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
abtest_window_active = False
abctest_window_active = False

layout = [
        [sg.Text('Pleae enter a variable label, text, and punches', font='Raleway 20')],
        [sg.Text('What type of question do you want to write?', font=user_typeface)],
        [sg.Button('Single', key='SINGLE1'), sg.Button('Multiple', key='MULTI1'), sg.Button('Openend', key='OPENEND1'), sg.Button('A-B test', key='ABTEST1'), sg.Button('A-B-C test', key='ABCTEST1'), sg.Cancel()]
        ]

window = sg.Window('Survey item entry window', layout, resizable=True, grab_anywhere=True, size = (700,300))

items = {}

i=0

while True:
    event, values = window.read(timeout=100)
    if event in (None,'Exit'):
        break
    i+=1
    # the single event window
    if event == 'SINGLE1' and not single_window_active:
        single_window_active = True
        single_window_layout = [
                [sg.Text('Single-response item')],
                [sg.Text('Variable alias: ', font=user_typeface), sg.Input(font=user_typeface, key='-SINGLEALIAS-')],
                [sg.Text('Variable label: ', font=user_typeface), sg.Input(font=user_typeface, key='-SINGLELABEL-')],
                [sg.Text('Item text', font=user_typeface), sg.Input(font=user_typeface, key='-SINGLEDESCRIPTION-')],
                [sg.Radio('Support-oppose', 'response_type', key='-SUPOP-', font=user_typeface), sg.Radio('Approve-disapprove', 'response_type', key='-APDIS-', font=user_typeface), sg.Radio('Favorable-unfavorable', 'response_type', key='-FAVUNFAV-', font=user_typeface)],
                [sg.Submit('Done', key='SINGLEDONE')]
                ]
        single_window = sg.Window('Single-response item window', single_window_layout)
    if single_window_active:
        event, values = single_window.read(timeout=100)
        if event != sg.TIMEOUT_KEY:
            print("single-reponse item window ", event)
        if event in (None, 'Exit', 'SINGLEDONE'):
            single_window_active = False
            single_window.close()
            item = {
                    "alias": values['-SINGLEALIAS-'],
                    "label": values['-SINGLELABEL-'],
                    "description": values['-SINGLEDESCRIPTION-'],
                    "type_supop": values['-SUPOP-'],
                    "type_apdis": values['-APDIS-'],
                    "type_favunfav": values['-FAVUNFAV-']
                    }
            
            items.update({values['-SINGLEALIAS-']: item})
            print(items)
            
    # the multiple event window
    if event == 'MULTI1' and not multi_window_active:
        multi_window_active = True
        multi_window_layout = [
                [sg.Text('Multiple-response item')],
                                [sg.Text('Variable alias ', font=user_typeface), sg.Input(font=user_typeface, key='-MULTIPLERESPONSEALIAS-')],
                [sg.Text('Variable label: ', font=user_typeface), sg.Input(font=user_typeface, key='-MULTIPLERESPONSELABEL-')],
                [sg.Text('Selections, separate by comma', font=user_typeface), sg.Input(font=user_typeface, key='-MULTIOPTIONS=')]
                [sg.Submit('Done', key='MULTIDONE')]
                ]
        multi_window = sg.Window('Multiple-response item window', multi_window_layout)
    if multi_window_active:
        event, values = multi_window.read(timeout=100)
        if event != sg.TIMEOUT_KEY:
            print("multiple-reponse item window ", event)
        if event in (None, 'Exit', 'MULTIDONE'):
            multi_window_active = False
            multi_window.close()
            
            item = {
                    "alias": values['-MULTIPLERESPONSEALIAS-'],
                    "label": values['-MULTIPLERESPONSELABEL-'],
                    "type": values['-MULTIOPTIONS-']
                    }
            
            items.update({values['-MULTIPLERESPONSEALIAS-']: item})

            print(items)
            
    # the openend event window
    if event == 'OPENEND1' and not openend_window_active:
        openend_window_active = True
        openend_window_layout = [
                [sg.Text('Variable alias', font=user_typeface), sg.Input(font=user_typeface, key='-OPENALIAS-' )],
                [sg.Text('Variable label', font=user_typeface), sg.Input(font=user_typeface, key='-OPENLAB-')],
                [sg.Text('Enter open-ended question text here', font=user_typeface), sg.Input(font=user_typeface)],
                [sg.Submit('Done', key='OPENDONE')]
                ]
        openend_window = sg.Window('Open-end item window', openend_window_layout)
    if openend_window_active:
        event, values = openend_window.read(timeout=100)
        if event != sg.TIMEOUT_KEY:
            print('open-end item window ', event)
        if event in (None, 'Exit', 'OPENDONE'):
            openend_window_active = False
            openend_window.close()
            
            item = {
                    "alias": values['-OPENALIAS-'],
                    "label": values['-OPENLAB-']
                    }
            
            items.update({values['-OPENALIAS-']: item})
            print(items)  
            
    #
    # ab test
    #
    if event == 'ABTEST1' and not abtest_window_active:
        abtest_window_active = True
        abtest_window_layout = [
                [sg.Text('Variable alias', font=user_typeface), sg.Input(font=user_typeface, key='-ABTESTALIAS-' )],
                [sg.Text('Variable label', font=user_typeface), sg.Input(font=user_typeface, key='-ABTESTLAB-')],
                [sg.Text('Enter statement A here', font=user_typeface), sg.Input(font=user_typeface)],
                [sg.Text('Enter statement B here', font=user_typeface), sg.Input(font=user_typeface)],

                [sg.Submit('Done', key='ABTESTDONE')]
                ]
        abtest_window = sg.Window('Open-end item window', abtest_window_layout)
    if abtest_window_active:
        event, values = abtest_window.read(timeout=100)
        if event != sg.TIMEOUT_KEY:
            print('open-end item window ', event)
        if event in (None, 'Exit', 'ABTESTDONE'):
            abtest_window_active = False
            abtest_window.close()   
            
            item = {
                    "alias": values['-ABTESTALIAS-'],
                    "label": values['-ABTESTLAB-'],
                    "type": values['-ABTESTONE-']
                    }
            
            items.update({values['-ABTESTALIAS-']: item})
            print(items)
    
window.close()

