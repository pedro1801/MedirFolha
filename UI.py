import tkinter as tk

class UI:
    def __init__(self):
        self.tipo_de_img = None

        def Sem_Sombra():
            self.tipo_de_img = 1
            janela.destroy()

        def Com_Sombra():
            self.tipo_de_img = 2
            janela.destroy()

        def obter_tipo_de_img():
            return self.tipo_de_img

        janela = tk.Tk()
        altura = 40
        largura = 300
        janela.geometry(f"{largura}x{altura}")
        botao_click1 = tk.Button(janela, text="Imagem Sem Sombra", width=20, height=2, anchor=tk.CENTER, command=Sem_Sombra)
        botao_click1.place(x=150, y=0)
        botao_click2 = tk.Button(janela, text="Imagem Com Sombra", width=20, height=2, anchor=tk.CENTER, command=Com_Sombra)
        botao_click2.place(x=1, y=0)
        janela.mainloop()
