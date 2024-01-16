from tkinter import Button
import sys
sys.path.append('../interface_otimizada')
from frames.frame_status import *


def botao_pesquisar(root):
        
    botao_pesquisar = Button(root, text='PESQUISAR', width=15, height=1, bg='silver')
    botao_pesquisar.place(x=635, y=150)
    
    