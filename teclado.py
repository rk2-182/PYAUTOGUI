import pyautogui
import time

#https://www.youtube.com/watch?v=N2-v0scoTVo&list=PLrMKroDxWn7JEtvM8Kvem46_u1vlBSHxY&index=3&t

pyautogui.hotkey("win","r")
#pyautogui.press("enter")
posicion=pyautogui.locateCenterOnScreen('img/abrir.png',confidence=.8)
pyautogui.moveTo(posicion, duration=3)
pyautogui.moveRel(80,0,duration=.3)
pyautogui.click(clicks=1,interval=.1)
pyautogui.press("backspace")
pyautogui.write("calc")
pyautogui.press("enter")