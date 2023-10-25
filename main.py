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
    min_trabalho = int(minutos_trabalho * 60)
    pausa_pequena_seg = int(pausa_pequena * 60)
    pausa_longa_seg = int(pausa_longa * 60)
    
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

def salvar_config():
    global minutos_trabalho, pausa_pequena, pausa_longa, config
    try:
        minutos_trabalho = float(minutos_trabalho_entry.get())
        pausa_pequena = float(pausa_pequena_entry.get())
        pausa_longa = float(pausa_longa_entry.get())
        config.destroy()  # Fecha a janela de configurações após salvar as configurações
    except:
        erro = Tk()
        erro.title('Erro de entrada')
        erro.config(padx=100, pady=50, bg=amarelo)
        mensagem = Label(erro, text="Digite apenas numeros", bg=amarelo, fg=vermelho)
        mensagem.pack()
        erro.mainloop()
        return False

def abrir_config():
    global minutos_trabalho_entry, pausa_pequena_entry, pausa_longa_entry, config
    # Janela de Configurações --------------------------
    config = Tk()
    config.title('Configurações')
    config.config(padx=100, pady=50, bg=amarelo)
    
    # Labels --------------------------------------------
    label_min_trabalho = Label(config, text='Minutos de trabalho', fg=vermelho, bg=amarelo)
    label_min_trabalho.grid(column=0, row=0)
    minutos_trabalho_entry = Entry(config, width=5)
    minutos_trabalho_entry.grid(column=1, row=0)
    
    label_pausa_pequena = Label(config, text='Minutos da pausa pequena', fg=vermelho, bg=amarelo)
    label_pausa_pequena.grid(column=0, row=1)
    pausa_pequena_entry = Entry(config, width=5)
    pausa_pequena_entry.grid(column=1, row=1)
    
    label_pausa_longa = Label(config, text='Minutos da pausa longa', fg=vermelho, bg=amarelo)
    label_pausa_longa.grid(column=0, row=2)
    pausa_longa_entry = Entry(config, width=5)
    pausa_longa_entry.grid(column=1, row=2)
    
    # Botão salvar -----------------------------------------
    salvar = Button(config, text='Salvar', highlightthickness=0, command=salvar_config)
    salvar.grid(column=1, row=5)
    
    config.mainloop()


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
timer = config = None

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
botao_config = Button(text='Configurações', highlightthickness=0, command=abrir_config)
botao_config.grid(column=1, row=2)

janela.mainloop()