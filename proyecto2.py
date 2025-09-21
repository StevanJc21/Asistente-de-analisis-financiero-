import yfinance as yf
import pyautogui
import pyperclip
import webbrowser
import time

# automatizando el Ticker de cada empresa para el usuario
tiker = input("Digita el Ticker de las acciones a visualisar: ")

data = yf.Ticker(tiker).history("6mo")
cierre = data.Close

# Se hace la buena practica, lo que se puede almacenar en una variable se hace

maximo = round(cierre.max(), 2)
minimo = round(cierre.min(), 2)
promedio = round(cierre.mean(), 2) # print(maximo, minimo, promedio, sep='\n') #el sep determina como se separan las impresiones

para = "estebanjimenez@unicomfacauca.edu.co"
asunto = "Analicis de acciones ultimos 6 meses"
cuerpo = f"""
Hola Esteban espero te encuentres bien, en este correo
se te enviara el analicis de los ultimos 6 meses de 
las finansas para la empresa de {tiker}:

Cotizacion max: USD {maximo}
Cotizacion min: USD {minimo}
Cotizacion media: USD {promedio}

quedo atento a cualquier inquietud 

PD: Stig J-C

""" 
# f string para utilizar las cadenas de texto con forma mas dinamica insertando calculos y bariables 
# f "xxxxxxxxxx {y lo que va}" se le dice formateo de texto

webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

time.sleep(3)

pyautogui.PAUSE = 2 # es una pausa entre comandos que puedan requerir un tiempo de carga}

# se utiliza ahora pytogui para indicar el click

pyautogui.click(117, 297)   
time.sleep(2)
# como habia dicho antes, la biblioteca ayuda a copiar informacion y tenerla en el  # porta papeles para despues utilizarla 
pyperclip.copy(para) 
# aqui utilizamos los comandos de copiar y pegar
pyautogui.hotkey("ctrl", "v") 
pyautogui.hotkey("tab")

pyperclip.copy(asunto)
pyautogui.hotkey("ctrl", "v")

pyautogui.hotkey("tab")

pyperclip.copy(cuerpo)
pyautogui.hotkey("ctrl", "v")

pyautogui.click(1105, 969)
pyautogui.hotkey("ctrl", "f4")