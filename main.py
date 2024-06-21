import tkinter as tk
from tkinter import ttk, Frame, Label
from frame_filial import frame_filial
from frame_data import frame_data
from frame_tipo import frame_tipo
from frame_status import frame_status
from frame_forn_comp import frame_forn_comp
from treeview import treeview
from label_assinatura import label_assinatura
from botao_exportar import botao_exportar
from botao_pesquisar import botao_pesquisar


root = tk.Tk()
root.title('Follow Up')
# Esse trecho até o geometry() é um algorítmo que faz a janela iniciar bem no centro da tela, independente a resolução do monitor
largura = 1000
altura = 610
largura_screen = root.winfo_screenwidth()
altura_screen = root.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
root.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))

def frame_aba_1(root):
    frame_aba_1 = Frame(root,
                        width=10, 
                        height=10, 
                        )
    frame_aba_1.pack(expand=True, fill='both')
    frame_filial(frame_aba_1)
    frame_data(frame_aba_1)
    frame_tipo(frame_aba_1)
    frame_status(frame_aba_1)
    frame_forn_comp(frame_aba_1)
    botao_pesquisar(frame_aba_1)
    treeview(frame_aba_1)
    label_assinatura(frame_aba_1)
    botao_exportar(frame_aba_1)
    return frame_aba_1

def frame_aba_2(root):
    frame_aba_2 = Frame(root,
                        width=10, 
                        height=10, 
                        )
    frame_aba_2.pack(expand=True, fill='both')
    label = Label(frame_aba_2, text='EM DESENVOLVIMENTO...')
    label.pack()
    return frame_aba_2

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')
notebook.add(frame_aba_1(notebook), text='Informações Gerais')
notebook.add(frame_aba_2(notebook), text='Pedidos Pendentes')
#frame_aba_1(root)

root.mainloop()