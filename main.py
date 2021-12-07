from cgitb import text
from tkinter import *
from tkinter import ttk

#Criar janela
janela = Tk()
janela.title('Calculadora de idade')
janela.geometry('300x400')

# cores
cor1= '#3b3b3b'  # preta/leve/black
cor2= '#333333'  # preta/pesada/black
cor3 = '#ffffff' # branca/ white 
cor4 = '#ff4500'  # laranja/ orange

# criando frames
frame_cima = Frame(janela, width=300, height=140, pady=0, padx=0, relief=FLAT, bg=cor2) #Largura, altura, estilo Flat, cor 
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=300, height=300, pady=0, padx=0, relief=FLAT, bg=cor1) #Largura, altura, estilo Flat, cor 
frame_baixo.grid(row=1, column=0)

# Criando label para frames cima

l_calculadora = Label(frame_cima, text= 'CALCULADORA', width=20, height=1, padx=5, relief=FLAT, anchor='center',font=('Ivi 15 bold'), bg=cor2, fg= cor3)
l_calculadora.place(x=0, y=30 )


l_idade = Label(frame_cima, text= 'DE IDADE', width=11, height=1, padx=0, relief='flat',anchor='center',font=('Arial 35 bold'), bg=cor2, fg= cor4)
l_idade.place(x=0, y=70 )




janela.mainloop()