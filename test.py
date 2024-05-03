import ctypes
image_path = r"CryptoGui\car2.cur"
def set_custom_cursor(image_path):
    h_cursor = ctypes.windll.user32.LoadImageW(None, image_path, ctypes.c_uint(2), 0, 0, ctypes.c_uint(0x10))
    ctypes.windll.user32.SetSystemCursor(h_cursor, ctypes.c_uint(32512))

set_custom_cursor(image_path)
