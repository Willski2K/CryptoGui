import PySimpleGUI as sg
import matplotlib.pyplot as plt
import pandas as pd
import os

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df = pd.read_csv('CryptoGui/coin_gecko_2022-03-17.csv')
price = df["price"]
coin = df["coin"]
sorted_df = df.sort_values(by='coin')

sorted_df.to_csv('CryptoGui/sorted_coin_gecko.csv', index=False)

sg.theme("LightBrown5")
defualt_font = 'Bold'

regulardf = [
    [sg.Text(coin), sg.Text(price),],
]


layout = [[sg.Text("CryptoPriceGui")],
            [sg.Button("Randomize"), sg.Button("SortName"), sg.Button("SortPrice"), sg.Button("Refreash price")],
            [sg.InputText("Filter1"), sg.InputText("Filter2")],
            [sg.Text("Name"), sg.Text("Price")],
            [sg.Column(regulardf, scrollable=True,  vertical_scroll_only=True, size = (700, 300), key='-COLUMN-')]
            
                                        
                                        
                                        ]
window = sg.Window("CryptoGUI", layout)


print(df)


while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    if event == "SortName":
        df = pd.read_csv('CryptoGui/sorted_coin_gecko.csv')
        window['-COLUMN-'].update(df)
        regulardf = [
    [sg.Text(coin), sg.Text(price),],
]
        elem = window['-COLUMN-']
        elem.update
        window.refresh()
window.close()