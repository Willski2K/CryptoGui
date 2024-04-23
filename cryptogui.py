import PySimpleGUI as sg
import matplotlib.pyplot as plt
import pandas as pd
import os
df = pd.read_csv('CryptoGui/coin_gecko_2022-03-17.csv')
price = df["price"]
coin = df["coin"]

sg.theme("LightBrown5")
defualt_font = 'Bold'

column1 = [
    [sg.Text(coin), sg.Text(price)],
]


layout = [[sg.Text("CryptoPriceGui")],
            [sg.Button("Randomize"), sg.Button("SortName"), sg.Button("SortPrice"), sg.Button("Refreash price")],
            [sg.InputText("Filter1"), sg.InputText("Filter2")],
            [sg.Text("Name"), sg.Text("Price")],
            [sg.Column(column1, scrollable=True,  vertical_scroll_only=True,)]
            
                                        
                                        
                                        ]
window = sg.Window("CryptoGUI", layout)




while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

window.close()