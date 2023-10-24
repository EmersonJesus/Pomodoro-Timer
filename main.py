from tkinter import *
import math

# Variaveis ------------------------------
rosa = '#e2979c'
vermelho = '#e7305b'
verde = '#9bdeac'
amarelo = '#f7f5dd'
fonte = 'Courier'
minutos_trabalho = 25
pausa_pequena = 5
pausa_longa = 20
repticoes = 0
timer = None

# Configurando Janela ---------------------
janela = Tk()
janela.title('Pomodoro')
janela.config(padx=100, pady=50, bg=amarelo)
label_titulo = Label(text='TIMER', fg=verde, bg=amarelo, font=(fonte, 50))
label_titulo.grid(column=1, row=0)


janela.mainloop()