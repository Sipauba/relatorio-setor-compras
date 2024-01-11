from tkinter import Label, Frame, SOLID, IntVar, Checkbutton

def frame_status(root):
    frame_status = Frame(root,
                         #relief=SOLID,
                         #bd=1
                         )
    frame_status.place(x=555, y= 5)
    
    label_status = Label(frame_status, text='STATUS PEDIDO', font=('Arial', 11))
    label_status.grid(row=0, column=0, pady=(20,0), padx=(0,0), sticky='w')

    box_status_agfaturamento_var = IntVar()
    box_status_agfaturamento = Checkbutton(frame_status, text='AGUARDANDO FATURAMENTO')
    box_status_agfaturamento.grid(row=1, column=0, sticky='w')
    
    box_status_agentrega_var = IntVar()
    box_status_agentrega = Checkbutton(frame_status, text='AGUARDANDO ENTREGA')
    box_status_agentrega.grid(row=2, column=0, sticky='w')
    
    box_status_parcial_var = IntVar()
    box_status_parcial = Checkbutton(frame_status, text='ENTREGA PARCIAL')
    box_status_parcial.grid(row=3, column=0, sticky='w')
    
    box_status_total_var = IntVar()
    box_status_total = Checkbutton(frame_status, text='ENTREGA TOTAL')
    box_status_total.grid(row=4, column=0, sticky='w')
    
    