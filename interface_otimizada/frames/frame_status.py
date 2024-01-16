from tkinter import Label, Frame, SOLID, IntVar, Checkbutton

def frame_status(root):
    frame_status = Frame(root,
                         #relief=SOLID,
                         #bd=1
                         )
    frame_status.place(x=555, y= 5)
    
    label_status = Label(frame_status, text='STATUS DO PEDIDO', font=('Arial', 9))
    label_status.grid(row=0, column=0, pady=(20,0), padx=(0,0), sticky='w')

    # Variáveis de controle para os Checkbuttons
    var_total = IntVar(value=1)
    var_parcial = IntVar(value=1)
    var_aguardando_faturamento = IntVar(value=1)
    var_aguardando_entrega = IntVar(value=1)
    
    # Checkbuttons individuais
    box_aguardando_faturamento = Checkbutton(frame_status, text='AGUARDANDO FATURAMENTO', variable=var_aguardando_faturamento)
    box_aguardando_faturamento.grid(row=1, column=0, sticky='w')
    
    box_aguardando_entrega = Checkbutton(frame_status, text='AGUARDANDO ENTREGA', variable=var_aguardando_entrega)
    box_aguardando_entrega.grid(row=2, column=0, sticky='w')
    
    box_parcial = Checkbutton(frame_status, text='ENTREGA PARCIAL', variable=var_parcial)
    box_parcial.grid(row=3, column=0, sticky='w')
    
    box_total = Checkbutton(frame_status, text='ENTREGA TOTAL', variable=var_total)
    box_total.grid(row=4, column=0, sticky='w')

    # Função para exibir os valores dos Checkbuttons
    def exibir_valores_status():
        valores = [
            f"'{status}'" if var.get() else ''
            for status, var in zip(['TOTAL', 'PARCIAL', 'AGUARDANDO FATURAMENTO', 'AGUARDANDO ENTREGA'],
                                   [var_total, var_parcial, var_aguardando_faturamento, var_aguardando_entrega])
        ]
        valores = [valor for valor in valores if valor]  # Remove os valores vazios
        resultado_status_sql = ', '.join(valores)
        print(resultado_status_sql)  # Substitua por qualquer ação que você deseja fazer com a lista de valores

        return resultado_status_sql
    