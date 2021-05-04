from tkinter import *
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class main:
    def __init__(self, master):
        self.master=master
        
        
        master.title('Frecuencias')
        master.geometry('1020x630')
        
root = Tk()
root.resizable(False, False)
root.config(bg = '#FFB7B7')
miVentana = main(root)
root.mainloop()