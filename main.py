from cgitb import text
from tkinter import *
from tkinter import ttk
from turtle import width

# Importando tkcalendar
from tkcalendar import Calendar, DateEntry

# Importando dateutil
from dateutil.relativedelta import relativedelta

# Importando datetime
from datetime import date

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

# Criar função calcular idade

def calcular():
    inicial = cal_1.get()
    data_nascimento = cal_2.get()

    # Separando valores inicial
    mes_1, dia_1, ano_1 = [int(f) for f in inicial.split('/')]
    
    #convertendo valor em formato date
    data_inicial = date(ano_1, mes_1, dia_1)
    print(data_inicial)


 # Separando valores data_nascimento
    mes_2, dia_2, ano_2 = [int(f) for f in data_nascimento.split('/')]
    
    #convertendo valor em formato date
    data_nascimento = date(ano_2, mes_2, dia_2)
    
    anos = relativedelta(data_inicial, data_nascimento). years # diminui data inicial de data de nascimento
    print(anos)

# Criando label para frames cima


l_calculadora = Label(frame_cima, text= 'CALCULADORA', width=20, height=1, padx=5, relief=FLAT, anchor='center',font=('Ivi 15 bold'), bg=cor2, fg= cor3)
l_calculadora.place(x=0, y=30 )


l_idade = Label(frame_cima, text= 'DE IDADE', width=11, height=1, padx=0, relief='flat',anchor='center',font=('Arial 35 bold'), bg=cor2, fg= cor4)
l_idade.place(x=0, y=60)

# Criando label para frames baixo

l_data_inicial= Label(frame_baixo, text= 'Data inicial', height=1, padx=0, pady=0, relief=FLAT, anchor=NW,font=('Ivi 11'), bg=cor1, fg= cor3) # Texto, altura, estilo flat, posição Norte Oeste, font, cor
l_data_inicial.place(x=20, y=25 )
cal_1 = DateEntry(frame_baixo, width= 13, bg='darkblue', fg= cor3, borderwidth=2, date_pattern ='mm/dd/y', y = 2021) # Largura, sombreamento, cor. borda da linha, formato de data e data inicial
cal_1.place (x = 170, y = 30)

l_data_nascimento= Label(frame_baixo, text= 'Data de nascimento', height=1, padx=0, pady=0, relief=FLAT, anchor=NW,font=('Ivi 11'), bg=cor1, fg= cor3)
l_data_nascimento.place(x=20, y=50 )
cal_2 = DateEntry(frame_baixo, width= 13, bg = 'darkblue', fg= cor3, borderwidth=2, data_pattern = 'mm/dd/y', y = 2021) # Largura, sombreamento, cor, borda de linha, formato de data e data inicial 
cal_2.place(x = 170, y=50)



# Criando label anos frame baixo

l_app_anos = Label(frame_baixo, text= '27', height=1, padx=0, pady=0, relief=FLAT, anchor='center',font=('Ivi 25 bold'), bg=cor1, fg= cor3) # Texto, altura, estilo flat, posição Norte Oeste, font, cor
l_app_anos.place(x=30, y=125 )
l_app_anos_nome = Label(frame_baixo, text= 'Anos', height=1, padx=0, pady=0, relief=FLAT, anchor='center',font=('Ivi 11 bold'), bg=cor1, fg= cor3) # Texto, altura, estilo flat, posição Norte Oeste, font, cor
l_app_anos_nome.place(x=30, y=175 )

# Criando label meses frame baixo

l_app_meses = Label(frame_baixo, text= '12', height=1, padx=0, pady=0, relief=FLAT, anchor='center',font=('Ivi 25 bold'), bg=cor1, fg= cor3) # Texto, altura, estilo flat, posição Norte Oeste, font, cor
l_app_meses.place(x=115, y=125 )
l_app_meses_nome = Label(frame_baixo, text= 'Meses', height=1, padx=0, pady=0, relief=FLAT, anchor='center',font=('Ivi 11 bold'), bg=cor1, fg= cor3) # Texto, altura, estilo flat, posição Norte Oeste, font, cor
l_app_meses_nome.place(x=115, y=175 )



# Criando label dias frame baixo

l_app_dias = Label(frame_baixo, text= '120', height=1, padx=0, pady=0, relief=FLAT, anchor='center',font=('Ivi 25 bold'), bg=cor1, fg= cor3) # Texto, altura, estilo flat, posição Norte Oeste, font, cor
l_app_dias.place(x=200, y=125 )
l_app_dias_nome = Label(frame_baixo, text= 'Dias', height=1, padx=0, pady=0, relief=FLAT, anchor='center',font=('Ivi 11 bold'), bg=cor1, fg= cor3) # Texto, altura, estilo flat, posição Norte Oeste, font, cor
l_app_dias_nome.place(x=200, y=175 )


# Criando botão calcular

b_calculcar = Button(frame_baixo,command= calcular, text= 'Calcular',width= 15, height=1, padx=0, pady=0, relief='raised',overrelief= 'ridge' ,font=('Ivi 15 bold'), bg=cor1, fg= cor3) # Comando calcular, tamanho, texto, altura, estilo flat, posição Norte Oeste, font, cor
b_calculcar.place(x=40, y=220 )


janela.mainloop()