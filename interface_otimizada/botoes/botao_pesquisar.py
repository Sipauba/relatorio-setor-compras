from tkinter import Button
import sys
sys.path.append('../interface_otimizada')
from frames.frame_status import *
from frames.frame_tipo import *

def botao_pesquisar(root):
    
    def executar_pesquisa():
        frame_status.exibir_valores_status()
        frame_tipo.exibir_valores_tipo()
    
    botao_pesquisar = Button(root, text='PESQUISAR', width=15, height=1, bg='silver', command=executar_pesquisa)
    botao_pesquisar.place(x=635, y=150)
    
    