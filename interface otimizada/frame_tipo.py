from tkinter import Frame, Label, SOLID, Checkbutton, IntVar

def frame_tipo(root):
    frame_tipo = Frame(root,
                       #relief=SOLID,
                       #bd=1
                       )
    frame_tipo.place(x=395, y=5)
    
    label_tipo = Label(frame_tipo, text='TIPO DO PEDIDO', font=('Arial', 11))
    label_tipo.grid(row=0, column=0, pady=(20,0), padx=(0,0), sticky='w')

    box_tipo_venda_var = IntVar()
    box_tipo_venda = Checkbutton(frame_tipo, text='VENDA')
    box_tipo_venda.grid(row=1, column=0, sticky='w')
    
    box_tipo_bonificacao_var = IntVar()
    box_tipo_bonificacao = Checkbutton(frame_tipo, text='BONIFICAÇÃO')
    box_tipo_bonificacao.grid(row=2, column=0, sticky='w')