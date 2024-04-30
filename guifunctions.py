def egg():
    layout = [[sg.Text("Yep egg in the search bar, who would have thought")],
              [sg.Button('Get me out')]]
    window = sg.Window('Egg?', layout, keep_on_top=True)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Get me out':
            break
    window.close()


def crazypop():
    layout = [[sg.Text("Did i ever tell you? The defenition of insanity?")],
              [sg.Button('sorry im insane')]]
    window = sg.Window('wow', layout, keep_on_top=True)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'sorry im insane':
            break
    window.close()


def est():
    layout = [[sg.Text('There are 3 easter eggs, have you found them?')], [sg.Button('i promise i will find them')]]
    window = sg.Window('Popup', layout, keep_on_top=True)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'i promise i will find them':
            break
    window.close()
















































































































































































