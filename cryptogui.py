import PySimpleGUI as sg
import pandas as pd
import numpy as np

def est():
    layout = [[sg.Text('Det finns 3 easter eggs på detta programmet och kanske till och med något mer ;) , Försök hitta dem utan att kolla koden')], [sg.Button('OK')]]
    window = sg.Window('Popup', layout, keep_on_top=True)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Jag lovar att hitta dem':
            break
    
    window.close()

df = pd.read_csv('CryptoGui/coin_gecko_2022-03-17.csv')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

sg.theme("LightBrown5")
default_font = 'Bold'

layout = [
    [sg.Text("CryptoPriceGui")],
    [sg.Button("Randomize"), sg.Button("SortName"), sg.Button("SortPrice"), sg.Button("Refresh Price"), sg.Button("EasterEggs")],
    [sg.InputText("Search*")],
    [sg.Table(values=df.values.tolist(), headings=df.columns.tolist(), display_row_numbers=False, auto_size_columns=False, col_widths=[20, 10], vertical_scroll_only=True, key='-TABLE-')]
]
window = sg.Window("CryptoGUI", layout)

sorted_by_name = False
sorted_by_price = False

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        df.to_csv('CryptoGui/coin_gecko_2022-03-17.csv', index=False)
        break
    if event == "SortName":
        if sorted_by_name:
            df = df.sort_values(by="coin", ascending=False)
            sorted_by_name = False
        else:
            df = df.sort_values(by="coin")
            sorted_by_name = True
        window['-TABLE-'].update(values=df.values.tolist())
    if event == "SortPrice":
        if sorted_by_price:
            df = df.sort_values(by="price", ascending=False)
            sorted_by_price = False
        else:
            df = df.sort_values(by="price")
            sorted_by_price = True
        window['-TABLE-'].update(values=df.values.tolist())
    if event == "Randomize":
        np.random.shuffle(df.values)
        window['-TABLE-'].update(values=df.values.tolist())
    if event == "EasterEggs":
        est()
