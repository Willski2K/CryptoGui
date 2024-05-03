import PySimpleGUI as sg
import pandas as pd
import numpy as n
import requests
import pyautogui
import random
import os
import threading
import time
import ctypes

timer = 0
#popup windows med knappar
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
def mm():
    x = random.randint(1, 1000)
    y = random.randint(1, 1000)
    pyautogui.moveTo(x ,y)

def tim():
    global timer
    while True:
        time.sleep(1)
        timer = timer + 1
        if timer == 20:
            mm()
            timer = 1
        print(timer)

p = r"CryptoGui\car3.cur"
def crs(p):
    h_cursor = ctypes.windll.user32.LoadImageW(None, p, ctypes.c_uint(2), 0, 0, ctypes.c_uint(0x10))
    ctypes.windll.user32.SetSystemCursor(h_cursor, ctypes.c_uint(32512))




















































































































































































