import tkinter as tk
from frame_cabecalho1 import *
from frame_cabecalho2 import *
from treeview import *
from label_assinatura import *
from botao_exportar import *

root = tk.Tk()
# Esse trecho até o geometry() é um algorítmo que faz a janela iniciar bem no centro da tela, independente a resolução do monitor
largura = 800
altura = 500
largura_screen = root.winfo_screenwidth()
altura_screen = root.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
root.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))

frame_cabecalho1(root)

frame_cabecalho2(root)

treeview(root)

label_assinatura(root)

botao_exportar(root)

root.mainloop()