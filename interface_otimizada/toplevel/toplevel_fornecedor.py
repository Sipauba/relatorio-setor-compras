from tkinter import Button, Toplevel, Frame, SOLID, Label, Entry
import sys
sys.path.append('../interface_otimizada')
from conecta_banco import cursor



def toplevel_fornecedor(root):
    toplevel_fornecedor = Toplevel(root)
    toplevel_fornecedor.title('FORNECEDORES')
    largura = 400
    altura = 400
    largura_screen = root.winfo_screenwidth()
    altura_screen = root.winfo_screenheight()
    posx = largura_screen/2 - largura/2
    posy = altura_screen/2 - altura/2
    toplevel_fornecedor.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))
    toplevel_fornecedor.grab_set()
  
    """ frame_fornecedor = Frame(toplevel_fornecedor,
                            width=370,
                            height=345,
                            relief= SOLID,
                            bd=1
                            )
    frame_fornecedor.pack(padx=(5,20), pady=(5,50))"""
    
    label_codigo = Label(toplevel_fornecedor, text='CÓDIGO', font=('Arial', 9))
    label_codigo.grid(row=0, column=0, padx=(10,0), pady=(10,0), sticky='w')
    
    campo_codigo = Entry(toplevel_fornecedor, width= 9)
    campo_codigo.grid(row=1, column=0, padx=(10,0), sticky='w')
    
    label_fornecedor = Label(toplevel_fornecedor, text='FORNECEDOR', font=('Arial', 9))
    label_fornecedor.grid(row=0, column=1, padx=(20,0), pady=(10,0), sticky='w')
    
    campo_fornecedor = Entry(toplevel_fornecedor, width=33)
    campo_fornecedor.grid(row=1, column=1, padx=(20,0), sticky='w')
    
    botao_pesquisar = Button(toplevel_fornecedor, text='PESQUISAR', width=10, bg='silver')
    botao_pesquisar.grid(row=1, column=2, padx=(20,0), sticky='w')

    """botao_filial_confirmar = Button(toplevel_fornecedor, text='CONFIRMAR', command=toplevel_fornecedor.destroy)
    botao_filial_confirmar.place(x=130, y=260)

    botao_filial_cancelar = Button(toplevel_fornecedor, text='CANCELAR', command=toplevel_fornecedor.destroy)
    botao_filial_cancelar.place(x=220, y=260)"""
