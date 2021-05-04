from tkinter import *
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class main:
    def __init__(self, master):
        
        self.master=master;
        master.title('Frecuencias');
        master.geometry('450x400');
        self.titleAbs = Label();
        self.titleAbs.place(y = 30);
        self.titleAbs.pack(anchor = CENTER);
        self.titleAbs.config(text = "Elija la frecuencia:", bg= '#243137', fg = "#A8E2FC", font = ("Arial", 20));
        self.absBtn = Button(master, text = "Grafica tipo barras \n (Frecuencia absoluta)", command = self.winFAbsoluta);
        self.absBtn.place(x=95, y = 100, width = 250, height = 100);
        self.absBtn.config(bg= '#2F4149', fg = '#A8E2FC', font = ("Century Gothic", 14));
        self.relBtn = Button(master, text = "Grafica tipo pastel \n (Frecuencia absoluta)", command = self.winFRelativa);
        self.relBtn.place(x = 95, y = 225, width = 250, height = 100);
        self.relBtn.config(bg= '#2F4149', fg = '#A8E2FC', font = ("Century Gothic", 14));

    def winFAbsoluta(self):
        
        new_1= Toplevel(root);
        new_1.geometry('300x540');
        new_1.config(bg = '#243137');
        self.titleRel = Label(new_1);
        self.titleRel.pack(anchor = CENTER);
        self.titleRel.config(text = "Elija la frecuencia \n absoluta:", bg= '#243137', fg = '#A8E2FC', font = ("Arial", 20));
        self.abs_colorBtn = Button(new_1, text="Color", command = self.FAColor);
        self.abs_colorBtn.place(x = 90, y = 100, width = 120, height = 80);
        self.abs_colorBtn.config(bg= '#2F4149', fg = '#A8E2FC', font = ("Century Gothic", 14));
        self.abs_velocidadBtn = Button(new_1, text="Velocidad", command = self.FAVelocidad);
        self.abs_velocidadBtn.place(x = 90, y = 200, width = 120, height = 80);
        self.abs_velocidadBtn.config(bg= '#2F4149', fg = '#A8E2FC', font = ("Century Gothic", 14));
        self.abs_pesoBtn = Button(new_1, text="Peso", command = self.FAPeso);
        self.abs_pesoBtn.place(x = 90, y = 300, width = 120, height = 80);
        self.abs_pesoBtn.config(bg= '#2F4149', fg = '#A8E2FC', font = ("Century Gothic", 14));
        self.abs_alturaBtn = Button(new_1, text="Altura", command = self.FAAltura);
        self.abs_alturaBtn.place(x = 90, y = 400, width = 120, height = 80);
        self.abs_alturaBtn.config(bg= '#2F4149', fg = '#A8E2FC', font = ("Century Gothic", 14));
        
    def FAColor(self):
        
        datos = pd.read_csv('datos.csv');
        dF = pd.DataFrame(datos);
        
        colores=dF['color'];
        
        ColorB = 0;
        ColorA = 0;
        ColorV = 0;
        ColorNA = 0;
        
        cntColores = [];
        colorStr = ['Blanco', 'Amarillo', "Verde", "NA"];

        for x in colores:
            if(x == 'Blanco'):
                ColorB += 1;
            elif(x == "Amarillo"):
                ColorA += 1;
            elif(x == "Verde"):
                ColorV += 1;
            elif(x == 'NA'):
                ColorNA += 1;

        cntColores.append(ColorB);
        cntColores.append(ColorA);
        cntColores.append(ColorV);
        cntColores.append(ColorNA);
        
        fig, ax = plt.subplots();
        ax.set_ylabel('Freq. Absoluta');
        ax.set_title('Colores');
        plt.bar(colorStr, cntColores);
        plt.savefig('F_Absoluta_Color.png');
        plt.show();
        
    def FAVelocidad(self):
        
        datos = pd.read_csv('datos.csv');
        dF = pd.DataFrame(datos);
        
    def FAPeso(self):
        
        datos = pd.read_csv('datos.csv');
        dF = pd.DataFrame(datos);
        
    def FAAltura(self):
        
        datos = pd.read_csv('datos.csv');
        dF = pd.DataFrame(datos);
        
    def winFRelativa(self):
        
        new_2= Toplevel(root);
        new_2.geometry('300x540');
        new_2.config(bg = '#243137');
        
        self.titleRel = Label(new_2);
        self.titleRel.pack(anchor = CENTER);
        self.titleRel.config(text = "Elija la frecuencia \n relativa:", bg= '#243137', fg = '#A8E2FC', font = ("Arial", 20));
        self.rel_colorBtn = Button(new_2, text="Color", command = self.FRColor);
        self.rel_colorBtn.place(x = 90, y = 100, width = 120, height = 80);
        self.rel_colorBtn.config(bg= '#2F4149', fg = '#A8E2FC', font = ("Century Gothic", 14));
        self.rel_velocidadBtn = Button(new_2, text="Velocidad", command = self.FRVelocidad),
        self.rel_velocidadBtn.place(x = 90, y = 200, width = 120, height = 80);
        self.rel_velocidadBtn.config(bg= '#2F4149', fg = '#A8E2FC', font = ("Century Gothic", 14));
        self.rel_pesoBtn = Button(new_2, text="Peso", command = self.FRPeso);
        self.rel_pesoBtn.place(x = 90, y = 300, width = 120, height = 80);
        self.rel_pesoBtn.config(bg= '#2F4149', fg = '#A8E2FC', font = ("Century Gothic", 14));
        self.rel_alturaBtn = Button(new_2, text="Altura", command = self.FRAltura);
        self.rel_alturaBtn.place(x = 90, y = 400, width = 120, height = 80);
        self.rel_alturaBtn.config(bg= '#2F4149', fg = '#A8E2FC', font = ("Century Gothic", 14));
        
    def FRColor(self):
        
        datos = pd.read_csv('datos.csv');
        dF = pd.DataFrame(datos);
        
        
    def FRVelocidad(self):
        
        datos = pd.read_csv('datos.csv');
        dF = pd.DataFrame(datos);
        
    def FRPeso(self):
        
        datos = pd.read_csv('datos.csv');
        dF = pd.DataFrame(datos);
        
    def FRAltura(self):
        
        datos = pd.read_csv('datos.csv');
        dF = pd.DataFrame(datos);

root = Tk();
root.resizable(0, 0);
root.config(bg = '#243137');
miVentana = main(root);
root.mainloop();