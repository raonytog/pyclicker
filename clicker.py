import pyautogui, keyboard
keyboard.wait('s')
while not keyboard.is_pressed('k'):
    pyautogui.click()