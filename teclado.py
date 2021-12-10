import pyautogui
import time

pyautogui.hotkey("win","r")
#pyautogui.press("enter")
posicion=pyautogui.locateCenterOnScreen('img/abrir.png',confidence=.8)
pyautogui.moveTo(posicion, duration=3)
pyautogui.moveRel(80,0,duration=.3)
pyautogui.click(clicks=2,interval=.1)