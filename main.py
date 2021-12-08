from cgitb import text
from tkinter import *
from tkinter import ttk
from turtle import width

# Importando tkcalendar
from tkcalendar import Calendar, DateEntry

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
l_idade.place(x=0, y=60)

# Criando label para frames baixo

l_data_inicial= Label(frame_baixo, text= 'Data inicial', height=1, padx=0, pady=0, relief=FLAT, anchor=NW,font=('Ivi 11'), bg=cor1, fg= cor3) # Texto, altura, estilo flat, posição Norte Oeste, font, cor
l_data_inicial.place(x=20, y=25 )
cal_1 = DateEntry(frame_baixo, width= 13, bg='darkblue', fg= cor3, borderwidth=2, date_patter ='mm/dd/y', y = 2021) # Largura, sombreamento, cor. borda da linha, formato de data e data inicial
cal_1.place (x = 170, y = 30)

l_data_nascimento= Label(frame_baixo, text= 'Data de nascimento', height=1, padx=0, pady=0, relief=FLAT, anchor=NW,font=('Ivi 11'), bg=cor1, fg= cor3)
l_data_nascimento.place(x=20, y=50 )
cal_2 = DateEntry(frame_baixo, width= 13, bg = 'darkblue', fg= cor3, borderwidth=2, data_patter = 'mm/dd/y', y = 2021) # Largura, sombreamento, cor, borda de linha, formato de data e data inicial 
cal_2.place(x = 170, y=50)


janela.mainloop()