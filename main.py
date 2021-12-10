import pyautogui
import time
import os

def conocer_resolucion():
    resolucion = pyautogui.size()

    return resolucion


def conocer_posicion():
    fin = 0
    print("========Conocer posicion=========")
    while True:
        #Ver posicion actual la cual sera impresa por consola
        #Donde x = izquierda(-) y derecha (+)

        print(pyautogui.position())
        
        fin +=1
        time.sleep(2)
        
        if fin > 10:
            print("fin")
            break

def mostrarPosicion_mouse():
    #Conocer posicion del puntero y mostrar el RGB de su ubicacion
    print(pyautogui.displayMousePosition())






#***********************************************************************************
os.system('cls')
print("Especiciaciones monitor: {0}".format(conocer_resolucion()))

print("")
conocer_posicion()

mostrarPosicion_mouse()
