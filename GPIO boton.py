import tkinter
import qrcode
import RPi.GPIO as GPIO
from tkinter import*

def apagar():
    print("Apagar")
    GPIO.output(2,GPIO.LOW)
    etiqueta.set("Apagado")
    
def encender():
    print("Encender")
    GPIO.output(2,GPIO.HIGH)
    etiqueta.set("Encendido")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.output(2,GPIO.LOW)

w=tkinter.Tk()
w.geometry("500x400")
w.title("INTERFAZ DE POTENCIA")
imagen=PhotoImage(file="imagen1")
fondo=Label(w,image=imagen).place(x=0,y=0)

etiqueta=tkinter.StringVar()
etiqueta.set("Apagado")
b1=tkinter.Button(w,text="Apagar",command=apagar).place(x=160,y=10)
b2=tkinter.Button(w,text="Encender",command=encender).place(x=300,y=10)
b3=tkinter.Button(w,text="Temperatura 1",command=encender).place(x=200,y=50)
b4=tkinter.Button(w,text="Temperatura 2",command=encender).place(x=200,y=90)
b5=tkinter.Button(w,text="Temperatura 3",command=encender).place(x=200,y=130)
lb=tkinter.Label(w,textvariable=etiqueta).place(x=225,y=190)


w.mainloop()