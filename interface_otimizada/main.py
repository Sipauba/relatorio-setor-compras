import tkinter as tk
from frames.frame_filial import *
from frames.frame_data import *
from frames.frame_tipo import *
from frames.frame_status import *
from frames.frame_forn_comp import *
from treeview import *
from label_assinatura import *
from botoes.botao_exportar import *
from botoes.botao_pesquisar import *


root = tk.Tk()
root.title('Follow Up')
# Esse trecho até o geometry() é um algorítmo que faz a janela iniciar bem no centro da tela, independente a resolução do monitor
largura = 800
altura = 500
largura_screen = root.winfo_screenwidth()
altura_screen = root.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
root.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))

frame_filial(root)

frame_data(root)

frame_tipo(root)

frame_status(root)

frame_forn_comp(root)

botao_pesquisar(root)

treeview(root)

label_assinatura(root)

botao_exportar(root)

root.mainloop()