import tkinter as tk
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