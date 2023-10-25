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

# Configurando Fundo -------------------------
tela = Canvas(width=200, height=224, bg=amarelo, highlightthickness=0)
tomate = PhotoImage(file='tomate.png')
tela.create_image(100, 112, image=tomate)
timer_text = tela.create_text(100, 130, text='00:00', fill='white', font=(fonte, 35, 'bold'))
tela.grid(column=1, row=1)

# Botoes ----------------------------------------
botao_iniciar = Button(text='Iniciar', highlightthickness=0, command=iniciar_timer)
botao_iniciar.grid(column=0, row=2)
botao_reiniciar = Button(text='Reiniciar', highlightthickness=0, command=reiniciar_timer)
botao_reiniciar.grid(column=2, row=2)

janela.mainloop()