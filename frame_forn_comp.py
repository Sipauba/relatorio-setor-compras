from tkinter import Frame, SOLID, Label, Entry, Button
from toplevel_comprador import toplevel_comprador
from toplevel_fornecedor import toplevel_fornecedor

def frame_forn_comp(root) :
    frame_forn_comp = Frame(root,
                            #relief = SOLID,
                            #bd = 1
                            )
    frame_forn_comp.pack(side = 'top', anchor ='w', pady = (0,10), padx=(40,0))

    label_fornecedor = Label(frame_forn_comp, text='FORNECEDOR', font=('Arial', 9))
    label_fornecedor.grid(row=0, column=0,columnspan=2, pady=(0,0), padx=(0,0), sticky='w')

    global campo_fornecedor
    campo_fornecedor = Entry(frame_forn_comp, width=11)
    campo_fornecedor.grid(row=1, column=0, pady=(0,0), padx=(0,0), sticky='w')

    botao_fornecedor = Button(frame_forn_comp, text='...', width=1, height=1, bg='silver', command=lambda:toplevel_fornecedor(root))
    botao_fornecedor.grid(row=1, column=1, padx=(0,0), sticky='w')

    label_comprador = Label(frame_forn_comp, text='COMPRADOR', font=('Arial', 9))
    label_comprador.grid(row=2, column=0, columnspan=2, pady=(0,0), padx=(0,0), sticky='w')

    global campo_comprador
    campo_comprador = Entry(frame_forn_comp, width=11)
    campo_comprador.grid(row=3, column=0, pady=(0,0), padx=(0,0), sticky='w')

    botao_comprador = Button(frame_forn_comp, text='...', width=1, height=1, bg='silver', command=lambda:toplevel_comprador(root))
    botao_comprador.grid(row=3, column=1, padx=(0,0), sticky='w')
    
    return frame_forn_comp
    #return campo_fornecedor
    
def atualiza_campo_fornecedor(campo_fornecedor,valor):
    campo_fornecedor.delete(0, 'end')
    campo_fornecedor.insert(0, valor)
    
def atualiza_campo_comprador(campo_comprador, valor):
    campo_comprador.delete(0, 'end')
    campo_comprador.insert(0, valor)
