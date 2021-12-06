from tkinter import *
from tkinter import ttk

#Criar janela
janela = Tk()
janela.title('Calculadora de idade')
janela.geometry('310x400')

# cores
cor1= '#3b3b3b'
cor2= '#333333'


# criando frames
frame_cima = Frame(janela, width=310, height=140, pady=0, padx=0, relief=FLAT, bg=cor2) #Largura, altura, estilo Flat, cor 
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=300, pady=0, padx=0, relief=FLAT, bg=cor1) #Largura, altura, estilo Flat, cor 
frame_baixo.grid(row=1, column=0)

janela.mainloop()