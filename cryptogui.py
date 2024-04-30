import PySimpleGUI as sg
import pandas as pd
import numpy as n
import requests
import os
import guifunctions

df = pd.read_csv('CryptoGui/coin_gecko_2022-03-17.csv')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

sg.theme("NeonBlue1")
default_font = 'Bold'

layout = [
    [sg.Text("CryptoPriceGui")],
    [sg.Button("Randomize"), sg.Button("SortName"), sg.Button("SortPrice"), sg.Button("Refresh Price", pad=((0, 530), (0, 0))), sg.Button("EasterEggs")],
    [sg.InputText("Search"), sg.Button('Search1')],
    [sg.Table(values=df.values.tolist(), headings=df.columns.tolist(), display_row_numbers=False, auto_size_columns=False, col_widths=[20, 10], vertical_scroll_only=True, key='-TABLE-')]
]
window = sg.Window("CryptoGUI", layout)

sorted_by_name = False
sorted_by_price = False
counter = 0


while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        df.to_csv('CryptoGui/coin_gecko_2022-03-17.csv', index=False)
        break
    if event == "SortName":
        counter = counter + 1
        if sorted_by_name:
            df = df.sort_values(by="coin", ascending=False)
            sorted_by_name = False
            if counter >= 10:
                crazypop()
                counter = 0
        else:
            df = df.sort_values(by="coin")
            sorted_by_name = True
        window['-TABLE-'].update(values=df.values.tolist())
    if event == "SortPrice":
        if counter > 1:
                counter = 0
        if sorted_by_price:
            df = df.sort_values(by="price", ascending=False)
            sorted_by_price = False
        else:
            df = df.sort_values(by="price")
            sorted_by_price = True
        window['-TABLE-'].update(values=df.values.tolist())
    if event == "Randomize":
        df = df.sample(frac=1).reset_index(drop=True)
        window['-TABLE-'].update(values=df.values.tolist())
        if counter > 1:
                counter = 0
    if event == "EasterEggs":
        est()
        if counter > 1:
                counter = 0
    if event == "Search1":
        search_text = values[0].lower()
        if "egg" in search_text:
            egg()
        else:
            print("wip")
        if counter > 1:
            counter = 0
