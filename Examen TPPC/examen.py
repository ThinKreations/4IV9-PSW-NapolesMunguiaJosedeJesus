from tkinter import *
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class main:
    def __init__(self, master):
        
        self.master=master
        
        
        master.title('Frecuencias')
        master.geometry('500x540')
        
        self.titleAbs = Label()
        self.titleAbs.place(y = 30)
        self.titleAbs.pack(anchor = CENTER)
        self.titleAbs.config(text = "Elija la frecuencia:", bg= '#243137', fg = "#A8E2FC", font = ("Arial", 18))
        
        self.absBtn = Button(master, text = "Grafica tipo barras \n (Frecuencia absoluta)", command = self.winFAbsoluta)
        self.absBtn.place(x=120, y = 100, width = 250, height = 100)
        self.absBtn.config(bg= '#2F4149', fg = '#A8E2FC', font = ("Arial", 15))
    
        self.relBtn = Button(master, text = "Grafica tipo pastel \n (Frecuencia absoluta)", command = self.winFAbsoluta)
        self.relBtn.place(x = 120, y = 225, width = 250, height = 100)
        self.relBtn.config(bg= '#2F4149', fg = '#A8E2FC', font = ("Arial", 15))
        
        self.mmmBtn = Button(master, text = "Moda \n Media \n Mediana", command = self.winFAbsoluta)
        self.mmmBtn.place(x = 120, y = 350, width = 250, height = 100)
        self.mmmBtn.config(bg= '#2F4149', fg = '#A8E2FC', font = ("Arial", 15))
    
    def winFAbsoluta(self):
        
        new_= Toplevel(root)
        new_.geometry('500x540')
        new_.config(bg = '#243137')
                
root = Tk()
root.resizable(False, False)
root.config(bg = '#243137')
miVentana = main(root)
root.mainloop()