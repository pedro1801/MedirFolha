import tkinter as tk
from tkinter import filedialog as fd
import os

class Seleciona:
    def __init__(self):
        self.img = None
        def Seleciona():
            self.img = fd.askopenfilename(initialdir=os.getcwd(),title='Escolha a imagem para execucao',filetypes=(('todos os arquivos','*.*'),('jpeg','*.jpeg'),('jpg','*.jpg'),('png','*.png')))#Faz A leitura da Imagem em cinza
            janela.destroy()
            return self.img
            

        def Fechar():
            self.img = 0
            janela.destroy()
            return self.img
        janela = tk.Tk()
        altura = 40
        largura = 300
        janela.geometry(f"{largura}x{altura}")
        botao_click1 = tk.Button(janela, text="Seleciona", width=20, height=2, anchor=tk.CENTER, command=Seleciona)
        botao_click1.place(x=150, y=0)
        botao_click1 = tk.Button(janela, text="Fechar", width=20, height=2, anchor=tk.CENTER, command=Fechar)
        botao_click1.place(x=1, y=0)
        janela.mainloop()
