from tkinter import *
import math

def contagem(contador):
    contagem_min = math.floor(contador / 60)
    contagem_seg = contador % 60
    
    if contagem_seg < 10:
        contagem_seg = f"0{contagem_seg}"
    tela.itemconfig(timer_texto, text=f'{contagem_min}:{contagem_seg}')
    
    if contador > 0:
        global timer
        timer = janela.after(1000, contagem, contador - 1)
    else:
        iniciar_timer()
        marcacao = ''
        sessoes_trabalho = math.floor(repticoes/2)
        for _ in range(sessoes_trabalho):
            marcacao += '✓'
        marca_visto.config(text=marcacao)

def iniciar_timer():
    global repticoes
    repticoes += 1
    min_trabalho = minutos_trabalho * 60
    pausa_pequena_seg = pausa_pequena * 60
    pausa_longa_seg = pausa_longa * 60
    
    if repticoes % 8 == 0:
        contagem(pausa_longa_seg)
    
        label_titulo.config(text='Pausa', fg=vermelho)
    elif repticoes % 2 == 0:
        contagem(pausa_pequena_seg)
        
        label_titulo.config(text='Pausa', fg=rosa)
    else:
        contagem(min_trabalho)
        label_titulo.config(text='Trabalhe', fg=verde)

def reiniciar_timer():
    janela.after_cancel(timer)
    tela.itemconfig(timer_texto, text='00:00')
    
    label_titulo.config(text='Timer')
    marca_visto.config(text='')
    global repticoes
    repticoes = 0   

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
timer_texto = tela.create_text(100, 130, text='00:00', fill='white', font=(fonte, 35, 'bold'))
tela.grid(column=1, row=1)

# Botoes ----------------------------------------
botao_iniciar = Button(text='Iniciar', highlightthickness=0, command=iniciar_timer)
botao_iniciar.grid(column=0, row=2)
botao_reiniciar = Button(text='Reiniciar', highlightthickness=0, command=reiniciar_timer)
botao_reiniciar.grid(column=2, row=2)
marca_visto = Label(text='✓', fg=verde, bg=amarelo)
marca_visto.grid(column=1, row=3)


janela.mainloop()