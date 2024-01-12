from tkinter import Button, Toplevel
import tkinter as tk

def toplevel_comprador(root):
    toplevel_comprador = Toplevel(root)
    toplevel_comprador.title('COMPRADORES')
    largura = 300
    altura = 300
    largura_screen = root.winfo_screenwidth()
    altura_screen = root.winfo_screenheight()
    posx = largura_screen/2 - largura/2
    posy = altura_screen/2 - altura/2
    toplevel_comprador.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))
    toplevel_comprador.grab_set()
  

    botao_filial_confirmar = Button(toplevel_comprador, text='CONFIRMAR', command=toplevel_comprador.destroy)
    botao_filial_confirmar.place(x=130, y= 260)

    botao_filial_cancelar = Button(toplevel_comprador, text='CANCELAR', command=toplevel_comprador.destroy)
    botao_filial_cancelar.place(x=220, y=260)
