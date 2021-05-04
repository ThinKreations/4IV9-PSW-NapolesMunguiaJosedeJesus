from tkinter import *
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class main:
    def __init__(self, master):
        
        self.master=master
        
        
        master.title('Frecuencias')
        master.geometry('450x520')
        
        self.titleAbs = Label()
        self.titleAbs.place(y = 30)
        self.titleAbs.pack(anchor = CENTER)
        self.titleAbs.config(text = "Elija la frecuencia:", bg= '#243137', fg = "#A8E2FC", font = ("Arial", 20))
        
        self.absBtn = Button(master, text = "Grafica tipo barras \n (Frecuencia absoluta)", command = self.winFAbsoluta)
        self.absBtn.place(x=95, y = 100, width = 250, height = 100)
        self.absBtn.config(bg= '#2F4149', fg = '#A8E2FC', font = ("Century Gothic", 14))
    
        self.relBtn = Button(master, text = "Grafica tipo pastel \n (Frecuencia absoluta)", command = self.winFRelativa)
        self.relBtn.place(x = 95, y = 225, width = 250, height = 100)
        self.relBtn.config(bg= '#2F4149', fg = '#A8E2FC', font = ("Century Gothic", 14))
        
        self.mmmBtn = Button(master, text = "Moda \n Media \n Mediana", command = self.winMMM)
        self.mmmBtn.place(x = 95, y = 350, width = 250, height = 100)
        self.mmmBtn.config(bg= '#2F4149', fg = '#A8E2FC', font = ("Century Gothic", 14))
    
    def winFAbsoluta(self):
        
        new_win1= Toplevel(root)
        new_win1.geometry('300x540')
        new_win1.config(bg = '#243137')
        
        self.titleRel = Label(new_win1)
        self.titleRel.pack(anchor = CENTER)
        self.titleRel.config(text = "Elija la frecuencia \n absoluta:", bg= '#243137', fg = '#A8E2FC', font = ("Arial", 20))
        
        self.abs_colorBtn = Button(new_win1, text = "Color", command = self.FAColor)
        self.abs_colorBtn.place(x = 90, y = 100, width = 120, height = 80)
        self.abs_colorBtn.config(bg= '#2F4149', fg = '#A8E2FC', font = ("Century Gothic", 14))
        
        self.abs_velocidadBtn = Button(new_win1, text = "Velocidad", command = self.FAVelocidad)
        self.abs_velocidadBtn.place(x = 90, y = 200, width = 120, height = 80)
        self.abs_velocidadBtn.config(bg= '#2F4149', fg = '#A8E2FC', font = ("Century Gothic", 14))
        
        self.abs_PesoBtn = Button(new_win1, text = "Peso", command = self.FAVelocidad)
        self.abs_PesoBtn.place(x = 90, y = 200, width = 120, height = 80)
        self.abs_PesoBtn.config(bg= '#2F4149', fg = '#A8E2FC', font = ("Century Gothic", 14))
        
    def FAColor(self):
        
        datos = pd.read_csv('datos.csv')
        dF = pd.DataFrame(datos)
        
    def FAVelocidad(self):
        
        datos = pd.read_csv('datos.csv')
        dF = pd.DataFrame(datos)
        
        
    def winFRelativa(self):
            
        a
        
    def winMMM(self):
            
        a
        
root = Tk()
root.resizable(False, False)
root.config(bg = '#243137')
miVentana = main(root)
root.mainloop()