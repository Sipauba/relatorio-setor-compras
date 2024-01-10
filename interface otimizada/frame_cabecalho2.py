from tkinter import Frame, SOLID, Label, Entry, Button

def frame_cabecalho2(root) :
    frame_cabecalho2 = Frame(root,
                            #width = 640,
                            #height = 110,
                            #relief = SOLID,
                            #bd = 1
                            )
    frame_cabecalho2.pack(side = 'top', anchor ='w', pady = (0,10), padx=(40,0))

    label_fornecedor = Label(frame_cabecalho2, text='Fornecedor')
    label_fornecedor.grid(row=0, column=0, pady=(0,0), padx=(20,0))

    campo_fornecedor = Entry(frame_cabecalho2, width=10)
    campo_fornecedor.grid(row=1, column=0, pady=(0,0), padx=(20,0))

    botao_fornecedor = Button(frame_cabecalho2, text='...', width=1, height=1)
    botao_fornecedor.grid(row=1, column=1, padx=(5,0))

    label_comprador = Label(frame_cabecalho2, text='Comprador')
    label_comprador.grid(row=2, column=0, pady=(0,0), padx=(20,0))

    campo_comprador = Entry(frame_cabecalho2,width=10)
    campo_comprador.grid(row=3, column=0, pady=(0,0), padx=(20,0))

    botao_comprador = Button(frame_cabecalho2, text='...', width=1, height=1)
    botao_comprador.grid(row=3, column=1, padx=(5,0))