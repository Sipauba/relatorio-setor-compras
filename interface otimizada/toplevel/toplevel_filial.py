from tkinter import Button, Toplevel


def toplevel_filial(root):
    toplevel_filial = Toplevel(root)
    toplevel_filial.title('FILIAIS')
    largura = 300
    altura = 300
    largura_screen = root.winfo_screenwidth()
    altura_screen = root.winfo_screenheight()
    posx = largura_screen/2 - largura/2
    posy = altura_screen/2 - altura/2
    toplevel_filial.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))
    toplevel_filial.grab_set()
  

    botao_filial_confirmar = Button(toplevel_filial, text='CONFIRMAR', command=toplevel_filial.destroy)
    botao_filial_confirmar.place(x=130, y= 260)

    botao_filial_cancelar = Button(toplevel_filial, text='CANCELAR', command=toplevel_filial.destroy)
    botao_filial_cancelar.place(x=220, y=260)

